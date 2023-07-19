import base64
from PIL import Image
from io import BytesIO

def base64_to_png(base64_data):
    image_data = base64.b64decode(base64_data)
    image = Image.open(BytesIO(image_data))
    image.save('C:/Users/User/Desktop/Ben/steel_label/api/tag_image.png', 'PNG')
    return image