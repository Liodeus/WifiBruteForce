#!/usr/bin/env Python
# -*- coding: utf-8 -*-

import os
from wifi import Cell



SSIDS = list(Cell.all('wlan0'))

for SSID in SSIDS:
    if SSID.encrypted:
        if SSID.encryption_type == "wpa2":
            print(SSID.encryption_type, '  |  ', SSID.address, '  |  ',SSID.ssid)
        else:
            print(SSID.encryption_type, '   |  ', SSID.address, '  |  ',SSID.ssid)
    else:
        print('None   |  ',SSID.address, '  |  ',SSID.ssid)

# nmcli d wifi connect HUAWEI_P9lite_01F4 password 0123456789 iface wlan0