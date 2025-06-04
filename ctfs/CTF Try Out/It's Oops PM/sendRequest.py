IP="94.237.54.54"
PORT=45594


import socket

def parse_response(response:str)->str:

    return response\
    .replace("Output",'')\
    .replace("Input",'')\
    .replace(":",'')\
    .strip()

def probe_host(ip, port, number):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))

        i=number

        foo = s.recv(1024)
        
        binary_input = f"{i:016b}"  # Format as 16-bit binary
        payload = binary_input.encode() + b'\n'
        s.sendall(payload)  # Send input
        response = s.recv(1024)  # Receive response

        output = response.decode().strip()

        output = parse_response(output)

        return output

if __name__ == "__main__":

    for i in range(2000, 7000, 51):
        response = probe_host(IP, PORT, 0)
        print(f"{i} = {response}")
