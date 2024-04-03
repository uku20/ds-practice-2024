import sys
import os

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/transaction_verification'))
sys.path.insert(0, utils_path)
import transaction_verification_pb2 as transaction_verification
import transaction_verification_pb2_grpc as transaction_verification_grpc

import grpc
from concurrent import futures
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TransactionService(transaction_verification_grpc.TransactionServiceServicer):
    def VerifyTransaction(self, request, context):
        logger.info(f"Received transaction verification request: {request}")
        # Create a HelloResponse object
        response = transaction_verification.VerificationResponse()
        value = True

        if(len(request.number)!=16):
            value = False

        if(len(request.expirationDate)<4):
            value = False
        
        if(len(request.cvv)!=3):
            value = False

        if(len(request.country)==0):
            value = False
        
        if(len(request.zip)<2):
            value = False

        # Check if the order items list is not empty
        if not request.orderItems:
            value = False

        # Check if mandatory user data is filled in
        if not request.userData.name or not request.userData.contact or not request.userData.address:
            value = False
        # Set the greeting field of the response object
        response.response = value
        # Log before returning the response
        logger.info(f"Returning transaction verification response: {response.response}")
        # Return the response object
        return response
    def ClearData(self, request, context):
        # Logic to clear data if your local vector clock <= request's vector clock
        return google.protobuf.empty_pb2.Empty()

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add HelloService
    transaction_verification_grpc.add_TransactionServiceServicer_to_server(TransactionService(), server)
    # Listen on port 50051
    port = "50052"
    server.add_insecure_port("[::]:" + port)
    logger.info("Server started. Listening on port {port}.")
    # Start the server
    server.start()
    # Keep thread alive
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
