file = open("text.txt", "w+")
file.write("This is shift")
file.lseek(0,0)
count_ch = file.readlines()
print count_ch
file.close()