import json
import os
import tkinter as tk
import webbrowser
from tkinter import messagebox, filedialog
import urllib.parse


class JobForm:
    def __init__(self, master, job=None):
        self.master = master
        self.job = job
        self.job_frame = tk.Toplevel(master)
        self.job_frame.title("Job Details")
        self.responsibility_entries = []
        self.init_widgets()
        if job:
            self.load_job_data(job)

    def init_widgets(self):
        tk.Label(self.job_frame, text="Job Title:").pack(pady=5)
        self.job_title_entry = tk.Entry(self.job_frame)
        self.job_title_entry.pack(pady=5)

        tk.Label(self.job_frame, text="Start Year:").pack(pady=5)
        self.start_year_entry = tk.Entry(self.job_frame)
        self.start_year_entry.pack(pady=5)

        tk.Label(self.job_frame, text="End Year (optional):").pack(pady=5)
        self.end_year_entry = tk.Entry(self.job_frame)
        self.end_year_entry.pack(pady=5)

        tk.Label(self.job_frame, text="Responsibilities:").pack(pady=5)
        self.add_responsibility()

        tk.Button(self.job_frame, text="Add Responsibility", command=self.add_responsibility).pack(pady=5)
        tk.Button(self.job_frame, text="Save Job", command=self.save_job).pack(pady=5)

    def add_responsibility(self):
        resp_label = tk.Label(self.job_frame, text="Responsibility:")
        resp_label.pack(pady=5)
        resp_entry = tk.Entry(self.job_frame)
        resp_entry.pack(pady=5)
        self.responsibility_entries.append(resp_entry)

    def load_job_data(self, job):
        self.job_title_entry.insert(0, job['title'])
        self.start_year_entry.insert(0, job['start_year'])
        self.end_year_entry.insert(0, job.get('end_year', ''))
        for resp in job.get('responsibilities', []):
            self.add_responsibility()
            self.responsibility_entries[-1].insert(0, resp)

    def save_job(self):
        title = self.job_title_entry.get()
        start_year = self.start_year_entry.get()
        end_year = self.end_year_entry.get()

        if not title or not start_year:
            messagebox.showwarning("Warning", "Please fill in the Job Title and Start Year.")
            return

        responsibilities = [entry.get() for entry in self.responsibility_entries if entry.get()]

        job_data = {
            'title': title,
            'start_year': start_year,
            'end_year': end_year if end_year else '',  # Handle optional end year
            'responsibilities': responsibilities
        }

        if self.job:
            # Edit existing job
            index = job_details.index(self.job)
            job_details[index] = job_data
        else:
            # Add new job
            job_details.append(job_data)

        self.job_frame.destroy()
        update_job_list()


class EducationForm:
    def __init__(self, master, education=None):
        self.master = master
        self.education = education
        self.edu_frame = tk.Toplevel(master)
        self.edu_frame.title("Education Details")
        self.init_widgets()
        if education:
            self.load_education_data(education)

    def init_widgets(self):
        tk.Label(self.edu_frame, text="Institution Name:").pack(pady=5)
        self.institution_entry = tk.Entry(self.edu_frame)
        self.institution_entry.pack(pady=5)

        tk.Label(self.edu_frame, text="Start Year:").pack(pady=5)
        self.start_year_entry = tk.Entry(self.edu_frame)
        self.start_year_entry.pack(pady=5)

        tk.Label(self.edu_frame, text="End Year (optional):").pack(pady=5)
        self.end_year_entry = tk.Entry(self.edu_frame)
        self.end_year_entry.pack(pady=5)

        tk.Button(self.edu_frame, text="Save Education", command=self.save_education).pack(pady=5)

    def load_education_data(self, education):
        self.institution_entry.insert(0, education['institution'])
        self.start_year_entry.insert(0, education['start_year'])
        self.end_year_entry.insert(0, education.get('end_year', ''))

    def save_education(self):
        institution = self.institution_entry.get()
        start_year = self.start_year_entry.get()
        end_year = self.end_year_entry.get()

        if not institution or not start_year:
            messagebox.showwarning("Warning", "Please fill in the Institution Name and Start Year.")
            return

        education_data = {
            'institution': institution,
            'start_year': start_year,
            'end_year': end_year if end_year else ''
        }

        if self.education:
            index = education_details.index(self.education)
            education_details[index] = education_data
        else:
            education_details.append(education_data)

        self.edu_frame.destroy()
        update_education_list()


def add_job():
    global job_form
    job_form = JobForm(root)
    job_form.job_frame.grab_set()  # Make the job form modal


def edit_job():
    selected_job_index = job_listbox.curselection()
    if selected_job_index:
        job_index = selected_job_index[0]
        job = job_details[job_index]
        global job_form
        job_form = JobForm(root, job)
        job_form.job_frame.grab_set()  # Make the job form modal
    else:
        messagebox.showwarning("Warning", "Select a job to edit.")


def delete_job():
    selected_job_index = job_listbox.curselection()
    if selected_job_index:
        job_index = selected_job_index[0]
        del job_details[job_index]
        update_job_list()
    else:
        messagebox.showwarning("Warning", "Select a job to delete.")


def update_job_list():
    job_listbox.delete(0, tk.END)
    for job in job_details:
        end_year = job.get('end_year', 'N/A')
        job_text = f"{job.get('title', 'No Title')} ({job.get('start_year', 'N/A')} - {end_year})"
        job_listbox.insert(tk.END, job_text)


def add_education():
    global education_form
    education_form = EducationForm(root)
    education_form.edu_frame.grab_set()


def edit_education():
    selected_education_index = education_listbox.curselection()
    if selected_education_index:
        edu_index = selected_education_index[0]
        education = education_details[edu_index]
        global education_form
        education_form = EducationForm(root, education)
        education_form.edu_frame.grab_set()
    else:
        messagebox.showwarning("Warning", "Select an education entry to edit.")


def delete_education():
    selected_education_index = education_listbox.curselection()
    if selected_education_index:
        edu_index = selected_education_index[0]
        del education_details[edu_index]
        update_education_list()
    else:
        messagebox.showwarning("Warning", "Select an education entry to delete.")


def update_education_list():
    education_listbox.delete(0, tk.END)
    for edu in education_details:
        end_year = edu.get('end_year', 'N/A')
        edu_text = f"{edu.get('institution', 'No Institution')} ({edu.get('start_year', 'N/A')} - {end_year})"
        education_listbox.insert(tk.END, edu_text)


def save_to_json():
    filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if filename:
        data = {
            'name': name_entry.get(),
            'job_title': job_title_entry.get(),
            'profile_summary': profile_summary_entry.get("1.0", "end-1c"),
            'location': location_entry.get(),
            'phone': phone_entry.get(),
            'email': email_entry.get(),
            'linkedin': linkedin_entry.get(),
            'jobs': job_details,
            'education': education_details
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

            job_title_entry.delete(0, tk.END)
            job_title_entry.insert(0, data.get('job_title', ''))

            profile_summary_entry.delete('1.0', tk.END)
            profile_summary_entry.insert('1.0', data.get('profile_summary', ''))

            location_entry.delete(0, tk.END)
            location_entry.insert(0, data.get('location', ''))

            phone_entry.delete(0, tk.END)
            phone_entry.insert(0, data.get('phone', ''))

            email_entry.delete(0, tk.END)
            email_entry.insert(0, data.get('email', ''))

            linkedin_entry.delete(0, tk.END)
            linkedin_entry.insert(0, data.get('linkedin', ''))

            global job_details
            job_details = data.get('jobs', [])
            update_job_list()

            global education_details
            education_details = data.get('education', [])
            update_education_list()

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
    global root, job_details, job_listbox, education_details, education_listbox, file_var, file_menu

    job_details = []
    education_details = []

    root = tk.Tk()
    root.title("CV Generator")

    file_var = tk.StringVar(root)
    file_var.set("Select a file")  # Default value

    file_menu = tk.OptionMenu(root, file_var, *get_available_files(),
                              command=lambda x: load_selected_file(file_var.get()))
    file_menu.pack(pady=5)

    tk.Label(root, text="Enter Your Name:").pack(pady=5)
    global name_entry
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)

    tk.Label(root, text="Job Title::").pack(pady=5)
    global job_title_entry
    job_title_entry = tk.Entry(root)
    job_title_entry.pack(pady=5)

    tk.Label(root, text="Profile Summary:").pack(pady=5)
    global profile_summary_entry
    profile_summary_entry = tk.Text(root, height=5, width=50)  # Adjust height and width as needed
    profile_summary_entry.pack(pady=5)

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

    tk.Label(root, text="Jobs:").pack(pady=5)
    job_listbox = tk.Listbox(root, width=80, height=10)
    job_listbox.pack(pady=5)

    tk.Button(root, text="Add Job", command=add_job).pack(pady=5)
    tk.Button(root, text="Edit Job", command=edit_job).pack(pady=5)
    tk.Button(root, text="Delete Job", command=delete_job).pack(pady=5)

    tk.Label(root, text="Education:").pack(pady=5)
    education_listbox = tk.Listbox(root, width=80, height=10)
    education_listbox.pack(pady=5)

    tk.Button(root, text="Add Education", command=add_education).pack(pady=5)
    tk.Button(root, text="Edit Education", command=edit_education).pack(pady=5)
    tk.Button(root, text="Delete Education", command=delete_education).pack(pady=5)

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    job_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=job_listbox.yview)

    tk.Button(root, text="Generate CV", command=generate_cv).pack(pady=5)
    tk.Button(root, text="Save Data", command=save_to_json).pack(pady=5)

    update_file_list()

    root.mainloop()


def get_available_files():
    return [f for f in os.listdir('.') if f.endswith('.json')]


def generate_cv():
    name = name_entry.get()
    job_title = job_title_entry.get()
    profile_summary = profile_summary_entry.get("1.0", "end-1c")
    location = location_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    linkedin = linkedin_entry.get()

    job_params = '||'.join([
        f"{job['title']}~{job['start_year']}~{job['end_year']}~{','.join(job['responsibilities'])}"
        for job in job_details
    ])

    education_params = '||'.join([
        f"{education['institution']}~{education['start_year']}~{education['end_year']}"
        for education in education_details
    ])

    url = (
        f'http://127.0.0.1:5000/generate_cv?name={urllib.parse.quote(name)}'
        f'&location={urllib.parse.quote(location)}&phone={urllib.parse.quote(phone)}'
        f'&email={urllib.parse.quote(email)}&linkedin={urllib.parse.quote(linkedin)}'
        f'&profile_summary={urllib.parse.quote(profile_summary)}'
        f'&jobs={urllib.parse.quote(job_params)}&job_title={urllib.parse.quote(job_title)}'
        f'&educations={urllib.parse.quote(education_params)}'
    )
    webbrowser.open(url)


if __name__ == '__main__':
    main()
