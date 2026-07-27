from pathlib import Path

import xbmcgui
import xbmcvfs

KEYMAP_NAME = "homebackexit.xml"

keymap_dir = Path(
    xbmcvfs.translatePath("special://masterprofile/keymaps")
)

keymap_file = keymap_dir / KEYMAP_NAME

dialog = xbmcgui.Dialog()

if keymap_file.exists():
    dialog.ok(
        "Home Back Exit",
        "Home Back Exit is already installed."
    )
else:
    dialog.ok(
        "Home Back Exit",
        "Home Back Exit is not installed."
    )