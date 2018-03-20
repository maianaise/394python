filename = "colors"
o_w = 256
o_h = 256
file_variable = open(filename+".ppm")
x = file_variable.readlines()
file_variable.close()
mylist = x[3:]
newfile = []
newfile2 = []
newfile3 = []
newfile4 = []


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
        newfile.append(((int(mylist[r1])) + int(mylist[r2])) / 2)
        newfile.append(((int(mylist[g1])) + int(mylist[g2])) / 2)
        newfile.append(((int(mylist[b1])) + int(mylist[b2])) / 2)
       
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
    

n_w = 128
n_h = 128 // 2

for i in range(int(n_h)):
    for j in range(int(n_w)):
        r1 = i * n_w * 3 * 2 + 3 * j
        g1 = r1 + 1
        b1 = r1 + 2
        r2 = i * n_w * 3 * 2 + 3 * j + 3 * n_w
        g2 = r2 + 1     
        b2 = r2 + 2
        newfile3.append((int(newfile2[r1]) + int(newfile2[r2])) / 2)
        newfile3.append((int(newfile2[g1]) + int(newfile2[g2])) / 2)
        newfile3.append((int(newfile2[b1]) + int(newfile2[b2])) / 2)
 
numcolors = 128 * 64
       
for i in range(numcolors // 2): 
    firstindex = 6*i
    secondindex = 6*i + 1
    thirdindex = 6*i + 2
    fourthindex = 6*i + 3
    fifthindex = 6*i + 4
    sixthindex = 6*i + 5
    newfile4.append(((int(newfile3[firstindex])+int(newfile3[fourthindex]))/2))
    newfile4.append(((int(newfile3[secondindex])+int(newfile3[fifthindex]))/2))
    newfile4.append(((int(newfile3[thirdindex])+int(newfile3[sixthindex]))/2))
    
    
    
    
        
outfile = open(filename+"3.ppm","w")
outfile.write("P3\n")
outfile.write("64 64\n")
outfile.write("255\n")
for i in newfile4:
    outfile.write(str(int(i)))
    outfile.write("\n")
outfile.close()

