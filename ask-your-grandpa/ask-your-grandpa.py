from PIL import Image
im = Image.open('ask.jpg', 'r')
width, height = im.size
pixel_values = list(im.getdata())

print(pixel_values)


# with open("ask.jpg", "rb") as fil:
#     for line in fil.readlines():
#         print(line)