# PHANTOM CORE v1.0


![Phantom Core Badge](https://img.shields.io/badge/Phantom_Core-v1.0-cyan?style=for-the-badge)
![OpenPrint3D](https://img.shields.io/badge/OpenPrint3D-Compliant-green?style=for-the-badge)

**Phantom Core** is a specialized, dark-mode GUI utility for generating standardized 3D printing metadata. It allows users to create, validate, and secure Filament, Printer, and Process profiles that adhere to the OpenPrint3D JSON schema.

## 🚀 Features

* **Filament Protocol:** Generate profiles for materials (PLA, PETG, ABS) with integrated thermal physics data (Nozzle/Bed temps).
* **Process Configuration:** Define slicer-agnostic print settings (Layer Height, Speed, Infill).
* **Printer Definition:** Create hardware profiles for any 3D printer (Build Volume, Model Info).
* **The Vault (Preview):** A secure steganography suite to embed these JSON profiles inside standard PNG images, allowing for "hidden" data transport.
* **Smart Pathing:** User-defined target directories for organized file generation.


<img width="553" height="440" alt="{5DC12071-8F9D-480A-9D67-143769BAD37E}" src="https://github.com/user-attachments/assets/9a1c2e89-edcb-441a-a52b-7d264ecb1665" />

<img width="554" height="443" alt="{7F7099AB-FA79-4656-9A05-0FB3A8C139A7}" src="https://github.com/user-attachments/assets/61c03844-12d3-4ce6-89db-f8cba5948b4b" />

<img width="554" height="443" alt="{E5D6E6E1-BE26-4738-A157-F32528D6DBF2}" src="https://github.com/user-attachments/assets/b40afe01-0c20-4409-a921-88b2565c23e6" />

<img width="554" height="444" alt="{29877968-965F-4C9C-AA32-1FAE8AD2215A}" src="https://github.com/user-attachments/assets/c3dc47af-b389-4b1f-81c1-8fb2cab4301a" />

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
