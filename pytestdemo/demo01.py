#coding:utf-8
import xlrd
import os


try:
    data = xlrd.open_workbook("/home/huang/桌面/PythonTes.xlsx")



except BaseException as e:
    print(e,"文件不存在！！")


