import code128
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import random
import string
import sys

height = 60
margin = 16
thickness = 1
cable_margin = 48

# get arguments
cable = int(sys.argv[1])

# generate random characters
seed = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
body = f"INV{datetime.now().strftime('%y%j%H%M')}{seed}"
code = code128.image(body, height=(height - margin), thickness=thickness)
img_width = (code.width * 2 + cable_margin) if cable else code.width
img = Image.new("RGB", (img_width, code.height + margin), "white")
img.paste(code, (0, 0))
caption = Image.new("RGB", (code.width, margin), "white")
draw = ImageDraw.Draw(caption)
# font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 18)
font = ImageFont.truetype("/System/Library/Fonts/Andale Mono.ttf", margin - 2)
draw.text((0, 0), body, font=font, fill="black")
text_width = font.getmask(body).getbbox()[2]
img.paste(caption, (int((code.width/2) - (text_width/2)), code.height))
if cable:
    wide_text = sys.argv[2]
    wide_caption = Image.new("RGB", (code.width, height), "white")
    draw = ImageDraw.Draw(wide_caption)
    font = ImageFont.truetype("/System/Library/Fonts/Futura.ttc", height - margin - 6)
    # font = ImageFont.truetype("/System/Library/Fonts/Andale Mono.ttf", height - margin - 4)
    draw.text((0, 0), wide_text, font=font, fill="black")
    text_width = font.getmask(wide_text).getbbox()[2]
    text_height = font.getmask(wide_text).getbbox()[3]
    img.paste(wide_caption, (int(cable_margin + code.width + ((code.width/2) - (text_width/2))), int((height/2) - (text_height/1.5))))
img.save("barcode.png")
