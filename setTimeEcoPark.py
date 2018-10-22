#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
from socket import *
import argparse
import datetime


def generateDateString():
    now = datetime.datetime.now()

    strYear = str(now.strftime("%y"))
    strMonth = str(now.strftime("%m"))
    strDay = str(now.strftime("%d"))

    strDayWeek = str(now.strftime("%w"))
    strDayWeek = int(strDayWeek) + 1
    strDayWeek = '%02d' % strDayWeek

    strHour = str(now.strftime("%H"))
    strMinute = str(now.strftime("%M"))

    return strMinute + strHour + strDayWeek + strDay + strMonth + strYear


def sendToSocket(host, port):
    addr = (host, port)
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    data = bytes.fromhex('57 45 43 46 47 03 02 FF 06' + generateDateString() + '00')

    if not data:
        udp_socket.close()
        sys.exit(1)

    udp_socket.sendto(data, addr)
    udp_socket.close()


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-ip', '--ip', required=True, help='ip xxx.xxx.xxx.xxx')
    parser.add_argument('-port', '--port', required=True, help='remote udp port')
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    sendToSocket(namespace.ip, int(namespace.port))
