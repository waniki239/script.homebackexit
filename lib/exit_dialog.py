import xbmc
import xbmcgui


def main() -> None:
    if xbmcgui.Dialog().yesno(
        heading="Exit Kodi",
        message="Are you sure you want to exit Kodi?"
    ):
        xbmc.executebuiltin("Quit")