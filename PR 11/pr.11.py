import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Ф.И.О. автора")
        
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Файл", menu=self.file_menu)
        self.file_menu.add_command(label="Открыть", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Выход", command=root.quit)

    
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text="Калькулятор")
        self.notebook.add(self.tab2, text="Чекбоксы")
        self.notebook.add(self.tab3, text="Работа с текстом")

        self.create_calculator_tab()
        self.create_checkbox_tab()
        self.create_text_tab()

    def create_calculator_tab(self):
        
        self.entry1 = tk.Entry(self.tab1)
        self.entry1.pack(pady=5)
        
        self.entry2 = tk.Entry(self.tab1)
        self.entry2.pack(pady=5)
        
        self.operation = ttk.Combobox(self.tab1, values=["+", "-", "*", "/"])
        self.operation.pack(pady=5)
        
        self.calculate_button = tk.Button(self.tab1, text="Рассчитать", command=self.calculate)
        self.calculate_button.pack(pady=5)

        self.result_label = tk.Label(self.tab1, text="")
        self.result_label.pack(pady=5)

    def calculate(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            op = self.operation.get()
            
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                result = num1 / num2
            
            self.result_label.config(text=f"Результат: {result}")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные числа.")

    def create_checkbox_tab(self):
        
        self.checkbox_var1 = tk.IntVar()
        self.checkbox_var2 = tk.IntVar()
        self.checkbox_var3 = tk.IntVar()

        self.checkbox1 = tk.Checkbutton(self.tab2, text="Первый", variable=self.checkbox_var1)
        self.checkbox1.pack(pady=5)
        
        self.checkbox2 = tk.Checkbutton(self.tab2, text="Второй", variable=self.checkbox_var2)
        self.checkbox2.pack(pady=5)
        
        self.checkbox3 = tk.Checkbutton(self.tab2, text="Третий", variable=self.checkbox_var3)
        self.checkbox3.pack(pady=5)

        self.submit_button = tk.Button(self.tab2, text="Проверить выбор", command=self.check_selection)
        self.submit_button.pack(pady=5)

    def check_selection(self):
        selected = []
        if self.checkbox_var1.get():
            selected.append("Первый")
            if self.checkbox_var2.get():
                selected.append("Второй")
            if self.checkbox_var3.get():
                selected.append("Третий")
            if selected:
                messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(selected)}")
            else:
                messagebox.showinfo("Выбор", "Ничего не выбрано")

    def create_text_tab(self):
        
        self.text_area = tk.Text(self.tab3, height=10)
        self.text_area.pack(pady=5)

        self.save_button = tk.Button(self.tab3, text="Сохранить текст", command=self.save_text)
        self.save_button.pack(pady=5)

    def open_file(self):
        filepath = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"),("All Files", "*.*")])
        if filepath:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                self.text_area.delete("1.0", tk.END)  
                self.text_area.insert(tk.END, content)  

    def save_text(self):
        text = self.text_area.get("1.0", tk.END)
        filepath = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files", "*.txt"),("All Files", "*.*")])
        if filepath:
            with open(filepath, 'w', encoding='utf-8') as file:file.write(text)
            messagebox.showinfo("Сохранение", "Текст успешно сохранен!")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

