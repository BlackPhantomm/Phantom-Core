<<<<<<< HEAD
# vault_page.py (Complete Vault UI)

from base_page import BasePage
from config import ACCENT_COLOR, VAULT_COLOR, TEXT_MAIN, SIDEBAR_COLOR, CARD_COLOR, BORDER_COLOR
import customtkinter as ctk
from tkinter import filedialog
import json
=======
# vault_page.py (V1.2 DEMO Placeholder)

from base_page import BasePage
from config import ACCENT_COLOR, VAULT_COLOR, TEXT_MAIN
import customtkinter as ctk
>>>>>>> 7f7f24a1d05f003b1845570bdd6844ac15db18ed

class VaultPage(BasePage):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, controller, **kwargs)
        self.controller.current_mode = "vault"
<<<<<<< HEAD
        self.SIDEBAR_COLOR = SIDEBAR_COLOR # Pass colors for local use
        self.BORDER_COLOR = BORDER_COLOR
        self.CARD_COLOR = CARD_COLOR
        self.TEXT_MAIN = TEXT_MAIN
=======
>>>>>>> 7f7f24a1d05f003b1845570bdd6844ac15db18ed
        self.render_ui()

    def render_ui(self):
        self.add_title("THE VAULT")
        
<<<<<<< HEAD
        ctk.CTkLabel(self, text="MASTER KEY & LOG MANAGEMENT", font=ctk.CTkFont(size=20), text_color=VAULT_COLOR).pack(pady=(50, 10))

        # --- MASTER KEY INPUT ---
        card_key = self.create_card("MASTER KEY (REQUIRED FOR DECRYPTION)")
        
        key_frame = ctk.CTkFrame(card_key, fg_color="transparent")
        key_frame.pack(fill="x", pady=5)
        ctk.CTkLabel(key_frame, text="Vault Password", width=150, anchor="w", text_color=self.TEXT_MAIN).pack(side="left")
        
        # Manually create the password entry field here
        self.entry_master_key = ctk.CTkEntry(key_frame, placeholder_text="Enter secure key", fg_color=self.SIDEBAR_COLOR, border_color=self.BORDER_COLOR, text_color="white", show="*")
        self.entry_master_key.pack(side="right", fill="x", expand=True)

        # Pass the master key field to the controller (needed for save_file and decryption)
        self.controller.page_fields['entry_master_key'] = self.entry_master_key

        # --- DECRYPT BUTTON ---
        self.btn_action = ctk.CTkButton(self, text="DECRYPT AND VIEW LOG", command=self.initiate_decrypt, height=50, fg_color=VAULT_COLOR, hover_color=ACCENT_COLOR, font=ctk.CTkFont(size=15, weight="bold"))
        self.btn_action.pack(pady=(30, 0), ipadx=20)
        
        # --- DISPLAY AREA ---
        self.text_output = ctk.CTkTextbox(self, height=300, fg_color=self.CARD_COLOR, text_color=self.TEXT_MAIN, wrap="word")
        self.text_output.insert("0.0", "Decrypted JSON data will appear here...")
        self.text_output.pack(fill="x", pady=20)

    def initiate_decrypt(self):
        # Retrieve the key
        master_key = self.entry_master_key.get()
        if not master_key:
            self.controller.show_popup("Error", "Master Key is required to decrypt the file.")
            return

        # Use the controller's logic to open and decrypt the file
        self.controller.decrypt_and_display_file(master_key, self.text_output)
=======
        ctk.CTkLabel(self, text="ENCRYPTED PROTOCOL MANAGEMENT", font=ctk.CTkFont(size=20), text_color=VAULT_COLOR).pack(pady=(50, 20))
        ctk.CTkLabel(self, text="This feature is currently undergoing final testing and will be released in the next patch (v1.3).", wraplength=700, text_color=TEXT_MAIN).pack(pady=10)

        # Placeholder button
        self.btn_action = ctk.CTkButton(self, text="FEATURE UNDER CONSTRUCTION", command=lambda: self.controller.show_popup("Vault Access", "This feature is currently disabled."), height=50, fg_color=VAULT_COLOR, hover_color=ACCENT_COLOR, font=ctk.CTkFont(size=15, weight="bold"))
        self.btn_action.pack(pady=(50, 0), ipadx=20)
>>>>>>> 7f7f24a1d05f003b1845570bdd6844ac15db18ed
