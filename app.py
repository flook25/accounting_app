import tkinter as tk
from tkinter import ttk

class PortfolioApp:
    def __init__(self, master):
        self.master = master
        master.title("My Portfolio")
        master.geometry("900x650")
        master.minsize(800, 600)

        # --- Color and Font Definitions ---
        self.COLOR_BG = "#2E2E2E"
        self.COLOR_FRAME_BG = "#3A3A3A"
        self.COLOR_TEXT = "#F0F0F0"
        self.COLOR_ACCENT = "#00BFFF"
        self.FONT_NORMAL = ("Segoe UI", 12)
        self.FONT_BOLD = ("Segoe UI", 12, "bold")
        self.FONT_HEADER = ("Segoe UI", 24, "bold")

        master.configure(bg=self.COLOR_BG)

        # --- No images/icons, just use None placeholders ---
        self.icons = {
            "home": None,
            "projects": None,
            "skills": None,
            "contact": None
        }

        # --- Configure ttk Styles ---
        self._configure_styles()

        # --- Configure Grid Layout ---
        master.columnconfigure(0, weight=0)
        master.columnconfigure(1, weight=1)
        master.rowconfigure(0, weight=1)

        # --- Sidebar Frame (Navigation) ---
        self.sidebar_frame = ttk.Frame(master, style="Nav.TFrame")
        self.sidebar_frame.grid(row=0, column=0, sticky="nsw")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        ttk.Label(self.sidebar_frame, text="Navigation", font=("Segoe UI", 16, "bold"),
                  style="NavHeader.TLabel").pack(pady=(20, 15), padx=10)

        self.create_nav_button("Home", None, self.show_home_page)
        self.create_nav_button("Projects", None, self.show_projects_page)
        self.create_nav_button("Skills", None, self.show_skills_page)
        self.create_nav_button("Contact", None, self.show_contact_page)

        exit_button = ttk.Button(self.sidebar_frame, text="Exit", command=master.quit, style="Nav.TButton")
        exit_button.pack(side=tk.BOTTOM, fill='x', padx=15, pady=20)

        # --- Main Content Frame ---
        self.content_frame = ttk.Frame(master, style="Content.TFrame")
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.pages = {}
        self.current_page = None

        self.create_pages()
        self.show_home_page()

    def _configure_styles(self):
        style = ttk.Style(self.master)
        style.theme_use("clam")

        style.configure(".",
                        background=self.COLOR_BG,
                        foreground=self.COLOR_TEXT,
                        font=self.FONT_NORMAL)

        style.configure("Nav.TFrame", background=self.COLOR_FRAME_BG)
        style.configure("Content.TFrame", background=self.COLOR_BG)

        style.configure("TLabel", background=self.COLOR_BG, foreground=self.COLOR_TEXT)
        style.configure("Header.TLabel", font=self.FONT_HEADER, padding=(0, 10, 0, 10))
        style.configure("NavHeader.TLabel", font=("Segoe UI", 16, "bold"),
                        background=self.COLOR_FRAME_BG, foreground=self.COLOR_ACCENT)

        style.configure("Nav.TButton",
                        font=self.FONT_BOLD,
                        background=self.COLOR_FRAME_BG,
                        foreground=self.COLOR_TEXT,
                        borderwidth=0,
                        anchor="w",
                        padding=(15, 10))

        style.map("Nav.TButton",
                  background=[("active", self.COLOR_ACCENT)],
                  foreground=[("active", self.COLOR_FRAME_BG)])

    def create_nav_button(self, text, icon, command):
        # icon is ignored, only text is used
        button = ttk.Button(self.sidebar_frame, text=text,
                            command=command, style="Nav.TButton", compound="left")
        button.pack(fill='x', padx=15, pady=2)
        return button

    def create_pages(self):
        for page_name in ["home", "projects", "skills", "contact"]:
            frame = ttk.Frame(self.content_frame, style="Content.TFrame")
            frame.grid(row=0, column=0, sticky="nsew")
            self.pages[page_name] = frame

        home_page = self.pages["home"]
        ttk.Label(home_page, text="Welcome to My Portfolio!", style="Header.TLabel").pack(pady=20, anchor="w")
        ttk.Label(home_page, text="This application demonstrates a modern, multi-page GUI using Python and Tkinter.",
                  wraplength=500, justify=tk.LEFT, font=self.FONT_NORMAL).pack(pady=10, anchor="w")
        ttk.Label(home_page, text="Navigate using the menu on the left.",
                  font=self.FONT_BOLD).pack(pady=20, anchor="w")

        projects_page = self.pages["projects"]
        ttk.Label(projects_page, text="My Projects", style="Header.TLabel").pack(pady=20, anchor="w")
        project_text = (
            "•  Project Alpha: A data analysis tool built with Pandas for processing large datasets.\n\n"
            "•  Project Beta: A web scraping script using BeautifulSoup and Requests to gather market data.\n\n"
            "•  Project Gamma: This very GUI portfolio, showcasing modern Tkinter styling techniques."
        )
        ttk.Label(projects_page, text=project_text, justify=tk.LEFT, font=self.FONT_NORMAL,
                  wraplength=500).pack(pady=10, padx=20, anchor="w")

        skills_page = self.pages["skills"]
        ttk.Label(skills_page, text="Technical Skills", style="Header.TLabel").pack(pady=20, anchor="w")
        skills_text = (
            "Programming Languages:\n"
            "    - Python (Proficient)\n"
            "    - SQL (Intermediate)\n\n"
            "Python Libraries:\n"
            "    - Tkinter / ttk\n"
            "    - Pandas & NumPy\n"
            "    - Matplotlib & Seaborn\n\n"
            "Tools & Technologies:\n"
            "    - Git & GitHub\n"
            "    - Jupyter Notebooks"
        )
        ttk.Label(skills_page, text=skills_text, justify=tk.LEFT,
                  font=("Courier New", 12)).pack(pady=10, padx=20, anchor="w")

        contact_page = self.pages["contact"]
        ttk.Label(contact_page, text="Contact Me", style="Header.TLabel").pack(pady=20, anchor="w")
        contact_text = (
            "You can reach me via the following channels:\n\n"
            "Email: your.email@example.com\n"
            "LinkedIn: linkedin.com/in/yourprofile\n"
            "GitHub: github.com/yourusername"
        )
        ttk.Label(contact_page, text=contact_text, justify=tk.LEFT,
                  font=self.FONT_NORMAL).pack(pady=10, padx=20, anchor="w")

    def show_page(self, page_name):
        if self.current_page:
            self.current_page.grid_remove()
        self.current_page = self.pages[page_name]
        self.current_page.grid()

    def show_home_page(self):
        self.show_page("home")

    def show_projects_page(self):
        self.show_page("projects")

    def show_skills_page(self):
        self.show_page("skills")

    def show_contact_page(self):
        self.show_page("contact")

# --- Main Application Execution ---
if __name__ == "__main__":
    root = tk.Tk()
    app = PortfolioApp(root)
    root.mainloop()
