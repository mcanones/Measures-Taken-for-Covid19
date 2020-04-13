import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formatdate
import os
#import email
import email.mime.application
from getpass import getpass

def generate_mail(mailto,p1,p2):
    if mailto:

        #Generate mail
        msg = MIMEMultipart()
        msg["Subject"] = 'Automatic Report Email'
        msg["Date"] = formatdate(localtime=True)
        msg.attach(MIMEText('Here you have your automatic report\n\nEnjoy\n\n\n\n'))
        
        fp=open("./output/report.pdf",'rb')
        att = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
        fp.close()
        msg.attach(att)
       
        img_data = open('./output/graph_confirmed'+p1+p2+'.png', 'rb').read()
        image = MIMEImage(img_data, name=os.path.basename('./output/graph_confirmed'+p1+p2+'.png'))
        msg.attach(image)

        img_data2 = open('./output/graph_deaths'+p1+p2+'.png', 'rb').read()
        image2 = MIMEImage(img_data2, name=os.path.basename('./output/graph_deaths'+p1+p2+'.png'))
        msg.attach(image2)

        img_data3 = open('./output/graph_measures'+p1+p2+'.png', 'rb').read()
        image3 = MIMEImage(img_data3, name=os.path.basename('./output/graph_measures'+p1+p2+'.png'))
        msg.attach(image3)

        #Send mail 
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        password = getpass("Email Password: ")
        server.login('from@gmail.com', password)
        server.sendmail('from@gmail.com', mailto, msg.as_string())
        server.quit()