import tkinter as tk
from time import time

class TextDisappearingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Disappearing App")

        self.text = tk.Text(root, wrap=tk.WORD)
        self.text.pack()

        self.last_typing_time = 0

        self.text.bind("<Key>", self.update_typing_time)

    def update_typing_time(self, event):
        # Update the last typing time whenever a key is pressed
        self.last_typing_time = time()

    def check_typing_activity(self):
        current_time = time()
        if (current_time - self.last_typing_time) >= 5:
            self.clear_text()

        self.root.after(1000, self.check_typing_activity)

    def clear_text(self):
        self.text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextDisappearingApp(root)
    app.check_typing_activity()
    root.mainloop()
