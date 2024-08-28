import json
import os
import tkinter as tk
import urllib.parse
import webbrowser
from tkinter import ttk, messagebox, filedialog


class JobForm:
    def __init__(self, master, job=None):
        self.master = master
        self.job = job
        self.job_frame = tk.Toplevel(master)
        self.job_frame.title("Job Details")
        self.job_frame.geometry('450x450')
        self.responsibility_entries = []
        self.init_widgets()
        if job:
            self.load_job_data(job)

    def init_widgets(self):
        ttk.Label(self.job_frame, text="Job Title:").pack(pady=(20, 5))
        self.job_title_entry = ttk.Entry(self.job_frame)
        self.job_title_entry.pack(pady=(0, 10), fill='x', padx=20)

        ttk.Label(self.job_frame, text="Start Year:").pack(pady=5)
        self.start_year_entry = ttk.Entry(self.job_frame)
        self.start_year_entry.pack(pady=(0, 10), fill='x', padx=20)

        ttk.Label(self.job_frame, text="End Year (optional):").pack(pady=5)
        self.end_year_entry = ttk.Entry(self.job_frame)
        self.end_year_entry.pack(pady=(0, 10), fill='x', padx=20)

        ttk.Label(self.job_frame, text="Responsibilities:").pack(pady=5)
        self.add_responsibility()

        add_resp_button = ttk.Button(self.job_frame, text="Add Responsibility", command=self.add_responsibility)
        add_resp_button.pack(pady=10)

        save_button = ttk.Button(self.job_frame, text="Save Job", command=self.save_job)
        save_button.pack(pady=20)

    def add_responsibility(self):
        resp_frame = ttk.Frame(self.job_frame)
        resp_frame.pack(pady=5, fill='x', padx=20)
        resp_entry = ttk.Entry(resp_frame)
        resp_entry.pack(side=tk.LEFT, fill='x', expand=True)
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
            'end_year': end_year if end_year else '',
            'responsibilities': responsibilities
        }

        if self.job:
            index = job_details.index(self.job)
            job_details[index] = job_data
        else:
            job_details.append(job_data)

        self.job_frame.destroy()
        update_job_list()


class EducationForm:
    def __init__(self, master, education=None):
        self.master = master
        self.education = education
        self.edu_frame = tk.Toplevel(master)
        self.edu_frame.title("Education Details")
        self.edu_frame.geometry('450x350')
        self.init_widgets()
        if education:
            self.load_education_data(education)

    def init_widgets(self):
        ttk.Label(self.edu_frame, text="Institution Name:").pack(pady=(20, 5))
        self.institution_entry = ttk.Entry(self.edu_frame)
        self.institution_entry.pack(pady=(0, 10), fill='x', padx=20)

        ttk.Label(self.edu_frame, text="Start Year:").pack(pady=5)
        self.start_year_entry = ttk.Entry(self.edu_frame)
        self.start_year_entry.pack(pady=(0, 10), fill='x', padx=20)

        ttk.Label(self.edu_frame, text="End Year (optional):").pack(pady=5)
        self.end_year_entry = ttk.Entry(self.edu_frame)
        self.end_year_entry.pack(pady=(0, 10), fill='x', padx=20)

        save_button = ttk.Button(self.edu_frame, text="Save Education", command=self.save_education)
        save_button.pack(pady=20)

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
    job_form.job_frame.grab_set()


def edit_job():
    selected_job_index = job_listbox.curselection()
    if selected_job_index:
        job_index = selected_job_index[0]
        job = job_details[job_index]
        global job_form
        job_form = JobForm(root, job)
        job_form.job_frame.grab_set()
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


def ensure_cv_directory():
    # Ensure the 'cv' directory exists in the project root
    cv_directory = os.path.join(os.getcwd(), 'cv')
    if not os.path.exists(cv_directory):
        os.makedirs(cv_directory)


def save_to_json():
    default_directory = os.path.join(os.getcwd(), 'cv')
    filename = filedialog.asksaveasfilename(
        initialdir=default_directory,
        title="Save JSON File",
        defaultextension=".json",
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
    )

    if filename:
        data = {
            'name': name_entry.get(),
            'job_title': job_title_entry.get(),
            'profile_summary': profile_summary_entry.get("1.0", "end-1c"),
            'location': location_entry.get(),
            'phone': phone_entry.get(),
            'email': email_entry.get(),
            'linkedin': linkedin_entry.get(),
            'languages': languages_entry.get(),
            'jobs': job_details,
            'education': education_details
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo("Success", "Resume data saved successfully!")


def load_from_json(filename=None):
    if filename:
        with open(filename, 'r') as file:
            data = json.load(file)
        populate_fields(data)
        messagebox.showinfo("Success", "Resume data loaded successfully!")


def populate_load_menu(menu):
    # Specify the project root directory
    directory = f'{os.getcwd()}/cv'

    # Clear the existing menu items
    menu.delete(0, tk.END)

    # Add a command to manually load JSON
    menu.add_command(label="Load JSON", command=lambda: load_from_json())

    # Populate the menu with existing files
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            menu.add_command(
                label=filename,
                command=lambda f=filename: load_from_json(os.path.join(directory, f))
            )


def populate_fields(data):
    name_entry.delete(0, tk.END)
    name_entry.insert(0, data.get('name', ''))

    job_title_entry.delete(0, tk.END)
    job_title_entry.insert(0, data.get('job_title', ''))

    profile_summary_entry.delete("1.0", tk.END)
    profile_summary_entry.insert(tk.END, data.get('profile_summary', ''))

    location_entry.delete(0, tk.END)
    location_entry.insert(0, data.get('location', ''))

    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, data.get('phone', ''))

    email_entry.delete(0, tk.END)
    email_entry.insert(0, data.get('email', ''))

    linkedin_entry.delete(0, tk.END)
    linkedin_entry.insert(0, data.get('linkedin', ''))

    languages_entry.delete(0, tk.END)
    languages_entry.insert(0, data.get('languages', ''))

    global job_details, education_details
    job_details = data.get('jobs', [])
    education_details = data.get('education', [])

    update_job_list()
    update_education_list()


def generate_cv():
    name = name_entry.get()
    job_title = job_title_entry.get()
    profile_summary = profile_summary_entry.get("1.0", "end-1c")
    location = location_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    linkedin = linkedin_entry.get()
    languages = languages_entry.get()

    job_params = '||'.join([
        f"{job['title']}~{job['start_year']}~{job['end_year']}~{',,'.join(job['responsibilities'])}"
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
        f'&languages={urllib.parse.quote(languages)}'
    )
    webbrowser.open(url)


def open_linkedin():
    url = linkedin_entry.get()
    if url:
        webbrowser.open(url, new=2)
    else:
        messagebox.showwarning("Warning", "No LinkedIn URL provided.")


def main():
    global root, education_listbox, job_listbox, linkedin_entry, languages_entry, profile_summary_entry, job_title_entry, name_entry, email_entry, phone_entry, location_entry
    root = tk.Tk()
    root.title("Resume Builder")
    root.geometry('600x600')

    # Create a Canvas widget with a Scrollbar
    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the Canvas and Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    style = ttk.Style(root)
    style.configure('TButton', font=('Helvetica', 10), padding=6)
    style.configure('TLabel', font=('Helvetica', 10))
    style.configure('TEntry', padding=6)
    style.configure('TFrame', padding=6)

    job_details = []
    education_details = []

    # Personal Information Frame
    personal_frame = ttk.LabelFrame(scrollable_frame, text="Personal Information")
    personal_frame.pack(fill="both", expand=True, padx=20, pady=10)

    ttk.Label(personal_frame, text="Name:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
    name_entry = ttk.Entry(personal_frame)
    name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    ttk.Label(personal_frame, text="Job Title:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
    job_title_entry = ttk.Entry(personal_frame)
    job_title_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    ttk.Label(personal_frame, text="Profile Summary:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
    profile_summary_entry = tk.Text(personal_frame, height=5, width=40)
    profile_summary_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    ttk.Label(personal_frame, text="Location:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
    location_entry = ttk.Entry(personal_frame)
    location_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

    ttk.Label(personal_frame, text="Phone:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
    phone_entry = ttk.Entry(personal_frame)
    phone_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

    ttk.Label(personal_frame, text="Email:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
    email_entry = ttk.Entry(personal_frame)
    email_entry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

    ttk.Label(personal_frame, text="LinkedIn:").grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)
    linkedin_entry = ttk.Entry(personal_frame)
    linkedin_entry.grid(row=6, column=1, padx=10, pady=5, sticky="ew")

    ttk.Label(personal_frame, text="Languages:").grid(row=7, column=0, sticky=tk.W, padx=10, pady=5)
    languages_entry = ttk.Entry(personal_frame)
    languages_entry.grid(row=7, column=1, padx=10, pady=5, sticky="ew")

    # Job Experience Frame
    jobs_frame = ttk.LabelFrame(scrollable_frame, text="Job Experience")
    jobs_frame.pack(fill="both", expand=True, padx=20, pady=10)

    job_listbox = tk.Listbox(jobs_frame, height=6)
    job_listbox.pack(side=tk.LEFT, fill="both", expand=True, padx=10, pady=5)

    job_scrollbar = ttk.Scrollbar(jobs_frame, orient="vertical", command=job_listbox.yview)
    job_listbox.configure(yscrollcommand=job_scrollbar.set)
    job_scrollbar.pack(side=tk.LEFT, fill="y")

    jobs_button_frame = ttk.Frame(jobs_frame)
    jobs_button_frame.pack(side=tk.LEFT, fill="both", padx=10)

    add_job_button = ttk.Button(jobs_button_frame, text="Add Job", command=add_job)
    add_job_button.pack(fill="x", pady=5)

    edit_job_button = ttk.Button(jobs_button_frame, text="Edit Job", command=edit_job)
    edit_job_button.pack(fill="x", pady=5)

    delete_job_button = ttk.Button(jobs_button_frame, text="Delete Job", command=delete_job)
    delete_job_button.pack(fill="x", pady=5)

    # Education Frame
    education_frame = ttk.LabelFrame(scrollable_frame, text="Education")
    education_frame.pack(fill="both", expand=True, padx=20, pady=10)

    education_listbox = tk.Listbox(education_frame, height=6)
    education_listbox.pack(side=tk.LEFT, fill="both", expand=True, padx=10, pady=5)

    education_scrollbar = ttk.Scrollbar(education_frame, orient="vertical", command=education_listbox.yview)
    education_listbox.configure(yscrollcommand=education_scrollbar.set)
    education_scrollbar.pack(side=tk.LEFT, fill="y")

    education_button_frame = ttk.Frame(education_frame)
    education_button_frame.pack(side=tk.LEFT, fill="both", padx=10)

    add_education_button = ttk.Button(education_button_frame, text="Add Education", command=add_education)
    add_education_button.pack(fill="x", pady=5)

    edit_education_button = ttk.Button(education_button_frame, text="Edit Education", command=edit_education)
    edit_education_button.pack(fill="x", pady=5)

    delete_education_button = ttk.Button(education_button_frame, text="Delete Education", command=delete_education)
    delete_education_button.pack(fill="x", pady=5)

    # Buttons Frame
    buttons_frame = ttk.Frame(scrollable_frame)
    buttons_frame.pack(fill="both", expand=True, padx=20, pady=10)

    save_button = ttk.Button(buttons_frame, text="Save to JSON", command=save_to_json)
    save_button.pack(side=tk.LEFT, padx=10, pady=10, expand=True)

    load_button = ttk.Menubutton(buttons_frame, text="Load JSON")
    load_button.pack(side=tk.LEFT, padx=10, pady=10, expand=True)
    load_menu = tk.Menu(load_button, tearoff=0)
    load_button["menu"] = load_menu
    load_menu.add_command(label="Load JSON", command=load_from_json)

    ensure_cv_directory()
    populate_load_menu(load_menu)

    generate_cv_button = ttk.Button(buttons_frame, text="Generate CV", command=generate_cv)
    generate_cv_button.pack(side=tk.LEFT, padx=10, pady=10, expand=True)

    open_linkedin_button = ttk.Button(buttons_frame, text="Open LinkedIn", command=open_linkedin)
    open_linkedin_button.pack(side=tk.LEFT, padx=10, pady=10, expand=True)

    root.mainloop()
