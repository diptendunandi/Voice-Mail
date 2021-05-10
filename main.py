import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
#It will recognize the speaker's voice
engine = pyttsx3.init()
#Computer speaking with me


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            #here we call Google API to convert source's voice into text
            print(info)
            return info.lower()
        #everything will be in lowercase
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('diptendu.nandi1999@gmail.com', '1diptendu1')
    email = EmailMessage()
    email['From'] = 'diptendu.nandi1999@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'dad': 'debkumar.nandi1969@gmail.com',
    'mum': 'amita.nandi2017@gmail.com',
    'me':'diptendu.nandi1999@gmail.com'
    
}


def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey homie. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
        
get_email_info()