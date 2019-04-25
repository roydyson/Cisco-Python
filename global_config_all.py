from netmiko import ConnectHandler
from datetime import datetime
from netmiko.ssh_exception import AuthenticationException, NetMikoTimeoutException
import xlrd
from pprint import pprint
import yaml

def main():
    today = datetime.now()

#Load data from YAML into Python dictionary
config_data = yaml.load(open('./newvlan.yaml'))
show_data = yaml.load(open('./qashow.yaml'))

#Load Jinja2 template
env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
dsw1_template = env.get_template('newvlan_dsw1.j2')

env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
dsw2_template = env.get_template('newvlan_dsw2.j2')

env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
qashow_template = env.get_template('qashow.j2')

#Render the template with data and print the output
print(dsw1_template.render(config_data))
dsw1cfg = open( "newvlan_dsw1" + "_.cfg", "w")
dsw1cfg.write(dsw1_template.render(config_data))

print(dsw2_template.render(config_data))
dsw2cfg = open( "newvlan_dsw2" + "_.cfg", "w")
dsw2cfg.write(dsw2_template.render(config_data))

print(qashow_template.render(config_data))
qashow = open( "qashow" + "_.cfg", "w")
qashow.write(qashow_template.render(show_data))

with open('newvlan_dsw1_.cfg', 'r') as f:
    dsw1_cmds = f.read().splitlines()



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


    }
