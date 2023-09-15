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
        filename = f"{savedate}/{fn}.md"
        with open(filename, "w", encoding="utf-8") as fp:
            fp.write(md)
        put_markdown(md)
    except requests.exceptions.RequestException as e:
        print("请求出错:", e)

# 根据标题查询数据
def search_data():
    query = input("请输入要查询的标题：", type=TEXT)
    savedate = "D:/360MoveData/Users/叶子呢/Desktop/录屏集合/num2"
    files = os.listdir(savedate)
    found = False
    for file in files:
        if query in file:
            with open(f"{savedate}/{file}", "r", encoding="utf-8") as fp:
                content = fp.read()
            put_markdown(content)
            found = True
    if not found:
        put_text("未找到匹配的数据")

# 主程序
def main():
    url = input("请输入URL：", type=TEXT)
    getlist(url)
    for p in P:
        problem_url = f"https://www.luogu.com.cn/problem/{p}"
        getproblem(problem_url)
    search_data()

if __name__ == "__main__":
    main()