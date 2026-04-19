import xmlrpc.client

# Connect to the server using its URL and port
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Get user input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Call the remote functions and print the results
print("Addition:", server.add(a, b))
print("Subtraction:", server.subtract(a, b))