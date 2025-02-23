name = input("icon name: ")

f = open(f"{name}.animated.cursor", "w")

x = 0
while x < 60:
	x = x + 1
	if x < 10:
		f.write(f"96 48 48 {name}96/{name}96_00{x}.png 16\n")
	else:
		f.write(f"96 48 48 {name}96/{name}96_0{x}.png 16\n")

x = 0
while x < 60:
	x = x + 1
	if x < 10:
		f.write(f"64 32 32 {name}64/{name}64_00{x}.png 16\n")
	else:
		f.write(f"64 32 32 {name}64/{name}64_0{x}.png 16\n")

x = 0
while x < 60:
	x = x + 1
	if x < 10:
		f.write(f"48 24 24 {name}48/{name}48_00{x}.png 16\n")
	else:
		f.write(f"48 24 24 {name}48/{name}48_0{x}.png 16\n")

x = 0
while x < 60:
	x = x + 1
	if x < 10:
		f.write(f"32 16 16 {name}32/{name}32_00{x}.png 16\n")
	else:
		f.write(f"32 16 16 {name}32/{name}32_0{x}.png 16\n")

x = 0
while x < 60:
	x = x + 1
	if x < 10:
		f.write(f"24 12 12 {name}24/{name}24_00{x}.png 16\n")
	else:
		f.write(f"24 12 12 {name}24/{name}24_0{x}.png 16\n")

f.close()

print(f"Use:\n\txcursorgen {name}.animated.cursor {name}")
print(f"Then:\n\tsudo cp {name} /usr/share/icons/Adwaita-Custom-Icons/cursors")
