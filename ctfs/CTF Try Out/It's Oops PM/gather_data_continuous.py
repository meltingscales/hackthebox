"""
Gather data by initiating a single TCP connection, sending bytes, and then continuing to send bytes.
"""
import util
from config import *
from util import *

if __name__ == "__main__":

    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP, PORT))

        i = 22

        # receive TCP, we don't care about the contents before. we only have to do this once.
        pre_data = s.recv(1024)

        while True:
            binary_input = number_to_bstring(i)  # Format as 16-bit binary
            payload = binary_input.encode() + b'\n'
            s.sendall(payload)  # Send input
            binary_response = s.recv(1024)  # Receive response

            output = binary_response.decode().strip()

            parsed_output = parse_response(output)
            try:
                int_output = util.bstring_to_number(parsed_output)
            except ValueError:
                int_output=-1

            print (pre_data, binary_response, parsed_output)

            print(f"{i}={int_output}")
            i+=1

