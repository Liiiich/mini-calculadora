import tkinter as tk
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Sofisticada")
        self.geometry("400x600")
        self.create_widgets()
        
    def create_widgets(self):
        self.result_var = tk.StringVar()
        self.result_var.set("0")

        # Display
        display = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=4, width=14, borderwidth=4, relief="ridge", justify="right")
        display.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('sqrt', 5, 0), ('log', 5, 1), ('exp', 5, 2), ('C', 5, 3)
        ]
        
        for (text, row, column) in buttons:
            if text == "=":
                button = tk.Button(self, text=text, padx=20, pady=20, font=("Arial", 18), command=self.evaluate)
            elif text == "C":
                button = tk.Button(self, text=text, padx=20, pady=20, font=("Arial", 18), command=self.clear)
            else:
                button = tk.Button(self, text=text, padx=20, pady=20, font=("Arial", 18), command=lambda t=text: self.append(t))
            button.grid(row=row, column=column, padx=5, pady=5)
    
    def append(self, text):
        current_text = self.result_var.get()
        if current_text == "0":
            self.result_var.set(text)
        else:
            self.result_var.set(current_text + text)
    
    def clear(self):
        self.result_var.set("0")
    
    def evaluate(self):
        expression = self.result_var.get()
        try:
            # Handle square root
            if 'sqrt' in expression:
                base = expression.replace('sqrt', '')
                result = math.sqrt(float(base))
            # Handle logarithm
            elif 'log' in expression:
                base = expression.replace('log', '')
                result = math.log10(float(base))
            # Handle exponentiation
            elif 'exp' in expression:
                base = expression.replace('exp', '')
                result = math.exp(float(base))
            else:
                # Replace mathematical symbols
                expression = expression.replace('×', '*').replace('÷', '/')
                result = eval(expression)
            
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("Error")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
