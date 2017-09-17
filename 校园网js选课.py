# -*- coding: utf-8 -*-
import hashlib
import base64
import execjs
import re2
from svmutil import *  
from PIL import Image,ImageEnhance,ImageFilter
import shutil
import os
import requests
import time
def svm_model_test():
    yt, xt = svm_read_problem('0.txt')
    model = svm_load_model('0.model')
    p_label, p_acc, p_val = svm_predict(yt, xt, model)#p_label即为识别的结果
    return p_label
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
    imgurl="http://202.113.110.24:8088/tjsfjw/cas/genValidateCode?dateTime="+str(_nowtime)
    image = requests.get(imgurl,cookies=cookie)
    with open(target, "wb") as code:
        code.write(image.content)
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
def getyzm():
    fp=open('0.txt','w+')
    im = Image.open('0.jpg')
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(4)
    im = im.convert('1')
    xsize,ysize=im.size
    for i in range(xsize):
        for j in range(ysize):
            quxian(im,i,j)
    im.crop((7,8,17,24)).save('1.jpg')
    im.crop((22,8,32,24)).save('2.jpg')
    im.crop((37,8,47,24)).save('3.jpg')
    im.crop((52,8,62,24)).save('4.jpg')
    im11=Image.open('1.jpg')
    bbq=tezheng(im11)
    fp.writelines('1 1:'+str(bbq[0])+' 2:'+str(bbq[1])+' 3:'+str(bbq[2])+' 4:'+str(bbq[3])+' 5:'+str(bbq[4])+' 6:'+str(bbq[5])+' 7:'+str(bbq[6])+' 8:'+str(bbq[7])+' 9:'+str(bbq[8])+' 10:'+str(bbq[9])+' 11:'+str(bbq[10])+' 12:'+str(bbq[11])+' 13:'+str(bbq[12])+' 14:'+str(bbq[13])+' 15:'+str(bbq[14])+' 16:'+str(bbq[15])+' 17:'+str(bbq[16])+' 18:'+str(bbq[17])+' 19:'+str(bbq[18])+' 20:'+str(bbq[19])+' 21:'+str(bbq[20])+' 22:'+str(bbq[21])+' 23:'+str(bbq[22])+' 24:'+str(bbq[23])+' 25:'+str(bbq[24])+' 26:'+str(bbq[25])+'\n')
    im22=Image.open('2.jpg')
    bbq=tezheng(im22)
    fp.writelines('1 1:'+str(bbq[0])+' 2:'+str(bbq[1])+' 3:'+str(bbq[2])+' 4:'+str(bbq[3])+' 5:'+str(bbq[4])+' 6:'+str(bbq[5])+' 7:'+str(bbq[6])+' 8:'+str(bbq[7])+' 9:'+str(bbq[8])+' 10:'+str(bbq[9])+' 11:'+str(bbq[10])+' 12:'+str(bbq[11])+' 13:'+str(bbq[12])+' 14:'+str(bbq[13])+' 15:'+str(bbq[14])+' 16:'+str(bbq[15])+' 17:'+str(bbq[16])+' 18:'+str(bbq[17])+' 19:'+str(bbq[18])+' 20:'+str(bbq[19])+' 21:'+str(bbq[20])+' 22:'+str(bbq[21])+' 23:'+str(bbq[22])+' 24:'+str(bbq[23])+' 25:'+str(bbq[24])+' 26:'+str(bbq[25])+'\n')
    im33=Image.open('3.jpg')
    bbq=tezheng(im33)
    fp.writelines('1 1:'+str(bbq[0])+' 2:'+str(bbq[1])+' 3:'+str(bbq[2])+' 4:'+str(bbq[3])+' 5:'+str(bbq[4])+' 6:'+str(bbq[5])+' 7:'+str(bbq[6])+' 8:'+str(bbq[7])+' 9:'+str(bbq[8])+' 10:'+str(bbq[9])+' 11:'+str(bbq[10])+' 12:'+str(bbq[11])+' 13:'+str(bbq[12])+' 14:'+str(bbq[13])+' 15:'+str(bbq[14])+' 16:'+str(bbq[15])+' 17:'+str(bbq[16])+' 18:'+str(bbq[17])+' 19:'+str(bbq[18])+' 20:'+str(bbq[19])+' 21:'+str(bbq[20])+' 22:'+str(bbq[21])+' 23:'+str(bbq[22])+' 24:'+str(bbq[23])+' 25:'+str(bbq[24])+' 26:'+str(bbq[25])+'\n')
    im44=Image.open('4.jpg')
    bbq=tezheng(im44)
    fp.writelines('1 1:'+str(bbq[0])+' 2:'+str(bbq[1])+' 3:'+str(bbq[2])+' 4:'+str(bbq[3])+' 5:'+str(bbq[4])+' 6:'+str(bbq[5])+' 7:'+str(bbq[6])+' 8:'+str(bbq[7])+' 9:'+str(bbq[8])+' 10:'+str(bbq[9])+' 11:'+str(bbq[10])+' 12:'+str(bbq[11])+' 13:'+str(bbq[12])+' 14:'+str(bbq[13])+' 15:'+str(bbq[14])+' 16:'+str(bbq[15])+' 17:'+str(bbq[16])+' 18:'+str(bbq[17])+' 19:'+str(bbq[18])+' 20:'+str(bbq[19])+' 21:'+str(bbq[20])+' 22:'+str(bbq[21])+' 23:'+str(bbq[22])+' 24:'+str(bbq[23])+' 25:'+str(bbq[24])+' 26:'+str(bbq[25])+'\n')
    fp.close()
    ans=svm_model_test()
    '''
    os.remove('1.jpg')
    os.remove('2.jpg')
    os.remove('3.jpg')
    os.remove('4.jpg')
    os.remove('0.txt')
    os.remove('0.jpg')
    '''
    return str(int(ans[0]))+str(int(ans[1]))+str(int(ans[2]))+str(int(ans[3]))
def md(s):
    m = hashlib.md5()  
    m.update(s)
    return m.hexdigest()
def base(s):
    return base64.b64encode(s)
def get_js():   
    f = open("./11.js", 'r')  
    line = f.readline()  
    htmlstr = ''  
    while line:  
        htmlstr = htmlstr + line  
        line = f.readline()  
    return htmlstr  
def getenc(s):
    jsstr = get_js()  
    ctx = execjs.compile(jsstr)  
    return (ctx.call('getEncParams',s,_deskey))
def refreshdeskey():
    global _deskey
    global _nowtime
    global _sessionid
    global cookie
    r=requests.get('http://202.113.110.24:8088/tjsfjw/custom/js/SetKingoEncypt.jsp?random=0.8868112635076488')
    p=re2.compile(r'_deskey = \'(.*?)\';')
    _deskey=re2.findall(p,r.text)[0]
    p=re2.compile(r'_nowtime = \'(.*?)\';')
    _nowtime=re2.findall(p,r.text)[0]
    _sessionid=str(r.cookies)[38:70]
    cookie={'JSESSIONID':_sessionid}
def logout():
    r=requests.get('http://202.113.110.24:8088/tjsfjw/DoLogoutServlet',cookies=cookie)
def chacklogstates():
    data={'hidOption':'getOnlineMessage'}
    r=requests.post('http://202.113.110.24:8088/tjsfjw/online/message',cookies=cookie,data=data,allow_redirects=False)
    if r.status_code==302:
        return False
    elif r.status_code==200:
        return True
def login(u='1630200127',p='83506876ok'):
    refreshdeskey()
    downloadpic(cookie)
    r=getyzm()
    token=p
    p=md(md(p)+md(r))
    u=base(u+";;"+_sessionid)
    p_username = "_u"+r
    p_password = "_p"+r
    params=p_username+"="+u+"&"+p_password+"="+p+"&randnumber="+r+"&isPasswordPolicy=1"
    token=md(md(params)+md(_nowtime))
    param=getenc(params)
    _params = {"params" : base(getenc(params)) ,
               "token" : token,
               "timestamp":_nowtime}
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    req=requests.post('http://202.113.110.24:8088/tjsfjw/cas/logon.action',data=_params,headers=headers,cookies=cookie)
    if '402' in req.text:
        return False
    elif '200' in req.text:
        return True
'''
def shangke(html):
    xktype=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    xn=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    xq=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    xh=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    nj=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    zydm=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    kcdm=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    kclb1=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    kclb2=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    kclb3=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    khfs=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    skbjdm=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    skbzdm=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    xf=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    is_checkTime=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    zfx_m=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    outnumber=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    xsszxq=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    xqdm=''
    zfx_m=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    zfx_m=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
    zfx_m=re2.findall(re2.compile(r'name=\"electiveCourseForm.xktype\" value=\"(.*?)\"/>'),html)[0]
'''

def js(s):
    refreshdeskey()
    timestamp = _nowtime
    params=s
    token = md(md(params)+md(timestamp))
    jsstr = get_js()  
    ctx = execjs.compile(jsstr)  
    params= (ctx.call('des_encode',params ,_deskey))
    param=base(params)
    return u"params=" + param + u"&token="+token+u"&timestamp="+timestamp; 
def xuankexinxi(html):
    su= re2.findall(re2.compile(r'type="hidden" id=".*" name=".*" value="(.*?)"'),html)
    banji='-002'
    params='xktype=%s&xn=%s&xq=%s&xh=%s&nj=%s&zydm=%s&kcdm=%s&kclb1=%s&kclb2=%s&kclb3=%s&khfs=%s&skbjdm=%s&skbzdm=%s&xf=%s&is_checkTime=%s&zfx_m=%s&outnumber=0&xsszxq=%s&xqdm=&txt_skbjdm=&xk_points=0&is_buy_book=0&is_cx=0&is_yxtj=1&menucode_current=JW1304'\
            %(su[0],su[1],su[2],su[3],su[4],su[5],su[6],su[7],su[8],su[9],su[10],su[6]+banji,su[11],su[12],su[13],su[14],su[15])
    print requeste.post(url='http://202.113.110.24:8088/tjsfjw/jw/common/saveElectiveCourse.action',cookies=cookie,data=params).text
def zhaoke():
    if 1:
        param='xktype=2&xh=201622348&xn=2017&xq=0&nj=2016&zydm=006202&_kcfw=zxggrx&items=&is_xjls=undefined&btnFilter=%C0%E0%B1%F0%B9%FD%C2%CB&btnSubmit=%CC%E1%BD%BB&kcfw=zxggrx&lbgl=&kcmc=&xwxmkc=on&menucode_current=JW1304'
        r=requests.post('http://202.113.110.24:8088/tjsfjw/taglib/DataTable.jsp?tableId=2568',cookies=cookie,data=param)
        if 'GEN15201L'in r.text:
            


if 1:
    _nowtime=''
    _deskey =''
    _sessionid =''
    cookie={'JSESSIONID':_sessionid}
    '''
    scode=['xktype=2&xn=2017&xq=0&xh=201622348&nj=2016&zydm=006202&kcdm=006365&kclb1=03&kclb2=01&kclb3=&khfs=01&skbjdm=006365-001&skbzdm=&xf=2.0&is_checkTime=1&zfx_m=0&outnumber=0&xsszxq=01&xqdm=&txt_skbjdm=&xk_points=0&is_buy_book=0&is_cx=0&is_yxtj=1&menucode_current=JW1304',
    #病毒周一
    'xktype=2&xn=2017&xq=0&xh=201622348&nj=2016&zydm=006202&kcdm=006365&kclb1=03&kclb2=01&kclb3=&khfs=01&skbjdm=006365-002&skbzdm=&xf=2.0&is_checkTime=1&zfx_m=0&outnumber=0&xsszxq=01&xqdm=&txt_skbjdm=&xk_points=0&is_buy_book=0&is_cx=0&is_yxtj=1&menucode_current=JW1304',
    #病毒周二
    'xktype=2&xn=2017&xq=0&xh=201622348&nj=2016&zydm=006202&kcdm=006223&kclb1=03&kclb2=01&kclb3=&khfs=01&skbjdm=006223-001&skbzdm=&xf=2.0&is_checkTime=1&zfx_m=0&outnumber=0&xsszxq=01&xqdm=&txt_skbjdm=&xk_points=0&is_buy_book=0&is_cx=0&is_yxtj=1&menucode_current=JW1304',
    #日本当代周一
    'xktype=2&xn=2017&xq=0&xh=201622348&nj=2016&zydm=006202&kcdm=006223&kclb1=03&kclb2=01&kclb3=&khfs=01&skbjdm=006223-002&skbzdm=&xf=2.0&is_checkTime=1&zfx_m=0&outnumber=0&xsszxq=01&xqdm=&txt_skbjdm=&xk_points=0&is_buy_book=0&is_cx=0&is_yxtj=1&menucode_current=JW1304',
    #日本当代周三
    'xktype=2&xn=2017&xq=0&xh=201622348&nj=2016&zydm=006202&kcdm=006243&kclb1=03&kclb2=01&kclb3=&khfs=01&skbjdm=006243-001&skbzdm=&xf=2.0&is_checkTime=1&zfx_m=0&outnumber=0&xsszxq=01&xqdm=&txt_skbjdm=&xk_points=0&is_buy_book=0&is_cx=0&is_yxtj=1&menucode_current=JW1304',]
    #创客技能
    '''
    if login():
        

