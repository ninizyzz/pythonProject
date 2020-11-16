import win32com.client

strComputer = "192.168.1.128"
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
objSWbemServices = objWMIService.ConnectServer(strComputer, "root\cimv2")
colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_LogicalDisk")

for objItem in colItems:
    print(objItem.Size)
