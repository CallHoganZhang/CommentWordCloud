# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 08:37:13 2019

@author: Administrator
"""
import requests
import os
import time
import json
import random
import jieba
import numpy as np
from wordcloud import  WordCloud
from PIL import Image
import matplotlib.pyplot as plt
from skimage import io


WC_MASK_IMG = 'wawa.jpg'
COMMENT_FILE = 'comment.txt'
WC_FONT_PATH = 'SIMLI.TTF'


def paramDict2Str(param):        
    str1 = ''
    for p,v in param.items():
        str1 = str1+ p+'='+str(v)+'&'
    return str1


def spider_comment(page=0):
    base_url = 'https://sclub.jd.com/comment/productPageComments.action'
    callback = 'fetchJSON_comment98vv4563'
    productId = 100003052761
    param = {
            'callback' : callback,
            'productId' : productId,
            'score' : 0,
            'sortType': 5,
            'pageSize': 10,
        }   
    
    Url = base_url +'?'+ paramDict2Str(param)+'isShadowSku=0&fold=1&page={}'.format(page)
#    print(Url)
#    url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv4563&productId=100003052761&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1' % page
    headers = {'user-agent': 'Mozilla/5.0', 'Referer': 'https://item.jd.com/{}.html'.format(productId)}
  #不同商品不同ID
    try:
        r = requests.get(Url, headers = headers)
#        print('r is ',r)
        r.raise_for_status()   #当发生错误时抛出异常
    except:
        print('爬取失败')
#    print(r.text)
    # 截取json数据字符串
#    r_json_str = r.text[26:-2]
    json_obj = json.loads(r.text[26:-2])
#    print(json_obj)
    json_comments = json_obj['comments']
    for com in json_comments:
        print(com['id'])
#        productId,
        print(com['guid'])
#        print(com['content'])
        print(com['creationTime'])
        print(com['referenceId'])
        print(com['referenceTime'])
        print(com['score'])
        print(com['nickname'])
        print(com['userLevelName'])
        print(com['isMobile'])
        print(com['userClientShow'])
        
#        print(com['content'])
#        with open(COMMENT_FILE, 'a+') as file:
#            file.write(com['content'] + '\n')


def batch_spider_comment():

    if os.path.exists(COMMENT_FILE):
        os.remove(COMMENT_FILE)
        
    for i in range(10):
        spider_comment(i)
        time.sleep(random.random() * 5)


def cut_word():
    """
    对数据分词
    :return: 分词后的数据
    """
    with open(COMMENT_FILE) as f:
        comment_txt = f.read()
        wordlist = jieba.cut(comment_txt, cut_all=True)
        wl = " ".join(wordlist)
#        print(wl)
        return wl


def create_word_cloud():

    # 设置词云形状图片遮罩
    wc_mask = np.array(Image.open(WC_MASK_IMG),dtype = np.uint8)
    # 设置词云的一些配置，如：字体，背景色，词云形状，大小
    wc = WordCloud(background_color="white", 
                   max_words=2000, 
                   mask=wc_mask, 
                   scale=4,
                   max_font_size=50, 
                   random_state=42, 
                   font_path=WC_FONT_PATH)
    
    result = wc.generate(cut_word())
    result.to_file('filename.jpg')

    plt.imshow(wc, interpolation="bilinear")  #different with imshow and show
    plt.axis("off")
    plt.figure()
    fig = plt.gcf()
    #shunxu
#    plt.savefig("filename.jpg")
    plt.show()


if __name__ == '__main__':
#     spider_comment(1)
#     batch_spider_comment()  #运行一次后注释掉，否则将重复重写
    create_word_cloud()