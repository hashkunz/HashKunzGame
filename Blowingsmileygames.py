#___________________อิมพอตโมดูจ__________________________

import random
import time

#___________________เครดิต____________________________

print ("Welcome To Game hammer paper scissors")
print 
print ("Create By HashKunz")
print ("___________________")
print ("                     ")
print ("Can Be Contacted At ")
print ("                    ")
print ("Gmail    | afdan2014dan@gmail.com ")
print ("Facebook | Ana Afdon Selamae")
print ("ID Line  | afdan-00")
print ("                        ")

#___________________ประกาศตัวแปร__________________________

paper = (3)
scissors = (2)
hammer = (6)
p = ("กระดาษ")
s = ("กรรไกร")
h = ("ค้อน")

#____________________ให้ bot สุ่ม_________________________

bot = (random.choice([paper, scissors, hammer]))
print (bot)

#____________________แสดงตัวเลือก_________________________

print ("[1] กระดาษ")
print ("[2] กรรไกร")
print ("[3] ค้อน")
print ("             ")
person = int(input("เลือก 1 อย่าง >  "))

#____________________กำหนดเงื่อนไข________________________

if person == 1:
  print ("คุณเลือก [ กระดาษ ]")
  answer = (paper+bot)
  
elif person == 2:
  print ("คุณเลือก [ กรรไกร ]")
  answer = (scissors+bot)
  
elif person == 3:
  print ("คุณเลือก [ ค้อน ]")
  answer = (hammer+bot)

else:
  print ("ไม่มีตัวเลือกที่คุณพิมพ์")
  
print ("กำลังวิเคราะห์....")
time.sleep(1)

#____________________กำหนดเงื่อนไขจากเงื่อนไขด้านบน___________________

if answer == 5:
  print("* ประกาศผล. *")
  if bot == 3:
    print ("บอทเลือก >",p)
  elif bot == 2:
    print ("บอทเลือก >",s)
  if person == 3:
    print ("คุณเลือก >",p)
  elif person == 2:
    print ("คุณเลือก >",s)
  if (bot < person):
    print ("[ บอท ชนะ! ]")
  if (person < bot):
    print ("[ คุณ ชนะ! ]")

if answer == 9:
  print(" *ประกาศผล.. *")
  if bot == 6:
    print ("บอทเลือก >",p)
  if bot == 3:
    print ("บอทเลือก >",s)
  if person == 6:
    print ("คุณเลือก >",p)
  if person == 3:
    print ("คุณเลือก >",s)
  if (bot < person):
    print (" [ บอท ชนะ! ]")
  if (person < bot):
    print (" [ คุณ ชนะ! ]")
    
if answer == 8:
  print("* ประกาศผล... *")
  if bot == 6:
    print ("บอทเลือก >",p)
  if bot == 2:
    print ("บอทเลือก >",s)
  if person == 6:
    print ("คุณเลือก >",p)
  if person == 2:
    print ("คุณเลือก >",s)
  if (person < bot):
    print ("[ บอท ชนะ! ]")
  if (bot < person):
    print ("[ คุณ ชนะ!]")
  
if answer == 6 or answer == 4 or answer == 12:
  print("* ประกาศผล!! *")
  print 
  print(" เสมอกัน!! ")
  
#____________________สิ้นสุดการทำงาน_________________________# HashKunzGame
