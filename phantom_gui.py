import customtkinter as ctk
import os
import json
import re
from datetime import datetime

# --- CONFIGURATION ---
ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# YOUR BRAND COLORS
PHANTOM_BLUE = "#2E86C1" # A nice electric blue
DARK_GREY = "#1B1B1B"

class PhantomApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("PHANTOM CORE v2.0")
        self.geometry("900x600")
        self.configure(fg_color=DARK_GREY)

        # Layout: 2 Columns (Sidebar + Main)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- SIDEBAR ---
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="PHANTOM\nEDITION", font=ctk.CTkFont(size=24, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.sidebar_btn_1 = ctk.CTkButton(self.sidebar_frame, text="New Filament", command=self.show_filament_page, fg_color=PHANTOM_BLUE)
        self.sidebar_btn_1.grid(row=1, column=0, padx=20, pady=10)
        
        self.sidebar_btn_2 = ctk.CTkButton(self.sidebar_frame, text="New Process", command=self.show_process_page, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.sidebar_btn_2.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_btn_3 = ctk.CTkButton(self.sidebar_frame, text="New Printer", command=self.show_printer_page, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.sidebar_btn_3.grid(row=3, column=0, padx=20, pady=10)

        # --- MAIN AREA ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
        # We start by showing the Filament page
        self.show_filament_page()

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # --- FILAMENT PAGE ---
    def show_filament_page(self):
        self.clear_main_frame()
        self.current_mode = "filament"
        
        # Title
        title = ctk.CTkLabel(self.main_frame, text=":: CREATE FILAMENT ::", font=ctk.CTkFont(size=20, weight="bold"), text_color=PHANTOM_BLUE)
        title.pack(pady=10, anchor="w")

        # Inputs
        self.entry_name = self.create_input("Display Name (e.g. Phantom PLA+)")
        self.entry_material = self.create_input("Material Type (PLA, PETG, etc.)")
        self.entry_temp = self.create_input("Nozzle Temp (°C)")
        self.entry_bed = self.create_input("Bed Temp (°C)")
        self.entry_color = self.create_input("Color Hex (#0000FF)")

        # Save Button
        save_btn = ctk.CTkButton(self.main_frame, text="GENERATE PROFILE", command=self.save_file, height=40, fg_color=PHANTOM_BLUE)
        save_btn.pack(pady=30, anchor="w")

    # --- PROCESS PAGE ---
    def show_process_page(self):
        self.clear_main_frame()
        self.current_mode = "process"
        
        title = ctk.CTkLabel(self.main_frame, text=":: CREATE PROCESS ::", font=ctk.CTkFont(size=20, weight="bold"), text_color=PHANTOM_BLUE)
        title.pack(pady=10, anchor="w")

        self.entry_name = self.create_input("Profile Name (e.g. Phantom Fast 0.20)")
        self.entry_layer = self.create_input("Layer Height (mm)")
        self.entry_infill = self.create_input("Infill Density (%)")
        self.entry_speed = self.create_input("Outer Wall Speed (mm/s)")

        save_btn = ctk.CTkButton(self.main_frame, text="GENERATE PROFILE", command=self.save_file, height=40, fg_color=PHANTOM_BLUE)
        save_btn.pack(pady=30, anchor="w")

    # --- PRINTER PAGE ---
    def show_printer_page(self):
        self.clear_main_frame()
        self.current_mode = "printer"
        
        title = ctk.CTkLabel(self.main_frame, text=":: CREATE PRINTER ::", font=ctk.CTkFont(size=20, weight="bold"), text_color=PHANTOM_BLUE)
        title.pack(pady=10, anchor="w")

        self.entry_name = self.create_input("Printer Model Name")
        self.entry_x = self.create_input("Bed X Size (mm)")
        self.entry_y = self.create_input("Bed Y Size (mm)")
        self.entry_z = self.create_input("Bed Z Height (mm)")

        save_btn = ctk.CTkButton(self.main_frame, text="GENERATE PROFILE", command=self.save_file, height=40, fg_color=PHANTOM_BLUE)
        save_btn.pack(pady=30, anchor="w")

    # --- HELPER FUNCTIONS ---
    def create_input(self, placeholder):
        label = ctk.CTkLabel(self.main_frame, text=placeholder, anchor="w")
        label.pack(fill="x", pady=(10, 0))
        entry = ctk.CTkEntry(self.main_frame, placeholder_text=placeholder)
        entry.pack(fill="x", pady=(5, 10))
        return entry

    def clean_id(self, name):
        clean = name.lower()
        clean = re.sub(r'[^a-z0-9]+', '_', clean)
        return clean.strip('_')

    def save_file(self):
        # Gather Data based on mode
        data = {}
        folder = ""
        
        try:
            if self.current_mode == "filament":
                folder = "filaments"
                name = self.entry_name.get()
                file_id = f"phantom_{self.clean_id(name)}"
                data = {
                    "schema_version": "1.0.0",
                    "type": "filament",
                    "id": file_id,
                    "maintainer": "BlackPhantomm",
                    "metadata": {"name": name, "author": "BlackPhantomm", "color": self.entry_color.get()},
                    "compatibility": {"printers": ["*"], "nozzles": ["0.4", "0.6"]},
                    "parameters": {"material": self.entry_material.get(), "density": 1.24, "diameter": 1.75},
                    "print_settings": {
                        "nozzle_temperature": int(self.entry_temp.get()),
                        "bed_temperature": int(self.entry_bed.get())
                    }
                }

            elif self.current_mode == "process":
                folder = "processes"
                name = self.entry_name.get()
                file_id = f"phantom_{self.clean_id(name)}"
                data = {
                    "schema_version": "1.0.0",
                    "type": "process",
                    "id": file_id,
                    "maintainer": "BlackPhantomm",
                    "metadata": {"name": name},
                    "resolution": {"layer_height": float(self.entry_layer.get())},
                    "structure": {"infill_density": int(self.entry_infill.get())},
                    "speed": {"outer_wall": int(self.entry_speed.get())}
                }
            
            elif self.current_mode == "printer":
                folder = "printers"
                name = self.entry_name.get()
                file_id = f"phantom_{self.clean_id(name)}"
                data = {
                    "schema_version": "1.0.0",
                    "type": "printer",
                    "id": file_id,
                    "maintainer": "BlackPhantomm",
                    "metadata": {"name": name},
                    "print_volume": {
                        "x": int(self.entry_x.get()), 
                        "y": int(self.entry_y.get()), 
                        "z": int(self.entry_z.get())
                    }
                }

            # Save Logic
            if not os.path.exists(folder):
                os.makedirs(folder)
            
            filename = f"{file_id}.json"
            filepath = os.path.join(folder, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            
            # Show Success Popup
            self.show_popup("SUCCESS", f"Saved to {folder}/{filename}")

        except ValueError:
            self.show_popup("ERROR", "Please fill in all numbers correctly!")
        except Exception as e:
            self.show_popup("ERROR", str(e))

    def show_popup(self, title, message):
        popup = ctk.CTkToplevel(self)
        popup.geometry("400x150")
        popup.title(title)
        label = ctk.CTkLabel(popup, text=message, wraplength=350)
        label.pack(pady=20)
        btn = ctk.CTkButton(popup, text="OK", command=popup.destroy, fg_color=PHANTOM_BLUE)
        btn.pack(pady=10)

if __name__ == "__main__":
    app = PhantomApp()
    app.mainloop()