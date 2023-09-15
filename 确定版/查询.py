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

# 获取题目的解答
def getsolution(url):
    # 发送请求
    headers = {
        "Cookie": "__client_id=7298f81227f1bc2d6e646cba05a73571d5f5ac0c; _uid=1091435",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
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
    savedate = "./"
    savedate = savedate + fn
    if not os.path.exists(savedate):
        os.mkdir(savedate)
    filename = savedate + '/' + fn + "-题解" ".md"
    with open(filename, "w", encoding="utf-8") as fp:
        fp.write(decoded_content)

# 查询题目
def query_problem():
    problem_id = input("请输入题目ID：", type=TEXT)
    filename = f"./{problem_id}/{problem_id}.md"
    try:
        with open(filename, "r", encoding="utf-8") as fp:
            content = fp.read()
            put_markdown(content)
    except FileNotFoundError:
        put_markdown("未找到该题目的数据")

# 查询题解
def query_solution():
    problem_id = input("请输入题目ID：", type=TEXT)
    url = f"https://www.luogu.com.cn/problem/P{problem_id}"
    getsolution(url)

# 查询普及组题目
def query_puji():
    puji_url = "https://www.luogu.com.cn/problem/list?difficulty=1"
    response = requests.get(puji_url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    problem_list = soup.find_all("a", class_="lg-right")
    for problem in problem_list:
        problem_id = problem["href"].split("/")[-1]
        problem_title = problem.text.strip()
        put_text(f"题目ID：{problem_id} 题目标题：{problem_title}")

# 查询提高组题目
def query_tigao():
    tigao_url = "https://www.luogu.com.cn/problem/list?difficulty=2"
    response = requests.get(tigao_url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    problem_list = soup.find_all("a", class_="lg-right")
    for problem in problem_list:
        problem_id = problem["href"].split("/")[-1]
        problem_title = problem.text.strip()
        put_text(f"题目ID：{problem_id} 题目标题：{problem_title}")

# 关键词搜索题目
def search_problem():
    keyword = input("请输入关键词：", type=TEXT)
    search_url = f"https://www.luogu.com.cn/problem/list?keyword={keyword}"
    response = requests.get(search_url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    problem_list = soup.find_all("a", class_="lg-right")
    for problem in problem_list:
        problem_id = problem["href"].split("/")[-1]
        problem_title = problem.text.strip()
        put_text(f"题目ID：{problem_id} 题目标题：{problem_title}")

# 主函数
def main():
    choice = radio("请选择查询类型：", options=["查询题目", "查询题解", "查询普及组题目", "查询提高组题目", "关键词搜索题目"])
    if choice == "查询题目":
        query_problem()
    elif choice == "查询题解":
        query_solution()
    elif choice == "查询普及组题目":
        query_puji()
    elif choice == "查询提高组题目":
        query_tigao()
    elif choice == "关键词搜索题目":
        search_problem()

main()