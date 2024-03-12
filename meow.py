import code128
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import random
import string

height = 60
margin = 16
thickness = 1

# generate random characters
seed = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
body = f"INV{datetime.now().strftime('%y%j%H%M')}{seed}"
code = code128.image(body, height=(height - margin), thickness=thickness)
img = Image.new("RGB", (code.width, code.height + margin), "white")
img.paste(code, (0, 0))
caption = Image.new("RGB", (code.width, margin), "white")
draw = ImageDraw.Draw(caption)
# font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 18)
font = ImageFont.truetype("/System/Library/Fonts/Andale Mono.ttf", margin - 2)
draw.text((0, 0), body, font=font, fill="black")
text_width = font.getmask(body).getbbox()[2]
img.paste(caption, (int((code.width/2) - (text_width/2)), code.height))
img.save("barcode.png")
