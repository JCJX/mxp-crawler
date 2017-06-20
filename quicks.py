# -*- coding:utf-8 -*-
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import subprocess
import requests
from PIL import Image
from PIL import ImageOps

def cleanImage(imagePath):
    image =Image.open(imagePath)
    image =image.point(lambda x: 0 if x<143 else 255)
    borderImage = ImageOps.expand(image,border=20,fill="white")
    borderImage.save(imagePath)

html =urlopen("http://www.880qp.net/AdminV2/AdminLogin.aspx")
bsObj =BeautifulSoup(html)
imageLocation =bsObj.find("img", {"id": "imgyzm"})["src"]
formBuildId =bsObj.find("input", {"name": "UserName"})["value"]
captchaSid =bsObj.find("input", {"name": "UserPwd"})["value"]
captchaToken =bsObj.find("input", {"name": "ValidCode"})["value"]

captchaUrl ="http://www.880qp.net/AdminV2/"+imageLocation
urlretrieve(captchaUrl,"captcha.jpg")
cleanImage("captcha.jpg")
p = subprocess.Popen(["tesseract", "captcha.jpg", "captcha"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
p.wait()
f = open("captcha.txt","r")

captchaResponse = f.read().replace(" ", "").replace("\n", "")
print("验证码解决方案尝试: "+captchaResponse)

if len(captchaResponse) == 4:
    params ={"UserName":formBuildId,"UserPwd":captchaSid,"captcha_response":captchaResponse, "name": "Ryan Mitchell", "subject":"I come to seek the Grall", "comment_body[und][0][value]":"...and I am definitely not abot"}
    r=requests.post("http://www.880qp.net/AdminV2/AdminLogin.aspx", date=params)
    responseObj = BeautifulSoup(r.text)
    if responseObj.find("title",{"id": "menubox"}) is not None:
        print(responseObj.find("title",{"id": "menubox"}).git_text())
    else:
        print("There was a problem reading the CAPTCHA correctly!")
