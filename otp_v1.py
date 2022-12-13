import random
import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('aniketgupta27@dbatu.ac.in',"hxeywiout")

otp = random.randrange(100000, 1000000)

message = "OTP for login is "+str(otp)

server.sendmail('aniketgupta27@dbatu.ac.in','ajg16201@gmail.com',message)
server.quit()

user = int(input("Enter the OTP: "))
if(user == otp):
    print("Access granted!")
else:
    print("Access Denied!")