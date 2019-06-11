| INFO | DESCRIBE  |
| --- | --- |
| Author  | Lkeme |
| Email | Useri@live.cn  |
| Website | [https://mudew.com](https://mudew.com "沐雨露の山头") |
| Group |  [55308141](https://jq.qq.com/?_wv=1027&k=5AIDaJg) 
| Date | 2019-06-11 |


## 文件

**`sign.py`**

### 功能

应用于`https://*.bilibili.com/*`的大部分API, 参数`sign`  
哔哩哔哩app客户端大部分请求的sign参数加密

### 更新

* 2019-5-31：第一次添加文件

### 说明

1. 提交参数需要按key排序(升序排序)  
2. 部分API需要可能需要有app_key参数(抓包结果)  
3. 尾部加上app_secret进行md5的加密

------

## 文件

**`watcher_enc_dec.py`**

### 功能

应用于`https://api.bilibili.com/x/report/click/android2`API  
哔哩哔哩app客户端播放数据请求体加解密，该API主要用于播放计数

### 更新

* 2019-6-11：第一次添加文件

### 说明

1. 提交参数可能需要按key排序(升序排序)  
2. SHA256加密是hashlib的不是hmac
3. [查阅文档](https://mudew.com/20190611/Bilibili-Android%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%92%AD%E6%94%BE%E6%95%B0%E6%8D%AE%E5%8C%85%E8%A7%A3%E6%9E%90/)
