# Very basic, good for its purpose
name = input("icon name: ")

f = open(f"{name}.cursor", "w")

f.write(f"96 48 48 {name}96.png 50\n")
f.write(f"64 32 32 {name}64.png 50\n")
f.write(f"48 24 24 {name}48.png 50\n")
f.write(f"32 16 16 {name}32.png 50\n")
f.write(f"24 12 12 {name}24.png 50\n")
f.close()

print(f"Use:\n\txcursorgen {name}.cursor {name}")
print(f"Then:\n\tsudo cp {name} /usr/share/icons/Circularity-Cursor/cursors")
