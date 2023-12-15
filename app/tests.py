from django.test import TestCase
import smtplib

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


image = configure_image('Carlos Figueiredo')



def send_mail(email, name):
    try:
        email_server = smtplib.SMTP('smtp.gmail.com', 587)
        email_server.starttls()
        email_server.login('emailsenderneg@gmail.com','emailsender1234')
        sender = 'emailsenderneg@gmail.com'
        recipient = email
        content= f'Hello {name}, You have asked for your invite some time ago\n here is!!\n{image}'
        email_server.sendmail(sender, recipient, content)
        email_server.quit()
    except Exception as e:
        print(e)
        return f'Error: {e}'

send_mail('devdeoliveira06@gmail.com', 'Carlos Figueiredo')




