import os


def read_in_file():
    filename = input("Please enter the file you would like to input")
    while not os.path.exists(filename):
        filename = input("Please enter the file you would like to input")

def process_file(infilename,outfilename):
    try:
        inputfile = open(infilename,"r")
        count = 0
        sum = 0
        for line in inputfile:
            status,survived,name,sex ,age ,embark,destination = line.split("|")
            if survived ==1:
                count+=1
                sum +=line
                num_of_survivors = sum
                print("The number  of people to survive tht titanic are"+num_of_survivors)
                if status ==1:
                count=0















    except:
        FileNotFoundError
