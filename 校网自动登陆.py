#coding=utf-8
from svmutil import *  
from PIL import Image,ImageEnhance,ImageFilter
import shutil
import urllib
import os
import requests
from selenium import webdriver
def svm_model_test():
    yt, xt = svm_read_problem('0.txt')
    model = svm_load_model('0.model')
    p_label, p_acc, p_val = svm_predict(yt, xt, model)#p_label即为识别的结果
    cnt = 0
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
    imgurl="http://202.113.110.24:8088/tjsfjw/cas/genValidateCode?dateTime=Sat Sep 09 2017 13:44:37 GMT+0800"
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

if 1:
    driver = webdriver.Chrome()
    driver.get("http://202.113.110.24:8088/tjsfjw/cas/login.action")
    driver.find_element_by_id('yhmc').send_keys('1630200127')
    driver.find_element_by_id('yhmm').send_keys('83506876ok')
    driver.find_element_by_id('randnumber').click()
    cookie={'JSESSIONID':driver.get_cookies()[0]['value']}
    downloadpic(cookie)
    ma=getyzm()
    driver.find_element_by_id('randnumber').send_keys(ma)
    driver.find_element_by_id('login').click()
