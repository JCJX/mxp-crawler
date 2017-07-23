# -*- coding:utf-8 -*-
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
#获取蜜柑计划上的番剧
html=urlopen("http://mikanani.me/")
bsobj=BeautifulSoup(html)
animalist=bsobj.findAll("", {"class": "an-text"})
for name in animalist:
   print(name.get_text())

#TODO
csvFile= open("../files/jun.cav", 'wt', nameline="", encoding="utf-8")
writer=csv.writer(csvFile)
try:
    for anima in animalist:
        csvRow=[]
        for cell in anima.findAll(["td","th"]):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()



