# rylie hurley
# quizzes of what I have learned in COP1500 by chapter (activity number)
def intro(fname):
    print("Hello, " + fname)
intro(input("Please enter your first name: "))
q = input("Would you like to take the COP1500 quiz?: ")
if q == "yes":
    chapterQuiz = input("Which chapter quiz would you like to take?: ")
# CHAPTER 1 QUIZ
    if chapterQuiz == "1" or chapterQuiz == "chapter 1":
        def chapterOne():
            questionOne = input("What is the output of print(2+5) in python: ")
            questionTwo = input("True or False, print(Hello my name is Pat) is a string literal: ")
            print(
                "What does a comma do in a print statement? \n a.) it outputs a comma after the print statement\n b.) It prevents the print from ending with a newline, allowing you to append a new print to the end of the line\n c.) nothing")
            questionThree = input("The answer is: ")
            print(
                "What does a '#' do when placed in front of any code? \n a.) makes the code a comment and doesn't print it \n b.) makes the code a comment and prints it \n c.) nothing")
            questionFour = input("The answer is: ")
            questionFive = input("What does the function '*' mean?: ")
            score = 0
            if questionOne == "7":
                score = score + 1
            else:
                score = score
            if questionTwo == "False" or questionTwo == "false":
                score = score + 1
            else:
                score = score
            if questionThree == "b" or questionThree == "B":
                score = score + 1
            else:
                score = score
            if questionFour == "a" or questionFour == "A":
                score = score + 1
            else:
                score = score
            if questionFive == "multiplication" or questionFive == "Multiplication":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/5!')
            print("Thanks for taking my quiz! Good Bye.")


        chapterOne()
#CHAPTER 2 QUIZ
    elif chapterQuiz == "2" or chapterQuiz == "chapter 2":
        def chapterTwo():
            questionOne = input("Is costoffirstitem a GOOD variable name?: ")
            questionTwo = input("Is '1st_name' a valid variable name?: ")
            questionThree = input(
                "State the output for this line of code: \n print('your name is' + 'Pat.') \nThe output is: ")
            score = 0
            if questionOne == "no":
                score = score + 1
            else:
                score = score
            if questionTwo == "yes":
                score = score + 1
            else:
                score = score
            if questionThree == "your name isPat.":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/3!')
            print("Thanks for taking my quiz! Good Bye.")


        chapterTwo()
#CHAPTER 3 QUIZ
    elif chapterQuiz == "3" or chapterQuiz == "chapter 3":
        def chapterThree():
            questionOne = input(
                "State the arithmetic operation each symbol represents.\n*\n**\n/\n//\n%\nUse a comma to seperate your answers: ")
            questionTwo = input("What is the one word that defines the '=' symbol in a line of code: ")
            questionThree = input(
                "Evaluate the following line of code.\nage = 15\nprint('your age is', age)\nWhat does the assignment statement 'age = 15' do?\na.) nothing\nb.) assigns the variable age to 15\nc.) assigns 15 to the variable age\nYour answer is: ")
            questionFour = input(
                "What does it mean when the '+' sign is put in between two strings?\na.) it outputs the sum the number of letters up in the strings\nb.) it's invalid\nc.) it concatenates the two strings stored in the variables into one string.\nYour answer is: ")
            score = 0
            if questionOne == "multiplication, exponent, division, quotient, modulus" or questionOne == "Multiplication, Exponent, Division, Quotient, Modulus" or questionOne == "Multiplication,Exponent,Division,Quotient,Modulus" or questionOne == "multiplication,exponent,division,quotient,modulus":
                score = score + 1
            else:
                score = score
            if questionTwo == "assignment" or questionTwo == "Assignment":
                score = score + 1
            else:
                score = score
            if questionThree == "C" or questionThree == "c":
                score = score + 1
            else:
                score = score
            if questionFour == "c" or questionFour == "C":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/4!')
            print("Thanks for taking my quiz! Good Bye.")


        chapterThree()
#CHAPTER 4 QUIZ
    elif chapterQuiz == "4" or chapterQuiz == "chapter 4":
        def chapterFour():
            print(
                "Enter and Execute the following code\n\nnumLaptops = 7\nlaptopCost = 599.50\nprice = numLaptops * laptopCost\nprint('Total cost of Laptops: ', price)")
            questionOne = input(
                "\nIf the last line of code was replaced with the following\n  print('Total cost of laptops:',format(price,'.2f'))\nWhat would the output be?: ")
            questionTwo = input(
                "How would you add a dollar sign to the number that was output previously?\na.) you cant\nb.) add it IN the string literal in the fourth line\nc.) add it after the string literal in teh fourth line, before price\n Your Answer: ")
            questionThree = input("What will be the output if you change .2 with .4 in the last line of code?:")
            questionFour = input(
                "Computers perform four main operations on data, what are they? Seperate your answers with commas: ")
            score = 0
            if questionOne == "Total cost of Laptops:  4196.50":
                score = score + 1
            else:
                score = score
            if questionTwo == "b" or questionTwo == "B":
                score = score + 1
            else:
                score = score
            if questionThree == "Total cost of Laptops:  4196.5000":
                score = score + 1
            else:
                score = score
            if questionFour == "input, output, process, store" or questionFour == "Input, Ouput, Process, Store":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/4!')
            print("Thanks for taking my quiz! Good Bye.")


        chapterFour()
#CHAPTER 5 QUIZ
    elif chapterQuiz == "5" or chapterQuiz == "chapter 5":
        def chapterFive():
            questionOne = input("What operators are used to compare the relationship between two operands?: ")
            questionTwo = input("Expressions whose result can only be true or false are known as _____________:")
            questionThree = input(
                "Assume:   word1 = 'hello' and word2 = 'good-bye'\nWhat is the result of the following expression?\nword1 < word2\nYour answer: ")
            questionFour = input(
                "How do the conditional operators work when the operands are strings?\na.) it won't work because the operands need to be integers\nb.)they evaluate the first values inside the strings\nYour answer: ")
            score = 0
            if questionOne == "conditional operators":
                score = score + 1
            else:
                score = score
            if questionTwo == "boolean expressions" or questionTwo == "Boolean Expressions":
                score = score + 1
            else:
                score = score
            if questionThree == "false" or questionThree == "False":
                score = score + 1
            else:
                score = score
            if questionFour == "b" or questionFour == "B":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/4!')
            print("Thanks for taking my quiz! Good Bye.")


        chapterFive()
#CHAPTER 6 QUIZ
    elif chapterQuiz == "6" or chapterQuiz == "chapter 6":
        def chapterSix():
            questionOne = input(
                "What is the output of the program listed below?\n\ngrade = 95\nif grade >= 94:\nprint('Excellent!')\n\nYour answer: ")
            questionTwo = input("In the first question, what would happen if 95 was changed to 90?: ")
            questionThree = input(
                "What function is used to return a floating point number from a number or a string?: ")
            questionFour = input(
                "What function allows multiple substitutions and value formatting and lets us concatenate elements within a string through positional formatting?: ")
            score = 0
            if questionOne == "Excellent!":
                score = score + 1
            else:
                score = score
            if questionTwo == "nothing" or questionTwo == "Nothing":
                score = score + 1
            else:
                score = score
            if questionThree == "float" or questionThree == "Float":
                score = score + 1
            else:
                score = score
            if questionFour == "format" or questionFour == "Format":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/4!')
            print("Thanks for taking my quiz! Good Bye.")


        chapterSix()
#CHAPTER 7 QUIZ
    elif chapterQuiz == "7" or chapterQuiz == "chapter 7":
        def chapterSeven():
            questionOne = input(
                "What is a Python keyword that represents else if and allows you to test for one of several options?: ")
            questionTwo = input(
                "True or False? As soon as an elif statement is tested as true, the rest of the elif statements are ignored.: ")
            questionThree = input(
                "How many elif statements can there be with in an if statement?\na.) 10\nb.) 1\nc.) infinite\nd.) 0\nYour answer: ")
            questionFour = input(
                "Does it matter where an elif is placed within an if statement?\na.) No, they are all evaluated so they can be placed anywhere.\nb.) Yes, the first true elif statement is outputted and the rest are ignored.\nYour answer: ")
            score = 0
            if questionOne == "elif":
                score = score + 1
            else:
                score = score
            if questionTwo == "true" or questionTwo == "True":
                score = score + 1
            else:
                score = score
            if questionThree == "c" or questionThree == "C":
                score = score + 1
            else:
                score = score
            if questionFour == "b" or questionFour == "B":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/4!')
            print("Thanks for taking my quiz! Good Bye.")


        chapterSeven()
#CHAPTER 8 QUIZ
    elif chapterQuiz == "8" or chapterQuiz == "chapter 8":
        def chapterEight():
            questionOne = input(
                "How does the Python interpreter know what lines of code belong to the loop body?\na.) anything after the loop is considered in the loop body\nb.) nothing\nc.) indentation\n Your answer: ")
            questionTwo = input(
                "State the output of the code below.\nnumber = 1\nwhile number <= 10:\n   if number % 2 == 0:\n      print(number, end = ' ')\nnumber = number + 1\n\n Your Answer:")
            questionThree = input(
                "What structure is where you know the number of times it will execute is known as a count-controlled loop: ")
            questionFour = input(
                "____________  _______ provide a concise way of creating assignment statements when the variable on the left-hand side of the assignment statement is also on the right-hand side.\nThe addition short-cut operator (+=) is usually used for incrementing a variable.: ")
            score = 0
            if questionOne == "c" or questionOne == "C":
                score = score + 1
            else:
                score = score
            if questionTwo == "2 4 6 8 10":
                score = score + 1
            else:
                score = score
            if questionThree == "looping structure" or questionThree == "Looping Structure":
                score = score + 1
            else:
                score = score
            if questionFour == "short-cut operators" or questionFour == "Short-Cut Operators":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/4!')
            print("Thanks for taking my quiz! Good Bye.")


        chapterEight()
#CHAPTER 9 QUIZ
    elif chapterQuiz == "9" or chapterQuiz == "chapter 9":
        def chapterNine():
            questionOne = input(
                "What is a python function that is used to define a series of numbers and can be used\nin a FOR loop to determine the number of times the loop is executed.: ")
            questionTwo = input(
                "What function converts what is in parentheses ( ) to a String, if it is not a string already?: ")
            questionThree = input("What is a variable that stores the sum of a group of values?: ")
            questionFour = input("What loop can you include a list of values in place of the range() function?: ")
            score = 0
            if questionOne == "range" or questionOne == "Range":
                score = score + 1
            else:
                score = score
            if questionTwo == "str()":
                score = score + 1
            else:
                score = score
            if questionThree == "accumulator" or questionThree == "Accumulator":
                score = score + 1
            else:
                score = score
            if questionFour == "for" or questionFour == "FOR" or questionFour == "for loop" or questionFour == "FOR loop":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/4!')
            print("Thanks for taking my quiz! Good Bye.")


        chapterNine()
#CHAPTER 10 QUIZ
    elif chapterQuiz == "10" or chapterQuiz == "chapter 10":
        def chapterTen():
            questionOne = input("A loop within another loop is known as...: ")
            print(
                "Use the following informtion to answer questions 2-4\nname = input('What is your name: ')\nfor x in range(5):\n   for x in range(3):\n      print(name + ' ', end = ' '\n   print()")
            questionTwo = input("How many FOR loops are in this code?: ")
            questionThree = input("Is one loop completely executed before the next loop begins?: ")
            questionFour = input(
                "print(name + ' ', end = ' ')\nHow many times is the following line of code executed in the program?: ")
            score = 0
            if questionOne == "nest loop" or questionOne == "nest":
                score = score + 1
            else:
                score = score
            if questionTwo == "2":
                score = score + 1
            else:
                score = score
            if questionThree == "yes" or questionThree == "Yes":
                score = score + 1
            else:
                score = score
            if questionFour == "5":
                score = score + 1
            else:
                score = score
            print('Your score is: ', score, '/4!')
            print("Thanks for taking my quiz! Good Bye.")


        chapterTen()

else:
    print("Thanks for trying my quiz!")



