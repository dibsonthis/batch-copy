import tkinter as tk
from batch_copy_threaded import begin_batch_copy, end_batch_copy

def begin():
    begin_batch_copy(seperator=seperator.get())
    status.config(text="Batch Copy In Progress", fg="red")
    batch_button.config(state="disabled")
    end_button.config(state="normal")
    seperator_button_space.config(state="disabled")
    seperator_button_newline.config(state="disabled")
    print(f"Batch Copy Started Using {seperator.get()}")

def end():
    end_batch_copy()
    status.config(text="Batch Copy Complete", fg="green")
    batch_button.config(state="normal")
    end_button.config(state="disabled")
    seperator_button_space.config(state="normal")
    seperator_button_newline.config(state="normal")

root = tk.Tk()
root.geometry("200x200")
root.title("Batch Copy")

top_frame = tk.Frame(root)
bottom_frame = tk.Frame(root)

seperator_label = tk.Label(top_frame, text="Seperator:")
seperator_label.configure(font=("Helvetica", 8, "bold"))
seperator_label.pack(fill=tk.X, pady=(0,10))
seperator = tk.StringVar()
seperator_button_space = tk.Radiobutton(top_frame, text="Space", variable=seperator, value='space')
seperator_button_space.invoke()
seperator_button_space.configure(font=("Helvetica", 8, "bold"))
seperator_button_space.pack(fill=tk.X)
seperator_button_newline = tk.Radiobutton(top_frame, text="Newline", variable=seperator, value='newline')
seperator_button_newline.configure(font=("Helvetica", 8, "bold"))
seperator_button_newline.pack(fill=tk.X, pady=(0,10))

batch_button = tk.Button(bottom_frame, text="Begin Batch Copy", command=begin)
batch_button.configure(font=("Helvetica", 12, "bold"))
batch_button.pack(fill=tk.X)
end_button = tk.Button(bottom_frame, text="End Batch Copy", command=end, state="disabled")
end_button.configure(font=("Helvetica", 12, "bold"))
end_button.pack(fill=tk.X)
status = tk.Label(bottom_frame, text="Ready")
status.configure(font=("Helvetica", 12, "bold"))
status.pack(fill=tk.X, pady=(10,0))

top_frame.pack()
bottom_frame.pack()


root.mainloop()
