# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:01:55 2023

@author: EricCC_Huang
"""
pwd = 'R10030190r'











###----------Use wmi to execute remote exe file.----------###(2023/06/14 Eric)
import wmi, win32api, win32
from socket import *

SW_SHOWNORMAL = 1

connection = wmi.WMI(computer = '10.109.37.105', user = 'COMPAL\EricCC_Huang', password = pwd)

process_startup = connection.Win32_ProcessStartup.new()
process_startup.ShowWindow = SW_SHOWNORMAL
process_id, result = connection.Win32_Process.Create(CommandLine="cmd.exe /c C:\\Users\\EricCC_Huang\\Desktop\\testbat.bat",ProcessStartupInformation=process_startup)
if result == 0:
  print("Process started successfully: %d" % process_id)
else:
  raise RuntimeError

"""
Not a GUI element.
"""
###----------Use pywinauto to set a connection.---------- (2023/06/07 Eric)
# from pywinauto import Application, Desktop


# #Connect to the remote desktop session
# remote_session = Desktop(backend="uia").RemoteDesktopConnect(address="10.109.55.23", username="COMPAL\EricCC_Huang", password="R10030190r")

# # Launch the application (.exe file)
# app = Application().start("C:\\Documents\\test.txt")

# # Wait for the application to start
# app.wait('visible')

# # Perform interactions with the application
# # For example, you can click a button or enter text in an input field
# # app.window().Button.click()
# # app.window().Edit.type_keys("Hello World")

# # Close the application
# app.kill()

# # Close the remote desktop session
# remote_session.close()

'''
Get done with ipconfig call but failed in executing exe.
'''
###----------Use winrm's Protocol and Session to build connection. (2023/06/06 ~ 06/07 Eric)
# import winrm
# from winrm.protocol import Protocol

# ip = '10.109.37.105'
# ip2 = '10.109.55.23'
# user = 'COMPAL\EricCC_Huang'
# pwd = 'R10030190r'
# cmdip = "ipconfig /all"
# cmd = "D: && D:/Released/92_RestartCadendeLicense_V0p1p0.exe"
# ps = "test.txt"
  
# url = f'http://{ip2}:5985/wsman'
# protocol = Protocol(endpoint = url, transport='ntlm', username = user, password = pwd, server_cert_validation = 'ignore')

# # Open the shell
# shell_id = protocol.open_shell()

#     # Execute the command
# command_id = protocol.run_command(shell_id, 'C:/Users/EricCC_Huang/Documents/test.txt')

#     # Get the command output
# std_out, std_err, status_code = protocol.get_command_output(shell_id, command_id)
    
#     # Print the output
# #print(std_err, std_out)

# # Close the shell
# protocol.cleanup_command(shell_id, command_id)
# protocol.close_shell(shell_id)

# session = winrm.Session(ip, auth = (user, pwd), transport = 'ntlm')
# # res = session.run_cmd(cmdip)
# # print(res.std_out)
# # for command in ps:
# #     res = session.run_cmd(command)
# #     print(res.std_err)
# res = session.run_cmd()
# print(res.std_err)
# # print('Something wrong: ', res.std_err)
# # print('Connection built: ', res.std_out)

'''
Paramiko is specifically designed for SSH communication and remote execution.
To start the service of SSH, you need to install OpenSSH Server and Client through Setting-> Apps-> Apps & features-> Optional features.
But I can't install it due to authorization.
'''
###----------Use paramiko to establish connection.----------### (2023/06/05;06/14 Eric)
# import paramiko, time, os, sys
# from decimal import Decimal, ROUND_HALF_UP
# from scp import SCPClient

# startTime = time.time()

# logList = []
# dateTime = 'Date & Time: '+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# currUser = 'User: ' + os.getlogin() + '\n'

# ip2 = '10.109.55.23'
# user = 'COMPAL\EricCC_Huang'
# pwd = 'R10030190r'
# cmdip = "ipconfig /all"

# #----------Establish SSH connection.----------
# # try:
# #     logList.append('=====Establish SSH connection.=====')
# #     ssh = paramiko.SSHClient()
# #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Allow connection to servers that don't have a host key.
# #     ssh.connect(ip2, username = user, password = pwd, timeout = 15)
# #     print("Connect to {}.".format(ip2))
# #     logList.append('Connect to {} successfully.'.format(ip2))
# # except paramiko.AuthenticationException:
# #     print("Fail to connect to {}.".format(ip2))
# #     logList.append('Fail to connect to {}. Exception.'.format(ip2))
# # except Exception as e:
# #     print(e)
# #     logList.append('Fail to connect to {}. Exception.'.format(ip2))


# # #Execute commands on the remote computer.
# # command1 = "C:/Users/EricCC_Huang/Documents/test.txt"

# # try:
# #     logList.append('Start to execute.')
# #     stdin, stdout, stderr = ssh.exec_command('ipconfig')
# #     logList.append('Command has been done.')
# # except Exception as e:
# #     print(e)
# #     logList.append('Command error.')

# # print(stdout.read())
# try:
#     ssh = paramiko.Transport((ip2, 22))
#     ssh.connect(username=user,password=pwd)
#     sftp = paramiko.SFTPClient.from_transport(ssh)
# except Exception as e:
#     print(e)

# f = sftp.open('C:/Users/EricCC_Huang/Documents/test.txt', mode = 'r', bufsize=-1)
# print(f.read())    
# #Close the SSH connection.
# ssh.close()

#logList.append('Execution over. It costs {} seconds.'.format(Decimal(str(time.time() - startTime)).quantize(Decimal('0.01'), rounding = ROUND_HALF_UP)))

# logPath = os.path.join(os.getcwd(), '{}'.format(os.getlogin() + ' ' + time.strftime("%Y%m%d-%H%M%S")))
# os.mkdir(logPath)
# with open(logPath + '/log.txt', 'w') as f:
#     for log in logList:
#         f.write(log + '\n')