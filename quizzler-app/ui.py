from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lbl = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 10))
        self.score_lbl.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Text",
            fill=THEME_COLOR,
            font=("Ariel", 15, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_img, borderwidth=0, highlightthickness=0,
                                command=lambda: self.choose_answer("False"))
        self.false_btn.grid(column=1, row=2)

        true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_img, borderwidth=0, highlightthickness=0,
                               command=lambda: self.choose_answer("True"))
        self.true_btn.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        self.score_lbl.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.buttons_state(ACTIVE)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")

    def choose_answer(self, answer):
        if answer == "True":
            self.give_feedback(self.quiz.check_answer(answer))
        else:
            self.give_feedback(self.quiz.check_answer(answer))

    def give_feedback(self, is_right):
        self.buttons_state(DISABLED)
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)

    def buttons_state(self, state: str):
        self.true_btn.config(state=state)
        self.false_btn.config(state=state)
