# vault_page.py (V1.2 DEMO Placeholder)

from base_page import BasePage
from config import ACCENT_COLOR, VAULT_COLOR, TEXT_MAIN
import customtkinter as ctk

class VaultPage(BasePage):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, controller, **kwargs)
        self.controller.current_mode = "vault"
        self.render_ui()

    def render_ui(self):
        self.add_title("THE VAULT")
        
        ctk.CTkLabel(self, text="ENCRYPTED PROTOCOL MANAGEMENT", font=ctk.CTkFont(size=20), text_color=VAULT_COLOR).pack(pady=(50, 20))
        ctk.CTkLabel(self, text="This feature is currently undergoing final testing and will be released in the next patch (v1.3).", wraplength=700, text_color=TEXT_MAIN).pack(pady=10)

        # Placeholder button
        self.btn_action = ctk.CTkButton(self, text="FEATURE UNDER CONSTRUCTION", command=lambda: self.controller.show_popup("Vault Access", "This feature is currently disabled."), height=50, fg_color=VAULT_COLOR, hover_color=ACCENT_COLOR, font=ctk.CTkFont(size=15, weight="bold"))
        self.btn_action.pack(pady=(50, 0), ipadx=20)