#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
- author: Lkeme
- contact: Useri@live.cn
- file: aes_ecb_login.py
- time: 2021/3/23 10:52
- desc:
"""

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

BS = AES.block_size
# 加密算法
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
# 解密算法
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


class AESCipher:
    def __init__(self, mode, key, iv=''):
        """
        ECB没有偏移量
        """
        self.key = key.encode("utf-8")
        self.iv = iv.encode("utf-8")
        self.mode = mode

    def error(self, data):
        return None

    def encrypt(self, data):
        switch = {
            'CBC': self.__cbc_encrypt,
            'ECB': self.__ecb_encrypt,
        }
        return switch.get(self.mode, self.error)(data)

    def decrypt(self, data):
        switch = {
            'CBC': self.__cbc_decrypt,
            'ECB': self.__ecb_decrypt,
        }
        return switch.get(self.mode, self.error)(data)

    def add_to_16(self, text):
        if len(text.encode('utf-8')) % 16:
            add = 16 - (len(text.encode('utf-8')) % 16)
        else:
            add = 0
        text = text + ('\0' * add)
        return text.encode('utf-8')

    # 加密
    def __cbc_encrypt(self, data):
        data = pad(data).encode("utf-8")
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return b2a_hex(cipher.encrypt(data))

    # 解密
    def __cbc_decrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return unpad(cipher.decrypt(a2b_hex(data)))

    # 加密函数
    def __ecb_encrypt(self, text):
        text = self.add_to_16(text)
        cipher = AES.new(self.key, AES.MODE_ECB)
        cipher_text = cipher.encrypt(text)
        return b2a_hex(cipher_text)

    # 解密后，去掉补足的空格用strip() 去掉
    def __ecb_decrypt(self, text):
        cipher = AES.new(self.key, AES.MODE_ECB)
        plain_text = cipher.decrypt(a2b_hex(text))
        return bytes.decode(plain_text, encoding='utf-8').rstrip('\0')


if __name__ == '__main__':
    key = '数据'
    enc_data = '数据'
    print(AESCipher("ECB", key).decrypt(enc_data))
