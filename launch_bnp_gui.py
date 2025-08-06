import tkinter as tk

def on_submit():
    user_input = entry.get()
    print("User entered:", user_input)
    root.destroy()  # Close the window

# Create main window
root = tk.Tk()
root.title("টেম্পু স্টেন্ড")

# Desired window size
window_width = 800
window_height = 450

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
# Disable window resizing (disables maximize button)
root.resizable(False, False)

# Disable close button by overriding the close protocol
def disable_event():
    pass  # do nothing when close button is clicked

root.protocol("WM_DELETE_WINDOW", disable_event)
# Label
label = tk.Label(
    root,
    text='''
💼 এখন থেকে Coder দের কোড করতেও লাগবে পার্টি অনুমতি ও চাঁদা!
💻 Java লিখতে হলে  = ১০,০০০০ টাকা চাঁদা! 
🐍 Python লিখতে হলে —  ৫,০০০ টাকা চাঁদা! 
⚙ JavaScript লিখতে হলে —  ৩,০০০ টাকা চাঁদা! 

🧠 Bug ধরলে বলবে — “এইটা বিএনপির ষড়যন্ত্র!”
📦 Deploy করতে গেলে — “লন্ডন অফিসে চাঁদা পাঠানোর রিসিট show করতে হবে”
🎨 CSS কালার দিলে — “এইটা তারেক ভাইয়ের ডিজাইন কি না আগে বলেন!”
''',
    font=("Helvetica", 16),
    justify="left"
)
label.pack(pady=10)

# Entry with full width and watermark
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Helvetica", 12))
entry.pack(fill="x", padx=20)
entry_var.set("send your money")

def clear_placeholder(event):
    if entry_var.get() == "send your money":
        entry_var.set("")

entry.bind("<FocusIn>", clear_placeholder)

# Submit button with blue background
submit_button = tk.Button(
    root,
    text="Submit",
    command=on_submit,
    bg="blue",
    fg="white",
    font=("Helvetica", 12, "bold")
)
submit_button.pack(pady=15)

# Run the GUI loop
root.mainloop()
