import requests
from PIL import Image
import  numpy as np

url = 'https://i.pinimg.com/originals/7f/13/e9/7f13e950f973962a84fa536575efc24a.jpg'
url9 = 'https://pojelaniye.ru/uploads/posts/2019-04/1555156142_9let-pozdravleniya.jpg'

def get_images(url_, name):

    # get an image
    cont = requests.get(url9)

    # save to a file
    with open(f"{name}.jpg", "wb") as f:
        f.write(cont.content)
