import os

#english 1 , any other 0
att = ["age","react","javascript","html","css","python","experience","language"]
prof = ["0","0","0","0","0","0","0","0"]

os.system("grep 'year old' ./input/resume.txt > cache")
f = open("cache","r")
temp = f.read().split(" ")
for i in range(len(temp)):
    if temp[i] == "year":
        if int(temp[i-1].replace(" ",""))<=26 and int(temp[i-1].replace(" ",""))>=21:
            prof[0] = "1"
        
os.system("grep 'react' ./input/resume.txt > cache")
f = open("cache","r")
if f.read() != "":
    prof[1] = "1"
os.system("grep 'React' ./input/resume.txt > cache")
f = open("cache","r")
if f.read() != "":
    prof[1] = "1"

os.system("grep 'javascript' ./input/resume.txt > cache")
f = open("cache","r")
if f.read() != "":
    prof[2] = "1"
os.system("grep 'JavaScript' ./input/resume.txt > cache")
f = open("cache","r")
if f.read() != "":
    prof[2] = "1"
os.system("grep 'js' ./input/resume.txt > cache")
f = open("cache","r")
if f.read() != "":
    prof[2] = "1"
os.system("grep 'JS' ./input/resume.txt > cache")
f = open("cache","r")
if f.read() != "":
    prof[2] = "1"

os.system("grep 'html' ./input/resume.txt > cache")
f = open("cache","r")
if f.read() != "":
    prof[3] = "1"
os.system("grep 'Html' ./input/resume.txt > cache")
f = open("cache","r")
if f.read() != "":
    prof[3] = "1"
os.system("grep 'HTML' ./input/resume.txt > cache")
f = open("cache","r")
if f.read() != "":
    prof[3] = "1"

os.system("grep 'css' ./input/resume.txt > cache")
f = open("cache","r")
if f.read() != "":
    prof[4] = "1"
os.system("grep 'Css' ./input/resume.txt > cache")
f = open("cache","r")
if f.read() != "":
    prof[4] = "1"
os.system("grep 'CSS' ./input/resume.txt > cache")
f = open("cache","r")
if f.read() != "":
    prof[4] = "1"
    
os.system("grep 'python' ./input/resume.txt > cache")
f = open("cache","r")
if f.read() != "":
    prof[5] = "1"
os.system("grep 'Python' ./input/resume.txt > cache")
f = open("cache","r")
if f.read() != "":
    prof[5] = "1"

os.system("grep 'experience' ./input/resume.txt > cache")
f = open("cache","r")
temp = f.read().split(" ")
for i in range(len(temp)):
    if temp[i] == "years":
        if int(temp[i-1].replace("\t","").replace(" ",""))>=3:
            prof[6] = "1"
os.system("grep 'no experience' ./input/resume.txt > cache")
f = open("cache","r")
if f.read() != "":
    prof[6] = "0"

        
os.system("grep 'english' ./input/resume.txt > cache")
f = open("cache","r")
if f.read() != "":
    prof[7] = "1"
os.system("grep 'English' ./input/resume.txt > cache")
f = open("cache","r")
if f.read() != "":
    prof[7] = "1"

####################################
for i in range(len(att)):
    if i==len(att)-1:
        print(att[i])
        break
    print(att[i]+",",end=" ")

for i in range(len(prof)):
    if i==len(prof)-1:
        print(prof[i],end=" ")
        break
    print(prof[i]+",",end=" ")

os.system("rm cache")
