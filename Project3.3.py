#coding=utf-8
questions = ["__1__", "__2__","__3__", "__4__"] # the comment upside, is to avoid the ASSCI error whit triple quotes,
# extracted here    https://stackoverflow.com/questions/24946776/syntaxerror-non-ascii-character-in-running-python-code
ntotal_quest = 4 # Total number of questions
questions_easy = """
 __1__ is a method that allow you to replace a specific word.
 __2__ is another method, that search the word you want, and show you the position of this word in a string. 
 You can join two text strings, just by using a __3__ operator, that's called concatenate.
 To define a variable, you just need a __4__ symbol, that's called an assignment."""

questions_normal = """
 Store a certain value whit a specific name, thats is the definition of __1__ .
 __2__ is a process that repeat itself over and over again, until return a False value.
 To define it , you use a __3__ statement.
 __4__ sentence, works to make a certain action if the declarated comparison is true"""

questions_hard = """
 __1__ is the name of a fuction that replace a certain word of a string whit the user input.
 __2__ happens when you forget to put the colon in a if or while statement, also if you write bad some word.
 when you change a variable that has an assignment whit another one, and both are changed, this is __3__.
 Approximately a computer can procces one __4__ instructions per second  """

correct_answer_easy = ["replace","find","+","="]
correct_answer_normal =["variable","loop","while","if"]
correct_answer_hard = ["mad lib generator","syntax error","mutation","billion"]

def lower_word(word):
    """
    Args:
        Word: A word thats is written whith at least one capital letter.
    Behaviour:
        Convert the entire word in lowercase.
    Returns:
        Returns the same word from the input but in lowercase.
    """ 

    word = word.lower()  
    return word

def congrats(string_p):
    """
    Args:
        String_p: Is a string that contains the questions. 
    Behaviour:
        Shows a message when you complete the test, and then shows the string_p.
    Returns:
        Prints a congratulation message. 
        Return the string_p. 
    """

    print "Congratulations, you have completed the fill-in-blank test\n"
    print string_p


def game_mode(diff_string, index, attempts, correct_ans):
    """ 
    Args:
        diff_string: Is the string that contains, the question statement.
        index: Is used to move along between the correct_ans.
        attempts: Attempts for the user if they write a wrong answer.
        correct_ans: Is the string that contains the four correct answer for the appropiate game difficult.
    Behaviour:
        This function ask for a user input, if the answer is equal to the correct answer, then shows a message, and replace the blank space whit the answer.
        Also after this, ask for the next question.
        If the answer is wrong, shows a message whit the appropiate remaining attempts. If the attempts goes to 0, or the user ask whith all the correct answers, the procees ends.
    Returns:
        Returns diff_string whit the blank space replaced.
        Returs next question.
        Print a message whit your remaining attempts.
        print Game Over and the procces ends.
    """
    print diff_string 
    print "\n" 
    user_input = raw_input("what's your answer for" + questions[index] + " ? ")
    if lower_word(user_input)==correct_ans[index]: 
        print "\n Excellent, that is the right answer, keep it up!"
        diff_string = diff_string.replace(questions[index], correct_ans[index])
        if index + 1 < ntotal_quest:
            game_mode(diff_string, index + 1, attempts,correct_ans) 
        else:
            congrats(diff_string)
    else:
        attempts = attempts - 1
        if attempts == 0:
            print "Game Over"
        else:
            print "\n sorry, your answer is wrong, please try again.(" + str(attempts) + " remaining attempts): "
            game_mode(diff_string, index, attempts,correct_ans) 


def diff_select():
    """
    Args:
        No args used in this function.
    Behaviour:
        Let the user select his difficult and then calls the respective difficult process.
    Returns:
        Prints a message exclusive for each dificult.
        Calls the procedure game_mode for the diffcult selected by the user.
        Else returNs a message and call diff_select again, to restart the selection.
     """  
    difficult = raw_input("easy, normal or hard: ")
    difficult = lower_word(difficult)
    if "easy" == difficult:
        print " \n Nice, you have chosen the easy mode. These are the questions:"
        game_mode(questions_easy, 0, 5,correct_answer_easy) 
    else:
        if difficult == "normal":
            print "\n Great, you have chosen the normal mode. These are the questions"
            game_mode(questions_normal,0,5,correct_answer_normal)
        else:
            if "hard" == difficult:
                print " \n Ohhh you are brave, you have chosen the hard mode, These are the questions,good Luck :"
                game_mode(questions_hard,0,5,correct_answer_hard)
            else:
                print "That's is not an option, please select again.\n"
                diff_select()


print " Hello, welcome to the fill-in-blank test. To start, please select your difficult"
diff_select()
