import os
import re
import requests
from bs4 import BeautifulSoup

class ToonDown:
    def __init__(self, text):
        self.text = text
        p = re.compile('[0-9]+')
        m = p.search(text)
        
        if m is not None:
            self.num = m.group()
        else:
            self.num = 0

    def is_valid(self):
        if '웹툰' in self.text and int(self.num) in range(1,272):
            return True
        else:
            return False

    def proc(self):
        result = ""
        webtoon_url = "https://comic.naver.com/webtoon/detail.nhn?titleId=682637&no=" + str(self.num)
  
        res = requests.get(webtoon_url)
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        tag_list = soup.select('.wt_viewer img')

        for tag in tag_list:
            img_url = tag['src']
            result += img_url + '\n'

        return result

class GuGu:
    def __init__(self, text):
        self.text = text
        p = re.compile('[0-9]+')
        m = p.search(text)

        if m is not None:
            self.num = m.group()
        else:
            self.num = 0
        
    def is_valid(self):
        if '구구단' in self.text and int(self.num) in range(1,20):
            return True
        else:
            return False

    def proc(self):
        result = ""

        for i in range(1,20):
            result += "{0} * {1} = {2}".format(self.num, i, int(self.num) * i) + '\n'

        return result

class EngDict:
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        if type(self.text) == str and '번역' in self.text:
            return True
        else:
            return False

    def proc(self):
        first_pos = self.text.find('\'')
        second_pos = first_pos + self.text[first_pos + 1:].find('\'')
        word = self.text[first_pos + 1:second_pos + 1]
        result = ""

        dict_url = "https://endic.naver.com/search.nhn?sLn=kr&searchOption=all&query=" + word

        res = requests.get(dict_url)
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        first_tag_list = soup.select('.fnt_e30')
        second_tag_list = soup.select('.fnt_k05')

        if bool(first_tag_list) == True:
            result = first_tag_list[0].text + second_tag_list[0].text
        else:
            result = '번역 결과가 없습니다!'

        return result
