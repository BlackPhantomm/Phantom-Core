<<<<<<< HEAD
# phantom_gui.py (Version 1.2 - Controller with Input Validation and Encryption)
=======
# phantom_gui.py (Version 1.2 Demo - Complete Controller)
>>>>>>> 7f7f24a1d05f003b1845570bdd6844ac15db18ed

import customtkinter as ctk
import os
import sys
import json
import re
import time
import threading
from tkinter import filedialog
from PIL import Image

# CRITICAL FIX: Add current working directory to path (for system module resolution)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import security and validation functions
<<<<<<< HEAD
from encryption import encrypt_data
=======
from encryption import encrypt_data # ONLY encrypt_data is imported for save functionality
>>>>>>> 7f7f24a1d05f003b1845570bdd6844ac15db18ed
from validation import validate_protocol_data 

# Import configuration and pages
from config import ACCENT_COLOR, VAULT_COLOR, SIDEBAR_COLOR, CARD_COLOR, TEXT_MAIN, TEXT_DIM, BORDER_COLOR
from filament_page import FilamentPage
from process_page import ProcessPage
from printer_page import PrinterPage
<<<<<<< HEAD
from vault_page import VaultPage
=======
from vault_page import VaultPage # Imports the simple placeholder VaultPage
>>>>>>> 7f7f24a1d05f003b1845570bdd6844ac15db18ed

# --- CONFIGURATION ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class PhantomApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("PHANTOM CORE v1.2") # CORRECTED VERSION NUMBER
        self.geometry("1100x850")
        self.configure(fg_color="#0D1117")

        # Path Setup
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.icon_path = os.path.join(self.script_dir, "phantom.ico")
        self.logo_path = os.path.join(self.script_dir, "phantom_logo.png")

        # --- STATE MANAGEMENT ---
        self.paths = {"filament": "", "process": "", "printer": ""}
        self.current_mode = None
        self.current_page = None
        self.SIDEBAR_COLOR = SIDEBAR_COLOR
        self.BORDER_COLOR = BORDER_COLOR
        self.CARD_COLOR = CARD_COLOR
        
        # UI references needed for the controller's save/update logic
        self.path_entry = None
        self.page_fields = {}
        self.btn_action = None
        self.progress = None

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

        # NAVIGATION BUTTONS
        self.btn_filament = self.create_nav_btn(":: FILAMENT", lambda: self.show_page(FilamentPage), 0.20)
        self.btn_process = self.create_nav_btn(":: PROCESS", lambda: self.show_page(ProcessPage), 0.28)
        self.btn_printer = self.create_nav_btn(":: PRINTER", lambda: self.show_page(PrinterPage), 0.36)
        
        self.btn_vault = ctk.CTkButton(
            self.sidebar, text=":: THE VAULT", command=lambda: self.show_page(VaultPage),
            fg_color="transparent", text_color=VAULT_COLOR, hover_color=CARD_COLOR,
            anchor="w", height=50, font=ctk.CTkFont(size=14, weight="bold"), border_spacing=20
        )
        self.btn_vault.place(relx=0, rely=0.48, relwidth=1)

        self.status_label = ctk.CTkLabel(self.sidebar, text="SYSTEM READY", font=("Consolas", 12), text_color=TEXT_DIM)
        self.status_label.place(relx=0.1, rely=0.92)

        # --- MAIN AREA ---
        self.main_area = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_area.grid(row=0, column=1, sticky="nsew", padx=40, pady=40)

        self.show_page(FilamentPage)

    # --- PAGE NAVIGATION ---
    def show_page(self, page_class):
        self.clear_ui()
        if self.current_page:
            self.current_page.destroy()

        if page_class == FilamentPage:
            self.set_active_nav(self.btn_filament)
            self.current_page = FilamentPage(self.main_area, self)
        elif page_class == ProcessPage:
            self.set_active_nav(self.btn_process)
            self.current_page = ProcessPage(self.main_area, self)
        elif page_class == PrinterPage:
            self.set_active_nav(self.btn_printer)
            self.current_page = PrinterPage(self.main_area, self)
        elif page_class == VaultPage:
            self.set_active_nav(self.btn_vault)
<<<<<<< HEAD
            self.current_page = VaultPage(self.main_area, self)
=======
            self.current_page = VaultPage(self.main_area, self) # Loads the placeholder VaultPage
>>>>>>> 7f7f24a1d05f003b1845570bdd6844ac15db18ed

    def clear_ui(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()

<<<<<<< HEAD
    # --- SAVE LOGIC (UPDATED WITH VALIDATION) ---
=======
    # --- SAVE LOGIC (WITH VALIDATION & ENCRYPTION HOOK) ---
>>>>>>> 7f7f24a1d05f003b1845570bdd6844ac15db18ed
    def initiate_save(self):
        # Retrieve path from the active path_entry widget
        base_path = self.path_entry.get() if self.path_entry else ""
        if not base_path:
            self.show_popup("MISSING PATH", "Please select a Target Directory first.")
            return

        # 1. RUN DATA VALIDATION
        is_valid, error_msg = validate_protocol_data(self.current_mode, self.page_fields)
        
        if not is_valid:
            # If data is invalid, stop the process and show an error popup
            self.show_popup("VALIDATION FAILED", error_msg)
            return
            
        # 2. If valid, proceed with animation and saving
        self.btn_action.pack_forget()
        self.progress.pack(fill="x", pady=(15,0))
        self.status_label.configure(text="ENCRYPTING...", text_color=ACCENT_COLOR)
        threading.Thread(target=self.run_simulation, daemon=True).start()

    def run_simulation(self):
        for i in range(101):
            time.sleep(0.05)
            self.progress.set(i / 100)
        self.after(50, self.save_file)

    def save_file(self):
        try:
            name = self.page_fields['entry_name'].get() if 'entry_name' in self.page_fields else ""
            if not name:
                self.show_popup("Error", "Name field is required.")
                self.reset_ui()
                return

<<<<<<< HEAD
            # Retrieve Master Key
=======
            # Retrieve Master Key (NOTE: This key will always be blank in the DEMO version)
>>>>>>> 7f7f24a1d05f003b1845570bdd6844ac15db18ed
            master_key_entry = self.page_fields.get('entry_master_key')
            master_key = master_key_entry.get() if master_key_entry and master_key_entry.winfo_exists() else ""

            # Prepare File Paths
            base_path = self.path_entry.get()
            folder_name = f"{self.current_mode}s"
            final_folder = os.path.join(base_path, folder_name)

            if not os.path.exists(final_folder):
                os.makedirs(final_folder, exist_ok=True)

            file_id = f"phantom_{self.clean_id(name)}"
            filename = f"{file_id}.json"
            full_path = os.path.join(final_folder, filename)

            # Assemble JSON Data
            data = {
                "id": file_id,
                "type": self.current_mode,
                "metadata": {"name": name, "timestamp": time.time(), "encrypted": bool(master_key)} 
            }

            # Data collection per mode
            if self.current_mode == "filament":
                data["print_settings"] = {
                    "nozzle_temperature": self.page_fields['entry_temp'].get(),
                    "bed_temperature": self.page_fields['entry_bed'].get()
                }
            elif self.current_mode == "process":
                data["process_settings"] = {
                    "layer_height": self.page_fields['entry_layer'].get(),
                    "infill_density": self.page_fields['entry_infill'].get(),
                }
            elif self.current_mode == "printer":
                data["hardware_settings"] = {
                    "build_volume_x": self.page_fields['entry_size_x'].get(),
                    "build_volume_y": self.page_fields['entry_size_y'].get(),
                    "build_volume_z": self.page_fields['entry_size_z'].get(),
                }

            # ENCRYPTION/SAVE LOGIC
            json_string = json.dumps(data, indent=2)

            if master_key:
                encrypted_bytes = encrypt_data(json_string.encode('utf-8'), master_key)
                with open(full_path, 'wb') as f:
                    f.write(encrypted_bytes)
                
                status_msg = f"ENCRYPTED! Saved to: {folder_name}/{filename}"
                popup_msg = f"File saved and ENCRYPTED using Master Key:\n{full_path}"
            else:
                with open(full_path, 'w') as f:
                    f.write(json_string)

                status_msg = f"SAVED (Unencrypted): {folder_name}/{filename}"
                popup_msg = f"File saved UNENCRYPTED:\n{full_path}"


            self.status_label.configure(text=status_msg, text_color="#00FF00")
            self.show_popup("SUCCESS", popup_msg)

        except Exception as e:
            if "InvalidKey" in str(e) or "InvalidToken" in str(e):
                 self.show_popup("ENCRYPTION ERROR", "Invalid Master Key or Data Corruption. Check key.")
            else:
                self.show_popup("SYSTEM ERROR", str(e))

        self.reset_ui()
    
<<<<<<< HEAD
    # --- DECRYPTION LOGIC FOR THE VAULT ---
    def decrypt_and_display_file(self, master_key: str, output_widget):
        from encryption import decrypt_data
        
        file_path = filedialog.askopenfilename(
            defaultextension=".json",
            filetypes=[("Protocol Files", "*.json")],
            title="Select Protocol File to Decrypt"
        )
        
        if not file_path:
            return

        try:
            # 1. Read Encrypted Data (Binary Mode)
            with open(file_path, 'rb') as f:
                encrypted_bytes = f.read()
            
            # 2. Decrypt
            decrypted_bytes = decrypt_data(encrypted_bytes, master_key)
            decrypted_json_string = decrypted_bytes.decode('utf-8')
            
            # 3. Format and Display
            output_widget.delete("1.0", "end")
            
            json_object = json.loads(decrypted_json_string)
            pretty_json = json.dumps(json_object, indent=4)
            
            output_widget.insert("1.0", pretty_json)
            self.status_label.configure(text=f"SUCCESS: Decrypted {os.path.basename(file_path)}", text_color="#00FF00")

        except Exception as e:
            output_widget.delete("1.0", "end")
            output_widget.insert("1.0", "DECRYPTION FAILED. Invalid key or file format.")
            self.status_label.configure(text="DECRYPTION FAILED", text_color="#FF0000")
            
            if "InvalidToken" in str(e):
                self.show_popup("DECRYPTION FAILED", "Invalid Master Key. The password is incorrect.")
            else:
                 self.show_popup("DECRYPTION ERROR", f"Error reading file: {str(e)}")
=======
    # --- DECRYPTION LOGIC: REMOVED FOR DEMO VERSION ---
    # The decrypt_and_display_file method is NOT included in this file.
>>>>>>> 7f7f24a1d05f003b1845570bdd6844ac15db18ed


    # --- RETAINED UTILITY METHODS ---
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
        
        if active_btn:
            active_btn.configure(fg_color=CARD_COLOR, border_width=2, border_color=ACCENT_COLOR)
            
    def browse_folder(self, mode, entry_widget):
        folder = filedialog.askdirectory(title=f"Select Base Folder for {mode.upper()}S")
        if folder:
            self.paths[mode] = folder
            entry_widget.delete(0, "end")
            entry_widget.insert(0, folder)
            self.status_label.configure(text="PATH UPDATED", text_color=ACCENT_COLOR)

    def reset_ui(self):
        self.progress.pack_forget()
        self.btn_action.pack(fill="x")
        self.progress.set(0)

    def clean_id(self, name):
        return re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_')
        
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

# --- RUN THE APP ---
if __name__ == "__main__":
    app = PhantomApp()
    app.mainloop()