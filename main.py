from PIL import Image
import math

img = Image.open("y.png")

width, height = img.size
columns = width/8
rows = height/8
totalsprites = columns*rows
print("width: {}px".format(width))
print("Height: {}px".format(height))
print("Columns: {}".format(columns))
print("Rows: {}".format(rows))
print ("Total Sprites: {}".format(totalsprites))

hashlist = []
uniqueimglist = []


left = 0
top = 0
right = 8
bottom = 8

r = 1
c = 1
i = 1

while r <= rows:
  while c <= columns:
    im1 = img.crop((left, top, right, bottom))

    hash = im1.tobytes()

    if hash not in hashlist:
      hashlist.append(hash)
      uniqueimglist.append(im1)
      i += 1
    c += 1
    left += 8
    right += 8
  c = 1
  r += 1
  left = 0
  right = 8
  top += 8
  bottom += 8

rows = math.ceil(len(uniqueimglist)/10)
cols = 10

new_image = Image.new('RGB', ((cols*8), (rows*8)), color = (224, 248, 207))

i = 0
xpos = 0
ypos = 0

for index in range(len(uniqueimglist)):
  new_image.paste(uniqueimglist[i],(xpos,ypos))
  i += 1
  xpos += 8
  if xpos == 80:
    xpos = 0
    ypos += 8
print("Unique Sprites: {}".format(len(uniqueimglist)))
new_image.save("final.png")
