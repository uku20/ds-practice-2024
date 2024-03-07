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

def detect_fraud(name, contact, street, city, state):
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        # Create a stub object.
        stub = fraud_detection_grpc.FraudDetectionStub(channel)
        # Call the service through the stub object.
        response = stub.DetectFraud(fraud_detection.FraudRequest(name=name, contact=contact, street=street, city=city, state=state))
    return response.response

def verify_transaction(number, expirationDate, cvv, country, zip):
    with grpc.insecure_channel('transaction_verification:50052') as channel:
        stub = transaction_verification_grpc.TransactionServiceStub(channel)
        response = stub.VerifyTransaction(transaction_verification.VerificationRequest(number=number, expirationDate=expirationDate, cvv=cvv, country=country, zip=zip))
    return response.response

def get_suggestions(name):
    with grpc.insecure_channel('suggestions:50053') as channel:
        stub = suggestions_grpc.SuggestServiceStub(channel)
        response = stub.FindSuggestions(suggestions.SuggestRequest(name=name))
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

@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Responds with a JSON object containing the order ID, status, and suggested books.
    """
    data = request.json
    # Print request object data
    print("Request Data:", request.json)
    greet(name='orchestrator')

    #Two boolean values
    fraud = detect_fraud(data['user']['name'], data['user']['contact'], data['billingAddress']['street'], data['billingAddress']['city'], data['billingAddress']['state'])
    verification = verify_transaction(data['creditCard']['number'], data['creditCard']['expirationDate'], data['creditCard']['cvv'], data['billingAddress']['country'], data['billingAddress']['zip'])
    print(fraud)
    print(verification)
    
    #Suggestions
    suggestions = get_suggestions(data['items'][0]['name'])
    first_name = suggestions.firstSuggestion[1]
    first_id = suggestions.firstSuggestion[0]
    first_author = suggestions.firstSuggestion[2]
    second_name = suggestions.secondSuggestion[1]
    second_id = suggestions.secondSuggestion[0]
    second_author = suggestions.secondSuggestion[2]
    # Dummy response following the provided YAML specification for the bookstore
    order_status_response = {
        'orderId': '10',
        'status': 'Order Approved',
        'suggestedBooks': [
            {'bookId': first_id, 'title': first_name, 'author': first_author},
            {'bookId': second_id, 'title': second_name, 'author': second_author}
        ]
    }

    return order_status_response


if __name__ == '__main__':
    # Run the app in debug mode to enable hot reloading.
    # This is useful for development.
    # The default port is 5000.
    app.run(host='0.0.0.0')
