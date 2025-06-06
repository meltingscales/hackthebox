"""
Gather data by initiating a single TCP connection, sending bytes, and then disconnecting. Repeat until you're done.
"""
import socket
from mongologger import MongoLogger
from config import *
from util import *

ml = MongoLogger("itsoopspm", "gather_data_single")


class ProbeHostResponse(object):
    def __init__(self, pre_data:bytes, raw_output:bytes, parsed_output:str):
        self.pre_data = pre_data
        self.raw_output = raw_output
        self.parsed_output = parsed_output

    def as_dict(self):
        return {
            "pre_data": self.pre_data,
            "raw_output": self.raw_output,
            "parsed_output": self.parsed_output
        }

def probe_host(ip, port, number):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))

        i=number

        # receive TCP, we don't care about the contents before
        pre_data = s.recv(1024)
        
        binary_input = number_to_bstring(i)  # Format as 16-bit binary
        payload = binary_input.encode() + b'\n'
        s.sendall(payload)  # Send input
        binary_response = s.recv(1024)  # Receive response

        output = binary_response.decode().strip()

        parsed_output = parse_response(output)

        return ProbeHostResponse(pre_data, binary_response, parsed_output)


def log_message(input:int, phr:ProbeHostResponse, timestamp, message=None):

    try:
        response_binary=number_to_bstring(bstring_to_number(phr.parsed_output))
        response_int = bstring_to_number(phr.parsed_output)
    except ValueError:
        response_binary=None
        response_int=None

    ml.log(
        {
            "input (int)": input,
            "input (binary)": number_to_bstring(input),
            "response (int)": response_int,
            "response (binary)": response_binary,
            "timestamp": timestamp,
            "timestamp (binary)": number_to_bstring(int(timestamp)),
            "message": message,
            "response_pre": phr.pre_data,
            "response_post": phr.raw_output,
        }
    )

if __name__ == "__main__":

    for i_int in range(0, ((2**16)-1), 1):
        i_binary = number_to_bstring(i_int)

        if not ml.do_we_have_i(i_int):
            response = probe_host(IP, PORT, i_int)

            while response.parsed_output == '':
                print("WARN empty response for "+str(i_int))
                log_message(i_int, response, now(), "EMPTY RESPONSE for i")
                print(ml.get_latest_entry())
                # retry
                response = probe_host(IP, PORT, i_int)


            log_message(i_int, response, now())
            print(ml.get_latest_entry())
        else:
            print("Already recorded "+str(i_int))