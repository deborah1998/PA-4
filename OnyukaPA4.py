import os


#Function Name:read_in_file
#Purpose:read in a file from the user and return it once they give one that exists
#Parameters:None
#Return:filename

def read_in_file():
    filename = input("Please enter the file you would like to input")
    while not os.path.exists(filename):
        filename = input("Please enter the file you would like to input")

    return filename


#Function Name:proccess_file
#Purpose:proccessing the files
#Parameters:filename,outfile_name
#Return:none


def process_file(filename,outfile_name):

#use try and except to prevent runtime errors
    try:

        inputfile = open(filename, "r")
        outputfile = open(outfile_name, "w")
        num_of_survivors = 0
        people_class1 = 0
        people_class2 = 0
        people_class3 = 0
        people_over_50 = 0
        survivors_class1=0
        survivors_class2= 0
        survivors_class3 = 0
        survivors_age50=0
        for line in inputfile:
            status, survived, name, sex, age, embark, destination = line.split("|")
            if survived == "1":
                num_of_survivors += 1
                print(name, destination,file=outputfile)

            if status == "1":
                    people_class1 += 1
                    if survived=="1":
                        survivors_class1+=1

            elif status == "2":
                people_class2 += 1
                if survived=="1":
                    survivors_class2+=1



            elif status == "3":
                people_class3 += 1
                if survived=="1":
                    survivors_class3+=1


            if age > "50":
                people_over_50 += 1
                if survived=="1":
                    survivors_age50+=1



        survivors_1 = (survivors_class1 / people_class1) * 100
        survivors_2 = (survivors_class2 / people_class2) * 100
        survivors_3 = (survivors_class3 / people_class3) * 100
        survivors_over_50 = (survivors_age50/people_over_50 ) * 100
        print("The number of survivors is",num_of_survivors,"The percent of survivors in class 1 is", survivors_1,"The percent of survivors in class 2 is",survivors_2)
        print( "The percent of survivors in class 3 is",survivors_3,"The percent of survivors over the age of  50 are",survivors_over_50 )


        inputfile.close()
        outputfile.close()
    except FileNotFoundError:
        print("This file does not exist")
        SystemExit(1)

#Function Name:main
#Purpose:run the overall program
#Parameters:none
#Return:none


def main():
    print("This program will determine the total amount of survivors on the titanic as well as the percentage of people who survived from each class.")
    print("This program will also determine how many people survived the titanic who were over the age of 50 years old")
    inputfile=read_in_file()
    outputfile =input("Please enter the the name of the outputfile")
    process_file(inputfile,outputfile)

main()
