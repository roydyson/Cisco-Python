from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
import time
#Import YAML module
import yaml
from datetime import datetime
import xlrd

#infoFromMac = open( "infoFromMac.yaml", "w")
#dsw1cfg = open( "newvlan_dsw1" + "_.cfg", "w")

#Load data from YAML into Python dictionary
config_data = yaml.load(open('./infoFromMac.yaml'))

#Load Jinja2 template
env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)

infoFromMac = env.get_template('infoFromMac.j2')
vlan = env.get_template('change_vlan.j2')

cmd = (infoFromMac.render(config_data))
change = (vlan.render(config_data))

#Render the template with data and print the output
print(infoFromMac.render(config_data))
print(vlan.render(config_data))



#dsw1cfg = open( "newvlan_dsw1" + "_.cfg", "w")


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
#            'global_delay_factor': 5,


        }

    print ("logging into device: ", hostname , str( datetime.now()))

    f = open("CFG_" + hostname + ".dun", "w")
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command(cmd)
    print(output)
    show = output
    output_ver = (show.find('G'))
    print(output_ver)
#    print(output)
#    show = output.readall()
    #print(len(show))

    #print(output_ver)
#    print(show[output_ver:(output_ver + 8)])

    interface = (show[output_ver:(output_ver + 8)])
#    print(interface)
#    guy = interface
    configer = change
    space = [ ]
#    showmefirst = (('show run int') + (interface))
#    print(showmefirst)
#    output1 = net_connect.send_command_timing(('show run int') + ' ' + (interface))
#    output2 = net_connect.send_command_timing(('show int status | in') + ' ' + (interface))
#    output3 = net_connect.send_command_timing(('show int') + ' ' + (interface))
    commands = ['interface']
    switchport = ['interface']

    forme = [interface, 'switchport mode access']
    dun = change
#    output_test = net_connect.send_config_set(forme)
    output_test = net_connect.send_config_set('interface' + ' ' + interface + '\n' +  change)
#    print(configer)
#    print(switchport)
#    output4 = net_connect.send_config_set("int")
#    print(output1)
#    print(output2)
#    print(output3)
#    print(output4)
    print(output_test)

    f.write(output)
    f.close()
