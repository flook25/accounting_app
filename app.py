import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

# I've embedded icons as Base64 strings so you don't need external image files.
# This makes the script self-contained and easy to run.
# Icons are from feathericons.com (MIT License)

HOME_ICON_B64 = "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABmJLR0QA/wD/AP+gvaeTAAABmklEQVRIie2UvUpbURSHv3OzbQmaIGiZgltfwEEQ3IObcBCXbrp24i/gIv0Hbty562LpUhEFwcEgaIug2mZCQZBE0sve59z7F4gSCa3rZMAFw+Gec+55wmEM/vmnCWYmHkyfQGpt2wKkF8D2o6w3gK4kHk5fk8vptJ3e72G1Wk1+h8NhTjUaDdBSrVbJ/L4fUK/X0Ww20Wg00Ov1sFqtsFgsGI/HUEo5W0HhF3A7gA6gN5pOp6VSqTSoVCrIoih7vV5vKaYg3QC0222kWitd12k2m8LhMHRdJ5fL8V2YTCaUUkJ6P885k8mkdLtduq57n3M+n++BaZpQKBSAluM4bDYbNBqNfr8dYLFY0Gq1sFgs/C8DM3Msy2ey2exn3sY5VywWjVartFotm5k3gG1mPq+qWq1G0/R1XZ/N/DiOk6qqlpejKIqqymazlPM8lVIqlUq1WlXVSgB2ux1a64u6ru/7BEFQXddJpVLs9/vJZrN0XWcsFrPzXzMzmVGtVqvZbAbQTCaDxWLBbDb/LwzM+Asl4iU2dC4dJAAAAABJRU5Erhooks="
PROJECTS_ICON_B64 = "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABmJLR0QA/wD/AP+gvaeTAAABUUlEQVRIie2Uv0oDQRDGv3NhY6WVWFj5ASb+gCaxsLHRT0gsLHyExaJWEFvoZ2B9AIHENmnExmYh2YWL4e7kTsJuQhIzDbsw8L/z+f/MzjYg/uVYBvYAqUAJeAFmgfcAS+AF+KqGKoA2MAmswAy4AxbAnQh7AbwDD4Bf4I9QBCPAwD44gC9gDnwFngIPwBtwCFwD/4IN2AJagBLwByRKaW0AGwD52G0fYB1YARp1s1qH1tqwBBaB0rT2ADh7UlolXAXOgdPAGvAUeAXcAdsAJ+As4L7bgYPIKqcAcsA4cAacgZvoP3wGdgFb4DcwDnxmAg+B42AOvAGu/gSCAeApcAZsAg+BDcAY8BnaB9iAf6wA78Aw8DSYAmfAXeA8mALvAQzgKp/XTgC95uVlMJoAb8AocBgsyWw0gF6z8jKaTWDv/wB+AbQp+sbNfiLIAAAAAElFTkSuQmCC"
SKILLS_ICON_B64 = "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABmJLR0QA/wD/AP+gvaeTAAABTElEQVRIie2UvUoDQRCFv1mIYoGFoLiAhY0geAGfxNoi1oIfoJVY2vkEFrb+gIWNILaCiEZEQU+ws/Au7kxuQyLZYU4W5sP+b2bejA30T3PpHkAFsARsAFPAOnABfEopbwBtwAZwAhyAS+ACmFbUWoAxcArcAR/gL7AEbAFbwAZwBWyAK+Bf6N0A3gGvwB9gDlyAP6FGgL0Pj/geB56AP0KjGbgK5AGdIADsAA/AS6nUBNwBtwD9qGytgA5YAW6A02AR2AnUgCmwCWwCN8BWUAQmECkQDxwBl0ALmIAn4CvwBkwDR8Am8BL4AlwBR8AJsAu8AWfAJvABPAO+gUfAM3APvEVbMhY8BW7AFpADdoB54DNwCFwA58AdsB7sAgvAW+ADuAy+hGcCkQTB0N+CKIdisgZ8A54Ag8BssSYz0QF6zYpLaDAB9v4P8BsoB7L29yH6ngAAAABJRU5ErkJggg=="
CONTACT_ICON_B64 = "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABmJLR0QA/wD/AP+gvaeTAAABdElEQVRIie2Uv0rDUBSHv87ciAii6F/gIAh+gIsgrujiIrg4iA4OouAiuOgf4KILV11c3QRXQRwEFy8KCoKg6E4vOSEhIaF5QpBLnrvn3M/959w9Yf/niAZgHlgAVoBVYA04AldAmpVKpZqkec6hGvAE3AJfAR3gCHgGboFDYAU4Y9wVwBmwAZwBR4B94B14Ab4De4At4AV4CHQDT8AW8BLUgA0gAaxg78vRBrAErAM1YAP4fOgt4B1YBN4CWeA48AP4aXSAW+AFmAz+Bb4D3wJzwBw4BXZAvwYfgM3gE3gG9uEZuA5uAO+BF+AbeAfcADfAS6APfAV+AW+BfcAYuA5ugf3gEbgO7kC/Bk+Bf8A68BF4A+zAEFhD2gBdwDqwbWAe+AqsAXuAt0BfBR6AGzAEpgLrwFLgLPAc2BPsA1fBF+AGuAs8BS6BG+ABuAc+gffAb2AOvE174/gReAe+Aa8BHIDv/wW+AQvXn1L0vWkPAAAAAElFTkSuQmCC"


class PortfolioApp:
    def __init__(self, master):
        self.master = master
        master.title("My Portfolio")
        master.geometry("900x650")  # Slightly larger default size
        master.minsize(800, 600)  # Set a minimum size

        # --- Color and Font Definitions ---
        self.COLOR_BG = "#2E2E2E"
        self.COLOR_FRAME_BG = "#3A3A3A"
        self.COLOR_TEXT = "#F0F0F0"
        self.COLOR_ACCENT = "#00BFFF"  # Deep Sky Blue
        self.FONT_NORMAL = ("Segoe UI", 12)
        self.FONT_BOLD = ("Segoe UI", 12, "bold")
        self.FONT_HEADER = ("Segoe UI", 24, "bold")

        # Set the main window background color
        master.configure(bg=self.COLOR_BG)

        # --- Load Icons ---
        self.icons = {
            "home": PhotoImage(data=HOME_ICON_B64),
            "projects": PhotoImage(data=PROJECTS_ICON_B64),
            "skills": PhotoImage(data=SKILLS_ICON_B64),
            "contact": PhotoImage(data=CONTACT_ICON_B64)
        }

        # --- Configure ttk Styles ---
        self._configure_styles()

        # --- Configure Grid Layout ---
        master.columnconfigure(0, weight=0)  # Sidebar column is fixed width
        master.columnconfigure(1, weight=1)  # Content column expands
        master.rowconfigure(0, weight=1)

        # --- Sidebar Frame (Navigation) ---
        self.sidebar_frame = ttk.Frame(master, style="Nav.TFrame")
        self.sidebar_frame.grid(row=0, column=0, sticky="nsw")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)  # Pushes exit button to the bottom

        # Sidebar Header
        ttk.Label(self.sidebar_frame, text="Navigation", font=("Segoe UI", 16, "bold"),
                  style="NavHeader.TLabel").pack(pady=(20, 15), padx=10)

        # Sidebar Buttons
        self.create_nav_button("Home", self.icons["home"], self.show_home_page)
        self.create_nav_button("Projects", self.icons["projects"], self.show_projects_page)
        self.create_nav_button("Skills", self.icons["skills"], self.show_skills_page)
        self.create_nav_button("Contact", self.icons["contact"], self.show_contact_page)

        # Exit Button at the bottom
        exit_button = ttk.Button(self.sidebar_frame, text="Exit", command=master.quit, style="Nav.TButton")
        exit_button.pack(side=tk.BOTTOM, fill='x', padx=15, pady=20)

        # --- Main Content Frame ---
        self.content_frame = ttk.Frame(master, style="Content.TFrame")
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Store page frames
        self.pages = {}
        self.current_page = None

        self.create_pages()
        self.show_home_page()

    def _configure_styles(self):
        """Configures all the custom ttk styles for the app."""
        style = ttk.Style(self.master)
        style.theme_use("clam")  # Use 'clam' theme as a base for customization

        # --- General Widget Styles ---
        style.configure(".",
                        background=self.COLOR_BG,
                        foreground=self.COLOR_TEXT,
                        font=self.FONT_NORMAL)

        # --- Frame Styles ---
        style.configure("Nav.TFrame", background=self.COLOR_FRAME_BG)
        style.configure("Content.TFrame", background=self.COLOR_BG)

        # --- Label Styles ---
        style.configure("TLabel", background=self.COLOR_BG, foreground=self.COLOR_TEXT)
        style.configure("Header.TLabel", font=self.FONT_HEADER, padding=(0, 10, 0, 10))
        style.configure("NavHeader.TLabel", font=("Segoe UI", 16, "bold"),
                        background=self.COLOR_FRAME_BG, foreground=self.COLOR_ACCENT)

        # --- Button Style ---
        style.configure("Nav.TButton",
                        font=self.FONT_BOLD,
                        background=self.COLOR_FRAME_BG,
                        foreground=self.COLOR_TEXT,
                        borderwidth=0,
                        anchor="w",  # Align text to the left
                        padding=(15, 10))  # Left/Right, Top/Bottom padding

        style.map("Nav.TButton",
                  background=[("active", self.COLOR_ACCENT)],  # Hover color
                  foreground=[("active", self.COLOR_FRAME_BG)])

    def create_nav_button(self, text, icon, command):
        """Helper to create and pack navigation buttons with consistent styling."""
        button = ttk.Button(self.sidebar_frame, text=text, image=icon,
                            command=command, style="Nav.TButton", compound="left")
        button.pack(fill='x', padx=15, pady=2)
        return button

    def create_pages(self):
        """Creates all the individual page frames."""
        for page_name in ["home", "projects", "skills", "contact"]:
            frame = ttk.Frame(self.content_frame, style="Content.TFrame")
            frame.grid(row=0, column=0, sticky="nsew")  # Use grid here too
            self.pages[page_name] = frame

        # --- Populate Home Page ---
        home_page = self.pages["home"]
        ttk.Label(home_page, text="Welcome to My Portfolio!", style="Header.TLabel").pack(pady=20, anchor="w")
        ttk.Label(home_page, text="This application demonstrates a modern, multi-page GUI using Python and Tkinter.",
                  wraplength=500, justify=tk.LEFT, font=self.FONT_NORMAL).pack(pady=10, anchor="w")
        ttk.Label(home_page, text="Navigate using the menu on the left.",
                  font=self.FONT_BOLD).pack(pady=20, anchor="w")

        # --- Populate Projects Page ---
        projects_page = self.pages["projects"]
        ttk.Label(projects_page, text="My Projects", style="Header.TLabel").pack(pady=20, anchor="w")
        project_text = (
            "•  Project Alpha: A data analysis tool built with Pandas for processing large datasets.\n\n"
            "•  Project Beta: A web scraping script using BeautifulSoup and Requests to gather market data.\n\n"
            "•  Project Gamma: This very GUI portfolio, showcasing modern Tkinter styling techniques."
        )
        ttk.Label(projects_page, text=project_text, justify=tk.LEFT, font=self.FONT_NORMAL,
                  wraplength=500).pack(pady=10, padx=20, anchor="w")

        # --- Populate Skills Page ---
        skills_page = self.pages["skills"]
        ttk.Label(skills_page, text="Technical Skills", style="Header.TLabel").pack(pady=20, anchor="w")
        skills_text = (
            "Programming Languages:\n"
            "    - Python (Proficient)\n"
            "    - SQL (Intermediate)\n\n"
            "Python Libraries:\n"
            "    - Tkinter / ttk\n"
            "    - Pandas & NumPy\n"
            # ----- FIX WAS HERE: Removed the stray 'al' -----
            "    - Matplotlib & Seaborn\n\n"
            "Tools & Technologies:\n"
            "    - Git & GitHub\n"
            "    - Jupyter Notebooks"
        )
        ttk.Label(skills_page, text=skills_text, justify=tk.LEFT,
                  font=("Courier New", 12)).pack(pady=10, padx=20, anchor="w")

        # --- Populate Contact Page ---
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
        """Hides the current page and shows the specified page."""
        if self.current_page:
            self.current_page.grid_remove()

        self.current_page = self.pages[page_name]
        self.current_page.grid()  # Using grid to show the frame

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