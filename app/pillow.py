from PIL import Image,ImageFont, ImageDraw
from datetime import date

#data = (7cm, 14,4 cm)

#name = (5,9 cm, 18,80 cm)

def configure_image(name, cpf):
    try:
        data = date.today().strtime('%d%m%Y')
        coord_data = (264,544)
        coord_name = (222, 710)

        image = Image.open(r'media/card.png')
        #font

        black_rgb =(0,0,0)
        draw = ImageDraw.Draw(image)

        draw.text(coord_data, data, fill=black_rgb)
        draw.text(coord_name, name, fill=black_rgb)
        final_image = image.save(f'invite_for_{name}.png')
        return final_image
    except:
        raise 'Something get wrong'
    


    

