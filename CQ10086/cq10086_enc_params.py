#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Lkeme
@contact: Useri@live.cn
@file: wx10086_enc_params.py
@time: 2019-6-10
"""
import random
import requests
import js2py

try:
    from urllib import urlencode
except:
    from urllib.parse import urlencode


# 获取js
def get_js_ctx():
    js = open(r'./js/securityencode.js', encoding='utf-8').read()
    context = js2py.EvalJs()
    context.execute(js)
    return context


# 登录
def login(phone, sms_passwd, ctx):
    base_url = "https://wap.cq.10086.cn/wap?service=ajaxDirect/1/touch.Login/touch.Login/javascript/&"
    xx = ctx.strEnc(sms_passwd, phone[:8], phone[1:9], phone[3:11])
    params = {
        "pagename": "touch.Login",
        'eventname': "smsLogin",
        'phoneNo': phone,  # 458731
        'smsCheckPwd': xx[:6],
        'pwd_encoded': 'yes',
        'pwd1': xx[6:],
        'validateCode': 'k4xe',
        'ID': 'undefined',
        'PAGERANDOMID': 'undefined',
        'ajaxSubmitType': 'get',
        'ajax_randomcode': random.uniform(0, 1),
    }
    url = f'{base_url}{urlencode(params)}'
    headers = {
        'Accept': 'application/xml, text/xml, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Origin': 'http://wap.cq.10086.cn',
        'Referer': 'http://wap.cq.10086.cn/login/Login.html',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    }
    response = requests.get(url, verify=False, headers=headers).text
    print(response)


if __name__ == '__main__':
    # 获取执行js对象
    ctx = get_js_ctx()
    # 手机号以及短信验证码
    phone = '18877766666'
    # sms_passwd = input("输入你的短信验证码")
    sms_passwd = '000000'
    login(phone, sms_passwd, ctx)
