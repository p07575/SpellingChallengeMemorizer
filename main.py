import pyttsx3, sys, os, time, jieba, re
global paragraph


engine = pyttsx3.init() 

def cls():
    os.system("cls")
def close():
    cls()
    print("Thankyou for using Spelling Challenge Memorizer!!!")
    print('\n\n\n')
    print("This software is based on the MIT License.")
    sys.exit()
    exit()
def say(words):
    engine.say(words)
    engine.runAndWait() 
def menu():
    global paragraph
    paragraph=""
    print("Please enter your paragraph below!")
    while True:
        w = input("")
        if w == "":
            break
        paragraph += w
    language = input("Which language you want to use?(en,zh)>>> ")
    say_text(load_text(language))
def en(d):
    return re.split('[.!?]', d)
def load_text(language):
    global paragraph
    if language == "en":
        text = en(paragraph)
    else:
        text = jieba.lcut(paragraph)
    return text
def say_text(text):
    cls()
    print("Now start?")
    os.system("pause")
    for t in text:
        for i in range(2):
            say(t)
            time.sleep(1.5)
    close()

menu()