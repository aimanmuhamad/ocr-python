from PIL import Image

im_file = "page09.jpg"

im = Image.open(im_file)

im.rotate(180).show()