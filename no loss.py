filename = "colors"
o_w = 256
o_h = 256
file_variable = open(filename+".ppm")
x = file_variable.readlines()
file_variable.close()
mylist = x[3:]
newfile = []

numcolors = 256 * 256


#for i in range(numcolors // 2):
   # firstindex = (3*i)
    #secondindex = (3*i + 1)
    #thirdindex = (3*i + 2)
 #   fourthindex = (3*i + 3)
  #  fifthindex = (3*i + 4)
   # sixthindex = (3*i + 5)
  #  newfile.append(((int(mylist[firstindex])+int(mylist[fourthindex]))/2))
   # newfile.append(((int(mylist[secondindex])+int(mylist[fifthindex]))/2))
    #newfile.append(((int(mylist[thirdindex])+int(mylist[sixthindex]))/2))

#/for i in range(((numcolors // 2)+numcolors)):
    #firstindex = (3*i)
    #secondindex = (3*i + 1)
    #thirdindex = (3*i + 2)
    #fourthindex = (3*i + 3)
    #fifthindex = (3*i + 4)
    #sixthindex = (3*i + 5)
    #newfile.append(((int(mylist[firstindex])+int(mylist[fourthindex]))/2))
    #newfile.append(((int(mylist[secondindex])+int(mylist[fifthindex]))/2))
    #newfile.append(((int(mylist[thirdindex])+int(mylist[sixthindex]))/2))


for i in range(numcolors): 
    firstindex = 12*i
    secondindex = 12*i + 1
    thirdindex = 12*i + 2
    fourthindex = 12*i + 3
    fifthindex = 12*i + 4
    sixthindex = 12*i + 5
    seventhindex = 12*i + 6
    eigthindex = 12*i + 7
    ninthindex = 12*i + 8
    tenthindex = 12*i + 9
    eleventhindex = 12*i + 10
    twelfthindex = 12*i + 11
    newfile.append(((float(mylist[firstindex])+float(mylist[fourthindex]))/2))
    newfile.append(((float(mylist[secondindex])+float(mylist[fifthindex]))/2))
    newfile.append(((float(mylist[thirdindex])+float(mylist[sixthindex]))/2))
    newfile.append(((float(mylist[fourthindex])+float(mylist[seventhindex]))/2))
    newfile.append(((float(mylist[fifthindex])+float(mylist[eigthindex]))/2))
    newfile.append(((float(mylist[sixthindex])+float(mylist[ninthindex]))/2))
    newfile.append(((float(mylist[seventhindex])+float(mylist[tenthindex]))/2))
    newfile.append(((float(mylist[eigthindex])+float(mylist[eleventhindex]))/2))
    newfile.append(((float(mylist[ninthindex])+float(mylist[twelfthindex]))/2))

outfile = open(filename+"4.ppm","w")
outfile.write("P3\n")
outfile.write("256 256\n")
outfile.write("255\n")
for i in newfile:
    outfile.write(str(int(i)))
    outfile.write("\n")
outfile.close()