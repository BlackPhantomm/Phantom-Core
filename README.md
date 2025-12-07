# PHANTOM CORE v1.0

<img width="554" height="444" alt="{29877968-965F-4C9C-AA32-1FAE8AD2215A}" src="https://github.com/user-attachments/assets/c3dc47af-b389-4b1f-81c1-8fb2cab4301a" />


![Phantom Core Badge](https://img.shields.io/badge/Phantom_Core-v1.0-cyan?style=for-the-badge)
![OpenPrint3D](https://img.shields.io/badge/OpenPrint3D-Compliant-green?style=for-the-badge)

**Phantom Core** is a specialized, dark-mode GUI utility for generating standardized 3D printing metadata. It allows users to create, validate, and secure Filament, Printer, and Process profiles that adhere to the OpenPrint3D JSON schema.

## 🚀 Features

* **Filament Protocol:** Generate profiles for materials (PLA, PETG, ABS) with integrated thermal physics data (Nozzle/Bed temps).
* **Process Configuration:** Define slicer-agnostic print settings (Layer Height, Speed, Infill).
* **Printer Definition:** Create hardware profiles for any 3D printer (Build Volume, Model Info).
* **The Vault (Preview):** A secure steganography suite to embed these JSON profiles inside standard PNG images, allowing for "hidden" data transport.
* **Smart Pathing:** User-defined target directories for organized file generation.

## 🛠️ Installation

### For Users
1.  Download the latest release `PhantomCore.exe`.
2.  Ensure `phantom.ico` and `phantom_logo.png` are in the same folder.
3.  Run the application.

### For Developers
1.  Clone the repository:
    ```bash
    git clone [https://github.com/BlackPhantomm/PhantomCore.git](https://github.com/BlackPhantomm/PhantomCore.git)
    ```
2.  Install dependencies:
    ```bash
    pip install customtkinter pillow
    ```
3.  Run the source:
    ```bash
    python phantom_gui.py
    ```

## 🔮 Roadmap (v2.0+)

The future of Phantom Core lies in the **Vault**. As the OpenPrint3D community evolves, this tool will become the primary method for securely sharing printer profiles embedded within images of the prints themselves.

* [ ] **Vault Activation:** Full implementation of Image Steganography (hiding JSON in PNG pixels).
* [ ] **Cloud Sync:** Optional integration with community profile repositories.
* [ ] **Drag & Drop:** Drag a "Phantom Image" into the app to auto-extract settings.

## 🤝 Contributing

This project is part of the OpenPrint3D initiative. Contributions, forks, and feature requests are welcome to help standardize 3D printing data.

---
*Maintained by BlackPhantomm*
