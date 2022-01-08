import requests
import json
import socket
import os
from datetime import datetime
import time
from skpy import Skype

def alert_BH():

    #send message sky
    sk = Skype("hbpu002@gmail.com", "chaocochao@123")  # connect to Skype

    ch = sk.chats["19:3389c0e93aac41efb74569cdf990d342@thread.skype"]
    now = datetime.now()

    def telnet(hostname, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result_e = sock.connect_ex((hostname, port))
        if result_e != 0:
            time.sleep(5)
            result_e1 = sock.connect_ex((hostname, port))
            if result_e1 != 0:
                ch.sendMsg(hostname + ' Error Service ' + str(port))
        sock.close()

    def ping(hostname):
        response = os.system("ping -n 1 " + hostname)
        if response != 0:
            time.sleep(5)
            response1 = os.system("ping -n 1 " + hostname)
            if response1 != 0:
                ch.sendMsg(hostname + ' Error Network ')

    # https://www.turkeyonlinetravels.com
    # 51.195.121.76    
    try:
        request = requests.get('https://www.turkeyonlinetravels.com')
        html = request.content
        lo = str(html)
        a = 'Turkey Best Selling Tours'
        if a in lo:
            print('okela1')
        else:
            ch = sk.chats["19:3389c0e93aac41efb74569cdf990d342@thread.skype"]
            ch.sendMsg('Website turkeyonlinetravels error on 51.195.121.75')
    except:
        ch = sk.chats["19:3389c0e93aac41efb74569cdf990d342@thread.skype"]
        ch.sendMsg('Website not turkeyonlinetravels access')
    
    # https://www.turkeyimmigration.org
    # 51.195.121.76
    try:
        request = requests.get('https://www.turkeyimmigration.org')
        html = request.content
        lo = str(html)
        a = 'Global Immigration Services Limited is company travelers through your trip to Turkey with our visa services. We give you advice and support for visa application'
        if a in lo:
            print('okela2')
        else:
            ch = sk.chats["19:3389c0e93aac41efb74569cdf990d342@thread.skype"]
            ch.sendMsg('Website turkeyimmigration error on 51.195.121.76')
    except:
        ch = sk.chats["19:3389c0e93aac41efb74569cdf990d342@thread.skype"]
        ch.sendMsg('Website not turkeyimmigration access')

    # https://www.indianimmigration.org/
    # 52.42.7.44
    try:
        request = requests.get('https://www.indianimmigration.org')
        html = request.content
        lo = str(html)
        a = 'Google Tag Manager (noscript)'
        if a in lo:
            print('okela3')
        else:
            ch = sk.chats["19:3389c0e93aac41efb74569cdf990d342@thread.skype"]
            ch.sendMsg('Website indianimmigration.org error on 52.42.7.44')
    except:
        ch = sk.chats["19:3389c0e93aac41efb74569cdf990d342@thread.skype"]
        ch.sendMsg('Website not indianimmigration.org access')
    
    # https://www.kenyaetravel.org/
    # 52.33.158.146
    try:
        request = requests.get('https://www.kenyaetravel.org')
        html = request.content
        lo = str(html)
        a = 'contact-us'
        if a in lo:
            print('okela4')
        else:
            ch = sk.chats["19:3389c0e93aac41efb74569cdf990d342@thread.skype"]
            ch.sendMsg('Website kenyaetravel.org error on 52.33.158.146')
    except:
        ch = sk.chats["19:3389c0e93aac41efb74569cdf990d342@thread.skype"]
        ch.sendMsg('Website not kenyaetravel.org access on 52.33.158.146')

    # https://www.offshorecompanycorp.com
    # 54.203.220.180
    try:
        request = requests.get('https://www.offshorecompanycorp.com')
        html = request.content
        lo = str(html)
        a = 'about-us'
        if a in lo:
            print('okela5')
        else:
            ch = sk.chats["19:3389c0e93aac41efb74569cdf990d342@thread.skype"]
            ch.sendMsg('Website offshorecompanycorp.com error on 54.203.220.180')
    except:
        ch = sk.chats["19:3389c0e93aac41efb74569cdf990d342@thread.skype"]
        ch.sendMsg('Website not offshorecompanycorp.com access on 54.203.220.180')
                
    print("IT is time:", now)
    time.sleep(180)

while True:
     try:
         alert_BH()
     except:
         pass

