import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import subprocess
import os

def run_linter():
    code = text_area.get("1.0", tk.END)
    language = language_var.get()

    with open("temp_code_file", "w") as temp_file:
        temp_file.write(code)
    
    if language == "Python":
        result = subprocess.run(['pylint', 'temp_code_file'], capture_output=True, text=True)
        output = result.stdout
    elif language == "Java":
        checkstyle_path = 'C:/Users/szapf/AppData/Roaming/Java/checkstyle-10.18.1-all.jar'  # Update with the correct path
        with open("temp_code_file.java", "w") as temp_file:
            temp_file.write(code)
        result = subprocess.run(['java', '-jar', checkstyle_path, '-c', '/sun_checks.xml', 'temp_code_file.java'], capture_output=True, text=True)
        output = result.stdout
        os.remove("temp_code_file.java")
    else:
        output = "Unsupported language selected."

    output_area.delete("1.0", tk.END)
    output_area.insert(tk.END, output)
    os.remove("temp_code_file")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py"), ("Java Files", "*.java")])
    if file_path:
        with open(file_path, 'r') as file:
            code = file.read()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, code)
        if file_path.endswith(".py"):
            language_var.set("Python")
        elif file_path.endswith(".java"):
            language_var.set("Java")

app = tk.Tk()
app.title("Code Linter")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

language_var = tk.StringVar(value="Python")

tk.Label(frame, text="Select Language:").grid(row=0, column=0, sticky=tk.W)
tk.Radiobutton(frame, text="Python", variable=language_var, value="Python").grid(row=0, column=1, sticky=tk.W)
tk.Radiobutton(frame, text="Java", variable=language_var, value="Java").grid(row=0, column=2, sticky=tk.W)

tk.Button(frame, text="Open File", command=open_file).grid(row=0, column=3, padx=5)
tk.Button(frame, text="Run Linter", command=run_linter).grid(row=0, column=4, padx=5)

text_area = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=80, height=20)
text_area.pack(padx=10, pady=10)

output_area = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=80, height=10, fg="white", bg="black")
output_area.pack(padx=10, pady=10)

app.mainloop()
