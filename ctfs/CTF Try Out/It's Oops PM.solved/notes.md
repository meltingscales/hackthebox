```
┌─[user@parrot]─[~/Git]
└──╼ $nc 94.237.58.82 54183
The input must be a binary signal of 16 bits.

Input : 102010
Error : Invalid length of bits.

Input : 1000000000010000
Output: 1100001110110000
```


# Notes

## 10

10 = `0000000000001010` crashes it?

## Parallel

When I ran a BUNCH of `gather_data_*.py` scripts in parallel, I'd get:

    Error  Command 'ghdl -a -v key.vhdl' returned non-zero exit status 2

Okay! So! This is a microcomputer. I'm probably sending it opcodes!

I need to think about what opcodes do ....stuff.

EDIT: I have files in `./hardware_its_oops_pm` that I can look at now. I didn't realize this.

## Cheating

I'm going to look at someone else's writeup to try and understand how to complete this challenge...

<https://github.com/hackthebox/business-ctf-2024/tree/main/hardware/It's%20Oops%20PM%20%5BVery%20Easy%5D>

So...I just needed to read the VHDL files and understand what bit-string to send to the server.

At least I wrote a MongoDB data scraper! This exercise wasn't totally useless.

    nc 94.237.62.237 53428
    1111111111101001    