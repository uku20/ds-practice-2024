import sys
import os

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/queue'))
sys.path.insert(0, utils_path)
import queue_pb2 as queue
import queue_pb2_grpc as queue_grpc

import grpc
from concurrent import futures
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class QueueService(queue_grpc.QueueServiceServicer):
    global the_queue
    the_queue = []
    def AddtoQueue(self, request, context):
        logger.info(f"Adding to queue: {request}")
        # Create a HelloResponse object
        response = queue.AddtoQueueResponse()
        value = True
        order = []
        order.append(request.orderId)
        order.append(request.name)
        order.append(request.number)
        order.append(request.expirationDate)
        order.append(request.cvv)
        order.append(request.contact)

        the_queue.append(order)
        # Set the greeting field of the response object
        response.response = value
        return response
    
    def RequestFromQueue(self, request, context):
        logger.info(f"Requesting from queue: {request}")
        # Create a HelloResponse object
        response = queue.GetFromQueueResponse()
        order = the_queue.pop(0)
        response.orderId = order[0]
        response.name = order[1]
        response.number = order[2]
        response.expirationDate = order[3]
        response.cvv = order[4]
        response.contact = order[5]
        logger.info(f"Returning from queue with orderId: {response.orderId}")
        # Return the response object
        return response


def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add HelloService
    queue_grpc.add_QueueServiceServicer_to_server(QueueService(), server)
    # Listen on port 50051
    port = "50055"
    server.add_insecure_port("[::]:" + port)
    logger.info("Server started. Listening on port {port}.")
    # Start the server
    server.start()
    # Keep thread alive
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
