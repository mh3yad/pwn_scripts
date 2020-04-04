from pwn import *
context(arch = 'i386', os = 'linux')
with open("file","r") as file:
        for line in file:
                print line
                s=remote("jh2i.com", 50031)
                print s.recv()
                s.send(line)
                a=s.recv()
                print a
                if "INCORRECT!" not in a:
                        print line
                        break




