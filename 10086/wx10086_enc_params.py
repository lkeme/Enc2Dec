#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Lkeme
@contact: Useri@live.cn
@file: wx10086_enc_params.py
@time: 2019-6-8
"""
from binascii import b2a_hex, a2b_hex
from Crypto.Cipher import AES

BS = AES.block_size
# 加密算法
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
# 解密算法
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


class AESCipher:
    def __init__(self, key, iv):
        self.key = key.encode("utf-8")
        self.iv = iv.encode("utf-8")

    # 加密
    def encrypt(self, data):
        data = pad(data).encode("utf-8")
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return b2a_hex(cipher.encrypt(data))

    # 解密
    def decrypt(self, enc):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return unpad(cipher.decrypt(a2b_hex(enc)))


if __name__ == '__main__':
    # 实例
    aes = AESCipher(key='1234123412ABCDEF', iv='ABCDEF1234123412')
    # 需要加解密的数据
    telephone = '18877766666'
    # 加密 加密数据需要大写转换
    enc_data = aes.encrypt(telephone)
    print(f'Encrypt: {enc_data.decode("utf-8").upper()}')
    # 解密
    dec_data = aes.decrypt(enc_data)
    print(f'Decrypt: {dec_data.decode("utf-8")}')
    # 结果
    # Encrypt: 1699B98FA643A5AE66CD3CB896A92F22
    # Decrypt: 18877766666
