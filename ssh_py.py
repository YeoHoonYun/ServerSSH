#-*- coding: utf-8 -*-

from multiprocessing import Process
from optparse import OptionParser
import csv, sys, time
import command_test

class ssh_test():
	# def __init__(self, result, com, func):
	def __init__(self, result, com):
		self.result = result
		self.command = com
		# self.func = func

	def ssh_keygen_chmod(self):
		command = "chmod 700 ~/.ssh;chmod 600 ~/.ssh/id_rsa;chmod 644 ~/.ssh/id_rsa.pub;chmod 644 ~/.ssh/authorized_keys;chmod 644 ~/.ssh/known_hosts"
		result = subprocess.Popen(command, shell=True)

	def mul_pro(self):
		pro_list = []
		for result in self.result:
			pro_list.append(Process(target = command_test.simple_command, args =(result, self.command))) # 프로세스 갯수 설정 : processes=4, 

		#process start
		for pro in pro_list:
			pro.daemon = True
			pro.start()
			time.sleep(1)

		for pro in pro_list:
			pro.join()

def csv_parser(col, filename='ip_test.csv'):
	#1번부터 시작
	with open(filename, 'r') as f:
		reader = csv.DictReader(f, delimiter=',')
		csv_list = []
		header = []
		for col in col:
			header.append(reader.fieldnames[col-1])

		for row in reader:
			result = []
			for head in header:
				#print(row[head])
				result.append(row[head])
			csv_list.append(result)
	return csv_list

if __name__ == '__main__':
	parser = OptionParser()
	# # type
	# parser.add_option("-T", "--type", dest="type", help="login, file")

	# #user_info
	# parser.add_option("-U", "--user", dest="user", help="")
	# parser.add_option("-P", "--passwd", dest="passwd", help="")
	# parser.add_option("-I", "--ip", dest="ip", help="")

	# #input side
	# parser.add_option("-C", "--csv", dest="csvfile", help="Input csvfile path in ip, user, password")
	# parser.add_option("-M", "--mysql", dest="mysql", help="")

	# #output side
	# parser.add_option("-M", "--command", dest="command", help="")
	# parser.add_option("-S", "--script", dest="script", help="")
	
	# (options, args) = parser.parse_args()
	# print(options.type)

	# # if options.type == None:
	# # 	print("Type 값을 입력하세요.")
	# 	#sys.exit()

	# if options.type == "login":
	# 	server_ip = [options.ip, options.user, options.passwd]

	# if options.type == "file":
	# 	if options.csvfile == True:
	# 		try:
	# 			server_ip = csv_parser([1,2,3], filename=options.csvfile)
	# 		except:
	# 			print("파일이 없습니다.")

	# 	#mysql modul
	# 	elif options.mysql == True:
	# 		server_ip = csv_parser([1,2,3], filename=options.csvfile)
		
	# 	else:
	# 		print("지원 하지 않습니다.")

	# if options.command == True:
	# 	command = options.command

	# #script modul
	# if options.command == True:
	# 	command = options.command
	

	command = "ls /"
	server_ip = csv_parser([1,2,3])

	#실행할 함수들 입력
	# ssh_test = ssh_test(function,server_ip, command)
	ssh_test = ssh_test(server_ip, command)
	ssh_test.mul_pro()