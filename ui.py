from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 18, "italic")

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.title_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 16))
        self.title_label.grid(column=0, row=0, columnspan=2, pady=10)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.quiz_text = self.canvas.create_text(150, 125, text="Quiz", font=FONT, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.true_image = PhotoImage(file="./images/true.png")
        self.false_image = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.answer_true)
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.answer_false)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        self.is_right = self.quiz.check_answer("True")
        self.give_feedback(self.is_right)
    def answer_false(self):
        self.is_right= self.quiz.check_answer("False")
        self.give_feedback(self.is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.title_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.get_next_question)