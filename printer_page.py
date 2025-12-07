# pages/printer_page.py

from base_page import BasePage

class PrinterPage(BasePage):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, controller, **kwargs)
        self.controller.current_mode = "printer"
        self.render_ui()

    def render_ui(self):
        self.add_title("PRINTER PROTOCOL")
        self.add_path_selector("printer")

        # Identity Card
        card_id = self.create_card("PRINTER IDENTIFICATION")
        self.entry_name = self.create_field(card_id, "Printer Display Name", "e.g. Phantom Core-X")
        self.entry_vendor = self.create_field(card_id, "Manufacturer/Vendor", "Custom Build")

        # Build Volume Card
        card_volume = self.create_card("BUILD VOLUME (mm)")
        self.entry_size_x = self.create_field(card_volume, "Bed Size X", "250")
        self.entry_size_y = self.create_field(card_volume, "Bed Size Y", "200")
        self.entry_size_z = self.create_field(card_volume, "Height Z", "300")

        self.add_action_button("GENERATE PRINTER")

        # Pass field references to the controller
        self.controller.page_fields = {
            'entry_name': self.entry_name,
            'entry_size_x': self.entry_size_x,
            'entry_size_y': self.entry_size_y,
            'entry_size_z': self.entry_size_z,
        }