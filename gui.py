import tkinter as tk
import webbrowser


def generate_cv():
    # Collect all inputs
    name = name_entry.get()
    job_title = job_title_entry.get()
    location = location_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    linkedin = linkedin_entry.get()
    profile_summary = profile_summary_entry.get()
    jobs = job_entries.get("1.0", tk.END).strip()  # Collect jobs and their descriptions from a text widget

    # Construct URL with all parameters
    url = (f'http://127.0.0.1:5000/generate_cv?name={name}&job_title={job_title}&location={location}'
           f'&phone={phone}&email={email}&linkedin={linkedin}&profile_summary={profile_summary}&jobs={jobs}')
    webbrowser.open(url)


def main():
    root = tk.Tk()
    root.title("CV Generator")

    # Define and pack labels and entry widgets
    tk.Label(root, text="Enter Your Name:").pack(pady=5)
    global name_entry
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)

    tk.Label(root, text="Enter Job Title:").pack(pady=5)
    global job_title_entry
    job_title_entry = tk.Entry(root)
    job_title_entry.pack(pady=5)

    tk.Label(root, text="Enter Location:").pack(pady=5)
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

    tk.Label(root, text="Job Descriptions (each job on a new line):").pack(pady=5)
    global job_entries
    job_entries = tk.Text(root, height=10, width=50)
    job_entries.pack(pady=5)

    tk.Button(root, text="Generate CV", command=generate_cv).pack(pady=20)

    root.mainloop()


if __name__ == '__main__':
    main()
