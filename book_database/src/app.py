from concurrent import futures
import grpc
import books_db_pb2
import books_db_pb2_grpc
from raft import RaftNode
import logging
import threading

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger( __name__)


class BooksDatabaseService(books_db_pb2_grpc.BooksDatabaseServicer):
    def __init__(self, node_id, peers):
        self.raft_node = RaftNode(node_id=node_id, peers=peers, state_machine=self)

    def Read(self, request, context):
        # Delegate read to the raft node (leader)
        if self.raft_node.state == 'leader':
            value = self.raft_node.state_machine.get(request.key)
            return books_db_pb2.ReadResponse(value=value)
        else:
            return books_db_pb2.ReadResponse(value="Not the leader")

    def Write(self, request, context):
        # Delegate write to the raft node (leader)
        if self.raft_node.state == 'leader':
            self.raft_node.state_machine[request.key] = request.value
            return books_db_pb2.WriteResponse(success=True)
        else:
            return books_db_pb2.WriteResponse(success=False)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    books_db_pb2_grpc.add_BooksDatabaseServicer_to_server(
        BooksDatabaseService(node_id='node1', peers=['node2', 'node3']), server)
    port = "50057"
    server.add_insecure_port("[::]:" + port)
    logger.info("Server started. Listening on port {port}.")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()