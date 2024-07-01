import tkinter as tk
from tkinter import scrolledtext, messagebox


# Функция для центрирования окна
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')


# Функция для обработки текста
def process_text(input_text):
    lines = input_text.strip().split('\n')
    output_lines = []
    i = 0

    while i < len(lines):
        if ':' in lines[i].strip():
            time_label = lines[i].strip()
            i += 1
            if i < len(lines) and (':' not in lines[i].strip()):
                output_lines.append(f"{time_label}\t{lines[i].strip()}")
                i += 1
            else:
                output_lines.append(time_label)
        else:
            i += 1

    return '\n'.join(output_lines)


# Функция для обработки кнопки "Форматирование"
def on_process():
    input_text = text_input.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Внимание", "Поле пустое!")
        return

    processed_text = process_text(input_text)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, processed_text)


# Функция для вставки текста из буфера обмена
def paste_from_clipboard():
    try:
        clipboard_text = root.clipboard_get()
        text_input.delete("1.0", tk.END)
        text_input.insert(tk.END, clipboard_text)
    except tk.TclError:
        messagebox.showerror("Ошибка", "Нет текста в буфере обмена")


# Функция для копирования текста в буфер обмена
def copy_to_clipboard():
    try:
        output_text = text_output.get("1.0", tk.END).strip()
        root.clipboard_clear()
        root.clipboard_append(output_text)
        messagebox.showinfo("Успешно", "Расписание скопировано в буфер обмена!")
    except tk.TclError:
        messagebox.showerror("Ошибка", "Не получилось скопировать текст")


# Функция для открытия окна с информацией
def show_info():
    info = """
    Разработчик: Максим М.
    
    Благодарю за использование программы!
    Обратная связь об ошибках и прочие вопросы:
    
    Telegram: @AntiSharp
    """
    messagebox.showinfo("О разработчике", info)


# Настройка основного окна
root = tk.Tk()
root.title("TWFM Text Formatter")

window_width = 600
window_height = 600
center_window(root, window_width, window_height)

# Установка иконки приложения
root.iconbitmap('logo.ico')

# Виджеты
label_input = tk.Label(root, text="Введите свое расписание из TWFM:")
label_input.pack()

text_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=10)
text_input.pack(pady=10)

button_paste = tk.Button(root, text="Вставить", command=paste_from_clipboard)
button_paste.pack(pady=5)

button_process = tk.Button(root, text="Форматирование", command=on_process)
button_process.pack(pady=5)

label_output = tk.Label(root, text="Готовое расписание:")
label_output.pack()

text_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=10)
text_output.pack(pady=10)

button_copy = tk.Button(root, text="Скопировать", command=copy_to_clipboard)
button_copy.pack(pady=5)

# Добавляем инфо-кнопку
button_info = tk.Button(root, text="Info", command=show_info)
button_info.pack(side=tk.RIGHT, padx=10, pady=10)

# Добавляем версию программы
label_version = tk.Label(root, text="v.1.010724", anchor=tk.W)
label_version.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
