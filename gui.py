import tkinter as tk
import webbrowser
from tkinter import StringVar, OptionMenu, messagebox, filedialog, simpledialog
import json
import os


def add_job():
    job_title = simpledialog.askstring("Job Title", "Enter job title:")
    start_year = simpledialog.askstring("Start Year", "Enter start year:")
    end_year = simpledialog.askstring("End Year", "Enter end year:")

    if job_title and start_year and end_year:
        job_details.append({
            'title': job_title,
            'start_year': start_year,
            'end_year': end_year,
            'responsibilities': []  # Placeholder for responsibilities
        })
        update_job_list()


def update_job_list():
    job_listbox.delete(0, tk.END)
    for job in job_details:
        job_text = f"{job.get('title', 'No Title')} ({job.get('start_year', 'N/A')} - {job.get('end_year', 'N/A')})"
        job_listbox.insert(tk.END, job_text)


def save_to_json():
    filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if filename:
        data = {
            'name': name_entry.get(),
            'location': location_entry.get(),
            'phone': phone_entry.get(),
            'email': email_entry.get(),
            'linkedin': linkedin_entry.get(),
            'profile_summary': profile_summary_entry.get(),
            'jobs': job_details
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo("Save", f"Data saved successfully to {filename}!")


def load_selected_file(filename):
    if filename:
        try:
            with open(filename, 'r') as file:
                data = json.load(file)

            name_entry.delete(0, tk.END)
            name_entry.insert(0, data.get('name', ''))

            location_entry.delete(0, tk.END)
            location_entry.insert(0, data.get('location', ''))

            phone_entry.delete(0, tk.END)
            phone_entry.insert(0, data.get('phone', ''))

            email_entry.delete(0, tk.END)
            email_entry.insert(0, data.get('email', ''))

            linkedin_entry.delete(0, tk.END)
            linkedin_entry.insert(0, data.get('linkedin', ''))

            profile_summary_entry.delete(0, tk.END)
            profile_summary_entry.insert(0, data.get('profile_summary', ''))

            global job_details
            job_details = data.get('jobs', [])
            update_job_list()

            messagebox.showinfo("Load", f"Data loaded successfully from {filename}!")
        except FileNotFoundError:
            messagebox.showwarning("Load", "File not found.")
        except json.JSONDecodeError:
            messagebox.showwarning("Load", "Error decoding JSON file.")


def update_file_list():
    file_menu['menu'].delete(0, 'end')
    files = [f for f in os.listdir() if f.endswith('.json')]
    if not files:
        file_menu['menu'].add_command(label="No files available", command=lambda: None)
    else:
        for file in files:
            file_menu['menu'].add_command(label=file, command=lambda f=file: load_selected_file(f))


def main():
    global root, job_details, job_listbox, file_var, file_menu

    job_details = []

    root = tk.Tk()
    root.title("CV Generator")

    file_var = StringVar(root)
    file_var.set("Select a file")  # Default value

    file_menu = OptionMenu(root, file_var, *get_available_files(), command=lambda x: load_selected_file(file_var.get()))
    file_menu.pack(pady=5)

    tk.Label(root, text="Enter Your Name:").pack(pady=5)
    global name_entry
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)

    tk.Label(root, text="Location:").pack(pady=5)
    global location_entry
    location_entry = tk.Entry(root)
    location_entry.pack(pady=5)

    tk.Label(root, text="Phone Number:").pack(pady=5)
    global phone_entry
    phone_entry = tk.Entry(root)
    phone_entry.pack(pady=5)

    tk.Label(root, text="Email Address:").pack(pady=5)
    global email_entry
    email_entry = tk.Entry(root)
    email_entry.pack(pady=5)

    tk.Label(root, text="LinkedIn URL:").pack(pady=5)
    global linkedin_entry
    linkedin_entry = tk.Entry(root)
    linkedin_entry.pack(pady=5)

    tk.Label(root, text="Profile Summary:").pack(pady=5)
    global profile_summary_entry
    profile_summary_entry = tk.Entry(root, width=50)
    profile_summary_entry.pack(pady=5)

    tk.Button(root, text="Add Job", command=add_job).pack(pady=5)

    tk.Label(root, text="Jobs:").pack(pady=5)
    job_listbox = tk.Listbox(root, width=80, height=10)
    job_listbox.pack(pady=5)

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    job_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=job_listbox.yview)

    tk.Button(root, text="Generate CV", command=generate_cv).pack(pady=5)
    tk.Button(root, text="Save Data", command=save_to_json).pack(pady=5)

    update_file_list()

    root.mainloop()


def get_available_files():
    # List all JSON files in the current directory
    return [f for f in os.listdir('.') if f.endswith('.json')]


def generate_cv():
    name = name_entry.get()
    location = location_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    linkedin = linkedin_entry.get()
    profile_summary = profile_summary_entry.get()

    job_params = '|'.join([
        f"{job['title']}|{job['start_year']}|{job['end_year']}|{','.join(job['responsibilities'])}"
        for job in job_details
    ])

    url = (f'http://127.0.0.1:5000/generate_cv?name={name}&location={location}&phone={phone}&email={email}'
           f'&linkedin={linkedin}&profile_summary={profile_summary}&jobs={job_params}')
    webbrowser.open(url)


if __name__ == '__main__':
    main()
