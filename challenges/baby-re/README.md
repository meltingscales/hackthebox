# Baby_RE

Zip Password: hackthebox
sha256: 13bdad272ee08f609bd41e7d24a3e2f8581d3a07e9e42fce92d3dd35d38da160 

<https://medium.com/@jacob16682/reverse-engineering-using-radare2-588775ea38d5>

## Writeup

### Method 1

1.  Run `strings` on `baby`.
2.  Enter `abcde122313\n` into STDIN for `baby`.
3.  Syrup?

### Method 2

1.  Run `radare2 baby`.
2.  Type `v` to enter visual mode.
3.  Search for the magic string/key.
4.  Syrup?

Alternatively, `rabin2 -z baby` will give you the string.

### Method 3

1.  Run `r2 baby`.
2.  Type `aaa` to analyze functions.
3.  Type `s main` to 'seek' to the `main` function.
4.  Type `VV` to enter graph mode.

Example output:

```
[0x00001155]> 0x1155 # int main (int argc, char **argv, char **envp);  
                       │ mov rdi, rax                                                                                │                      
                       │ ; int strcmp(const char *s1, const char *s2)                                                │                      
                       │ call sym.imp.strcmp;[oc]                                                                    │                      
                       │ test eax, eax                                                                               │                      
                       │ jne 0x11da                                                                                  │                      
                       └───────────────────────────────────────────────────────────────────────────────┘                      
                               f t                                                                                            
                               │ │                                                                                            
                               │ └────────────────────────────────────┐                                                       
                            ┌──┘                                            │                                                       
                            │                                               │                                                       
                        ┌───────────────────────────────────┐    ┌──────────────────────────────────┐                        
                        │  0x11a3 [oe]                            │    │  0x11da [of]                           │                        
                        │ ; 'HTB{B4BY'                            │    │ ; const char *s                        │                        
                        │ movabs rax, 0x594234427b425448          │    │ ; CODE XREF from main @ 0x11a1         │                        
                        │ ; '_R3V_TH4'                            │    │ ; 0x2060                               │                        
                        │ movabs rdx, 0x3448545f5633525f          │    │ ; "Try again later."                   │                        
                        │ mov qword [s], rax                      │    │ lea rdi, str.Try_again_later.          │                        
                        │ mov qword [var_38h], rdx                │    │ ; int puts(const char *s)              │                        
                        │ ; 'TS_E'                                │    │ call sym.imp.puts;[oa]                 │                        
                        │ mov dword [var_30h], 0x455f5354         │    └──────────────────────────────────┘                        
                        │ ; 'Z}'                                  │        v                                                       
                        │ mov word [var_2ch], 0x7d5a              │        │                                                       
                        │ lea rax, [s]                            │        │                                                       
                        │ ; const char *s                         │        │                                                       
                        │ mov rdi, rax                            │        │                                                       
                        │ ; int puts(const char *s)               │        │                                                       
                        │ call sym.imp.puts;[oa]                  │        │                                                       
                        │ jmp 0x11e6                              │        │                                                       
                        └───────────────────────────────────┘        │                                                       
                            v                                              │                                                       
                            │                                              │                                                       
```