filename = "colors"
o_w = 256
o_h = 256
file_variable = open(filename+".ppm")
x = file_variable.readlines()
file_variable.close()
mylist = x[3:]
newfile = []
newfile2 = []

width = o_w
height = o_h // 2

for i in range(int(height)):
    for j in range(int(width)):
        r1 = i * width * 3 * 2 + 3 * j
        g1 = r1 + 1
        b1 = r1 + 2
        r2 = i * width * 3 * 2 + 3 * j + 3 * width
        g2 = r2 + 1     
        b2 = r2 + 2
        newfile.append((int(mylist[r1]) + int(mylist[r2])) / 2)
        newfile.append((int(mylist[g1]) + int(mylist[g2])) / 2)
        newfile.append((int(mylist[b1]) + int(mylist[b2])) / 2)
       
numcolors = 256 * 128

for i in range(numcolors // 2): # how many times my loop ru
    firstindex = 6*i
    secondindex = 6*i + 1
    thirdindex = 6*i + 2
    fourthindex = 6*i + 3
    fifthindex = 6*i + 4
    sixthindex = 6*i + 5
    newfile2.append(((int(newfile[firstindex])+int(newfile[fourthindex]))/2))
    newfile2.append(((int(newfile[secondindex])+int(newfile[fifthindex]))/2))
    newfile2.append(((int(newfile[thirdindex])+int(newfile[sixthindex]))/2))
    
        
outfile = open(filename+"2.ppm","w")
outfile.write("P3\n")
outfile.write("128 128\n")
outfile.write("255\n")
for i in newfile2:
    outfile.write(str(int(i)))
    outfile.write("\n")
outfile.close()