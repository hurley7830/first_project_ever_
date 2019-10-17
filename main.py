# rylie hurley
# quizzes of what I have learned in COP1500 by chapter (or activity number)
print("Hello!")
q = input("Would you like to take the COP1500 quiz?: ")
right1 = ("Correct!")
right2 =("Awesome!")
right3 = ("You got it!")
wrong1 = ("Incorrect :(")
wrong2 = ("Sorry, wrong answer.")
wrong3 = ("Nope... Try again next time!")
if q == "yes":
    chapterQuiz = input("Which chapter quiz would you like to take?: ")
#CHAPTER 1 QUIZ
    if chapterQuiz == "1" or chapterQuiz == "chapter 1":
#question one
        questionOne = input("What is the output of print(2+5) in python: ")
        if questionOne == "7":
            print(right1)
        else:
            print(wrong1)
#question two
        questionTwo = input("True or False, print(Hello my name is Pat) is a string literal: ")
        if questionTwo == "False" or questionTwo == "false":
            print(right2)
        else:
            print(wrong2)
#question three
        print("What does a comma do in a print statement? \n a.) it outputs a comma after the print statement\n b.) It prevents the print from ending with a newline, allowing you to append a new print to the end of the line\n c.) nothing")
        questionThree = input("The answer is: ")
        if questionThree == "b" or questionThree == "B":
            print(right2)
        else:
            print(wrong2)
#question four
        print("What does a '#' do when placed in front of any code? \n a.) makes the code a comment and doesn't print it \n b.) makes the code a comment and prints it \n c.) nothing")
        questionFour = input("The answer is: ")
        if questionFour == "a" or questionFour == "A":
            print(right1)
        else:
            print(wrong1)
#question five
        questionFive = input("What does the function '*' mean?: ")
        if questionFive == "multiplication" or questionFive == "Multiplication":
            print(right3)
        else:
            print(wrong3)
        print("Thanks for taking my quiz! Good Bye.")
#CHAPTER 2 QUIZ
    elif chapterQuiz == "2" or chapterQuiz == "chapter 2":
#question one
        ch2_questionOne = input("Is costoffirstitem a GOOD variable name?: ")
        if ch2_questionOne == "no":
            print(right2)
        else:
            print(wrong1)
#question two
        ch2_questionTwo = input("Is '1st_name' a valid variable name?: ")
        if ch2_questionTwo == "yes":
            print(right3)
        else:
            print(wrong2)
#question three
        ch2_questionThree = input("State the output for this line of code: \n print('your name is' + 'Pat.') \nThe output is: ")
        if ch2_questionThree == "your name isPat.":
            print(right1)
        else:
          print(wrong3)
        print("Thanks for taking my quiz! Good Bye.")
#CHAPTER 3 QUIZ
    elif chapterQuiz == "3" or chapterQuiz == "chapter 3":
#question one
        ch3_questionOne = input("State the arithmetic operation each symbol represents.\n*\n**\n/\n//\n%\nUse a comma to seperate your answers: ")
        if ch3_questionOne == "multiplication, exponent, division, quotient, modulus" or ch3_questionOne == "Multiplication, Exponent, Division, Quotient, Modulus" or ch3_questionOne == "Multiplication,Exponent,Division,Quotient,Modulus" or ch3_questionOne == "multiplication,exponent,division,quotient,modulus":
            print(right3)
        else:
            print(wrong1)
#question two
        ch3_questionTwo = input("What is the one word that defines the '=' symbol in a line of code: ")
        if ch3_questionTwo == "assignment" or ch3_questionTwo == "Assignment":
            print(right2)
        else:
            print(wrong2)
#question three
        ch3_questionThree = input("Evaluate the following line of code.\nage = 15\nprint('your age is', age)\nWhat does the assignment statement 'age = 15' do?\na.) nothing\nb.) assigns the variable age to 15\nc.) assigns 15 to the variable age\nYour answer is: ")
        if ch3_questionThree == "C" or ch3_questionThree == "c":
            print(right3)
        else:
            print(wrong1)
#question four
        ch3_questionFour = input("What does it mean when the '+' sign is put in between two strings?\na.) it outputs the sum the number of letters up in the strings\nb.) it's invalid\nc.) it concatenates the two strings stored in the variables into one string.\nYour answer is: ")
        if ch3_questionFour == "c" or ch3_questionFour == "C":
            print(right2)
        else:
            print(wrong3)
        print("Thanks for taking my quiz! Good Bye.")
#CHAPTER 4 QUIZ
    elif chapterQuiz == "4" or chapterQuiz == "chapter 4":
        print("Enter and Execute the following code\n\nnumLaptops = 7\nlaptopCost = 599.50\nprice = numLaptops * laptopCost\nprint('Total cost of Laptops: ', price)")
        ch4_questionOne = input("\nIf the last line of code was replaced with the following\n  print('Total cost of laptops:',format(price,'.2f'))\nWhat would the output be?: ")
        if ch4_questionOne == "Total cost of Laptops:  4196.50":
            print(right3)
        else:
            print(wrong1)
        ch4_questionTwo = input("How would you add a dollar sign to the number that was output previously?\na.) you cant\nb.) add it IN the string literal in the fourth line\nc.) add it after the string literal in teh fourth line, before price\n Your Answer: ")
        if ch4_questionTwo == "b" or ch4_questionTwo == "B":
            print(right1)
        else:
            print(wrong2)
        ch4_questionThree = input("What will be the output if you change .2 with .4 in the last line of code?:")
        if ch4_questionThree == "Total cost of Laptops:  4196.5000":
            print(right2)
        else:
            print(wrong2)
        ch4_questionFour = input("Computers perform four main operations on data, what are they? Seperate your answers with commas: ")
        if ch4_questionFour == "input, output, process, store" or ch4_questionFour == "Input, Ouput, Process, Store":
            print(right1)
        else:
            print(wrong3)
        print("Thanks for taking my quiz! Good Bye.")
#CHAPTER 5 QUIZ
    elif chapterQuiz == "5" or chapterQuiz == "chapter 5":
#question one
        ch5_questionOne = input("What operators are used to compare the relationship between two operands?: ")
        if ch5_questionOne == "conditional operators" or ch5_questionOne == "Conditional Operators" or ch5_questionOne == "conditional" or ch5_questionOne =="Conditional":
            print(right1)
        else:
            print(wrong1)
#question two
        ch5_questionTwo = input("Expressions whose result can only be true or false are known as _____________:")
        if ch5_questionTwo == "Boolean Expressions" or ch5_questionTwo == "boolean expressions" or ch5_questionTwo == "boolean" or ch5_questionTwo == "Boolean":
            print(right2)
        else:
            print(wrong2)
#question three
        ch5_questionThree = input("Assume:   word1 = 'hello' and word2 = 'good-bye'\nWhat is the result of the following expression?\nword1 < word2\nYour answer: ")
        if ch5_questionThree == "false" or ch5_questionThree == "False":
            print(right2)
        else:
            print(wrong1)
#question four
        ch5_questionFour = input("How do the conditional operators work when the operands are strings?\na.) it won't work because the operands need to be integers\nb.)they evaluate the first values inside the strings\nYour answer: ")
        if ch5_questionFour == "b" or ch5_questionFour == "B":
            print(right1)
        else:
            print(wrong3)
        print("Thanks for taking my quiz! Good Bye.")
#CHAPTER 6 QUIZ
    elif chapterQuiz == "6" or chapterQuiz == "chapter 6":
#question one
        ch6_questionOne = input("What is the output of the program listed below?\n\ngrade = 95\nif grade >= 94:\nprint('Excellent!')\n\nYour answer: ")
        if ch6_questionOne == "Excellent!":
            print(right3)
        else:
            print(wrong1)
#question two
        ch6_questionTwo = input("In the first question, what would happen if 95 was changed to 90?: ")
        if ch6_questionTwo == "Nothing" or ch6_questionTwo == "nothing":
            print(right2)
        else:
            print(wrong3)
#question three
        ch6_questionThree = input("What function is used to return a floating point number from a number or a string?: ")
        if ch6_questionThree == "Float" or ch6_questionThree == "float":
            print(right3)
        else:
            print(wrong2)
#question four
        ch6_questionFour = input("What function allows multiple substitutions and value formatting and lets us concatenate elements within a string through positional formatting?: ")
        if ch6_questionFour == "format" or ch6_questionFour == "Format":
            print(right1)
        else:
            print(wrong3)
        print("Thanks for taking my quiz! Good Bye.")
#CHAPTER 7 QUIZ
    elif chapterQuiz == "7" or chapterQuiz == "chapter 7":
#question one
        ch7_questionOne = input("What is a Python keyword that represents else if and allows you to test for one of several options?: ")
        if ch7_questionOne == "elif":
            print(right2)
        else:
            print(wrong1)
#question two
        ch7_questionTwo = input("True or False? As soon as an elif statement is tested as true, the rest of the elif statements are ignored.: ")
        if ch7_questionTwo == "True" or ch7_questionTwo == "true":
            print(right2)
        else:
            print(wrong2)
#question three
        ch7_questionThree = input("How many elif statements can there be with in an if statement?\na.) 10\nb.) 1\nc.) infinite\nd.) 0\nYour answer: ")
        if ch7_questionThree == "c" or ch7_questionThree == "C":
            print(right3)
        else:
            print(wrong3)
#question four
        ch7_questionFour = input("Does it matter where an elif is placed within an if statement?\na.) No, they are all evaluated so they can be placed anywhere.\nb.) Yes, the first true elif statement is outputted and the rest are ignored.\nYour answer: ")
        if ch7_questionFour == "b" or ch7_questionFour == "B":
            print(right2)
        else:
            print(wrong1)
        print("Thanks for taking my quiz! Good Bye.")
#CHAPTER 8 QUIZ
    elif chapterQuiz == "8" or chapterQuiz == "chapter 8":
#question one
        ch8_questionOne = input("How does the Python interpreter know what lines of code belong to the loop body?\na.) anything after the loop is considered in the loop body\nb.) nothing\nc.) indentation\n Your answer: ")
        if ch8_questionOne == "c" or ch8_questionOne == "C":
            print(right3)
        else:
            print(wrong2)
#question two
        ch8_questionTwo = input("State the output of the code below.\nnumber = 1\nwhile number <= 10:\n   if number % 2 == 0:\n      print(number, end = ' ')\nnumber = number + 1\n\n Your Answer:")
        if ch8_questionTwo == "2 4 6 8 10":
            print(right1)
        else:
            print(wrong2)
#question 3
        ch8_questionThree = input("What structure is where you know the number of times it will execute is known as a count-controlled loop: ")
        if ch8_questionThree == "looping structure" or ch8_questionThree == "Looping Structure":
            print(right3)
        else:
            print(wrong1)
#question 4
        ch8_questionFour = input("____________  _______ provide a concise way of creating assignment statements when the variable on the left-hand side of the assignment statement is also on the right-hand side.\nThe addition short-cut operator (+=) is usually used for incrementing a variable.: ")
        if ch8_questionFour == "Short-cut Operators" or ch8_questionFour == "short-cut operators":
            print(right2)
        else:
            print(wrong3)
        print("Thanks for taking my quiz! Good Bye.")
#CHAPTER 9 QUIZ
    elif chapterQuiz == "9" or chapterQuiz == "chapter 9":
#question one
        ch9_questionOne = input("What is a python function that is used to define a series of numbers and can be used\nin a FOR loop to determine the number of times the loop is executed.: ")
        if ch9_questionOne == "range" or ch9_questionOne == "Range":
            print(right1)
        else:
            print(wrong2)
#question two
        ch9_questionTwo = input("What function converts what is in parentheses ( ) to a String, if it is not a string already?: ")
        if ch9_questionTwo == "str()":
            print(right1)
        else:
            print(wrong2)
#question three
        ch9_questionThree = input("What is a variable that stores the sum of a group of values?: ")
        if ch9_questionThree == "accumulator" or ch9_questionThree == "Accumulator":
            print(right3)
        else:
            print(wrong1)
#question four
        ch9_questionFour = input("What loop can you include a list of values in place of the range() function?: ")
        if ch9_questionFour == "FOR" or ch9_questionFour == "for" or ch9_questionFour == "FOR loop" or ch9_questionFour == "for loop":
            print(right2)
        else:
            print(wrong3)
        print("Thanks for taking my quiz! Good Bye.")
#CHAPTER 10 QUIZ
    elif chapterQuiz == "10" or chapterQuiz == "chapter 10":
#question one
        ch10_questionOne = input("A loop within another loop is known as...: ")
        if ch10_questionOne == "nest loop" or ch10_questionOne == "nest":
            print(right3)
        else:
            print(wrong3)
#question 2-4
        print("name = input('What is your name: ')\nfor x in range(5):\n   for x in range(3):\n      print(name + ' ', end = ' '\n   print()")
        ch10_questionTwo = input("How many FOR loops are in this code?: ")
        if ch10_questionTwo == "2":
            print(right2)
        else:
            print(wrong1)
        ch10_questionThree = input("Is one loop completely executed before the next loop begins?: ")
        if ch10_questionThree == "yes" or ch10_questionThree == "Yes":
            print(right1)
        else:
            print(wrong2)
        ch10_questionFour = input("print(name + ' ', end = ' ')\nHow many times is the following line of code executed in the program?: ")
        if ch10_questionFour == "5":
            print(right2)
        else:
            print(wrong3)
        print("Thanks for taking my quiz! Good Bye.")
else:
    print("Thanks for trying my quiz!")



