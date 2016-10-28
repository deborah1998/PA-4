# CS201 PROGRAMMING ASSIGNMENT #4  
60  POINTS   (10pts design, 50pts final)  
DESIGN DUE: 11/02/16  
FINAL DUE: 11/09/16  

## PROBLEM 
Create a program that will analyze data on the passenger of the Titanic. 

## PURPOSE OF THE ASSIGNMENT
The purpose of this assignment is to give you practice with

1. reading from a file
2. processing Strings
3. function design and implementation
4. error checking

## REQUIREMENTS ANALYSIS
The first stage in your programming assignment is the requirements analysis stage.  You need to make sure you understand the below requirements for what your program needs to do. You have access to a file containing information on most of the Titanic passengers, and your job is to make the data in that file accessible to the user of your program.  There is some disagreement on the exact number of passengers on board during the disaster, but this file is close to being comprehensive. One “official” count is 1316 passengers.

The input data was taken from http://biostat.mc.vanderbilt.edu/twiki/bin/view/Main/DataSets but has been altered so that each of the 11 data values (fields) for each passenger is separated from the next by a vertical slash “|” (the character below the backspace key on most keyboards).  The altered file you have been provided is called 'titanic.txt', but you should ask the user for the name of the file to use as input. Your program should work for any file of the following format.  Each passenger's line holds 7 pieces of data.  The data conforms to the following ordering: 

Each line contains: Class | Survived | Name |  Sex | Age | Embark | Dest  
* Class is either 1 or 2 or 3  
* Survived is either 1 or 0  (1 means survived and 0 means died)  
* Name is a string  
* Age is a real number  (babies have ages < 1; unavailable ages are shown as 0)  
* Sex is either “female” or “male”  
* Embark is either ‘C’ or ‘S’ or ’Q’  (for Cherbourg, Southampton, or Queenstown)  
* Dest is a string but is not uniform in format. Unavailable data is shown as XXX.  

Your program should determine the following for the user:

1. The total number of people to survive
2. The percentage of each class who survived in the format "XX.X%" (e.g. 6.9%, 76.4%) 
3. Save to a file (named by user) the names of everyone who survived and their destination, one name with their destination per line
4. One other question of your choosing, although it MUST use at least one piece of data from a line that is not used in the 3 required questions OR do something very interesting with Name or Destination (there are so many questions you can ask about this data! Asking the right questions is part of data science. Pick what you'd like to answer that isn't essentially identical to one of the 3 required questions).

## DESIGN
The second stage is to design your solution based on the requirements:

1. Determine what you want your 4th question to be and list that at the top of designInitial.txt as "My question: ". Write in a similar format to the question above (so, as a question, not as how you will solve it).
2. Determine the tasks being accomplished in your program. Although generally every task is a function, for our first file processing program you'll need to put all file processing in the same function. In a few weeks we'll learn how to store file data to process later. There are other tasks, however, that SHOULD be their own functions.
3. Write an algorithm for each function. This algorithm includes parameters, calculations, and returned values. This algorithm should include your personally designed question.
4. Double check that you included all of the requirements, and appropriate error checking.

*NOTE:* There are no aspects of this design/code that you can google how to solve. The only appropriate googling will be if you want to understand more about the Titanic or its passengers.

**DESIGN SUBMISSION: 11/02/16**
Submit to GitHub: the description of your self-designed question and your algorithm for your program in designInitial.txt. The general format for your algorithm should match the format of PA3, and recent labs.

***Remember to double check on github.com that your files pushed. If they didn’t, you need to push them. I can only see what is on github.com, not what is only on your computer.


## PROGRAMMING REQUIREMENTS
After your design is complete and correct, it’s time to start programming and then testing:

* Fix design issues: If there were issues with your design, either not meeting requirements or in the format, fix that before you start writing your code.
* Implementation: Write your program following the requirements and based on your design.
  * Follow good usability/HCI principles in your input and output (make it clear the type of input you are asking for)
  * Follow good use of functions
  * Remember to define functions before they are used (so if function A calls function B, you need to define function B first in your program)
  * Remember to state the purpose of the program
  * Follow iterative development to make your life easier. Implement ONE question, and get that working. Then worry about adding in the next question. New questions shouldn't stop old questions from working, but should only add on to it.
* Testing: Make sure it works correctly; give it sample input, and check that the output is correct.
  * Create a test file that contains at most 10-15 lines from the original file, or make up your own data in the same format. Name it testinput.txt. Create a set of test cases based on this test file (1 case per question). If you have a representative set of 10 lines (i.e. survivors, non-survivors, people of each sex, class, and embark point), then if it works on this file then it *probably* works on the real file. This is a standard way to test file code, because it makes it easier to figure out the right answer.
  * Test your program using the test cases. Also test all error checking. Make sure it seems to work with the full file as well.

## ASSIGNMENT REMINDERS
Follow the programming assignment requirements document for comments, formatting, etc. You may not use lists even if you have learned them in a prior course, only because it significantly changes the algorithmic thinking on this problem and it's good to be able to think through it this way too (we'll get there soon, I promise).

Recall that you may not do someone else’s work, or have someone else do your work. Sharing of solutions is an honor code violation. This includes someone who is not in the class, including a tutor, writing any or all of your algorithm or code or dictating to you how to do it. As everyone in the class is solving the same problem, no code may change hands. See the syllabus for details or ask the professor if you are unsure.

## EXTRA CREDIT 
Create a particularly interesting/difficult question for your 4th question. You may ask if your planned question will qualify you for extra credit at any point, including during the design stage. The more impressive, the more extra credit (up to 2 points). *Describe in extracredit.txt why you think your question deserves extra credit (keep it brief).*

## REFLECTION
Write a short reflection about the programming assignment in reflection.txt: what did you learn, what would you do differently next time, what was difficult, what do you like/dislike about working with files?  This should be no more than a page.

## FINAL SUBMISSION   
* To GitHub:
  * Your .py file
  * A brief description of why you deserve extra credit in extracredit.txt if applicable
  * Your reflection of the programming assignment (reflection.txt)
  * Your final algorithm, including the changes you made based on the design feedback (designFinal.txt)
  * Your testing input file of 10-15 lines (testinput.txt)
  * Your test cases (testcases.txt)
* Hardcopy in class:
  * A printout of your .py file

***Remember to double check on github.com that your files pushed. If they didn’t, you need to push them. I can only see what is on github.com, not what is only on your computer.


