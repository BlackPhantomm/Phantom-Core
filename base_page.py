# pages/base_page.py

import customtkinter as ctk
from config import ACCENT_COLOR, CARD_COLOR, SIDEBAR_COLOR, BORDER_COLOR, TEXT_MAIN

class BasePage(ctk.CTkFrame):
    """
    Base class for all Phantom Core UI pages (Filament, Process, Printer, Vault).
    Handles shared methods like creating cards, fields, and action buttons.
    """
    def __init__(self, master, controller, **kwargs):
        # Master is the parent frame (main_area in PhantomApp)
        # Controller is the PhantomApp instance itself (to access global methods like save_file)
        super().__init__(master, fg_color="transparent", **kwargs)
        self.controller = controller
        self.pack(fill="both", expand=True)

    def add_title(self, text):
        lbl = ctk.CTkLabel(self, text=text, font=ctk.CTkFont(size=26, weight="bold"), text_color=TEXT_MAIN)
        lbl.pack(anchor="w", pady=(0, 20))

    def create_card(self, title):
        card = ctk.CTkFrame(self, fg_color=CARD_COLOR)
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
        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(fill="x", pady=(20, 0))

        # IMPORTANT: Action button now calls the controller's save method
        self.btn_action = ctk.CTkButton(frame, text=text, command=self.controller.initiate_save, height=50, fg_color=ACCENT_COLOR, hover_color=ACCENT_COLOR, font=ctk.CTkFont(size=15, weight="bold"))
        self.btn_action.pack(fill="x")

        self.progress = ctk.CTkProgressBar(frame, height=15, progress_color=ACCENT_COLOR)
        self.progress.set(0)

        # Pass references back to controller for progress bar updates/reset
        self.controller.btn_action = self.btn_action
        self.controller.progress = self.progress

    def add_path_selector(self, mode):
        # NOTE: This is a direct copy of your path selector logic
        card = ctk.CTkFrame(self, fg_color=CARD_COLOR, border_width=1, border_color=ACCENT_COLOR)
        card.pack(fill="x", pady=(0, 20), ipadx=10, ipady=10)

        header = ctk.CTkLabel(card, text="TARGET DIRECTORY", font=ctk.CTkFont(size=12, weight="bold"), text_color=ACCENT_COLOR)
        header.pack(anchor="w", padx=10)

        row = ctk.CTkFrame(card, fg_color="transparent")
        row.pack(fill="x", pady=(5, 0), padx=10)

        self.path_entry = ctk.CTkEntry(row, placeholder_text="No directory selected...", text_color="white", fg_color=SIDEBAR_COLOR, border_color=BORDER_COLOR)
        self.path_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        if self.controller.paths[mode]:
            self.path_entry.insert(0, self.controller.paths[mode])

        btn = ctk.CTkButton(row, text="BROWSE", width=100, command=lambda: self.controller.browse_folder(mode, self.path_entry), fg_color=SIDEBAR_COLOR, hover_color=ACCENT_COLOR)
        btn.pack(side="right")
        
        # Store path_entry reference in controller for path selection logic
        self.controller.path_entry = self.path_entry