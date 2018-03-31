#!/usr/bin/env python

import csv
from netmiko import Netmiko
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

deviceConfig = {
    'host': '10.0.0.29',
    'username': 'admin',
    'password': 'admin',
    'device_type': 'cisco_ios',
}

def getRouterInterface(deviceConfig={}):
    net_connect = Netmiko(**deviceConfig)
    output = net_connect.send_command('show ip int brief')
    net_connect.disconnect()
    return str(output)

def routerInterfaceToCsv(routerInterface, writeToFile='router_int_output.csv'):
    '''router Interface string-
    Interface     IP-Address     OK?  Method  Status                  Protocol
    Ethernet0     10.0.0.29      YES  DHCP    up                      up
    '''
    fileHandler = open(writeToFile, 'w')
    with fileHandler:
        csvWriter = csv.writer(fileHandler, delimiter=';')

        routerInterfaceLines = routerInterface.split('\n')
        for line in routerInterfaceLines:
            csvWriter.writerow([ o for o in routerInterfaceLines.split(' ') if o])

    print('Output written to: ' + writeToFile)

def mailRouterInterface(sendTo='choudharynidhi9@gmail.com', intOutputFile='router_int_output.csv', server='localhost'):
    msg = MIMEMultipart()
    sendFrom = sendTo
    msg['From'] = sendFrom
    msg['To'] = sendTo
    msg['Subject'] = 'Router Interface output'

    msg.attach(MIMEText('Router Interface output attached.'))

    fileHandler = open(intOutputFile, "rb")
    part = MIMEApplication(fileHandler.read(), Name=basename(intOutputFile))
    part['Content-Disposition'] = 'attachment; filename="{0}"'.format(basename(intOutputFile))
    msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.sendmail(sendFrom, sendTo, msg.as_string())
    smtp.close()

    print('Mail Sent to: ', sendTo)

def main():
    routerInterface = getRouterInterface()
    routerInterfaceToCsv(routerInterface)

    mailRouterInterface(sendTo='choudharynidhi9@gmail.com', intOutputFile='router_int_output.csv')

if __name__ == "__main__":
    main()
