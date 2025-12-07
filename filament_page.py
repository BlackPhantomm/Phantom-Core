# pages/filament_page.py

from base_page import BasePage

class FilamentPage(BasePage):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, controller, **kwargs)
        self.controller.current_mode = "filament"
        self.render_ui()

    def render_ui(self):
        self.add_title("FILAMENT PROTOCOL")
        self.add_path_selector("filament")

        # Identity Card
        card_id = self.create_card("IDENTITY")
        self.entry_name = self.create_field(card_id, "Display Name", "e.g. Phantom PLA+")
        self.entry_material = self.create_field(card_id, "Material Type", "PLA")
        self.entry_color = self.create_field(card_id, "Color Hex", "#0000FF")

        # Thermal Physics Card (RESTORED)
        card_temp = self.create_card("THERMAL PHYSICS")
        self.entry_temp = self.create_field(card_temp, "Nozzle Temperature (°C)", "210")
        self.entry_bed = self.create_field(card_temp, "Bed Temperature (°C)", "60")

        self.add_action_button("GENERATE FILAMENT")

        # IMPORTANT: Pass field references to the controller for use in save_file
        self.controller.page_fields = {
            'entry_name': self.entry_name,
            'entry_temp': self.entry_temp,
            'entry_bed': self.entry_bed,
        }