import random
import urllib.request

def download_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpeg"
    urllib.request.urlretrieve(url, full_name)

download_image("https://pbs.twimg.com/profile_images/645794884943675394/sS_sfIN_.jpg")