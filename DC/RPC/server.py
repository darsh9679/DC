from xmlrpc.server import SimpleXMLRPCServer

# Define the functions to be called remotely
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Initialize the server on localhost at port 8000
server = SimpleXMLRPCServer(("localhost", 8000))
print("RPC Server started...")

# Register the functions so they are accessible to the client
server.register_function(add, "add")
server.register_function(subtract, "subtract")

# Run the server's main loop
server.serve_forever()