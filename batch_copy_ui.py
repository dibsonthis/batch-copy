import tkinter as tk
from batch_copy_threaded import begin_batch_copy, end_batch_copy
import pyperclip

def begin():
    begin_batch_copy()
    status.config(text="Batch Copy In Progress", fg="red")
    batch_button.config(state="disabled")
    end_button.config(state="normal")

def end():
    end_batch_copy()
    status.config(text="Batch Copy Complete", fg="green")
    batch_button.config(state="normal")
    end_button.config(state="disabled")

root = tk.Tk()
root.geometry("200x100")
root.title("Batch Copy")

batch_button = tk.Button(root, text="Begin Batch Copy", command=begin)
batch_button.configure(font=("Helvetica", 12, "bold"))
batch_button.pack()
end_button = tk.Button(root, text="End Batch Copy", command=end, state="disabled")
end_button.configure(font=("Helvetica", 12, "bold"))
end_button.pack()
status = tk.Label(root, text="Ready")
status.configure(font=("Helvetica", 12, "bold"))
status.pack()


root.mainloop()
