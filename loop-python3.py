#!/usr/bin/python3
# coding: utf-8
#---------------------------
# Writed By WitBlack HAcker
#---------------------------
# Version : 1.0.2
try:
	import os
	import sys
	from sys import exit
	from time import sleep
	from termcolor import colored
except:
	print("Erorr!\nSome deepends not installed!")
else:
	if len(sys.argv) == 1:
		print(colored('NOTE: ','yellow') + colored('You can use -h or --help for see help list.','blue'))
	if '-h' in list(map(str.lower,sys.argv)) or '--help' in list(map(str.lower,sys.argv)):
		print(colored('~~~~~~~~~','blue'))
		print(colored('HELP MENU','yellow'))
		print(colored('~~~~~~~~~','blue'))
		print(colored('Switchs:','green'))
		print(colored('	-h , --help    ~>   Get help list','white'))
		print(colored('	-c , --command ~>   Set command in line (Optinal)','white'))
		print(colored('	-s , --sleep    ~>   Sleep time beetwen commands (By sec)','white'))
		print('')
		print(colored('Note:','green'))
		print(colored('	You can enter script without switch and enter value in app.','white'))
	else:
		if '-c' in list(map(str.lower,sys.argv)) or '--command' in list(map(str.lower,sys.argv)):
			if '-c' in list(map(str.lower,sys.argv)):
				Command = sys.argv[list(map(str.lower,sys.argv)).index('-c') + 1]
			else:
				Command = sys.argv[list(map(str.lower,sys.argv)).index('--command') + 1]
		else:
			try:
				Command = input("Enter command: ")
			except:
				exit(0)
		if '-s' in list(map(str.lower,sys.argv)) or '--sleep' in list(map(str.lower,sys.argv)):
			if '-s' in list(map(str.lower,sys.argv)):
				try:
					int(sys.argv[list(map(str.lower,sys.argv)).index('-s') + 1])
				except:
					print(colored('[!] Invalid sleep time number.','yellow'))
					exit(1)
				else:
					Time = int(sys.argv[list(map(str.lower,sys.argv)).index('-s') + 1])
			else:
				try:
					int(sys.argv[list(map(str.lower,sys.argv)).index('--sleep') + 1])
				except:
					print(colored('[!] Invalid sleep time number.','yellow'))
					exit(1)
				else:
					Time = int(sys.argv[list(map(str.lower,sys.argv)).index('--sleep') + 1])
		else:
			while True:
				try:
					try:
						Time = input(colored("Sleep by sec (Default=1) (q to exit): ",'white'))
					except:
						exit(0)
					if str.lower(Time) == 'q':
						print(colored('[*] Exit with user request.','yellow'))
						exit(0)
					if Time == '':
						Time = int(1)
					else:
						Time = int(Time)
				except:
					print(colored("Time number is invalid! Try some else.",'yellow'))
					sleep(0.5)
				else:
					break
		if os.name == 'nt':
			OS = 'Windows'
		elif os.name == 'posix':
			OS = 'Linux'
		else:
			print(colored('Your Operation system not supported! :(','yellow'))
			exit(1)
		def clear():
			if OS == 'Windwos':
				os.system('cls')
			else:
				os.system('clear')
		print(colored('[+] Use CTRL + C to break.','yellow'))
		sleep(1)
		while True:
			try:
				clear()
				print(os.popen(Command).read())
				sleep(Time)
			except:
				print(colored("\nInvalid command or exit with client request.",'yellow'))
				exit(0)
