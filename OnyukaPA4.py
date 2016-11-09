import os


def read_in_file():
    filename = input("Please enter the file you would like to input")
    while not os.path.exists(filename):
        filename = input("Please enter the file you would like to input")

def process_file(infilename):
    try:
        inputfile = open(infilename,"r")
        num_of_survivors = 0
        people_class1 = 0
        people_class2 = 0
        people_class3 = 0
        people_over_50=0
        for line in inputfile:
            status,survived,name,sex ,age ,embark,destination = line.split("|")
            if survived ==1:
                num_of_survivors+=1
                if status ==1:
                    people_class1+=1
                    survivors_1 =(people_class1/num_of_survivors)*100

                elif status==2:
                    people_class2+=1
                    survivors_2 = (people_class2/num_of_survivors)*100

                elif status ==3:
                    people_class3+=1
                survivors_3=(people_class3/num_of_survivors)*100

                if age > 50:
                    people_over_50+=1
                    survivors_over_50 = (people_over_50/num_of_survivors)*100
        inputfile.close()



    except:
        FileNotFoundError
    print("File does not exist")
    SystemExit(1)

    def main():
        print( "This program will determine the total amount of survivors on the titanic as well as the ")
        process_file()
        outfile_name=input("Please enter the the name of the outputfile")
        outputfile=open(outfile_name,"w")
        print("The number of survivors on the titanic were ",num_of_survivors,"\nThe percentage  of survivors form class one were",survivors_1,
        "\nThe percentage  of survivors form class two were",survivors_2 ,"\nThe percentage  of survivors form class one were",survivors_3,
        "\nThe percentagesurvivors_over_50 were",survivors_over_50)


    main()