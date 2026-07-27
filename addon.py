from pathlib import Path

import xbmcgui
import xbmcvfs

KEYMAP_NAME = "homebackexit.xml"

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


def install_keymap(keymap_file: Path) -> None:
    """Install the Home Back Exit keymap."""

    keymap_file.parent.mkdir(parents=True, exist_ok=True)
    keymap_file.write_text(KEYMAP_XML, encoding="utf-8")


def main() -> None:
    dialog = xbmcgui.Dialog()

    keymap_dir = Path(
        xbmcvfs.translatePath("special://masterprofile/keymaps")
    )

    keymap_file = keymap_dir / KEYMAP_NAME

    if keymap_file.exists():
        dialog.ok(
            "Home Back Exit",
            "Home Back Exit is already installed."
        )
        return

    install = dialog.yesno(
        "Home Back Exit",
        "Home Back Exit is not installed.",
        "",
        "Install now?"
    )

    if not install:
        return

    install_keymap(keymap_file)

    dialog.ok(
        "Home Back Exit",
        "Home Back Exit has been installed.\n\n"
        "Please restart Kodi for the changes to take effect."
    )


if __name__ == "__main__":
    main()