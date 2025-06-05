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