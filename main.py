# Importo a biblioteca tkinter que será usada para criar a interface gráfica
import tkinter as tk
from tkinter import messagebox

# Crio a janela principal da calculadora
root = tk.Tk()

# Defino o título da janela como "Calculadora Lo-Fi"
root.title("Calculadora Lo-Fi")

# Defino a cor de fundo da janela para um tom escuro de azul
root.configure(bg='#2F2E41')

# Crio um campo de entrada onde serão exibidos os números e resultados
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Defino o campo de entrada como somente leitura
entry.config(state='readonly')

# Crio um campo de texto onde será exibido o histórico de cálculos
history = tk.Text(root, width=35, height=10)
history.grid(row=7, column=0, columnspan=4)

# Defino o campo de texto do histórico como somente leitura
history.config(state='disabled')

# Aqui defino duas variáveis globais que serão usadas para armazenar o número e a operação selecionados
global num
global op

# Esta função adiciona o número do botão pressionado ao campo de entrada
def button_click(number):
    entry.config(state='normal')
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))
    entry.config(state='readonly')

# Esta função limpa o campo de entrada
def button_clear():
    entry.config(state='normal')
    entry.delete(0, tk.END)
    entry.config(state='readonly')

# Estas funções definem a operação a ser realizada (adição, subtração, multiplicação, divisão ou módulo)
def button_add():
    global num
    global op
    num = float(entry.get())
    op = '+'
    entry.config(state='normal')
    entry.delete(0, tk.END)
    entry.config(state='readonly')

def button_subtract():
    global num
    global op
    num = float(entry.get())
    op = '-'
    entry.config(state='normal')
    entry.delete(0, tk.END)
    entry.config(state='readonly')

def button_multiply():
    global num
    global op
    num = float(entry.get())
    op = '*'
    entry.config(state='normal')
    entry.delete(0, tk.END)
    entry.config(state='readonly')

def button_divide():
    global num
    global op
    num = float(entry.get())
    op = '/'
    entry.config(state='normal')
    entry.delete(0, tk.END)
    entry.config(state='readonly')

def button_modulo():
    global num
    global op
    num = float(entry.get())
    op = '%'
    entry.config(state='normal')
    entry.delete(0, tk.END)
    entry.config(state='readonly')

# Esta função calcula o resultado da operação selecionada
def button_equal():
    second_num = float(entry.get())
    entry.config(state='normal')
    entry.delete(0, tk.END)

    if op == '+':
        result = num + second_num
    elif op == '-':
        result = num - second_num
    elif op == '*':
        result = num * second_num
    elif op == '/':
        if second_num != 0:
            result = num / second_num
        else:
            result = "Erro"
    elif op == '%':
        if second_num != 0:
            result = num % second_num
        else:
            result = "Erro"

    entry.insert(0, result)
    entry.config(state='readonly')

    # Adiciono o cálculo ao histórico
    history.config(state='normal')
    history.insert(tk.END, f"{num} {op} {second_num} = {result}\n")
    history.config(state='disabled')

# Aqui crio os botões da calculadora
for i in range(9):
    button = tk.Button(root, text=str(i+1), padx=40, pady=20, command=lambda i=i: button_click(i+1), bg='#BB9457', fg='#FFFFFF')
    button.grid(row=(i//3)+1, column=i%3)

button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), bg='#BB9457', fg='#FFFFFF')
button_0.grid(row=4, column=0)

button_clear = tk.Button(root, text="Limpar", padx=79, pady=20, command=button_clear, bg='#6A057F', fg='#FFFFFF')
button_clear.grid(row=4, column=1, columnspan=2)

button_equal = tk.Button(root, text="=", padx=91, pady=20, command=button_equal, bg='#6A057F', fg='#FFFFFF')
button_equal.grid(row=5, column=0, columnspan=2)

button_add = tk.Button(root, text="+", padx=39, pady=20, command=button_add, bg='#BB9457', fg='#FFFFFF')
button_add.grid(row=2, column=3)

button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=button_subtract, bg='#BB9457', fg='#FFFFFF')
button_subtract.grid(row=3, column=3)

button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=button_multiply, bg='#BB9457', fg='#FFFFFF')
button_multiply.grid(row=4, column=3)

button_divide = tk.Button(root, text="/", padx=41, pady=20, command=button_divide, bg='#BB9457', fg='#FFFFFF')
button_divide.grid(row=5, column=3)

button_modulo = tk.Button(root, text="%", padx=39, pady=20, command=button_modulo, bg='#BB9457', fg='#FFFFFF')
button_modulo.grid(row=6, column=3)

# Função para abrir o link do GitHub
def open_github():
    import webbrowser
    webbrowser.open('https://github.com/lucascandev')

# Crio um rótulo com o texto "Desenvolvido por lucascandev" e faço com que ele seja um link clicável
credit = tk.Label(root, text="Desenvolvido por lucascandev", bg='#2F2E41', fg='#BB9457', cursor="hand2")
credit.grid(row=8, column=0, columnspan=4)
credit.bind("<Button-1>", lambda e: open_github())

# Aqui inicio o loop da interface gráfica
root.mainloop()