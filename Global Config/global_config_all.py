from netmiko import ConnectHandler
from datetime import datetime
from netmiko.ssh_exception import AuthenticationException, NetMikoTimeoutException
import xlrd
from pprint import pprint
import yaml

def main():
    today = datetime.now()

with open('qashow.cfg', 'r') as f:
    qashow = f.read().rstrip()
print(qashow)

workbook = xlrd.open_workbook(r"c:\GitHub\Cisco-Python\automation-lab.xlsx")

sheet = workbook.sheet_by_index(0)

for index in range(1, sheet.nrows):
    hostname = sheet.row(index)[0].value
    ipaddr = sheet.row(index)[1].value
    username = sheet.row(index)[2].value
    password = sheet.row(index)[3].value
    enable_password = sheet.row(index)[4].value
    vendor = sheet.row(index)[5].value

    device = {
            'device_type': vendor,
            'ip': ipaddr,
            'username': username,
            'password': password,
            'secret': enable_password,
            'global_delay_factor': 6,


        }

    print ("logging into device: ", hostname , str( datetime.now()))



#for equipment in all_devices:
    f = open("SHOW_" + hostname + ".qa", "w")
    net_connect = ConnectHandler(**device)
    qa_show = net_connect.send_command_timing(qashow)
    qa_show_header = "\n++++++++++++++++++++++++++++++++++++\n"
    print(qashow)


    f.write(qa_show_header)
    f.write(qa_show)
    f.close()
