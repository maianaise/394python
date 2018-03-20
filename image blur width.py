
filename = "colors"

file_variable = open(filename+".ppm")
x = file_variable.readlines()
file_variable.close()
mylist = x[3:]
numcolors = 256 * 256
newcheck = []
for i in range(numcolors // 2): # how many times my loop ru
    firstindex = 6*i
    secondindex = 6*i + 1
    thirdindex = 6*i + 2
    fourthindex = 6*i + 3
    fifthindex = 6*i + 4
    sixthindex = 6*i + 5
    newcheck.append(((int(mylist[firstindex])+int(mylist[fourthindex]))/2))
    newcheck.append(((int(mylist[secondindex])+int(mylist[fifthindex]))/2))
    newcheck.append(((int(mylist[thirdindex])+int(mylist[sixthindex]))/2))
    
outfile = open("new"+filename+".ppm","w")
outfile.write("P3\n")
outfile.write("128 256\n")
outfile.write("255\n")
for i in newcheck:
    outfile.write(str(int(i)))
    outfile.write("\n")



outfile.close()
