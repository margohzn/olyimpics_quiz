from tkinter import *
from tkinter import messagebox 

score = 0

#fonctions 

#first question
def first_question():
    window.geometry("600x400")
    question_1.place(x = 7, y = 190)
    answer1.place(x = 30, y = 250)
    answer2.place(x = 330, y = 250)
    answer3.place(x = 30, y = 330)
    answer4.place(x = 330, y = 330)

def correct_answer1():
    global score
    messagebox.showinfo("Correct answer", "Correct answer!")
    score += 1
    score_widjet.config(text = f"Score = {score}")

    question_1.place_forget()
    answer1.place_forget()
    answer2.place_forget()
    answer3.place_forget()
    answer4.place_forget()
    start_button.place_forget()

    next2.place(x = 80, y = 110)


def wrong_answer1():
    messagebox.showwarning("Wrong answer", "Wrong answer")

    question_1.place_forget()
    answer1.place_forget()
    answer2.place_forget()
    answer3.place_forget()
    answer4.place_forget()
    start_button.place_forget()
    
    next2.place(x = 80, y = 110)

#second question 
def second_question():
    question_2.place(x = 7, y = 190)
    answer1_2.place(x = 30, y = 250)
    answer2_2.place(x = 330, y = 250)
    answer3_2.place(x = 30, y = 330)
    answer4_2.place(x = 330, y = 330)
    
def correct_answer2():
    global score
    messagebox.showinfo("Correct answer", "Correct answer!")
    score += 1
    score_widjet.config(text = f"Score = {score}")

    question_2.place_forget()
    answer1_2.place_forget()
    answer2_2.place_forget()
    answer3_2.place_forget()
    answer4_2.place_forget()
    next2.place_forget()

    next3.place(x = 80, y = 110)

def wrong_answer2():
    messagebox.showwarning("Wrong answer", "Wrong answer")

    question_2.place_forget()
    answer1_2.place_forget()
    answer2_2.place_forget()
    answer3_2.place_forget()
    answer4_2.place_forget()
    next2.place_forget()

    next3.place(x = 80, y = 110)

#third question 
def third_question():
    question_3.place(x = 7, y = 190)
    answer1_3.place(x = 30, y = 250)
    answer2_3.place(x = 330, y = 250)
    answer3_3.place(x = 30, y = 330)
    answer4_3.place(x = 330, y = 330)
    
def correct_answer3():
    global score
    messagebox.showinfo("Correct answer", "Correct answer!")
    score += 1
    score_widjet.config(text = f"Score = {score}")

    question_3.place_forget()
    answer1_3.place_forget()
    answer2_3.place_forget()
    answer3_3.place_forget()
    answer4_3.place_forget()
    next3.place_forget()

    next4.place(x = 80, y = 110)

def wrong_answer3():
    messagebox.showwarning("Wrong answer", "Wrong answer")

    question_3.place_forget()
    answer1_3.place_forget()
    answer2_3.place_forget()
    answer3_3.place_forget()
    answer4_3.place_forget()
    next3.place_forget()   

    next4.place(x = 80, y = 110)

#forth question 
def forth_question():
    question_4.place(x = 7, y = 190)
    answer1_4.place(x = 30, y = 250)
    answer2_4.place(x = 330, y = 250)
    answer3_4.place(x = 30, y = 330)
    answer4_4.place(x = 330, y = 330)
    
def correct_answer4():
    global score
    messagebox.showinfo("Correct answer", "Correct answer!")
    score += 1
    score_widjet.config(text = f"Score = {score}")

    question_4.place_forget()
    answer1_4.place_forget()
    answer2_4.place_forget()
    answer3_4.place_forget()
    answer4_4.place_forget()
    next4.place_forget()

    next5.place(x = 80, y = 110)

def wrong_answer4():
    messagebox.showwarning("Wrong answer", "Wrong answer")

    question_4.place_forget()
    answer1_4.place_forget()
    answer2_4.place_forget()
    answer3_4.place_forget()
    answer4_4.place_forget()
    next4.place_forget()   

    next5.place(x = 80, y = 110)


#fifth question 
def fifth_question():
    question_5.place(x = 7, y = 190)
    answer1_5.place(x = 30, y = 250)
    answer2_5.place(x = 330, y = 250)
    answer3_5.place(x = 30, y = 330)
    answer4_5.place(x = 330, y = 330)
    
def correct_answer5():
    global score
    messagebox.showinfo("Correct answer", "Correct answer!")
    score += 1
    score_widjet.config(text = f"Score = {score}")

    question_5.place_forget()
    answer1_5.place_forget()
    answer2_5.place_forget()
    answer3_5.place_forget()
    answer4_5.place_forget()
    next5.place_forget()
    result = Label(window, text = f"Score = {score}/5, well done", fg = "green", bg = "white", font = ("times", 25, "bold")).place(x = 190, y = 190)
    thank_you = Label(window, text = "Thank you for playing", fg = "navy", bg = "white", font = ("helvetica", 23, "bold")).place(x = 190, y = 235)

def wrong_answer5():
    messagebox.showwarning("Wrong answer", "Wrong answer")

    question_5.place_forget()
    answer1_5.place_forget()
    answer2_5.place_forget()
    answer3_5.place_forget()
    answer4_5.place_forget()
    next5.place_forget()
    result = Label(window, text = f"Score = {score}/5, well done", fg = "green", bg = "white", font = ("times", 25, "bold")).place(x = 190, y = 190)
    thank_you = Label(window, text = "Thank you for playing", fg = "navy", bg = "white", font = ("helvetica", 23, "bold")).place(x = 175, y = 235)


#creating window 
window = Tk()
window.geometry("600x170")
window.title("Olympics Quiz! 5 questions")
window.configure(background = "white")


#title on window
title = Label(window, text = "How much do you know about the olyimpics?", font = ("times", 30, "underline", "bold"), bg = "white", fg = "#000090").pack()

#rings for olimpycs sign
ring = Label(window, text = "◯", fg = "#6082B6", bg = "white", font = ("times", 60, )).place(x = 200, y = 70)
ring2 = Label(window, text = "◯", fg = "black", bg = "white", font = ("times", 60)).place(x = 270, y = 70)
ring3 = Label(window, text = "◯", fg = "red", bg = "white", font = ("times", 60)).place(x = 340, y = 70)
ring4 = Label(window, text = "◯", fg = "#FFBF00", bg = "white", font = ("times", 60)).place(x = 235, y = 100)
ring4 = Label(window, text = "◯", fg = "green", bg = "white", font = ("times", 60)).place(x = 305, y = 100)

#top left corner 
score_widjet = Label(window, text = f"Score = {score}", bg = "white", fg = "black", font = ("times", 30))
score_widjet.place(x = 5, y = 70)
start_button = Button(window, text = "start", command = first_question)
start_button.place(x = 80, y = 110)
exit_button = Button(window, text = "Exit", command = window.quit).place(x = 7, y = 110)

#first question widjets
question_1 = Label(window, text = "1. Where and when was the first Olypics held?", fg = "black", bg = "white", font = ("helvetica", 28))
answer1 = Button(window, text = "Athens Greece, 1896", font = ("helvetica", 20), command = correct_answer1)
answer2 = Button(window, text = "Rome Italy, 1884", font = ("helvetica", 20), command = wrong_answer1)
answer3 = Button(window, text = "Berlin Germany, 1932", font = ("helvetica", 20), command = wrong_answer1)
answer4 = Button(window, text = "Tokyo Japan, 1964", font = ("helvetica", 20), command = wrong_answer1)

#second question widjets 
next2 = Button(window, text = "Next", command = second_question)
question_2 = Label(window, text = "2. Which sport was added to the Summer Olympics for the first time in 2021?", fg = "black", bg = "white", font = ("helvetica", 17))
answer1_2 = Button(window, text = "Golf", font = ("helvetica", 20), width = 15, command = wrong_answer2)
answer2_2 = Button(window, text = "Baseball", font = ("helvetica", 20), width = 15, command = wrong_answer2)
answer3_2 = Button(window, text = "Tennis", font = ("helvetica", 20),  width = 15, command = wrong_answer2)
answer4_2 = Button(window, text = "Skatebording", font = ("helvetica", 20),  width = 15, command = correct_answer2)

#third question widjets 
next3 = Button(window, text = "Next", command = third_question)
question_3 = Label(window, text = "3. Which city has hosted the Summer Olympics the most?", fg = "black", bg = "white", font = ("helvetica", 22))
answer1_3 = Button(window, text = "Rome", font = ("helvetica", 20), width = 15, command = wrong_answer3)
answer2_3 = Button(window, text = "London", font = ("helvetica", 20), width = 15, command = correct_answer3)
answer3_3 = Button(window, text = "Valleta", font = ("helvetica", 20),  width = 15, command = wrong_answer3)
answer4_3 = Button(window, text = "Venice", font = ("helvetica", 20),  width = 15, command = correct_answer3)

#forth question widjets 
next4 = Button(window, text = "Next", command = forth_question)
question_4 = Label(window, text = "4. Which country has won the most Winter Olympic medals in history?", fg = "black", bg = "white", font = ("helvetica", 19))
answer1_4 = Button(window, text = "Canada", font = ("helvetica", 20), width = 15, command = wrong_answer4)
answer2_4 = Button(window, text = "Norway", font = ("helvetica", 20), width = 15, command = correct_answer4)
answer3_4 = Button(window, text = "United states", font = ("helvetica", 20),  width = 15, command = wrong_answer4)
answer4_4 = Button(window, text = "Finland", font = ("helvetica", 20),  width = 15, command = wrong_answer4)

#fifth question widjets 
next5 = Button(window, text = "Next", command = fifth_question)
question_5 = Label(window, text = "5. Which sport will not appear in the 2024 Olympics??", fg = "black", bg = "white", font = ("helvetica", 23))
answer1_5 = Button(window, text = "Basketball", font = ("helvetica", 20), width = 15, command = wrong_answer5)
answer2_5 = Button(window, text = "Equestrian", font = ("helvetica", 20), width = 15, command = wrong_answer5)
answer3_5 = Button(window, text = "Baseball", font = ("helvetica", 20),  width = 15, command = correct_answer5)
answer4_5 = Button(window, text = "Fencing", font = ("helvetica", 20),  width = 15, command = wrong_answer5)

window.mainloop()