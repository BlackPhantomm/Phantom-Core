import customtkinter as ctk
import os
import json
import re
import time
import threading
from tkinter import filedialog
from PIL import Image

# --- CONFIGURATION ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# --- PALETTE ---
ACCENT_COLOR = "#00A8E8"    # Cyan
VAULT_COLOR = "#D9534F"     # Red
HOVER_COLOR = "#007EA7"     # Darker Cyan
BG_COLOR = "#0D1117"        # Black/Grey
SIDEBAR_COLOR = "#161B22"   # Sidebar Grey
CARD_COLOR = "#21262D"      # Card Grey
TEXT_MAIN = "#C9D1D9"       # White-ish
TEXT_DIM = "#8B949E"        # Grey Text
BORDER_COLOR = "#30363D"    # Borders

class PhantomApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("PHANTOM CORE v1.0")
        self.geometry("1100x850")
        self.configure(fg_color=BG_COLOR)

        # Path Setup
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.icon_path = os.path.join(self.script_dir, "phantom.ico")
        self.logo_path = os.path.join(self.script_dir, "phantom_logo.png")

        # MEMORY: Stores paths for each category
        self.paths = {
            "filament": "",
            "process": "",
            "printer": ""
        }

        # Load Icon
        if os.path.exists(self.icon_path):
            self.iconbitmap(self.icon_path)

        # Layout Grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- SIDEBAR ---
        self.sidebar = ctk.CTkFrame(self, width=260, corner_radius=0, fg_color=SIDEBAR_COLOR)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

        self.setup_sidebar_header()

        self.btn_filament = self.create_nav_btn(":: FILAMENT", self.show_filament_page, 0.20)
        self.btn_process = self.create_nav_btn(":: PROCESS", self.show_process_page, 0.28)
        self.btn_printer = self.create_nav_btn(":: PRINTER", self.show_printer_page, 0.36)
        
        self.btn_vault = ctk.CTkButton(
            self.sidebar, text=":: THE VAULT", command=self.show_vault_page,
            fg_color="transparent", text_color=VAULT_COLOR, hover_color=CARD_COLOR,
            anchor="w", height=50, font=ctk.CTkFont(size=14, weight="bold"), border_spacing=20
        )
        self.btn_vault.place(relx=0, rely=0.48, relwidth=1)

        self.status_label = ctk.CTkLabel(self.sidebar, text="SYSTEM READY", font=("Consolas", 12), text_color=TEXT_DIM)
        self.status_label.place(relx=0.1, rely=0.92)

        # --- MAIN AREA ---
        self.main_area = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_area.grid(row=0, column=1, sticky="nsew", padx=40, pady=40)

        self.show_filament_page()

    # --- HELPERS ---
    def setup_sidebar_header(self):
        try:
            if os.path.exists(self.logo_path):
                pil_image = Image.open(self.logo_path)
                base_width = 200
                w_percent = (base_width / float(pil_image.size[0]))
                h_size = int((float(pil_image.size[1]) * float(w_percent)))
                logo_img = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(base_width, h_size))
                self.logo_label = ctk.CTkLabel(self.sidebar, text="", image=logo_img)
                self.logo_label.place(relx=0.5, rely=0.08, anchor="center")
            else:
                raise Exception("Logo missing")
        except:
            self.brand_label = ctk.CTkLabel(self.sidebar, text="PHANTOM\nCORE", font=ctk.CTkFont(family="Segoe UI", size=28, weight="bold"), text_color=ACCENT_COLOR)
            self.brand_label.place(relx=0.5, rely=0.08, anchor="center")

    def create_nav_btn(self, text, command, rely):
        btn = ctk.CTkButton(self.sidebar, text=text, command=command, fg_color="transparent", text_color=TEXT_MAIN, hover_color=CARD_COLOR, anchor="w", height=50, font=ctk.CTkFont(size=14, weight="bold"), border_spacing=20)
        btn.place(relx=0, rely=rely, relwidth=1)
        return btn

    def set_active_nav(self, active_btn):
        for btn in [self.btn_filament, self.btn_process, self.btn_printer, self.btn_vault]:
            btn.configure(fg_color="transparent", border_width=0)
        active_btn.configure(fg_color=CARD_COLOR, border_width=2, border_color=ACCENT_COLOR)

    def clear_ui(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()

    # --- COMPONENT: PATH SELECTOR ---
    def add_path_selector(self, mode):
        card = ctk.CTkFrame(self.main_area, fg_color=CARD_COLOR, border_width=1, border_color=ACCENT_COLOR)
        card.pack(fill="x", pady=(0, 20), ipadx=10, ipady=10)
        
        header = ctk.CTkLabel(card, text="TARGET DIRECTORY", font=ctk.CTkFont(size=12, weight="bold"), text_color=ACCENT_COLOR)
        header.pack(anchor="w", padx=10)

        row = ctk.CTkFrame(card, fg_color="transparent")
        row.pack(fill="x", pady=(5, 0), padx=10)

        self.path_entry = ctk.CTkEntry(row, placeholder_text="No directory selected...", text_color="white", fg_color=SIDEBAR_COLOR, border_color=BORDER_COLOR)
        self.path_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        if self.paths[mode]:
            self.path_entry.insert(0, self.paths[mode])
        
        btn = ctk.CTkButton(row, text="BROWSE", width=100, command=lambda: self.browse_folder(mode), fg_color=SIDEBAR_COLOR, hover_color=HOVER_COLOR)
        btn.pack(side="right")

    def browse_folder(self, mode):
        folder = filedialog.askdirectory(title=f"Select Base Folder for {mode.upper()}S")
        if folder:
            self.paths[mode] = folder
            self.path_entry.delete(0, "end")
            self.path_entry.insert(0, folder)
            self.status_label.configure(text="PATH UPDATED", text_color=ACCENT_COLOR)

    # --- PAGES ---

    def show_filament_page(self):
        self.clear_ui()
        self.current_mode = "filament"
        self.set_active_nav(self.btn_filament)
        self.add_title("FILAMENT PROTOCOL")
        
        self.add_path_selector("filament")

        card_id = self.create_card("IDENTITY")
        self.entry_name = self.create_field(card_id, "Display Name", "e.g. Phantom PLA+")
        self.entry_material = self.create_field(card_id, "Material Type", "PLA")
        self.entry_color = self.create_field(card_id, "Color Hex", "#0000FF")

        card_temp = self.create_card("THERMAL PHYSICS")
        self.entry_temp = self.create_field(card_temp, "Nozzle Temperature (°C)", "210")
        self.entry_bed = self.create_field(card_temp, "Bed Temperature (°C)", "60")

        self.add_action_button("GENERATE FILAMENT")

    def show_process_page(self):
        self.clear_ui()
        self.current_mode = "process"
        self.set_active_nav(self.btn_process)
        self.add_title("PROCESS CONFIGURATION")
        
        self.add_path_selector("process")
        
        card = self.create_card("METADATA")
        self.entry_name = self.create_field(card, "Profile Name", "e.g. Phantom Fast 0.20")

        card_mech = self.create_card("MECHANICS")
        self.entry_layer = self.create_field(card_mech, "Layer Height", "0.20")
        self.entry_speed = self.create_field(card_mech, "Speed (mm/s)", "200")

        self.add_action_button("GENERATE PROCESS")

    def show_printer_page(self):
        self.clear_ui()
        self.current_mode = "printer"
        self.set_active_nav(self.btn_printer)
        self.add_title("PRINTER DEFINITION")
        
        self.add_path_selector("printer")
        
        card = self.create_card("HARDWARE INFO")
        self.entry_name = self.create_field(card, "Model Name", "e.g. Creality K1")

        self.add_action_button("GENERATE PRINTER")

    def show_vault_page(self):
        self.clear_ui()
        self.current_mode = "vault"
        self.set_active_nav(self.btn_vault)
        self.add_title("THE VAULT")
        
        desc = ctk.CTkLabel(self.main_area, text="Steganography Suite: Hide data inside standard image files.", text_color=TEXT_DIM)
        desc.pack(anchor="w", pady=(0, 20))

        card = self.create_card("ENCRYPTION TARGETS")
        ctk.CTkButton(card, text="SELECT COVER IMAGE", fg_color=SIDEBAR_COLOR).pack(fill="x", pady=5)
        ctk.CTkButton(card, text="SELECT PAYLOAD JSON", fg_color=SIDEBAR_COLOR).pack(fill="x", pady=5)

        self.add_action_button("ENCRYPT TO IMAGE")

    # --- UI COMPONENTS ---
    def add_title(self, text):
        lbl = ctk.CTkLabel(self.main_area, text=text, font=ctk.CTkFont(size=26, weight="bold"), text_color=TEXT_MAIN)
        lbl.pack(anchor="w", pady=(0, 20))

    def create_card(self, title):
        card = ctk.CTkFrame(self.main_area, fg_color=CARD_COLOR)
        card.pack(fill="x", pady=(0, 20), ipadx=20, ipady=15)
        ctk.CTkLabel(card, text=title, font=ctk.CTkFont(size=12, weight="bold"), text_color=ACCENT_COLOR).pack(anchor="w", pady=(0, 10))
        return card

    def create_field(self, parent, label_text, placeholder):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=5)
        ctk.CTkLabel(frame, text=label_text, width=150, anchor="w", text_color=TEXT_MAIN).pack(side="left")
        entry = ctk.CTkEntry(frame, placeholder_text=placeholder, fg_color=SIDEBAR_COLOR, border_color=BORDER_COLOR, text_color="white")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def add_action_button(self, text):
        frame = ctk.CTkFrame(self.main_area, fg_color="transparent")
        frame.pack(fill="x", pady=(20, 0))

        self.btn_action = ctk.CTkButton(frame, text=text, command=self.initiate_save, height=50, fg_color=ACCENT_COLOR, hover_color=HOVER_COLOR, font=ctk.CTkFont(size=15, weight="bold"))
        self.btn_action.pack(fill="x")
        
        self.progress = ctk.CTkProgressBar(frame, height=15, progress_color=ACCENT_COLOR)
        self.progress.set(0)

    # --- LOGIC ---
    def initiate_save(self):
        if self.current_mode == "vault":
             pass
        else:
            current_path_in_box = self.path_entry.get()
            if not current_path_in_box:
                self.show_popup("MISSING PATH", "Please select a Target Directory first.")
                return

        self.btn_action.pack_forget()
        self.progress.pack(fill="x", pady=(15,0))
        self.status_label.configure(text="ENCRYPTING...", text_color=ACCENT_COLOR)
        threading.Thread(target=self.run_simulation, daemon=True).start()

    def run_simulation(self):
        for i in range(101):
            time.sleep(0.1) 
            self.progress.set(i / 100)
        self.after(100, self.save_file)

    def clean_id(self, name):
        return re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_')

    def save_file(self):
        try:
            if self.current_mode == "vault":
                self.show_popup("Pending", "Vault logic coming soon.")
                self.reset_ui()
                return

            name = self.entry_name.get()
            if not name: 
                self.show_popup("Error", "Name field is required.")
                self.reset_ui()
                return

            base_path = self.path_entry.get()
            folder_name = f"{self.current_mode}s"
            final_folder = os.path.join(base_path, folder_name)

            if not os.path.exists(final_folder):
                os.makedirs(final_folder, exist_ok=True)
            
            file_id = f"phantom_{self.clean_id(name)}"
            filename = f"{file_id}.json"
            full_path = os.path.join(final_folder, filename)

            data = {
                "id": file_id, 
                "type": self.current_mode, 
                "metadata": {"name": name, "timestamp": time.time()}
            }

            if self.current_mode == "filament":
                data["print_settings"] = {
                    "nozzle_temperature": self.entry_temp.get(),
                    "bed_temperature": self.entry_bed.get()
                }

            with open(full_path, 'w') as f:
                json.dump(data, f, indent=2)

            self.status_label.configure(text=f"SAVED TO: {folder_name}/{filename}", text_color="#00FF00")
            self.show_popup("SUCCESS", f"File saved in:\n{full_path}")

        except Exception as e:
            self.show_popup("ERROR", str(e))
        
        self.reset_ui()

    def reset_ui(self):
        self.progress.pack_forget()
        self.btn_action.pack(fill="x")
        self.progress.set(0)

    def show_popup(self, title, message):
        popup = ctk.CTkToplevel(self)
        popup.geometry("500x200")
        popup.title(title)
        popup.geometry(f"+{self.winfo_x()+300}+{self.winfo_y()+250}")
        popup.configure(fg_color=SIDEBAR_COLOR)
        
        ctk.CTkLabel(popup, text=title, font=ctk.CTkFont(size=16, weight="bold"), text_color=ACCENT_COLOR).pack(pady=(20, 10))
        ctk.CTkLabel(popup, text=message, wraplength=450, text_color=TEXT_MAIN).pack(pady=10)
        ctk.CTkButton(popup, text="OK", command=popup.destroy, fg_color=ACCENT_COLOR, width=100).pack(pady=20)
        
        popup.transient(self)
        popup.grab_set()

if __name__ == "__main__":
    app = PhantomApp()
    app.mainloop()