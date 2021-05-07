
file_name = "sample00.txt"
with open(file_name, 'w') as f:
    for num in range(70):
        cmd = "REN " + str(num) + ".jpg " + str(num) + "A.jpg \n"
        f.write(cmd)