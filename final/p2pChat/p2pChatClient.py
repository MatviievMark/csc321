import zmq

# create a context object
context = zmq.Context()

# create a socket object and connect to the server
print("Connecting to hello world server...")
with context.socket(zmq.REQ) as req_socket:
    req_socket.connect("tcp://node00:5556")

    # send and receive messages
    while True:
        try:
            # get user input
            message = input("Type your message here: ")

            # check if the user wants to exit
            if message == "exit":
                break

            # send the message
            req_socket.send(message.encode())

            # receive the response
            response = req_socket.recv()

            # print the response
            print(f"Received reply: {response.decode()}")
        except KeyboardInterrupt:
            break

# close the socket and context objects
context.term()
