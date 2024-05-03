import sys
import os

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/payment'))
sys.path.insert(0, utils_path)
import payment_pb2 as payment
import payment_pb2_grpc as payment_grpc

import grpc
from concurrent import futures
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Create a class to define the server functions, derived from
# fraud_detection_pb2_grpc.HelloServiceServicer
class PaymentService(payment_grpc.PaymentServiceServicer):
    # Create an RPC function to say hello
    def Vote(self, request, context):
        logger.info("Received Vote request.")
        # Create a HelloResponse object
        response = payment.VoteResponse()
        # Set the greeting field of the response object
        if (request.name == "request"):
            response.response = "VOTE-COMMIT"
        else:
            response.response = "VOTE-ABORT"
        logger.info(response.response)
        # Return the response object
        return response

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add HelloService
    payment_grpc.add_PaymentServiceServicer_to_server(PaymentService(), server)
    # Listen on port 50051
    port = "50058"
    server.add_insecure_port("[::]:" + port)
    logger.info(f"Server started. Listening on port {port}.")
    # Start the server
    server.start()
    # Keep thread alive
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
