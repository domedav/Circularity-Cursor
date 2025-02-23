# Very basic, for simple task

from PIL import Image

name = input("filename: ")
scale = input("base scale: ")
size_to = int(input("new scale: "))
x = 0
while x < 60:
	x = x + 1
	if x < 10:
		img = Image.open(f"{name}{scale}_00{x}.png")
		new_img = img.resize((size_to, size_to))
		new_img.save(f"{name}{size_to}_00{x}.png")
	else:
		img = Image.open(f"{name}{scale}_0{x}.png")
		new_img = img.resize((size_to, size_to))
		new_img.save(f"{name}{size_to}_0{x}.png")
