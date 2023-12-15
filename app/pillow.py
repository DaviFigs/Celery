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

        black_rgb =(0,0,0)
        font = ImageFont.truetype('font/roboto/Roboto-Regular.ttf', 60)
        draw = ImageDraw.Draw(image)

        draw.text(coord_data, data, font=font,fill=black_rgb)
        draw.text(coord_name, name, font=font,fill=black_rgb)
        #image.save(f'invite_for_{name}.png') we won't save the pics
        final_image = image
        return final_image
    
    except Exception as e:
        raise f'Something get wrong: {e}'
    


    

