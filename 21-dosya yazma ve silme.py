fileToAppend = open("deneme2.txt","w")
fileToAppend.close()
import os
os.remove("deneme2.txt") #silme

os.rmdir("Yeni klasör")  #klasör siler
