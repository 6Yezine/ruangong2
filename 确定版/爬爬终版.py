import os
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import re
from bs4 import BeautifulSoup
import time
import urllib.request
from pywebio.input import *
from pywebio.output import *

# 题目序号
def getlist(url):
    headers = {
        "Cookie": "client_id=98cfc2cc86d451827cf762d426dc1b5e5551a763; login_referer=https%3A%2F%2Fwww.luogu.com.cn%2Fproblem%2FP1000; _uid=561385",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
        html = response.text
        pattern = re.compile(r'(<a\shref=".*?">)*?')
        problemlist = re.findall(pattern, response.text)
        for x in problemlist:
            if (x != ""):
                P.append(x[9:14])
    except requests.exceptions.RequestException as e:
        print("请求出错:", e)

# 题目
def getproblem(url):
    headers = {
        "Cookie": "client_id=98cfc2cc86d451827cf762d426dc1b5e5551a763; login_referer=https%3A%2F%2Fwww.luogu.com.cn%2Fproblem%2FP1000; _uid=561385",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
        html = response.text
        # 数据整理
        bs = BeautifulSoup(html, "html.parser")
        core = bs.select("article")[0]
        md = str(core)
        md = re.sub("<h1>", "# ", md)
        md = re.sub("<h2>", "## ", md)
        md = re.sub("<h3>", "#### ", md)
        md = re.sub("</?[a-zA-Z]+[^<>]*>", "", md)
        # 保存数据
        global fn
        fn = bs.title.string
        fn = fn[:-5]
        savedate = "D:/360MoveData/Users/叶子呢/Desktop/录屏集合/num2"
        if not os.path.exists(savedate):
            os.mkdir(savedate)
        filename = savedate + '/' + fn + ".md"
        with open(filename, "w", encoding="utf-8") as fp:
            fp.write(md)
    except requests.exceptions.RequestException as e:
        print("请求出错:", e)

# 获取题目的解答
def getsolution(url):
        headers = {
            "Cookie": "__client_id=7298f81227f1bc2d6e646cba05a73571d5f5ac0c; _uid=1091435",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        }
        try:
            response = requests.get(url=url, headers=headers)
            response.raise_for_status()  # 检查请求是否成功
            # 整理数据
            html = response.text
            soup = BeautifulSoup(html, "html.parser")
            encoded_content_element = soup.find('script')
            encoded_content = encoded_content_element.text
            start = encoded_content.find('"')
            end = encoded_content.find('"', start + 1)
            encoded_content = encoded_content[start + 1:end]
            decoded_content = urllib.parse.unquote(encoded_content)
            decoded_content = decoded_content.encode('utf-8').decode('unicode_escape')
            start = decoded_content.find('"content":"')
            end = decoded_content.find('","type":"题解"')
            decoded_content = decoded_content[start + 11:end]
            # 保存数据
            savedate = "D:/360MoveData/Users/叶子呢/Desktop/录屏集合/num2"
            if not os.path.exists(savedate):
                os.mkdir(savedate)
            filename = savedate + '/' + fn + "-题解" ".md"
            with open(filename, "w", encoding="utf-8") as fp:
                fp.write(decoded_content)
        except requests.exceptions.RequestException as e:
            print("请求出错:", e)

# 主程序
url_list = []
for i in range(1000, 1050):
    url = "https://www.luogu.com.cn/problem/P" + str(i)
    url_list.append(url)

for url in url_list:
    getproblem(url)
    getsolution(url)
    time.sleep(3)  # 添加间隔时间，每次请求后休眠3秒