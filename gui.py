import tkinter as tk
from tkinter import ttk
import requests  # To communicate with the Flask app


class CVApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CV Generator")
        self.root.geometry("400x300")

        # Create and place labels and entries for CV details
        self.create_form()

        # Create and place the submit button
        self.submit_button = ttk.Button(root, text="Generate CV", command=self.submit_form)
        self.submit_button.pack(pady=20)

    def create_form(self):
        self.name_label = ttk.Label(self.root, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.pack(pady=5)

        self.job_label = ttk.Label(self.root, text="Job Title:")
        self.job_label.pack(pady=5)
        self.job_entry = ttk.Entry(self.root)
        self.job_entry.pack(pady=5)

        # Add more fields as needed...

    def submit_form(self):
        name = self.name_entry.get()
        job = self.job_entry.get()

        # You can either save this data to a file or send it to the Flask server
        response = requests.post('http://localhost:5000/update_cv', json={'name': name, 'job': job})

        if response.status_code == 200:
            print("CV data submitted successfully!")
        else:
            print("Error submitting CV data.")


if __name__ == "__main__":
    root = tk.Tk()
    app = CVApp(root)
    root.mainloop()
