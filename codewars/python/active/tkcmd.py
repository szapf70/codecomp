import tkinter as tk
from tkinter import scrolledtext
import cmd
import threading

class MyCmd(cmd.Cmd):
    intro = 'Willkommen! Geben Sie help oder ? ein, um Hilfe zu erhalten.\n'
    prompt = '(cmd) '
    
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget
    
    def do_greet(self, line):
        """Greet the user."""
        self.text_widget.insert(tk.END, 'Hello!\n')
        
    def do_exit(self, line):
        """Exit the application."""
        return True
    
    # Add more command functions here

class CmdInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter CMD Interface")

        # Create a scrolled text widget
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
        self.text_area.pack(padx=10, pady=10)
        
        # Bind the enter key to execute command
        self.text_area.bind("<Return>", self.execute_command)
        
        # Initialize the cmd instance
        self.cmd_instance = MyCmd(self.text_area)
        
    def execute_command(self, event):
        # Get the current line
        command = self.text_area.get("end-2c linestart", "end-1c")
        
        # Execute command in a separate thread
        threading.Thread(target=self.cmd_instance.onecmd, args=(command,)).start()
        
        # Move the cursor to a new line
        self.text_area.insert(tk.END, "\n")
        
        # Prevent default behavior of the enter key
        return "break"

if __name__ == "__main__":
    root = tk.Tk()
    app = CmdInterface(root)
    root.mainloop()
