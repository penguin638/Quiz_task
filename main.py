def startscreen():
   print("Welcome to this game!")
   print("Please chose which game you want to play:")
   print("Quiz")
   print("Guess the number")

   choose = input()
   if choose == ("Quiz"):
        quiz_screen()
   elif choose == ("Guess the number"):
        number_guess_start()
   elif choose
            
   else:
        print("Please copy exactly what the options are.")
        startscreen()    

 # My codespace timed out or deleted or somthing, so i had to redo it. as it was going to take me ages, i used the basis of my quiz (though i expanded it a lot)to get it done sooner.


def quiz_screen():
    print("Welcome to this quiz!")
    print("Please chose which quiz you wish to play:")
    print("US Presidents")
    print("Shakespeare")
    print("Countries")
    with open("quizscore.txt","w") as file:
      pass

    choice = input()
    if choice == ("US Presidents"):
        president_quiz()
    elif choice == ("Shakespeare"):
        shakespeare_quiz()
    elif choice == ("Countries"):
        countries_quiz()
    else:
        print("Please copy exactly what the quiz options are.")
        quiz_screen()

def president_quiz():
    print("Welcome to the Presdient quiz!")
    print("You will be asked questions on the Presidents of the United States")
    print("Type 'score' if you wish to see your score")
    print("Type 'exit' if you wish to exit the quiz")
    print("Make sure you capatilise your answers")
    print("And put at least the first and sirnames")
    print("Good luck!")
    p_quiz()


def p_quiz(): 
 
    incorrect = 0

    print("Do you wish to exit or see your score? (if you dont type anything else)")
    exore = input()
    if exore == ("exit"):
      startscreen()
    elif exore == ("score"):
      with open("quizscore.txt","r") as fp:
         lines = len(fp.readlines())
         print("Score:", lines)
    else:
      print("OK!") 
   
    with open("president.txt","w") as file:
       file.write("Who was the first President?\n")
       file.write("Who was the 40th President of the United States?\n")
       file.write("Who was the shortest serving Presidet?\n")
       file.write("Who was the longest serving President?\n")
       file.write("Who came after Calvin Coolidge?\n")
 
    import random
 
    with open("president.txt","r") as file:
       questions = file.readlines()
 
    random_line_number = random.randint(0, len(questions) - 1)
    random_question = questions[random_line_number].strip()
    print(f"Question: {random_question}")
 
    answer = input("Your answer: ")
 
 
 
    with open("presanswers.txt","w") as file:
         file.write("George Washington\n")
         file.write("Ronald Reagan\n")
         file.write("William Henry Harrison\n")
         file.write("Franklin D Roosevelt\n")
         file.write("Franklin Roosevelt\n")
         file.write("FDR\n")
         file.write("Franklin Delano Roosevelt\n")
         file.write("William Harrison\n")
         file.write("William H Harrison\n")
         file.write("William H. Harrison\n")
         file.write("Franklin D. Roosevelt\n")
         file.write("Herbert Hoover\n")
 
    with open("presanswers.txt","r") as file:
      for line in file:
        if answer in line:
           incorrect += 1  
           if incorrect == 1:
            print("That's correct")
            with open("quizscore.txt","w") as file:
               file.write("1\n") 
      
           
    if incorrect == 0:
         print("Sorry, that's not correct")
 
    incorrect = 0  
    p_quiz()
 


def shakespeare_quiz():
    print("Welcome to the Shakespeare quiz!")
    print("You will be asked questions on Shakespeare and his plays")
    print("Type 'score' if you wish to see your score")
    print("Type 'exit' if you wish to exit the quiz")
    print("Make sure you capatilise your answers")
    print("Good luck!")
    s_quiz()

def s_quiz():
    incorrect = 0

    print("Do you wish to exit or see your score? (if you dont type anything else)")
    exore = input()
    if exore == ("exit"):
      startscreen()
    elif exore == ("score"):
      with open("quizscore.txt","r") as fp:
         lines = len(fp.readlines())
         print("Score:", lines)
    else:
      print("OK!") 

    with open("shakespeare.txt","w") as file:
       file.write("Did Romeo or Juliet die first?\n")
       file.write("What was Othello's wife called?\n")
       file.write("What was Shakespeare's first name?\n")
       file.write("What was Shakespeare's longest play?\n")
       file.write("What was the youngest sister in King Lear called?\n")
       file.write("What is the name of Helena's lover in All's Well That Ends Well?\n")
       file.write("Finish the Macbeth line: What you ...? He stabs him.\n")
       file.write("Where was Shakespeare born?\n")
 
    import random
 
    with open("shakespeare.txt","r") as file:
       questions = file.readlines()
 
    random_line_number = random.randint(0, len(questions) - 1)
    random_question = questions[random_line_number].strip()
    print(f"Question: {random_question}")
 
    answer = input("Your answer: ")
 
 
 
    with open("shakanswers.txt","w") as file:
         file.write("Romeo\n")
         file.write("Desdemona\n")
         file.write("William\n")
         file.write("Hamlet\n")
         file.write("Cordelia\n")
         file.write("Betram\n")
         file.write("egg\n")
         file.write("Egg\n")
         file.write("Stratford upon avon\n")
         file.write("Stratford Upon Avon\n")
         file.write("Stratford upon Avon\n")
 
 
    with open("shakanswers.txt","r") as file:
      for line in file:
        if answer in line:
           incorrect += 1  
           if incorrect == 1:
            print("That's correct")
            with open("quizscore.txt","a") as file:
               file.write("1\n") 
       
           
    if incorrect == 0:
         print("Sorry, that's not correct")
 
    incorrect = 0  
    s_quiz()




def countries_quiz():
    print("Welcome to the Countries quiz!")
    print("You will be asked questions on the countries of the world")
    print("Type 'score' if you wish to see your score")
    print("Type 'exit' if you wish to exit the quiz")
    print("Make sure you capatilise your answers")
    print("Good luck!")
    c_quiz()
    

def c_quiz():    

    incorrect = 0

    print("Do you wish to exit or see your score? (if you dont type anything else)")
    exore = input()
    if exore == ("exit"):
      startscreen()
    elif exore == ("score"):
      with open("quizscore.txt","r") as fp:
         lines = len(fp.readlines())
         print("Score:", lines)
    else:
      print("OK!")    

 
    with open("countries.txt","w") as file:
       file.write("What is the most populated country?\n")
       file.write("What is the capital of Scotland?\n")
       file.write("What is the biggest coutry (landmass)?\n")
       file.write("What is the capital of Egypt?\n")
       file.write("In what continent is Canada?\n")
       file.write("What is the top stripe in the Dutch flag?\n")
 
    import random
 
    with open("countries.txt","r") as file:
       questions = file.readlines()
 
    random_line_number = random.randint(0, len(questions) - 1)
    random_question = questions[random_line_number].strip()
    print(f"Question: {random_question}")
 
    answer = input("Your answer: ")


    with open("countanswers.txt","a") as file:
         file.write("India\n")
         file.write("Edinburgh\n")
         file.write("Russia\n")
         file.write("Cairo\n")
         file.write("North America\n")
         file.write("Blue\n")
         file.write("blue\n")
 

    with open("countanswers.txt","r") as file:
      for line in file:
        if answer in line:
           incorrect += 1  
           if incorrect == 1:
            print("That's correct")
           with open("quizscore.txt","a") as file:
               file.write("1\n") 
      
      
      
    if incorrect == 0:
      print("Sorry, that's not correct")
      

 
    incorrect = 0  
    c_quiz()



def number_guess_start():
   print("Welcome to guess the number!")
   print("Please chose your level of difficulty:")
   print("easy")
   print("medium")
   print("hard")
   print("or 'go back'")

   guessdifficulty = input()
   if guessdifficulty == ("easy"):
    easy()
   elif guessdifficulty == ("medium"):
    medium()
   elif guessdifficulty == ("hard"):
    hard()
   elif guessdifficulty == ("go back"):
    startscreen()
   else:
    print("Please exactly copy the options") 
    number_guess_start()
   
def easy():
  print("Welcome to the easy version of this game!")
  print("You must enter a number from 1-10")
  print("The game will also have chosen a random number")
  print("You get 5 attempts")
  print("See how many tries it takes for you to guess the same number!")

  import random

  lower = 1
  upper = 10
 
  attempts = 0


  secret_number = random.randint(lower, upper)



  while True:
        try:
            guess = int(input(f"Please choose a number between {lower} and {upper}: "))
            
            if guess == secret_number:
              attempts += 1
              print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
              number_guess_start()
            elif guess < secret_number:
              print("Too low")
              attempts += 1
              if attempts >= 5:
                print(f"Sorry, you ran out of attempts! The secret number is {secret_number}.")

            elif guess > secret_number:
              print("Too high")
              attempts += 1
              if attempts >= 5:
                print(f"Sorry, you ran out of attempts! The secret number is {secret_number}.")
            else:
                print("Please put in a number between 1 and 10")
        except ValueError:
            print("Please put in a number between 1 and 10")


def medium():
  print("Welcome to the medium version of this game!")
  print("You must enter a number from 1-30")
  print("The game will also have chosen a random number")
  print("You get 10 attempts")
  print("See how many tries it takes for you to guess the same number!")

  import random

  lower = 1
  upper = 30

  attempts = 0


  secret_number = random.randint(lower, upper)



  while True:
        try:
            guess = int(input(f"Please choose a number between {lower} and {upper}: "))
            
            if guess == secret_number:
              attempts += 1
              print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
              number_guess_start()
            elif guess < secret_number:
              print("Too low")
              attempts += 1
              if attempts >= 10:
                print(f"Sorry, you ran out of attempts! The secret number is {secret_number}.")

            elif guess > secret_number:
              print("Too high")
              attempts += 1
              if attempts >= 10:
                print(f"Sorry, you ran out of attempts! The secret number is {secret_number}.")
            else:
                print("Please put in a number between 1 and 30")
        except ValueError:
            print("Please put in a number between 1 and 30")

def hard():
  print("Welcome to the hard version of this game!")
  print("You must enter a number from 1-100")
  print("The game will also have chosen a random number")
  print("You get 15 attempts")
  print("See how many tries it takes for you to guess the same number!")

  import random

  lower = 1
  upper = 100
  
  attempts = 0


  secret_number = random.randint(lower, upper)



  while True:
        try:
            guess = int(input(f"Please choose a number between {lower} and {upper}: "))
            
            if guess == secret_number:
              attempts += 1
              print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
              number_guess_start()
            elif guess < secret_number:
              print("Too low")
              attempts += 1
              if attempts >= 15:
                print(f"Sorry, you ran out of attempts! The secret number is {secret_number}.")

            elif guess > secret_number:
              print("Too high")
              attempts += 1
              if attempts >= 15:
                print(f"Sorry, you ran out of attempts! The secret number is {secret_number}.")
            else:
                print("Please put in a number between 1 and 100")
        except ValueError:
            print("Please put in a number between 1 and 100")


  


    







startscreen()