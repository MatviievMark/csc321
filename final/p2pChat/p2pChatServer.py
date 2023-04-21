import zmq

# create a context object
context = zmq.Context()

# create a socket object and bind to the server address
with context.socket(zmq.REP) as rep_socket:
    rep_socket.bind("tcp://*:5556")

    # receive and respond to messages
    while True:
        try:
            # receive the message from the client
            client_request = rep_socket.recv_string()
            print(f"Client request: {client_request}")

            # check if the user wants to exit
            if client_request == "exit":
                break

            # get the response from the user
            message = input("Enter the message here: ")
            rep_socket.send(message.encode())
            print("Message sent")
        except KeyboardInterrupt:
            break

# close the socket and context objects
context.term()
