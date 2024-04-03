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

import grpc
from concurrent import futures
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Create a class to define the server functions, derived from
# fraud_detection_pb2_grpc.HelloServiceServicer
class HelloService(fraud_detection_grpc.HelloServiceServicer):
    # Create an RPC function to say hello
    def SayHello(self, request, context):
        logger.info("Received SayHello request.")
        # Create a HelloResponse object
        response = fraud_detection.HelloResponse()
        # Set the greeting field of the response object
        response.greeting = "Hello, " + request.name
        logger.info(response.greeting)
        # Return the response object
        return response
    def DetectFraud(self, request, context):
        logger.info("Received DetectFraud request.")
        # Create a HelloResponse object
        response = fraud_detection.FraudResponse()
        # Set the greeting field of the response object
        value = True
        if(len(request.name) < 2):
            value = False
        if(len(request.contact) < 2):
            value = False
        if(len(request.street) < 2):
            value = False
        if(len(request.city) < 2):
            value = False
        if(len(request.state) < 2):
            value = False
        response.response = value
        logger.info(f"Sending response: {response.response}")
        # Return the response object
        return response

    def ClearData(self, request, context):
        # Logic to clear data if your local vector clock <= request's vector clock
        return google.protobuf.empty_pb2.Empty()

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add HelloService
    fraud_detection_grpc.add_HelloServiceServicer_to_server(HelloService(), server)
    fraud_detection_grpc.add_FraudDetectionServicer_to_server(HelloService(), server)
    # Listen on port 50051
    port = "50051"
    server.add_insecure_port("[::]:" + port)
    logger.info(f"Server started. Listening on port {port}.")
    # Start the server
    server.start()
    # Keep thread alive
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
