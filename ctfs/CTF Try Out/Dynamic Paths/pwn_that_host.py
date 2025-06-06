from pwn import *


from dynamicpaths import parse_input, InputData
from config import *

if __name__ == "__main__":
    p = remote(HOST, PORT)
    context.log_level = "info"

    id = None
    while True:

        if id and (id.test_number_low == id.test_number_high):

            print("We're done!")
            print(p.recvline())
            break

        # consume the intro block we don't care about
        data = p.recvuntil("Test")
        print(data)

        # start running tests repeatedly
        test_number = b"Test" + p.recvline()  # test number
        print(test_number)

        dim = p.recvline()  # dimensions
        print(dim)

        grid = p.recvline()  # grid data
        print(grid)

        # construct our glob of text
        glob_of_text = b"".join([test_number, dim, grid])
        # make it ascii
        glob_of_text = glob_of_text.decode("utf-8")

        # get our input object
        id = parse_input(glob_of_text)

        print(id)

        # get our calculated response
        minimum_sum = id.generate_response()

        # send our calculated response to the server
        # note that sendline includes a newline
        p.sendline(str(minimum_sum))

        print(f"SOLVED {id.test_number_low}/{id.test_number_high}")

        # now we get a new test, go to the beginning of the loop
