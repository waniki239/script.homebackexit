# Home Back Exit

![Kodi](https://img.shields.io/badge/Kodi-21%20(Omega)-17B2E7)
![License](https://img.shields.io/badge/License-MIT-green)

A lightweight Kodi addon that installs a keymap to open the **Shutdown Menu** when the **Back** button is pressed on the Kodi Home screen.

---

## Features

- ✅ Install the Home screen Back button keymap
- ✅ Remove the installed keymap
- ✅ Lightweight
- ✅ No background service
- ✅ Kodi 21 (Omega) compatible

---

## Installation

1. Download the latest release ZIP.
2. In Kodi, open **Settings → Add-ons**.
3. Select **Install from ZIP file**.
4. Choose the downloaded ZIP file.
5. Open **Programs** and run **Home Back Exit**.

---

## Usage

When you launch the addon:

- If the keymap is **not installed**, you will be prompted to install it.
- If the keymap **is already installed**, you will be prompted to remove it.

Restart Kodi after installing or removing the keymap for the changes to take effect.

---

## Project Structure

```text
script.homebackexit/
├── addon.py
├── addon.xml
├── changelog.txt
├── LICENSE
├── README.md
└── resources/
    ├── icon.png
    ├── fanart.png
    └── keymaps/
        └── homebackexit.xml
```

---

## Compatibility

| Kodi Version | Status |
|--------------|--------|
| 21 (Omega) | ✅ Supported |

---

## Roadmap

### v0.1.0

- [x] Install bundled keymap
- [x] Remove installed keymap
- [x] Installation detection
- [x] Installation confirmation
- [x] Restart notification

### Planned

- [ ] Localization
- [ ] Configurable actions
- [ ] Additional keymap presets

---

## License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.