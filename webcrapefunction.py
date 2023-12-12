from urllib.request import urlopen
import re


def pagetextonly(url, htmlbegin, htmlend):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    page_index = html.find(htmlbegin)
    page_startindex = page_index + len(htmlbegin)
    page_end_index = html.find(htmlend)
    page = html[page_startindex:page_end_index]
    page = re.sub("<.*?>", "", page)
    return page


def page(url, htmlbegin, htmlend):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    page_index = html.find(htmlbegin)
    page_startindex = page_index + len(htmlbegin)
    page_end_index = html.find(htmlend)
    page = html[page_startindex:page_end_index]
    return page
