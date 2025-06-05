IP="94.237.58.82"
PORT=54183

import socket
import time 
from mongologger import MongoLogger

ml = MongoLogger()

def now()->float:
    return time.time()

def parse_response(response:str)->str:

    return response\
    .replace("Output",'')\
    .replace("Input",'')\
    .replace(":",'')\
    .strip()

def number_to_bstring(n:int)->str:
    return f"{n:016b}"

def bstring_to_number(bstr:str)->int:
    return int(bstr,2)

def probe_host(ip, port, number):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))

        i=number

        # slurp buffer and discard it, we don't care about the contents before
        foo = s.recv(1024)
        
        binary_input = number_to_bstring(i)  # Format as 16-bit binary
        payload = binary_input.encode() + b'\n'
        s.sendall(payload)  # Send input
        response = s.recv(1024)  # Receive response

        output = response.decode().strip()

        output = parse_response(output)

        return output


def log_message(i:int, response:int, timestamp, message=None):
    ml.log(
        {
            "i (int)": i,
            "i (binary)": number_to_bstring(i),
            "response (int)": response,
            "response (binary)": number_to_bstring(response),
            "timestamp": timestamp,
            "timestamp (binary)": number_to_bstring(int(timestamp)),
            "message": message,
        }
    )

if __name__ == "__main__":

    for i_int in range(0, ((2**16)-1), 1):
        i_binary = number_to_bstring(i_int)

        if not ml.do_we_have_i(i_int):
            response_binary = probe_host(IP, PORT, i_int)

            while (response_binary == ''):
                print("WARN empty response for "+str(i_int))
                log_message(i_int, -1, now(), "EMPTY RESPONSE for i")
                print(ml.get_latest_entry())
                # retry
                response_binary = probe_host(IP, PORT, i_int)


            response_int = bstring_to_number(response_binary)

            log_message(i_int, response_int, now())
            print(ml.get_latest_entry())
        else:
            print("Already recorded "+str(i_int))