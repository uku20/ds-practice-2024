# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import fraud_detection_pb2 as fraud__detection__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class HelloServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/hello.HelloService/SayHello',
                request_serializer=fraud__detection__pb2.HelloRequest.SerializeToString,
                response_deserializer=fraud__detection__pb2.HelloResponse.FromString,
                )


class HelloServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HelloServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=fraud__detection__pb2.HelloRequest.FromString,
                    response_serializer=fraud__detection__pb2.HelloResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hello.HelloService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HelloService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hello.HelloService/SayHello',
            fraud__detection__pb2.HelloRequest.SerializeToString,
            fraud__detection__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class FraudDetectionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DetectFraud = channel.unary_unary(
                '/hello.FraudDetection/DetectFraud',
                request_serializer=fraud__detection__pb2.FraudRequest.SerializeToString,
                response_deserializer=fraud__detection__pb2.FraudResponse.FromString,
                )


class FraudDetectionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DetectFraud(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FraudDetectionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DetectFraud': grpc.unary_unary_rpc_method_handler(
                    servicer.DetectFraud,
                    request_deserializer=fraud__detection__pb2.FraudRequest.FromString,
                    response_serializer=fraud__detection__pb2.FraudResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hello.FraudDetection', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FraudDetection(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DetectFraud(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hello.FraudDetection/DetectFraud',
            fraud__detection__pb2.FraudRequest.SerializeToString,
            fraud__detection__pb2.FraudResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class YourServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ClearData = channel.unary_unary(
                '/hello.YourService/ClearData',
                request_serializer=fraud__detection__pb2.ClearDataRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class YourServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ClearData(self, request, context):
        """Existing rpc methods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_YourServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ClearData': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearData,
                    request_deserializer=fraud__detection__pb2.ClearDataRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hello.YourService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class YourService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ClearData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hello.YourService/ClearData',
            fraud__detection__pb2.ClearDataRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
