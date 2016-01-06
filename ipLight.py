import RPi.GPIO as gpio
import sys, os, socket
import ipaddress

print (ipaddress.get_lan_ip() + ' is the ip address of this system.')

ip = ipaddress.get_lan_ip()
