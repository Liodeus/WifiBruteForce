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
    SSIDS = list(Cell.all('wlan0'))

    for number, SSID in enumerate(SSIDS):
        if SSID.encrypted:
            if SSID.encryption_type == "wpa2":
                print("{}   |  {}  |    {}".format(SSID.encryption_type, SSID.address, SSID.ssid))
            else:
                print("{}    |  {}  |    {}".format(SSID.encryption_type, SSID.address, SSID.ssid))
        else:
            print("{}   |  {}  |    {}".format(SSID.encryption_type, SSID.address, SSID.ssid))



def bruteForce():
    # Verify if name exist
    wifiChoice = input("Wifi name : ")
    # Same verify
    dictionnaryPath = input("Dictionnary path : ")

    # if both exist try to connect
    # os.system(nmcli d wifi connect ssidName password 0123456789 iface wlan0)


if __name__ == '__main__':
    displayMenu()

