from pathlib import Path

import xbmcvfs
import xbmcgui

KEYMAP_XML = """<?xml version="1.0" encoding="UTF-8"?>
<keymap>
    <Home>
        <keyboard>
            <backspace>ActivateWindow(shutdownmenu)</backspace>
            <escape>ActivateWindow(shutdownmenu)</escape>
        </keyboard>

        <remote>
            <back>ActivateWindow(shutdownmenu)</back>
        </remote>
    </Home>
</keymap>
"""

keymap_dir = Path(
    xbmcvfs.translatePath("special://masterprofile/keymaps")
)

keymap_dir.mkdir(parents=True, exist_ok=True)

keymap_file = keymap_dir / "homebackexit.xml"

keymap_file.write_text(KEYMAP_XML, encoding="utf-8")

xbmcgui.Dialog().ok(
    "Home Back Exit",
    f"Installed:\n{keymap_file}"
)