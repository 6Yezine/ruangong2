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

# 获取符合需求的题目序号
def getlist(url):
    # 爬取数据集的代码...
# 获取题目的函数
 def getproblem(url):
    # 获取题目的代码...
# 获取题目的解答
def getsolution(url):
    # 获取题目解答的代码...

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
    choice = radio("请选择查询类型：", options=["查询题目", "查询题解", "查询普及组题目", "查询提高组题目", "关键词搜索题目"])
    if choice == "查询题目":
        query = input("请输入URL：", type=TEXT)
        getlist(query)
    elif choice == "查询题解":
        query = input("请输入URL：", type=TEXT)
        getsolution(query)
    elif choice == "查询普及组题目":
        puji_url = "https://www.luogu.com.cn/problem/list?difficulty=1"
        getlist(puji_url)
    elif choice == "查询提高组题目":
        tigao_url = "https://www.luogu.com.cn/problem/list?difficulty=2"
        getlist(tigao_url)
    elif choice == "关键词搜索题目":
        search_data()

main()