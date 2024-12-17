import tkinter as tk

def create_text_window(text):
    root = tk.Tk()
    root.title("Extracted Text")

    # Create a Text widget
    text_box = tk.Text(root, wrap='word', height=20, width=80)
    text_box.insert('1.0', text)
    text_box.pack(expand=True, fill='both')

    # Make text selectable and copyable
    text_box.config(state='normal')

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, command=text_box.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_box.config(yscrollcommand=scrollbar.set)

    root.mainloop()
