# -*- coding:utf-8- -*-
"""
作者：苦瓜
日期：2022年04月05日
"""
import requests
import html
from bs4 import BeautifulSoup

def run(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/99.0.4844.84 Safari/537.36"
    }       # UA伪装历览器
    resp = requests.get(url=url, headers=headers)  # 向服务器发送请求
    resp.encoding = 'utf-8'  # 设置编码格式，防止乱码

    main_page = BeautifulSoup(html.unescape(resp.text), "html.parser")  # 解析页面代码

    pic_list = main_page.find("section", attrs={"class": "normal markdown-section"}).find_all("p")  # 定向查找小说内容
    title = str(main_page.find("title")).replace('<title>', '').replace('</title>', '')  # 获取小说章节标题

    f = open("{}.txt".format(title), "w", encoding='utf-8')  # 以txt格式写入小说

    for j in pic_list:
        b = str(j).replace('<p>', '').replace('</p>', '')   # 去除小说内容中的<p>,</p>
        f.write(b)
        f.write('\n')   # 规范小说txt文本格式
        f.write('\n')

    f.close()
    print("已获取\t{}\t内容".format(title))  # 获取完成提示

for i in range(68, 100):
    if i < 10:
        url = "http://lyy289065406.github.io/re0-web/gitbook/book/markdown/ch/chapter050/0{}.html".format(i)
        run(url)
    elif i > 10:
        url = "http://lyy289065406.github.io/re0-web/gitbook/book/markdown/ch/chapter050/{}.html".format(i)
        run(url)
