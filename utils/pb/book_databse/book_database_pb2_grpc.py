# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import book_database_pb2 as book__database__pb2


class BooksDatabaseStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Read = channel.unary_unary(
                '/BooksDatabase/Read',
                request_serializer=book__database__pb2.ReadRequest.SerializeToString,
                response_deserializer=book__database__pb2.ReadResponse.FromString,
                )
        self.Write = channel.unary_unary(
                '/BooksDatabase/Write',
                request_serializer=book__database__pb2.WriteRequest.SerializeToString,
                response_deserializer=book__database__pb2.WriteResponse.FromString,
                )


class BooksDatabaseServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BooksDatabaseServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=book__database__pb2.ReadRequest.FromString,
                    response_serializer=book__database__pb2.ReadResponse.SerializeToString,
            ),
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=book__database__pb2.WriteRequest.FromString,
                    response_serializer=book__database__pb2.WriteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'BooksDatabase', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BooksDatabase(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BooksDatabase/Read',
            book__database__pb2.ReadRequest.SerializeToString,
            book__database__pb2.ReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BooksDatabase/Write',
            book__database__pb2.WriteRequest.SerializeToString,
            book__database__pb2.WriteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
