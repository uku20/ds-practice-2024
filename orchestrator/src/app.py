import sys
import os

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/fraud_detection'))
sys.path.insert(0, utils_path)
import fraud_detection_pb2 as fraud_detection
import fraud_detection_pb2_grpc as fraud_detection_grpc

FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/transaction_verification'))
sys.path.insert(0, utils_path)
import transaction_verification_pb2 as transaction_verification
import transaction_verification_pb2_grpc as transaction_verification_grpc

FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/suggestions'))
sys.path.insert(0, utils_path)
import suggestions_pb2 as suggestions
import suggestions_pb2_grpc as suggestions_grpc

import grpc


def greet(name='you'):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        # Create a stub object.
        stub = fraud_detection_grpc.HelloServiceStub(channel)
        # Call the service through the stub object.
        response = stub.SayHello(fraud_detection.HelloRequest(name=name))
    return response.greeting

import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def detect_fraud(name, contact, street, city, state):
    logger.info("Received fraud detection request for user: %s", name)
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        # Create a stub object.
        stub = fraud_detection_grpc.FraudDetectionStub(channel)
        # Call the service through the stub object.
        response = stub.DetectFraud(fraud_detection.FraudRequest(name=name, contact=contact, street=street, city=city, state=state))
    logger.info("Fraud detection response received: %s", response.response)
    return response.response

def verify_transaction(number, expirationDate, cvv, country, zip):
    logger.info("Received transaction verification request for card number: %s", number)
    with grpc.insecure_channel('transaction_verification:50052') as channel:
        stub = transaction_verification_grpc.TransactionServiceStub(channel)
        response = stub.VerifyTransaction(transaction_verification.VerificationRequest(number=number, expirationDate=expirationDate, cvv=cvv, country=country, zip=zip))
    logger.info("Transaction verification response received: %s", response.response)
    return response.response

def get_suggestions(name):
    logger.info("Received book suggestions request for book: %s", name)
    with grpc.insecure_channel('suggestions:50053') as channel:
        stub = suggestions_grpc.SuggestServiceStub(channel)
        response = stub.FindSuggestions(suggestions.SuggestRequest(name=name))
    logger.info("Book suggestions response received: %s", response)
    return response

# Import Flask.
# Flask is a web framework for Python.
# It allows you to build a web application quickly.
# For more information, see https://flask.palletsprojects.com/en/latest/
from flask import Flask, request
from flask_cors import CORS

# Create a simple Flask app.
app = Flask(__name__)
# Enable CORS for the app.
CORS(app)

# Define a GET endpoint.
@app.route('/', methods=['GET'])
def index():
    """
    Responds with 'Hello, [name]' when a GET request is made to '/' endpoint.
    """
    # Test the fraud-detection gRPC service.
    response = greet(name='orchestrator')
    # Return the response.
    return response

import threading
@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Responds with a JSON object containing the order ID, status, and suggested books.
    """
    data = request.json
    logger.info("Received checkout request: %s", data)

        
    class TaskThread(threading.Thread):
        def __init__(self, target, *args, **kwargs):
            super(TaskThread, self).__init__(target=target, args=args, kwargs=kwargs)
            self._result = None

        @property
        def result(self):
            return self._result

        def run(self):
            self._result = self._target(*self._args, **self._kwargs)

    # Function to handle fraud detection
    def detect_fraud_task():
        logger.info("Starting fraud detection task")
        return detect_fraud(data['user']['name'], data['user']['contact'], data['billingAddress']['street'], data['billingAddress']['city'], data['billingAddress']['state'])

    # Function to handle transaction verification
    def verify_transaction_task():
        logger.info("Starting transaction verification task")
        return verify_transaction(data['creditCard']['number'], data['creditCard']['expirationDate'], data['creditCard']['cvv'], data['billingAddress']['country'], data['billingAddress']['zip'])

    # Function to handle book suggestions
    def get_suggestions_task():
        logger.info("Starting book suggestions task")
        return get_suggestions(data['items'][0]['name'])

    # Create threads for each microservice
    fraud_thread = TaskThread(target=detect_fraud_task)
    verification_thread = TaskThread(target=verify_transaction_task)
    suggestions_thread = TaskThread(target=get_suggestions_task)

    # Start the threads
    fraud_thread.start()
    verification_thread.start()
    suggestions_thread.start()

    # Wait for all threads to finish
    fraud_thread.join()
    verification_thread.join()
    suggestions_thread.join()

    # Retrieve results from each microservice
    fraud_result = fraud_thread.result
    verification_result = verification_thread.result
    suggestions_result = suggestions_thread.result

    # Combine results and communicate the decision to the user frontend
    if not fraud_result or not verification_result:
        order_status_response = {'orderId': '10', 'status': 'Order Rejected'}
    else:
        # Process suggestions_result accordingly
        first_name = suggestions_result.firstSuggestion[1]
        first_id = suggestions_result.firstSuggestion[0]
        first_author = suggestions_result.firstSuggestion[2]
        second_name = suggestions_result.secondSuggestion[1]
        second_id = suggestions_result.secondSuggestion[0]
        second_author = suggestions_result.secondSuggestion[2]

        order_status_response = {
            'orderId': '10',
            'status': 'Order Approved',
            'suggestedBooks': [
                {'bookId': first_id, 'title': first_name, 'author': first_author},
                {'bookId': second_id, 'title': second_name, 'author': second_author}
            ]
        }
    logger.info("Returning order status response: %s", order_status_response)
    return order_status_response



if __name__ == '__main__':
    # Run the app in debug mode to enable hot reloading.
    # This is useful for development.
    # The default port is 5000.
    app.run(host='0.0.0.0')
