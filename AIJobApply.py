# ==========================================
# AI JOB APPLICATION ASSISTANT
# Ridge Francis Edition
# Python 3 + Tkinter GUI
# ==========================================

# FEATURES
# - Upload Resume
# - Select Job Titles (Option List)
# - Select Locations (Option List)
# - Select Job Boards (Option List)
# - Choose Apply Mode
# - Daily 10 Job Limit
# - LinkedIn Easy Apply Support
# - Application Tracking
# - Selenium Automation Ready
# ==========================================

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import json
import os

CONFIG_FILE = "config.json"

class JobBotGUI:

# ==========================================
# DASHBOARD ANALYTICS
# ==========================================

    def create_dashboard(self):

        dashboard_frame = tk.LabelFrame(
            self.root,
            text="Dashboard Analytics",
            padx=10,
            pady=10
        )

        dashboard_frame.pack(fill="both", padx=20, pady=20)

        # ======================================
        # SAMPLE ANALYTICS DATA
        # ======================================

        jobs_found = 52
        applications_sent = 18
        interviews = 3
        rejected = 7
        pending = 8

        success_rate = round(
            (interviews / applications_sent) * 100,
            2
        )

        # ======================================
        # STAT CARDS
        # ======================================

        stats_frame = tk.Frame(dashboard_frame)
        stats_frame.pack(fill="x")

    def create_stat_card(parent, title, value):

        card = tk.Frame(
            parent,
            bg="#f2f2f2",
            padx=15,
            pady=15,
            relief="ridge",
            bd=2
        )

        card.pack(side="left", padx=10, pady=10)

        tk.Label(
            card,
            text=title,
            font=("Arial", 12, "bold"),
            bg="#f2f2f2"
        ).pack()

        tk.Label(
            card,
            text=str(value),
            font=("Arial", 18, "bold"),
            bg="#f2f2f2",
            fg="blue"
        ).pack()

        create_stat_card(stats_frame, "Jobs Found", jobs_found)
        create_stat_card(stats_frame, "Applications", applications_sent)
        create_stat_card(stats_frame, "Interviews", interviews)
        create_stat_card(stats_frame, "Rejected", rejected)
        create_stat_card(stats_frame, "Success %", f"{success_rate}%")

        # ======================================
        # DAILY LIMIT PROGRESS BAR
        # ======================================

        progress_frame = tk.Frame(dashboard_frame)
        progress_frame.pack(fill="x", pady=20)

        tk.Label(
            progress_frame,
            text="Daily Application Progress",
            font=("Arial", 12, "bold")
        ).pack(anchor="w")

        progress = ttk.Progressbar(
            progress_frame,
            orient="horizontal",
            length=500,
            mode="determinate"
        )

        progress.pack(pady=10)

        daily_limit = self.daily_limit.get()
        progress["maximum"] = daily_limit
        progress["value"] = applications_sent

        # ======================================
        # PIE CHART
        # ======================================

        chart_frame = tk.Frame(dashboard_frame)
        chart_frame.pack(fill="both", expand=True)

        fig = plt.Figure(figsize=(5, 4), dpi=100)

        ax = fig.add_subplot(111)

        labels = ["Interviews", "Rejected", "Pending"]
        sizes = [interviews, rejected, pending]

        ax.pie(
            sizes,
            labels=labels,
            autopct='%1.1f%%'
        )

        ax.set_title("Application Outcomes")

        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()

        canvas.get_tk_widget().pack(fill="both", expand=True)
        
    def __init__(self, root):
        self.root = root
        self.resume_path = ""

        # =========================
        # TITLE
        # =========================
        title = tk.Label(
            root,
            text="AI Job Application Assistant",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        # =========================
        # RESUME SECTION
        # =========================
        resume_frame = tk.LabelFrame(root, text="1. Upload Resume")
        resume_frame.pack(fill="x", padx=20, pady=10)

        self.resume_label = tk.Label(
            resume_frame,
            text="No Resume Uploaded"
        )
        self.resume_label.pack(pady=5)

        upload_btn = tk.Button(
            resume_frame,
            text="Upload Resume",
            command=self.upload_resume
        )
        upload_btn.pack(pady=5)

        # =========================
        # JOB TITLES
        # =========================
        title_frame = tk.LabelFrame(root, text="2. Select Job Titles")
        title_frame.pack(fill="x", padx=20, pady=10)

        self.job_titles = {
            "Technical Support Specialist": tk.BooleanVar(),
            "Help Desk Analyst": tk.BooleanVar(),
            "IT Support Technician": tk.BooleanVar(),
            "Cloud Support Associate": tk.BooleanVar(),
            "AWS Support Associate": tk.BooleanVar(),
            "Junior DevOps Engineer": tk.BooleanVar(),
            "Software Support Specialist": tk.BooleanVar(),
            "Remote Technical Analyst": tk.BooleanVar(),
        }

        for title, var in self.job_titles.items():
            tk.Checkbutton(
                title_frame,
                text=title,
                variable=var
            ).pack(anchor="w")

        # =========================
        # LOCATIONS
        # =========================
        location_frame = tk.LabelFrame(root, text="3. Preferred Locations")
        location_frame.pack(fill="x", padx=20, pady=10)

        self.locations = {
            "Remote Only": tk.BooleanVar(),
            "United States": tk.BooleanVar(),
            "Florida": tk.BooleanVar(),
            "Maryland": tk.BooleanVar(),
            "Virginia": tk.BooleanVar(),
            "Washington DC": tk.BooleanVar(),
        }

        for location, var in self.locations.items():
            tk.Checkbutton(
                location_frame,
                text=location,
                variable=var
            ).pack(anchor="w")

        # =========================
        # JOB BOARDS
        # =========================
        board_frame = tk.LabelFrame(root, text="4. Select Job Boards")
        board_frame.pack(fill="x", padx=20, pady=10)

        self.job_boards = {
            "LinkedIn": tk.BooleanVar(),
            "Indeed": tk.BooleanVar(),
            "Glassdoor": tk.BooleanVar(),
            "ZipRecruiter": tk.BooleanVar(),
        }

        for board, var in self.job_boards.items():
            tk.Checkbutton(
                board_frame,
                text=board,
                variable=var
            ).pack(anchor="w")

        # =========================
        # APPLY MODE
        # =========================
        mode_frame = tk.LabelFrame(root, text="5. Apply Mode")
        mode_frame.pack(fill="x", padx=20, pady=10)

        self.apply_mode = tk.StringVar(value="Review Before Submit")

        ttk.Radiobutton(
            mode_frame,
            text="Review Before Submit (Recommended)",
            variable=self.apply_mode,
            value="Review Before Submit"
        ).pack(anchor="w")

        ttk.Radiobutton(
            mode_frame,
            text="Fully Automatic",
            variable=self.apply_mode,
            value="Fully Automatic"
        ).pack(anchor="w")

        # =========================
        # DAILY LIMIT
        # =========================
        limit_frame = tk.LabelFrame(root, text="Daily Application Limit")
        limit_frame.pack(fill="x", padx=20, pady=10)

        self.daily_limit = tk.IntVar(value=10)

        limit_spin = tk.Spinbox(
            limit_frame,
            from_=1,
            to=50,
            textvariable=self.daily_limit
        )
        limit_spin.pack(pady=5)

        # =========================
        # SAVE BUTTON
        # =========================
        save_btn = tk.Button(
            root,
            text="Save Configuration",
            bg="green",
            fg="white",
            font=("Arial", 12, "bold"),
            command=self.save_config
        )
        save_btn.pack(pady=20)

        # =========================
        # START BUTTON
        # =========================
        start_btn = tk.Button(
            root,
            text="Start Job Bot",
            bg="blue",
            fg="white",
            font=("Arial", 14, "bold"),
            command=self.start_bot
        )
        start_btn.pack(pady=10)

    # ==================================
    # UPLOAD RESUME
    # ==================================
    def upload_resume(self):
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("PDF Files", "*.pdf"),
                ("Word Files", "*.docx"),
                ("Image Files", "*.jpg *.png")
            ]
        )

        if file_path:
            self.resume_path = file_path
            self.resume_label.config(text=os.path.basename(file_path))

    # ==================================
    # SAVE CONFIG
    # ==================================
    def save_config(self):

        selected_titles = [
            title for title, var in self.job_titles.items()
            if var.get()
        ]

        selected_locations = [
            location for location, var in self.locations.items()
            if var.get()
        ]

        selected_boards = [
            board for board, var in self.job_boards.items()
            if var.get()
        ]

        config = {
            "resume": self.resume_path,
            "job_titles": selected_titles,
            "locations": selected_locations,
            "job_boards": selected_boards,
            "apply_mode": self.apply_mode.get(),
            "daily_limit": self.daily_limit.get()
        }

        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)

        messagebox.showinfo(
            "Success",
            "Configuration Saved Successfully!"
        )

    # ==================================
    # START BOT
    # ==================================
    def start_bot(self):

        messagebox.showinfo(
            "Starting",
            "Launching Job Application Bot..."
        )

        print("Bot Started")
        print("This is where Selenium/Playwright automation begins.")

        # ==================================
        # FUTURE IMPLEMENTATION
        # ==================================
        # 1. Login to LinkedIn
        # 2. Search jobs
        # 3. Apply filters
        # 4. Open Easy Apply jobs
        # 5. Autofill forms
        # 6. Upload resume
        # 7. Submit or ask for review
        # 8. Track applications
        # ==================================

# ==========================================
# RUN APPLICATION
# ==========================================

# ==========================================
# RUN APPLICATION WITH SCROLLABLE WINDOW
# ==========================================

if __name__ == "__main__":

    root = tk.Tk()
    root.title("AI Job Application Assistant")
    root.geometry("750x700")

    # ======================================
    # CREATE SCROLLABLE CANVAS
    # ======================================

    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=1)

    canvas = tk.Canvas(main_frame)
    canvas.pack(side="left", fill="both", expand=1)

    scrollbar = ttk.Scrollbar(
        main_frame,
        orient="vertical",
        command=canvas.yview
    )

    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    # ======================================
    # SECOND FRAME INSIDE CANVAS
    # ======================================

    second_frame = tk.Frame(canvas)

    canvas.create_window(
        (0, 0),
        window=second_frame,
        anchor="nw"
    )

    # ======================================
    # MOUSE WHEEL SUPPORT
    # ======================================

    def _on_mousewheel(event):
        canvas.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units"
        )

    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    # ======================================
    # LOAD APPLICATION INTO FRAME
    # ======================================

    app = JobBotGUI(second_frame)

    root.mainloop()