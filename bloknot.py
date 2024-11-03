from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename 


def open_file():
    filepath = askopenfilename(filetypes=[('Текстовые файлы', '*.txt'), ('Все файлы', '*.*')])

    if not filepath:
        return
    
    txt_edit.delete('1.0', END)

    with open(filepath, 'r') as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
    window.title(f'Блокнот {filepath}')


def save_file():
    filepath = asksaveasfilename( defaultextension='txt', filetypes=[('Текстовые файлы', '*.txt'), ('Все файлы', '*.*')])

    if not filepath:
        return
    
    with open(filepath, 'w') as output_file:
        text = txt_edit.get('1.0', END)
        output_file.write(text)
    window.title(f'Блокнот {filepath}')

def close_window():
    window.destroy()


fonts=[]

window = Tk()
window.title('Блокнот <Без названия>')
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
window.option_add('*tearOff', FALSE)

main_menu = Menu()
file_menu = Menu()

main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_command(label='Выйти', command=close_window)

file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_separator()
file_menu.add_command(label='Сохранить как...', command=save_file)


txt_edit = Text(window)
zametki = Frame(window, relief=RAISED, bd=2)

zametki.grid(row=0, column=0, sticky='ns')
txt_edit.grid(row=0, column=1, sticky='nsew')

window.config(menu=main_menu)
window.mainloop()