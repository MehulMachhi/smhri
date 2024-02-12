import base64
import string 
import random
from django.core.files.base import ContentFile

def convert_to_base64(bytedata:str):
    format, basestr = bytedata.split(';base64')
    ext = format.split('/')[-1]
    res = ''.join(random.choices(string.ascii_letters, k=8))
    data = ContentFile(base64.b64decode(basestr), name=res+'.'+ ext)
    return  data