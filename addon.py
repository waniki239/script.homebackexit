from pathlib import Path

import xbmcaddon
import xbmcgui
import xbmcvfs

KEYMAP_NAME = "homebackexit.xml"

ADDON = xbmcaddon.Addon()

ADDON_DIR = Path(
    xbmcvfs.translatePath(
        ADDON.getAddonInfo("path")
    )
)

RESOURCE_DIR = ADDON_DIR / "resources"

KEYMAP_RESOURCE = (
    RESOURCE_DIR
    / "keymaps"
    / KEYMAP_NAME
)


def install_keymap(destination: Path) -> bool:
    """Install the bundled keymap."""

    destination.parent.mkdir(parents=True, exist_ok=True)

    return xbmcvfs.copy(
        str(KEYMAP_RESOURCE),
        str(destination),
    )


def remove_keymap(keymap_file: Path) -> bool:
    """Remove the installed keymap."""

    if not keymap_file.exists():
        return False

    keymap_file.unlink()

    return True


def main() -> None:
    dialog = xbmcgui.Dialog()

    keymap_dir = Path(
        xbmcvfs.translatePath(
            "special://masterprofile/keymaps"
        )
    )

    keymap_file = keymap_dir / KEYMAP_NAME

    if keymap_file.exists():

        remove = dialog.yesno(
            "Home Back Exit",
            "Home Back Exit is already installed.\n\n"
            "Remove it?"
        )

        if not remove:
            return

        if not remove_keymap(keymap_file):
            dialog.ok(
                "Home Back Exit",
                "Failed to remove Home Back Exit."
            )
            return

        dialog.ok(
            "Home Back Exit",
            "Home Back Exit has been removed.\n\n"
            "Please restart Kodi for the changes to take effect."
        )

        return

    install = dialog.yesno(
        "Home Back Exit",
        "Home Back Exit is not installed.\n\n"
        "Install now?"
    )

    if not install:
        return

    if not install_keymap(keymap_file):
        dialog.ok(
            "Home Back Exit",
            "Failed to install Home Back Exit."
        )
        return

    dialog.ok(
        "Home Back Exit",
        "Home Back Exit has been installed.\n\n"
        "Please restart Kodi for the changes to take effect."
    )


if __name__ == "__main__":
    main()