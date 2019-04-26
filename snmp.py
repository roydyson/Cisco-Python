from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
import time
#Import YAML module
import yaml
from datetime import datetime
import xlrd

snmp = open( "snmp.yaml", "w")
#dsw1cfg = open( "newvlan_dsw1" + "_.cfg", "w")

#Load data from YAML into Python dictionary
config_data = yaml.load(open('./snmp.yaml'))

#Load Jinja2 template
env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
snmp = env.get_template('snmp.j2')

#Render the template with data and print the output
print(session_timeout.render(config_data))
#dsw1cfg = open( "newvlan_dsw1" + "_.cfg", "w")
(snmp.render(config_data))



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
            'global_delay_factor': 0,


        }

    print ("logging into device: ", hostname , str( datetime.now()))

    f = open("CFG_" + hostname + ".dun", "w")
    net_connect = ConnectHandler(**device)
    qashow = net_connect.send_config_set(session_timeout.render(config_data))
    print(qashow)

    f.write(qashow)
    f.close()