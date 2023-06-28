# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:01:55 2023

@author: GelzoneCC
"""
pwd = 'xxx'

###----------Use wmi to execute remote exe file.----------###
import wmi, win32api, win32
from socket import *

SW_SHOWNORMAL = 1

connection = wmi.WMI(computer = 'ServerSideIP', user = 'UserName', password = pwd)

process_startup = connection.Win32_ProcessStartup.new()
process_startup.ShowWindow = SW_SHOWNORMAL
# Execute a .bat file on the server desktop.
process_id, result = connection.Win32_Process.Create(CommandLine="cmd.exe /c C:\\Users\\UserName\\Desktop\\testbat.bat",ProcessStartupInformation=process_startup)
if result == 0:
  print("Process started successfully: %d" % process_id)
else:
  raise RuntimeError
