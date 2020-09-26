# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 07:38:55 2020

@author: Satyam
"""

#pip install PyPDF2
import PyPDF2
import os
import re


path = r'D://Satyam//Papers//IEEE SAM 2020 Papers'
#direc = os.listdir(path)
#print(len(direc))
for zz in (os.listdir(path)):
    #if filename.endswith(".pdf") or filename.endswith(".png"):
    if zz.endswith(".pdf"):
        name = os.path.join(path, zz)
        print(name)
        file = open(name, 'rb') 
        pdfReader = PyPDF2.PdfFileReader(file)
        pages = pdfReader.numPages 
        for i in range(pages):   
            page = pdfReader.getPage(i)   
            print("Page no:",i)
            #print(page.extractText())
            value= page.extractText()        
            emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", value)
            #values = re.findall('\S+@\S+', value)
            print(emails)
            break
