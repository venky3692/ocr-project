import pytesseract as pt
from PIL import Image
import os
# os.path.expanduser('~')  +'/Downloads/' + 
def read_image(image): 
    print("This is image", image.filename)
    text = pt.image_to_string(Image.open(image))
    return text


# venkatesh@inbound-coast-368112.iam.gserviceaccount.com