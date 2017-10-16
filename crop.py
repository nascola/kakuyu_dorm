#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 寮食メニューを取得してcropした後に
#pdftotxtで抽出した年月日データでラベリングできるモノ
# ubuntu 16.04 @ bash on windows
# $sudo apt-get update & upgrade
# $sudo apt-get install wget python3 poppler-utils
import subprocess
import sys
import glob
import datetime

def console(cmd): #cmd に明記されたコマンドを実行する関数 エラー時はerror: cmd 吐いて死ぬ
    print(cmd)
    try:
        subprocess.run(cmd,shell=True,check=True)
    except subprocess.CalledProcessError:
        print("error: "+cmd)
        quit()

argvs = sys.argv #引数読み込み
argc = len(argvs) #引数の数
if (argc != 3): #引数が2つあるかチェック
    print ("error! :Usage python3 crop.py [year] [month] ex. $python3 crop.py 2017 04")
    quit()
year = argvs[1]
month = argvs[2]

console("wget -nc http://www.maizuru-ct.ac.jp/files/06life/menu/menu_dormitory_"+year+"-"+month+".pdf")
console("convert -density 300 menu_dormitory_"+year+"-"+month+".pdf menu_dormitory_"+year+"-"+month+".jpg")
console("pdftotext menu_dormitory_"+year+"-"+month+".pdf menu_dormitory_"+year+"-"+month+".txt")


console("grep 月.*日 menu_dormitory_"+year+"-"+month+".txt > date_"+ year+"-"+month+".txt")


text_fnames = glob.glob('menu_dormitory_*-*-*.jpg')

for fname in text_fnames: #余白の切り取って1週間ごとに
    console("convert -crop 3010x1982+308+318 "+ fname +" "+ fname)

for fname in text_fnames: #1日ごとに切り取り
    console("convert -crop 430x1982 "+fname + " "+fname)

for fname in text_fnames: #1週間分のやつを消去
    console("rm "+fname)

Date_files = open("date_"+year+"-"+month+".txt")
Date_bad = Date_files.readlines();
Date_files.close();

text_fnames2 = glob.glob('menu_dormitory_*-*-*-*')

print(text_fnames2)
print(Date_bad)

Date =[0]*len(Date_bad)
i=0;
for var in Date_bad:
    var = var.strip()
    var = var.replace("月", "-")
    var = var.replace("日", "")
    dt = datetime.datetime.strptime(year+"-"+var, '%Y-%m-%d')
    Date[i] = dt.strftime('%Y-%m-%d')
    i+=1
print(Date)

i=0
for fname in text_fnames2:
    console("mv "+fname+" ./img/"+Date[i]+".jpg")
    i+=1

console("rm date_"+year+"-"+month+".txt")
console("rm menu_dormitory_"+year+"-"+month+".txt")
console("rm menu_dormitory_"+year+"-"+month+".pdf")


print("end processing.")
