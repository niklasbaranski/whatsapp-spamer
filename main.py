import datetime
import pywhatkit as kit
import pyautogui as auto

#start query (phone + message)
print("Who do you want to send a message to?")
phone = input("Telephoner's: ")
print("What message do you want to write?")
message = input("Message: ")
#query time
e = datetime.datetime.now()
if e.minute <= 59:
    minute = e.minute + 1
else:
    minute = 0
if e.second > 45:
    minute = minute + 10
print("Your message will be sent in less than a minute.")
#send message
kit.sendwhatmsg(phone, message, e.hour, minute)
#instant spam message
while True:
    auto.write(message)
    auto.press('enter')
