import sys
import os

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/executor'))
sys.path.insert(0, utils_path)
import executor_pb2 as executor
import executor_pb2_grpc as executor_grpc

import grpc
from concurrent import futures
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ExecuteOrderService(executor_grpc.ExecuteOrderServiceServicer):
    def Execute(self, request, context):
        logger.info(f"Executing order with orderid: {request}")
        # Create a HelloResponse object
        response = executor.ExecuteResponse()
        value = True
        # Return the response object
        return response
    


def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add HelloService
    executor_grpc.add_ExecuteOrderServiceServicer_to_server(ExecuteOrderService(), server)
    # Listen on port 50051
    port = "50056"
    server.add_insecure_port("[::]:" + port)
    logger.info("Server started. Listening on port {port}.")
    # Start the server
    server.start()
    # Keep thread alive
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
