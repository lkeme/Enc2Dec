#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
@author: Lkeme
@contact: Useri@live.cn
@file: sign.py
@time: 2019/5/31
"""
import hashlib

try:
    from urllib import urlencode
except:
    from urllib.parse import urlencode

# iOS 6680
# app_key = '27eb53fc9058f8c3'
# app_secret = 'c2ed53a74eeefe3cf99fbd01d8c9c375'
# 云视听 TV
# app_key = '4409e2ce8ffd12b8'
# app_secret = '59b43e04ad6965f34319062b478f83dd'
# Android
app_key = '1d8b6e7d45233436'
app_secret = '560c52ccd288fed045859ed18bffd973'


# 计算sign
def calc_sign(params, salt):
    sign_hash = hashlib.md5()
    sign_hash.update(f"{urlencode(params)}{salt}".encode())
    return sign_hash.hexdigest()


if __name__ == '__main__':
    payload = {'sex': 1, 'age': 1, 'name': 'lkeme'}
    print('计算SIGN结果', calc_sign(payload, app_secret))
    # 计算SIGN结果 f9d6ba632d58e2fe592e69d1c3b12fa7
