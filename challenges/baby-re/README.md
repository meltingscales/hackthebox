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