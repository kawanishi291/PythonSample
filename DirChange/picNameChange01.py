import random

l = list(range(70))

file_name = "sample01.txt"
with open(file_name, 'w') as f:
    for num in range(70):
        var = random.sample(l, 1)[0]
        cmd = "REN " + str(num) + "A.jpg " + str(var) + ".jpg\n"
        f.write(cmd)
        l.remove(var)
        #print(l)