import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer() 
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source,duration=1)
            print("Listening . . .")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print("You said: " + info)
            return info.lower()
    except:
        pass

def send_email(reciever, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("sanjayroxx804@gmail.com", "aryan2kool")
    email = EmailMessage()
    email['From'] = 'sanjayroxx804@gmail.com'
    email['To'] = reciever
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    
email_list = {
    'red' : 'aryan.bhardwaj1233@gmail.com',
    'pink' : 'anshikadigarse2002@gmail.com',
    'yellow' : '7999254145sanjay@gmail.com',
    'white' : 'awantikanigam101220@gmail.com'
}
    
def get_email_info():
    talk('To whom you want to send the message')
    name = get_info()
    reciever = email_list.get(name)
    print(reciever)
    talk('What is the subject of your email')
    subject = get_info()
    talk('What is the message you want to send')
    message = get_info()
    send_email(reciever, subject, message)
    talk('Hey Lazy man The mail is sent')
    talk('Do you want to send more email')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
    
get_email_info()