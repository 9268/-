# -*- coding: utf-8 -*-
import hashlib
import base64
import re2
from svmutil import *  
from PIL import Image,ImageEnhance,ImageFilter
import requests
import io
model = svm_load_model('jingcai.model')
yt=[3,6,6,7]
def tezheng(img):
    pixel_cnt_list = []
    xsize,ysize=img.size
    for i in range(ysize):
        pix_cnt_x = 0
        for j in range(xsize):
            if img.getpixel((j,i))==0:  # 黑色点
                pix_cnt_x += 1
        pixel_cnt_list.append(pix_cnt_x)
    for j in range(xsize):
        pix_cnt_y = 0
        for i in range(ysize):
            if img.getpixel((j,i)) == 0:  # 黑色点
                pix_cnt_y += 1
        pixel_cnt_list.append(pix_cnt_y)
    return pixel_cnt_list
def downloadpic(cookie):
    target ='0.jpg'
    imgurl="http://202.113.110.24:8088/tjsfjw/cas/genValidateCode"
    image = requests.get(imgurl,cookies=cookie)
    return image.content
def quxian(im,i,j):
    if (im.getpixel((i,j))==1 or i>=69 or j>=29 or i==0 or j==0):
        return 0
    else:
        q=0
        if (im.getpixel((i+1,j+1))==0):
            q=q+1
        if (im.getpixel((i+1,j))==0):
            q=q+1
        if (im.getpixel((i,j+1))==0):
            q=q+1
        if (im.getpixel((i-1,j-1))==0):
            q=q+1
        if (im.getpixel((i-1,j))==0):
            q=q+1
        if (im.getpixel((i,j-1))==0):
            q=q+1
        if (im.getpixel((i+1,j-1))==0):
            q=q+1
        if (im.getpixel((i-1,j+1))==0):
            q=q+1
        if (q<3):
            im.putpixel((i,j),(1))
def getyzm(cookie):
    im =Image.open(io.BytesIO(downloadpic(cookie)))
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(4)
    im = im.convert('1')
    xsize,ysize=im.size
    for i in range(xsize):
        for j in range(ysize):
            quxian(im,i,j)
    xt=[{},{},{},{}]
    im1=im.crop((7,8,17,24))
    im2=im.crop((22,8,32,24))
    im3=im.crop((37,8,47,24))
    im4=im.crop((52,8,62,24))
    bbq=tezheng(im1)
    for i in range(1,27):
        xt[0][i]=bbq[i-1]
    bbq=tezheng(im2)
    for i in range(1,27):
        xt[1][i]=bbq[i-1]
    bbq=tezheng(im3)
    for i in range(1,27):
        xt[2][i]=bbq[i-1]
    bbq=tezheng(im4)
    for i in range(1,27):
        xt[3][i]=bbq[i-1]
    ans,b,c = svm_predict(yt, xt, model,'-q')
    return str(int(ans[0]))+str(int(ans[1]))+str(int(ans[2]))+str(int(ans[3]))
def md(s):
    m = hashlib.md5()  
    m.update(s)
    return m.hexdigest()
def base(s):
    return base64.b64encode(s)
def login(u='',p=''):
    global _sessionid
    _sessionid='2F0EE3129D561ABA6999D7ED8DB46007'
    cookie={'JSESSIONID':_sessionid}
    r=getyzm(cookie)
    token=p
    p=md(md(p)+md(r))
    p_username = "_u"+r
    p_password = "_p"+r
    u=base(u+";;"+_sessionid)
    params=p_username+"="+u+"&"+p_password+"="+p+"&randnumber="+r+"&isPasswordPolicy=1"
    params={p_username:u,
            p_password:p,
            "randnumber":r,
            "isPasswordPolicy":"1"}
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    req=requests.post('http://202.113.110.24:8088/tjsfjw/cas/logon.action',data=params,headers=headers,cookies=cookie)
    print req.text
login()
