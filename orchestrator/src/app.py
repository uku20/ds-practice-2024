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

FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/queue'))
sys.path.insert(0, utils_path)
import queue_pb2 as queue
import queue_pb2_grpc as queue_grpc

FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/executor'))
sys.path.insert(0, utils_path)
import executor_pb2 as executor
import executor_pb2_grpc as executor_grpc

FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/book_databse'))
sys.path.insert(0, utils_path)
import book_database_pb2 as bookdatabase
import book_database_pb2_grpc as bookatabase_grpc

FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/payment'))
sys.path.insert(0, utils_path)
import payment_pb2 as payment
import payment_pb2_grpc as payment_grpc

import grpc
import time

vector_clocks = {} 
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
    order_id = generate_order_id()
    order_data = {}
    order_data[order_id] = {'name': name, 'contact': contact, 'street': street, 'city': city, 'state': state}
    vector_clocks[order_id] = [0, 0, 0]  # Initialize vector clock for the order
    time.sleep(1)  # Simulate processing time
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        # Create a stub object.
        stub = fraud_detection_grpc.FraudDetectionStub(channel)
        # Call the service through the stub object.
        response = stub.DetectFraud(fraud_detection.FraudRequest(name=name, contact=contact, street=street, city=city, state=state))
    logger.info("Fraud detection response received: %s", response.response)
    return response.response

def verify_transaction(number, expirationDate, cvv, country, zip, orderItems, userData):
    logger.info("Received transaction verification request for card number: %s", number)
    order_id = generate_order_id()
    order_data = {}
    order_data[order_id] = {'number': number, 'expirationDate': expirationDate, 'cvv': cvv, 'country': country, 'zip': zip}
    vector_clocks[order_id] = [0, 0, 0]  # Initialize vector clock for the order
    time.sleep(1)  # Simulate processing time
    with grpc.insecure_channel('transaction_verification:50052') as channel:
        stub1 = transaction_verification_grpc.TransactionServiceStub(channel)
        stub2 = transaction_verification_grpc.OrderItemServiceStub(channel)
        stub3 = transaction_verification_grpc.UserDataServiceStub(channel)
        for item in orderItems:
            items_response = stub2.OrderItemTransaction(transaction_verification.OrderItemRequest(name = item['name'], quantity = item['quantity']))
            if (items_response):
                print("THIS STEP WAS COMPLETED SUCCESSFULLY")
        user_data_response = stub3.UserDataTransaction(transaction_verification.UserDataRequest(name=userData['name'], contact=userData['contact']))
        if (user_data_response):
            print("THIS STEP WAS COMPLETED SUCCESSFULLY")
        response = stub1.VerifyTransaction(transaction_verification.VerificationRequest(number=number, expirationDate=expirationDate, cvv=cvv, country=country, zip=zip))
    logger.info("Transaction verification response received: %s", response.response)
    return response.response

def get_suggestions(name):
    logger.info("Received book suggestions request for book: %s", name)
    order_id = generate_order_id()
    order_data = {}
    order_data[order_id] = {'name': name}
    vector_clocks[order_id] = [0, 0, 0]  # Initialize vector clock for the order
    time.sleep(1)  # Simulate processing time
    with grpc.insecure_channel('suggestions:50053') as channel:
        stub = suggestions_grpc.SuggestServiceStub(channel)
        response = stub.FindSuggestions(suggestions.SuggestRequest(name=name))
    logger.info("Book suggestions response received: %s", response)
    return response

def add_to_queue(orderId, name, number, expirationDate, cvv, contact):
    time.sleep(1)  # Simulate processing time
    with grpc.insecure_channel('queue:50055') as channel:
        # Create a stub object.
        stub = queue_grpc.QueueServiceStub(channel)
        # Call the service through the stub object.
        response = stub.AddtoQueue(queue.AddtoQueueRequest(orderId=orderId, name=name, number=number, expirationDate=expirationDate, cvv=cvv, contact=contact))
    logger.info("Added to queue: %s", response.response)
    return response.response

def get_from_queue(orderId):
    time.sleep(1)  # Simulate processing time
    with grpc.insecure_channel('queue:50055') as channel:
        # Create a stub object.
        stub = queue_grpc.QueueServiceStub(channel)
        # Call the service through the stub object.
        response = stub.RequestFromQueue(queue.AddtoQueueRequest(orderId=orderId))
    logger.info("Received From Queue: %s", response)
    return response

def executeorder(orderId):
    time.sleep(1)  # Simulate processing time
    logger.info("Executing order: %s", orderId)
    with grpc.insecure_channel('executor:50056') as channel:
        # Create a stub object.
        stub = executor_grpc.ExecuteOrderServiceStub(channel) 
        order = get_from_queue(orderId)
        orderid = order.orderId
        pc = vote()
        if (pc == "VOTE-COMMIT"):
            response = stub.Execute(executor.ExecuteRequest(orderId=orderid))
        else:
            pass
    return response

def read(key):
    time.sleep(1)  # Simulate processing time
    logger.info("read: %s", key)
    with grpc.insecure_channel('book_database:50057') as channel:
        # Create a stub object.
        stub = bookatabase_grpc.BookDatabaseStub(channel) 
        response = stub.Read(bookdatabase.ReadRequest(key=key))
    return response

def write(key,value):
    time.sleep(1)  # Simulate processing time
    logger.info("write: %s", value)
    with grpc.insecure_channel('book_database:50057') as channel:
        # Create a stub object.
        stub = bookatabase_grpc.BookDatabaseStub(channel) 
        response = stub.Write(bookdatabase.WriteRequest(key=key,value=value))
    return response

def vote():
    time.sleep(1)
    with grpc.insecure_channel('payment:50058') as channel:
        # Create a stub object.
        stub = payment_grpc.PaymentOrderServiceStub(channel) 
        response = stub.Execute(payment.VoteRequest(name="request"))
    return response

# Import Flask.
# Flask is a web framework for Python.
# It allows you to build a web application quickly.
# For more information, see https://flask.palletsprojects.com/en/latest/
from flask import Flask, request, jsonify
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

# Function to increment vector clock for a given order
def increment_vector_clock(order_id, index):
    vector_clocks[order_id][index] += 1

def broadcast_clear_data(order_id):
    final_vector_clock = vector_clocks.get(order_id, [0, 0, 0])
    # Establish a channel and send ClearDataRequest to each service
    with grpc.insecure_channel('your_service_address') as channel:
        stub = suggestions_grpc.YourServiceStub(channel)
        stub.ClearData(suggestions.ClearDataRequest(vector_clock=final_vector_clock))

import uuid  # Import the uuid module
# Function to generate a unique OrderID
def generate_order_id():
    return str(uuid.uuid4())  # Generate a random UUID and convert it to a string

import threading
@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Responds with a JSON object containing the order ID, status, and suggested books.
    """
    data = request.json
    logger.info("Received checkout request: %s", data)

    # Generate a unique OrderID for the current order
    order_id = generate_order_id()
    # Include the OrderID in the data payload sent to backend services
    data['orderId'] = order_id
    vector_clocks[order_id] = [0, 0, 0]  # Initialize vector clock
    # Initialize continue_processing as a threading.Event
    continue_processing = threading.Event()
    continue_processing.set()  # Initially allow processing to continue

    class TaskThread(threading.Thread):
        def __init__(self, target, *args, **kwargs):
            super(TaskThread, self).__init__(target=target, args=args, kwargs=kwargs)
            self._result = None

        @property
        def result(self):
            return self._result

        def run(self):
            if not continue_processing.is_set():
               return 
            self._result = self._target(*self._args, **self._kwargs)
            # Check result and decide whether to continue

    # Function to handle fraud detection
    def detect_fraud_task():
        logger.info("Starting fraud detection task")
        result = detect_fraud(data['user']['name'], data['user']['contact'], data['billingAddress']['street'], data['billingAddress']['city'], data['billingAddress']['state'])
        increment_vector_clock(data['orderId'], 1)  # Increment vector clock for fraud detection
        return result
    # Function to handle transaction verification
    def verify_transaction_task():
        logger.info("Starting transaction verification task")
        orderItems = data.get('items', [])
        userData = data.get('user', {})
        result = verify_transaction(data['creditCard']['number'], data['creditCard']['expirationDate'], data['creditCard']['cvv'], data['billingAddress']['country'], data['billingAddress']['zip'],orderItems=orderItems, userData=userData)
        increment_vector_clock(data['orderId'], 0)  # Increment vector clock for transaction verification
        return result
    # Function to handle book suggestions
    def get_suggestions_task():
        logger.info("Starting book suggestions task")
        result = get_suggestions(data['items'][0]['name'])
        increment_vector_clock(data['orderId'], 2)  # Increment vector clock for book suggestions
        return result
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
        order_status_response = {'orderId': order_id, 'status': 'Order Rejected'}
    else:
        # Process suggestions_result accordingly
        first_name = suggestions_result.firstSuggestion[1]
        first_id = suggestions_result.firstSuggestion[0]
        first_author = suggestions_result.firstSuggestion[2]
        second_name = suggestions_result.secondSuggestion[1]
        second_id = suggestions_result.secondSuggestion[0]
        second_author = suggestions_result.secondSuggestion[2]

        order_status_response = {
            'orderId': order_id,
            'status': 'Order Approved',
            'suggestedBooks': [
                {'bookId': first_id, 'title': first_name, 'author': first_author},
                {'bookId': second_id, 'title': second_name, 'author': second_author}
            ]
        }
        add_to_queue(order_id, data['user']['name'], data['creditCard']['number'], data['creditCard']['expirationDate'], data['creditCard']['cvv'], data['user']['contact'])
        executeorder(order_id)
    logger.info("Returning order status response: %s", order_status_response)
    return order_status_response





if __name__ == '__main__':
    # Run the app in debug mode to enable hot reloading.
    # This is useful for development.
    # The default port is 5000.
    app.run(host='0.0.0.0')
