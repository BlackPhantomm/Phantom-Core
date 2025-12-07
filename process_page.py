# pages/process_page.py

# NOTE: The import below is FIXED to use the simple relative path
from base_page import BasePage

class ProcessPage(BasePage):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, controller, **kwargs)
        self.controller.current_mode = "process"
        self.render_ui()

    def render_ui(self):
        self.add_title("PROCESS PROTOCOL")
        self.add_path_selector("process")

        # Identity Card
        card_id = self.create_card("PROFILE IDENTIFICATION")
        self.entry_name = self.create_field(card_id, "Profile Name", "e.g. Fine Quality PLA")
        self.entry_layer = self.create_field(card_id, "Layer Height (mm)", "0.2")
        self.entry_nozzle = self.create_field(card_id, "Nozzle Diameter (mm)", "0.4")
        self.entry_infill = self.create_field(card_id, "Infill Density (%)", "20")

        # Speed Card
        card_speed = self.create_card("SPEED SETTINGS")
        self.entry_print_speed = self.create_field(card_speed, "Print Speed (mm/s)", "60")
        self.entry_travel_speed = self.create_field(card_speed, "Travel Speed (mm/s)", "150")

        self.add_action_button("GENERATE PROCESS")

        # Pass field references to the controller for use in save_file
        self.controller.page_fields = {
            'entry_name': self.entry_name,
            'entry_layer': self.entry_layer,
            'entry_infill': self.entry_infill,
        }