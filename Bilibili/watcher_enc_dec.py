#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Lkeme
@contact: Useri@live.cn
@file: watcher_enc_dec.py
@time: 2019-6-11
"""
import sys
from Crypto.Cipher import AES
import base64
import hashlib

PY2 = sys.version_info[0] == 2

if PY2:
    def s(x):
        return x.encode('utf-8') if isinstance(x, unicode) else x


    b = s
else:
    def s(x):
        return x.decode('utf-8') if isinstance(x, bytes) else x


    def b(x):
        return x.encode('utf-8') if not isinstance(x, bytes) else x

BS = AES.block_size
# 加密算法
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
# 解密算法
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


class AESCipher:

    def __init__(self, key, iv):
        self.key = key.encode("utf-8")
        self.iv = iv.encode("utf-8")
        self.space = "".encode("utf-8")
        self.__BS = 16

    @property
    def BS(self):
        return self.__BS

    # 加密
    def encrypt(self, dec):
        msg = b(dec)
        pad = lambda s: s + b(
            (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS))
        msg = pad(msg)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return cipher.encrypt(msg)

    # 解密
    def decrypt(self, enc):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return unpad(cipher.decrypt(base64.b64decode(enc)))


# sha256 hash salt
def hashlib_sha256(data, salt='9cafa6466a028bfb'):
    data = bytes(data, encoding='utf-8')
    salt = bytes(salt, encoding='utf-8')
    hash = hashlib.sha256(data)
    hash.update(salt)
    return hash.hexdigest()


if __name__ == '__main__':
    # 实例
    aes = AESCipher(
        key='fd6b639dbcff0c2a1b03b389ec763c4b',
        iv='77b07a672d57d64c'
    )

    # 需要解密的数据 base64
    enc_data = ""
    # 解密
    dec_data = aes.decrypt(enc_data)
    print(f'Decrypt: {dec_data.decode("utf-8")}')

    # 需要加密的数据 string
    dec_data = ""
    # 加密
    enc_data = aes.encrypt(dec_data)
    print(f'Encrypt: {base64.b64encode(enc_data)}')

    # SIGN加密
    sign = hashlib_sha256("params")

    # 结果
    # Encrypt: 涉及一部分隐私数据
    # Decrypt: 我就不贴结果了
    # SIGN:
