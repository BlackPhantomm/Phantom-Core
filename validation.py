# validation.py

def is_valid_numeric(value: str, min_val: float = 0.0, max_val: float = 999.0) -> (bool, str):
    """Checks if the value is a valid number within a specified range."""
    try:
        num = float(value)
        if not (min_val <= num <= max_val):
            return False, f"Value must be between {min_val} and {max_val}."
        return True, ""
    except ValueError:
        return False, "Input must be a valid number."

def validate_protocol_data(mode: str, fields: dict) -> (bool, str):
    """Runs specific validation rules based on the current protocol mode."""
    
    # Check for Name (required in all modes)
    if not fields.get('entry_name').get():
        return False, "The Display Name field is required."

    if mode == "filament":
        temp = fields['entry_temp'].get()
        bed = fields['entry_bed'].get()
        
        # Validate Nozzle Temperature (e.g., 180C to 300C)
        valid, msg = is_valid_numeric(temp, 180, 300)
        if not valid: return False, f"Nozzle Temperature: {msg}"
        
        # Validate Bed Temperature (e.g., 0C to 120C)
        valid, msg = is_valid_numeric(bed, 0, 120)
        if not valid: return False, f"Bed Temperature: {msg}"
        
    elif mode == "process":
        layer = fields['entry_layer'].get()
        infill = fields['entry_infill'].get()
        
        # Validate Layer Height (e.g., 0.05mm to 0.4mm)
        valid, msg = is_valid_numeric(layer, 0.05, 0.4)
        if not valid: return False, f"Layer Height: {msg}"

        # Validate Infill Density (0% to 100%)
        valid, msg = is_valid_numeric(infill, 0, 100)
        if not valid: return False, f"Infill Density: {msg}"
        
    elif mode == "printer":
        size_x = fields['entry_size_x'].get()
        
        # Validate Build Volume X (must be positive)
        valid, msg = is_valid_numeric(size_x, 1, 1000) # Assuming max 1000mm bed
        if not valid: return False, f"Build Volume X: {msg}"
        
    # If all checks pass for the specific mode
    return True, "Data is valid."