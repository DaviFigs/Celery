from django.test import TestCase

# Create your tests here.

from PIL import Image,ImageFont, ImageDraw
from datetime import date

#data = (7cm, 14,4 cm)

#name = (5,9 cm, 18,80 cm)

def configure_image(name, cpf):
    try:
        data = date.today().strftime('%d/%m/%Y')
        coord_data = (700,1235)
        coord_name = (700, 1840)

        image = Image.open(r'media/card.png')
        #font

        black_rgb =(0,0,0)
        #font = ImageFont.truetype
        draw = ImageDraw.Draw(image)

        draw.text(coord_data, data, fill=black_rgb)
        draw.text(coord_name, name, fill=black_rgb)
        image.save(f'invite_for_{name}.png')
        final_image = image
        return final_image
    
    except Exception as e:
        raise f'Something get wrong: {e}'
    


image = configure_image('carlos', '00000000')
image.show()