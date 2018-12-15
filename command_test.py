#-*- coding: utf-8 -*-
import subprocess

# command = ""
# ip_info = []

def simple_java():
	print("============= check ============")

# remote_server check
def simple_check():
	print("============= check ============")

# keygen creat
def ssh_keygen_chmod():
	command = "chmod 700 ~/.ssh;chmod 600 ~/.ssh/id_rsa;chmod 644 ~/.ssh/id_rsa.pub;chmod 644 ~/.ssh/authorized_keys;chmod 644 ~/.ssh/known_hosts"
	result = subprocess.Popen(command, shell=True)

def simple_keygen(col, key="~/.ssh/id_rsa.pub", file="~/.ssh/authorized_keys"):
	print("============= keygen ============ -r")
	command= "sshpass -p "+str(col[2])+" scp -o StrictHostKeyChecking=no "+file+" "+str(col[1])+"@"+str(col[0])+":"+file+" | ping "+ str(col[0]) +" -c 1"
	result = subprocess.Popen(command, shell=True)
	print(result)

# scp function
def simple_scp():
	print("============= scp ============")

# yum install
def simple_install(modul):
	print("============= install ============")
	command = "sudo yum install -y" + modul
	result = subprocess.Popen(command, shell=True)
# yum list
def simple_list_check():
	print("============= list ============")

# remote command
def simple_command(col, com):
	command = "sshpass -p " +str(col[2])+" ssh -o StrictHostKeyChecking=no "+str(col[1])+"@"+str(col[0])+" "+com # + " | ping "+ str(col[0]) +" -c 1"
	print(command)
	result = subprocess.Popen(command, shell=True)
	print(result)

# scp command
def simple_ssh(col, file, remote="~/"):
	command= "sshpass -p "+str(col[2])+" scp -o StrictHostKeyChecking=no "+file+" "+str(col[1])+"@"+str(col[0])+":"+remote+file + " | ping "+ str(col[0]) +" -c 1"
	print(command)
	result = subprocess.Popen(command, shell=True)
	print(result)

def log_error():
	print("============= log_error ============")

def log_pass():
	print("============= log_pass ============")


def word_change():
	print("============= word_change ============")
	command = "sed -e 's/transport.host: 192.168.56.101/transport.host: 192.168.56.103/g' config/elasticsearch.yml > config/elasticsearch1.yml"
if __name__ == '__main__':
	# simple_command(['210.92.91.236','ezfarm','ezfarm#3414'], 'ls /')
	simple_ssh(['192.168.56.101','hadoop','hadoop'], "ip_test.csv")
	simple_ssh(['210.92.91.236','ezfarm','ezfarm#3414'], "ip_test.csv")