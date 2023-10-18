import tkinter as tk
import random
import time

class SpeedTypingTest:
    def __init__(self, root):
        # This is to define the window.
        self.root = root
        self.root.title('Speed Typing Test')
        self.root.geometry('600x400')

        self.texts = [
            "The quick brown fox jumps over the lazy dog.",
            "Python is a high-level programming language.",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "Programming is fun and rewarding."
        ]

        self.current_text = ""
        self.time_start = None

        self.label = tk.Label(root, text="Press Start to begin the test", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.text_display = tk.Label(root, text="", font=("Helvetica", 14))
        self.text_display.pack(pady=20)

        self.entry = tk.Entry(root, font=("Helvetica", 14))
        self.entry.pack(pady=20)
        self.entry.bind('<Return>', self.check_text)

        self.start_button = tk.Button(root, text="Start", command=self.start_test, font=("Helvetica", 12))
        self.start_button.pack()

    def start_test(self):
        self.current_text = random.choice(self.texts)
        self.text_display.config(text=self.current_text)
        self.entry.delete(0, 'end')
        self.entry.config(state='normal')
        self.start_button.config(state='disabled')
        self.time_start = time.time()
        self.root.after(60000, self.stop_test)

    def check_text(self, event):
        user_input = self.entry.get()
        if user_input == self.current_text:
            elapsed_time = time.time() - self.time_start
            words_per_minute = int(len(self.current_text.split()) / (elapsed_time / 60))
            result = f"You typed at {words_per_minute} words per minute!"
            self.label.config(text=result, fg='green')
        else:
            self.label.config(text="Try again.", fg='red')
            self.entry.delete(0, 'end')

    def stop_test(self):
        self.entry.delete(0, 'end')
        self.entry.config(state='disabled')
        self.start_button.config(state='normal')
        self.label.config(text="Press Start to begin the test")

if __name__ == '__main__':
    root = tk.Tk()
    app = SpeedTypingTest(root)
    root.mainloop()
