from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady= 20, bg = THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg = "white", bg = THEME_COLOR)
        self.score_label.grid(row=0, column = 1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Questions", fill=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row = 1, columnspan=2, pady = 20)  # grid and pack can't use together

        # Correct | Wrong buttons
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.correct_button = Button(image= true_image, highlightthickness=0, highlightbackground=THEME_COLOR, command = self.clicked_True)
        self.correct_button.grid(column=0, row=2)
        self.wrong_button = Button(image= false_image, highlightthickness=0, highlightbackground=THEME_COLOR, command = self.clicked_False)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score:{self.quiz.score}")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "You've reached the end of the list")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def clicked_True(self):
         self.give_feedback(self.quiz.check_answer("True"))
    def clicked_False(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")

        self.window.after(1000, self.get_next_question)