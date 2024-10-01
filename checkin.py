
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
# import json
import os
# import random
# import re
# -------------------------------------------------------------------------------------------
# github workflows
# -------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # cookies = ['gXRl_2132_seccodecSSP8eLb=1013.e0a6b82d187bb8304b; gXRl_2132_seccodecSADxWH8mGqF=1015.e3a0b0db6305053e0d; gXRl_2132_home_diymode=1; gXRl_2132_seccodecSAq7VH8mGqF=1026.1bf97bf75a8e4c7f6b; gXRl_2132_seccodecSAKk3H8mGqF=1030.41ff605d60792554d5; gXRl_2132_seccodecSASKCH8mGqF=1038.b69f599a38f81f8945; gXRl_2132_nofavfid=1; gXRl_2132_resendemail=1713881556; gXRl_2132_seccodecSH8mGqF=1046.8bbf63511db2ee5130; gXRl_2132_smile=1D1; HMACCOUNT=1C58803CACC5A547; gXRl_2132_saltkey=cT7q5O5t; gXRl_2132_lastvisit=1727266612; Hm_lvt_08bda441815c73e22fecf1ea1187dc47=1727270214; gXRl_2132_seccodecSApibDOy2on=455.d472c93e6219611099; gXRl_2132_seccodecSDOy2on=457.4ad74f50574a3f9eea; gXRl_2132_seccodecSAP3RDOy2on=462.7555304fbd469b66d2; gXRl_2132_ulastactivity=79bbH/9ArLiCnZJ1uzkER3aO/izi531GOcHBP5Cssd63pexD96HB; gXRl_2132_auth=f60bGN8vYFwt3aiZLcbsLYU/mdgoijOCIzUmZ6Kerdj5I7Nx8t4sMcxr6ywuiDG3uYPGcleKj/71i0jSSZFhzRcpIA; gXRl_2132_lastcheckfeed=85138|1727270323; popnotice=test5; gXRl_2132_st_t=85138|1727270519|8e01a2283ea4bf3aaf2add519f45c412; gXRl_2132_forum_lastvisit=D_38_1727270519; gXRl_2132_st_p=85138|1727271083|66efcd2789f4c9a92d88a3bbcecf0bf2; gXRl_2132_visitedfid=72D38D55; gXRl_2132_viewid=tid_24429; gXRl_2132_sendmail=1; gXRl_2132_sid=m8uPRT; gXRl_2132_lip=52.195.228.139,1727271910; gXRl_2132_lastact=1727272004	home.php	spacecp; gXRl_2132_checkpm=1; Hm_lpvt_08bda441815c73e22fecf1ea1187dc47=1727272005']
    cookies = os.environ.get("COOKIES", []).split("&")
    if cookies[0] == "":
        print('未获取到COOKIE变量')
        cookies = []
        exit(0)

    base_url = "https://bbs.hassbian.com"
    url = f"{base_url}/home.php?mod=spacecp&ac=credit&op=base"
    url2 = f"{base_url}/forum-72-1.html"

    referer = base_url
    origin = base_url
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    # payload = {'token': 'glados.one'}

    for cookie in cookies:
        session = requests.Session()
        posts_page = session.get(url2, headers={'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent})
        soup = BeautifulSoup(posts_page.text, 'html.parser')
        post_links = [a['href'] for a in soup.find_all('a', {'class': 'xst'}, href=True)]
        print(post_links)
        
        credit_page = session.get(url, headers={'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent})
        # credit_page = session.get(url)
        # print(credit_page.text)
        soup = BeautifulSoup(credit_page.text, 'html.parser')
        for ul in soup.find_all('ul', class_="creditl mtm bbda cl"):
            print(ul.get_text())
    # --------------------------------------------------------------------------------------------------------#
    # exit()

    
