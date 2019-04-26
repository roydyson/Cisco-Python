from jinja2 import Environment, FileSystemLoader
import time
#Import YAML module
import yaml
from datetime import datetime
import xlrd
#Load data from YAML into Python dictionary
config_data = yaml.load(open('./config_gen.yaml'))
#config_gen_name = yaml.load(open('./config_gen_name.yaml'))
#Load Jinja2 template
env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
config_gen = env.get_template('config_gen.j2')
#config_gen_name = env.get_template('config_gen_name.j2')

#Render the template with data and print the output
print(config_gen.render(config_data))
#dsw1cfg = open( "newvlan_dsw1" + "_.cfg", "w")
(config_gen.render(config_data))

#Render the template with data and print the output
#print(config_gen_name.render(config_data))
#dsw1cfg = open( "newvlan_dsw1" + "_.cfg", "w")
#(config_gen_name.render(config_data))

    #f = open("SHOW_" + hostname + ".py", "w")

f = open("vty_ssh" + ".py", "w")
n = open("vty_ssh" + ".j2", "w")
o = open("vty_ssh" + ".yaml", "w")
f.write(config_gen.render(config_data))
f.close()
o.write('example_1: example')
o.close()
n.write('{{  example_1  }}')
n.close()
