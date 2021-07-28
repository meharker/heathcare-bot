import  os
import time

print("Hello there, I am your digital docter.")

print("*note not all diognosis are fully acrute. this is not a replacement for real docters. some devises may see words alreay placed where you enter info, just add a space and enter the info as normal")

time.sleep(3)

name = input(print("what is your full name?"))

number =  input(print("what is your phone number? "))

email = input(print("what is your email? "))

print("Thank You!")
print("pls wait while we prosses your info...")

time.sleep(10)

print("hello " +name)
pain = input(print("on a scale of 1-5 how will you rate your pain"))

if pain == 1:
    print("that is very minor pain perhaps you should wait it out.")
    time.sleep(20)

if pain == 2:
    print("that is minor pain perhaps you should wait it out and if it increses come back")
    time.sleep(20)

if pain == 3:
    print("that is  minor pain perhaps you should wait it out and if it increses come back or take a advil ")
    time.sleep(20)

if pain == 4:
    print("that is a moderate amount of pain. try takeing some off the conter medicine for what you feel.")
    problem = input(print("what are you feeling(allergy,head pain,vomiting,cold,fever)"))
   
    if problem == "allergy":
        print("ok, we advise you to take some allegra from a local store. if your semptoms increse contact a docter or if you have large side effects from allegra contact a docter and stop useing allergra ")
        time.sleep(20)

