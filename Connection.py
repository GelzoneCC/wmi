# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:01:55 2023

@author: GelzoneCC
"""
pwd = 'xxx'

###----------Use wmi to execute remote exe file.----------###
import wmi, win32api, win32

SW_SHOWMINIMIZED = 1

connection = wmi.WMI(computer = 'ServerIP', user = 'UserName', password = pwd)

process_startup = connection.Win32_ProcessStartup.new()
process_startup.ShowWindow = SW_SHOWMINIMIZED
# Execute a .bat file on the server desktop.
process_id, result = connection.Win32_Process.Create(CommandLine = "cmd.exe /c C:\\Users\\UserName\\Desktop\\testbat.bat", ProcessStartupInformation = process_startup)
if result == 0:
  print("Process started successfully: %d" % process_id)
else:
  raise RuntimeError("Problem creating process: %d" % result)

# List all running processes.
for process in connection.Win32_Process():
    print(process.ProcessId, process.Name)

# Show the IP and MAC addresses for IP-enabled network interfaces.
for interface in connection.Win32_NetworkAdapterConfiguration(IPEnabled = 1):
    print(interface.Description, interface.MACAddress)
    for ip_address in interface.IPAddress:
        print (ip_address)
