import sys
import os

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/suggestions'))
sys.path.insert(0, utils_path)
import suggestions_pb2 as suggestions
import suggestions_pb2_grpc as suggestions_grpc

import grpc
from concurrent import futures

# Create a class to define the server functions, derived from
# fraud_detection_pb2_grpc.HelloServiceServicer
class SuggestService(suggestions_grpc.SuggestServiceServicer):
    # Create an RPC function to say hello
    def FindSuggestions(self, request, context):
        # Create a HelloResponse object
        response = suggestions.SuggestResponse()
        # Set the greeting field of the response object

        suggested_name_1 = ""
        suggested_author_1 = ""
        suggested_id_1 = ""
        name = request.name

        suggested_name_2 = ""
        suggested_author_2 = ""
        suggested_id_2 = ""
        if(name == 'Learning Python'):
            suggested_name_1 = "Design Patterns: Elements of Reusable Object-Oriented Software"
            suggested_author_1 = "Erich Gamma, Richard Helm, Ralph Johnson, & John Vlissides"
            suggested_id_1 = "4"

            suggested_name_2 = "JavaScript - The Good Parts"
            suggested_author_2 = "Jane Doe"
            suggested_id_2 = "2"
        elif(name == 'JavaScript - The Good Parts'):
            suggested_name_1 = "Domain-Driven Design: Tackling Complexity in the Heart of Software"
            suggested_author_1 = "Eric Evans"
            suggested_id_1 = "3"

            suggested_name_2 = "Learning Python"
            suggested_author_2 = "John Smith"
            suggested_id_2 = "1"
        elif(name == 'Domain-Driven Design: Tackling Complexity in the Heart of Software'):
            suggested_name_1 = "JavaScript - The Good Parts"
            suggested_author_1 = "Jane Doe"
            suggested_id_1 = "2"

            suggested_name_2 = "Design Patterns: Elements of Reusable Object-Oriented Software"
            suggested_author_2 = "Erich Gamma, Richard Helm, Ralph Johnson, & John Vlissides"
            suggested_id_2 = "4"
        elif(name == 'Design Patterns: Elements of Reusable Object-Oriented Software'):
            suggested_name_1 = "Learning Python"
            suggested_author_1 = "John Smith"
            suggested_id_1 = "1"

            suggested_name_2 = "Domain-Driven Design: Tackling Complexity in the Heart of Software"
            suggested_author_2 = "Eric Evans"
            suggested_id_2 = "3"


        response.firstSuggestion.append(suggested_id_1)
        response.firstSuggestion.append(suggested_name_1)
        response.firstSuggestion.append(suggested_author_1)

        response.secondSuggestion.append(suggested_id_2)
        response.secondSuggestion.append(suggested_name_2)
        response.secondSuggestion.append(suggested_author_2)
        # Print the greeting message
        print(response)
        # Return the response object
        return response

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add HelloService
    suggestions_grpc.add_SuggestServiceServicer_to_server(SuggestService(), server)
    # Listen on port 50051
    port = "50053"
    server.add_insecure_port("[::]:" + port)
    # Start the server
    server.start()
    print("Server started. Listening on port 50053.")
    # Keep thread alive
    server.wait_for_termination()

if __name__ == '__main__':
    serve()