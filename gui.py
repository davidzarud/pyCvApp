import tkinter as tk
import webbrowser


def generate_cv():
    name = name_entry.get()
    url = f'http://127.0.0.1:5000/generate_cv?name={name}'
    webbrowser.open(url)


def main():
    root = tk.Tk()
    root.title("CV Generator")

    tk.Label(root, text="Enter Your Name:").pack(pady=10)
    global name_entry
    name_entry = tk.Entry(root)
    name_entry.pack(pady=10)

    tk.Button(root, text="Generate CV", command=generate_cv).pack(pady=20)

    root.mainloop()


if __name__ == '__main__':
    main()
