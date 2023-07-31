import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Create the text field for displaying the input and result
        self.display = tk.Entry(self.master, width=20, font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Define the buttons
        self.buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]

        # Create the buttons and attach their commands
        for row, button_list in enumerate(self.buttons, start=1):
            for col, label in enumerate(button_list):
                button = tk.Button(self.master, text=label, width=5, height=2, font=("Arial", 16),command=lambda x=label: self.handle_click(x))
                button.grid(row=row, column=col, padx=5, pady=5)

    def handle_click(self, label):
        if label == "=":
            # Evaluate the expression and display the result
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        else:
            # Add the clicked button label to the input field
            self.display.insert(tk.END, label)

# Create the main window and run the calculator
root = tk.Tk()
calc = Calculator(root)
root.mainloop()
