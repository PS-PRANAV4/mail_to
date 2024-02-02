from PIL import Image,ImageDraw,ImageFont
from san_mail.settings import BASE_DIR
import os
from rest_framework.decorators import action
from datetime import datetime


def send_single_mail():
    
    
    
    print(BASE_DIR)
    image_path = os.path.join(BASE_DIR,'send_mail/recipt.jpg')
    image = Image.open(image_path)
    draw_amount = ImageDraw.Draw(image)
    draw_date = ImageDraw.Draw(image)
    draw_name = ImageDraw.Draw(image)
    draw_no = ImageDraw.Draw(image)
    font = ImageFont.load_default().font_variant(size=40)
    font_date = ImageFont.load_default().font_variant(size=20)
     
    position = (300,400)
    text_amount = '5000'
    text_name = 'pranav'
    text_date = datetime.strftime(datetime.now(),"%d-%m-%y")
    print(text_date)
    no = "1"
    text_colour = (0,0,0)
    draw_amount.text(position,text_amount,font=font,fill=text_colour)
    
    
    
    draw_date.text((800,150),text_date,font=font_date,fill=text_colour)
    
    
    
    draw_name.text((500,170),text_name,font=font,fill=text_colour)
    draw_no.text((800,120),no,font=font_date,fill=text_colour)
    
    image.save('./static_photo_of_recipt/pranav.jpg')


