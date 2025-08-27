import tkinter as tk
import random

# Funny Tricky Questions
QUESTIONS = [
    ("If you throw a red stone into the blue sea, what will it become?", "Wet", ["Red", "Blue", "Wet", "Heavy"]),
    ("How many months have 28 days?", "All 12", ["1", "12", "6", "All 12"]),
    ("If a rooster lays an egg on a roof, which way will it roll?", "Roosters don’t lay eggs", ["Left", "Right", "Down", "Roosters don’t lay eggs"]),
    ("What can you never eat for breakfast?", "Lunch or Dinner", ["Rice", "Beans", "Lunch or Dinner", "Fruits"]),
    ("What goes up but never comes down?", "Your Age", ["Ball", "Rocket", "Your Age", "Rain"]),
    ("If you drop your phone in water, what’s the first thing you should do?", "Cry 😂", ["Cry 😂", "Call Mom", "Put in rice", "Swim after it"]),
    ("Which weighs more: 1kg of cotton or 1kg of iron?", "They weigh the same", ["Cotton", "Iron", "Both same", "Cotton if wet"]),
    ("What’s heavier: a ton of feathers or a ton of bricks?", "Same weight", ["Feathers", "Bricks", "Same weight", "Depends on wind"]),
    ("If you had one match and entered a dark room with a lamp, a candle, and a stove, what would you light first?", "The match", ["Lamp", "Candle", "Stove", "The match"]),
    ("If there are 6 apples and you take away 4, how many do you have?", "4", ["2", "6", "4", "None"]),
]

BUTTON_COLORS = ["#FFB6C1", "#ADD8E6", "#90EE90", "#FFD700"]  # Pink, Blue, Green, Yellow


class IQGame:
    def __init__(self, root):
        self.root = root
        self.root.title("How Dumb Can You Be???")
        self.root.geometry("500x550")
        self.root.configure(bg="#FFFACD")  # Light yellow
        self.iq = 0
        self.score = 0
        self.question_index = 0
        self.feedback_label = None
        self.home_screen()

    def home_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="How Dumb Can You Be???", font=("Arial", 24, "bold"), bg="#FFFACD").pack(pady=30)

        tk.Label(self.root, text="Enter your IQ (0 - 300):", font=("Arial", 14), bg="#FFFACD").pack()
        self.iq_entry = tk.Entry(self.root, font=("Arial", 14), justify="center")
        self.iq_entry.pack(pady=10)

        tk.Button(self.root, text="Start Game", font=("Arial", 14), bg="#87CEFA", command=self.start_game).pack(pady=20)

    def start_game(self):
        try:
            self.iq = int(self.iq_entry.get())
            if not (0 <= self.iq <= 300):
                raise ValueError
        except ValueError:
            self.iq = 100  # default if invalid
        self.score = 0
        self.question_index = 0
        random.shuffle(QUESTIONS)
        self.show_question()

    def show_question(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        if self.question_index >= 10:
            self.root.after(500, self.show_result)
            return

        q, correct, options = QUESTIONS[self.question_index]
        tk.Label(self.root, text=f"Q{self.question_index + 1}: {q}", font=("Arial", 16, "bold"),
                 wraplength=450, bg="#FFFACD").pack(pady=30)

        for i, opt in enumerate(options):
            tk.Button(self.root, text=opt, font=("Arial", 14), width=25, bg=BUTTON_COLORS[i % 4],
                      command=lambda o=opt, c=correct: self.check_answer(o, c)).pack(pady=8)

        # space for feedback
        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 14, "bold"), fg="black", bg="#FFFACD")
        self.feedback_label.pack(pady=20)

    def check_answer(self, selected, correct):
        if selected == correct:
            self.score += 1
            self.feedback_label.config(text="✅ Correct ☑", fg="green")
        else:
            self.iq -= 10
            self.feedback_label.config(
                text=f"❌ You're as dumb as I thought!\nCorrect answer: {correct}",
                fg="red"
            )
        self.question_index += 1
        # delay before next question
        self.root.after(1500, self.show_question)

    def show_result(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Final IQ: {self.iq}", font=("Arial", 20, "bold"), fg="#1E90FF", bg="#FFFACD").pack(pady=20)
        tk.Label(self.root, text=f"Score: {self.score}/10", font=("Arial", 16), bg="#FFFACD").pack(pady=10)

        if self.score >= 8:
            msg = "😏 Hmmmm You're not so dumb after all!"
        elif 4 <= self.score < 8:
            msg = "🏖 Your brain is on vacation!"
        else:
            msg = "🪨 You're as dumb as a rock you empty head!"

        tk.Label(self.root, text=msg, font=("Arial", 16, "bold"), fg="#FF4500", wraplength=450, bg="#FFFACD").pack(pady=15)

        tk.Button(self.root, text="Play Again", font=("Arial", 14), bg="#87CEFA", command=self.home_screen).pack(pady=20)


# ---- RUN THE GAME ----
if __name__ == "__main__":
    root = tk.Tk()
    app = IQGame(root)
    root.mainloop()