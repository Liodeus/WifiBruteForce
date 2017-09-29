#!/usr/bin/env Python
# -*- coding: utf-8 -*-

import os
from wifi import Cell


def displayMenu():
    print("1 - See available network ")
    print("2 - Brute Force ")
    print()
    choice = input("Choice : ")
    
    if choice == "1":
        print("\n\n\n")
        displaySSIDS()
        print("\n\n\n")
        displayMenu()

    if choice == "2":
        bruteForce()


def displaySSIDS():
    print("Wait a few seconds...")
    SSIDS = list(Cell.all('wlan0'))
    # for number, SSID in enumerate(SSIDS):
    #     if SSID.encrypted:
    #         if SSID.encryption_type == "wpa2":
    #             print("{}   |  {}  |    {}".format(SSID.encryption_type, SSID.address, SSID.ssid))
    #         else:
    #             print("{}    |  {}  |    {}".format(SSID.encryption_type, SSID.address, SSID.ssid))
    #     else:
    #         print("{}   |  {}  |    {}".format(SSID.encryption_type, SSID.address, SSID.ssid))



def bruteForce():
    print("Wait a few seconds...")
    lstSSID = list(x.ssid for x in Cell.all('wlan0'))

    flagChoice = False

    while not flagChoice:
        wifiChoice = input("Wifi name : ").strip()
        if wifiChoice not in lstSSID:
            print("Doesn't exist... try again...")
        else:
            flagChoice = True

    # Same verify
    flagPath = False

    while not flagPath:
        dictionnaryPath = input("Dictionnary path : ").strip()
        if os.path.exists(dictionnaryPath):
            flagPath = True
        else:
            print("Doesn't exist... try again...")

    # /usr/share/wordlists

    # if both exist try to connect
    # os.system(nmcli d wifi connect ssidName password 0123456789 iface wlan0)


if __name__ == '__main__':
    displayMenu()

# https://stackoverflow.com/questions/21662351/connect-wifi-with-python-or-linux-terminal