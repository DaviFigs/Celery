from django.test import TestCase
import smtplib
from email.message import EmailMessage

# Create your tests here.

from PIL import Image,ImageFont, ImageDraw
from datetime import date

#data = (7cm, 14,4 cm)

#name = (5,9 cm, 18,80 cm)

def configure_image(name):
    try:
        data = date.today().strftime('%d/%m/%Y')
        coord_data = (590,1180)
        coord_name = (350, 1790)

        image = Image.open(r'media/card.png')
        #font

        black_rgb =(0,0,0)
        font = ImageFont.truetype('font/roboto/Roboto-Regular.ttf', 60)
        draw = ImageDraw.Draw(image)

        draw.text(coord_data, data, font=font,fill=black_rgb)
        draw.text(coord_name, name, font=font,fill=black_rgb)
        image.save(f'invite_for_{name}.png')
        final_image = image
        return final_image
    
    except Exception as e:
        raise f'Something get wrong: {e}'
    

#Creating test for email sent


class SendEmail:
    def __init__(self):
        self.email_server = smtplib.SMTP('smtp.gmail.com', 587)
        
    def __enter__(self):
        self.email_server.starttls()
        self.email_server.login('emailsenderneg@gmail.com', 'emailsender123')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.email_server.quit()                                                                                                                        

    def send_email(self, email, name, image):
        sender = 'emailsenderneg@gmail.com'
        recipient = [f'{email}']
        content= f'Hello {name}, You have asked for your invite some time ago\n here is!!\n{image}'
        self.email_server.sendmail(sender, recipient, content)


image = configure_image('Giovana Pianezze')

'''
#first try withoout html
def send_mail(email, name):
    try:
        email_server = smtplib.SMTP('smtp.gmail.com', 587)
        email_server.starttls()
        email_server.login('emailsenderneg@gmail.com','egoz zmsj tpva ptki')
        sender = 'emailsenderneg@gmail.com'
        recipient = email
        content= f'Hello {name}, You have asked for your invite some time ago\n here is!!\n{image}'
        email_server.sendmail(sender, recipient, content)
        email_server.quit()
    except Exception as e:
        print(e)
        return f'Error: {e}'

send_mail('giovana.talaveira@estudante.ifms.edu.br', 'Giovana')'''


def send_mail(email, name):
    try:
        email_server = smtplib.SMTP('smtp.gmail.com', 587)
        email_server.starttls()
        email_server.login('emailsenderneg@gmail.com','egoz zmsj tpva ptki')
        sender = 'emailsenderneg@gmail.com'
        recipient = email

        message = EmailMessage()
        message['Subject'] = 'Here is your invite'
        message_body = f"""

                    <h1>Good Morning!! {name}\n</h1>
                    <h5>You have asked for a invite, so, there is your invite!!</h5>
                    <img src="/home/davi/DEV/GIT/Celery/Celery/media/card.png"></img>

                        """
        message.add_header('Content-Type', 'text/html')
        message.set_payload(message_body)

        email_server.sendmail(sender, recipient, message.as_string().encode('utf-8'))
        email_server.quit()
    except Exception as e:
        print(e)
        return f'Error: {e}'

send_mail('emailsenderneg@gmail.com', 'Giovana')









