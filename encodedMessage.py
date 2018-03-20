

with open("colors.ppm") as fn:
    file_object = fn.readlines()

fn.close()

L = file_object[3:]  # start with the fourth line, first three lines are useless for the operation below

# insert message below

L = list(map(int, L))

i = 0

width = 256.0
height = 256.0

wd = input("Please input a three lettered-word: ")
list(wd)

print(L[:3])

num1 = ord(wd[0]) - ord('a') + 1
num0 = ord(wd[1]) - ord('a') + 1
num2 = ord(wd[2]) - ord('a') + 1

L[i + 2] += num2
L[i] += num0
L[i + 1] += num1

L[2] = 0
L[1] = 255
L[0] = 0
L[i + int((width*height*3/2)+(width*3/2))] += num0
L[i + int((width*height*3/2 + 1)+(width*3/2))] += num1
L[i + int((width*height*3/2 + 2)+(width*3/2))] += num2

#L[i + int((width*height*3/2)+(width*3/2))] = 0
#L[i + int((width*height*3/2 + 1)+(width*3/2))] = 255
#L[i + int((width*height*3/2 + 2)+(width*3/2))] = 0


L = ['{:.0f}'.format(x) for x in L]
for i in range(len(L)):
    L[i] = L[i] + "\n"

print(L[:3])

with open('colors1.ppm', 'w') as fh:
        fh.write("P3\n")
        fh.write("256 256\n")
        fh.write("255\n")
        for i in range(len(L)):
            fh.write(L[i])

fh.close()