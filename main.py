import os
import re
import subprocess

from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.event import ItemEnterEvent, KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem


class GreenClip(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())  # <-- add this line


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        query = event.get_argument() or ""

        # Get clipboard history from greenclip
        clipboard_data = self.get_greenclip_data()
        pattern = r"[-+]?\d+"
        image_directory = extension.preferences["greenclip_image_cache_directory"]
        filtered_data = [clip for clip in clipboard_data if query.lower() in clip.lower()]
        # Limit the number of items shown to 5 (or adjust as needed)
        # Limit the number of items shown to 5 (or adjust as needed)
        for i, clip in enumerate(filtered_data[:10]):
            # Check if it's an image entry in the format "image/png <id>"
            if clip.startswith("image/png"):
                image_id = re.search(pattern, clip).group()
                image_path = f"{image_directory}{image_id}.png"
                if os.path.exists(image_path):
                    items.append(
                        ExtensionResultItem(
                            icon=image_path,
                            name=f"Image Clipboard {i + 1}",
                            description=f"Image ID: {image_id}",
                            on_enter=ExtensionCustomAction(image_path),
                        )
                    )
                else:
                    # If image path doesn't exist, show an error item
                    items.append(
                        ExtensionResultItem(
                            icon="images/error_icon.png",
                            name=f"Image Clipboard {i + 1} (Error)",
                            description=f"Image file not found: {image_path}",
                        )
                    )
            else:
                # Handle normal text clipboard entry
                items.append(
                    ExtensionResultItem(
                        icon="images/logo.png",
                        name=f"Clipboard {i + 1}",
                        description=clip,
                        on_enter=ExtensionCustomAction(clip),
                    )
                )

        return RenderResultListAction(items)

    def get_greenclip_data(self):
        try:
            # Run the greenclip print command and capture the output
            result = subprocess.run(
                ["greenclip", "print"], stdout=subprocess.PIPE, text=True
            )
            # Split the output into lines (each clipboard entry)
            clipboard_history = result.stdout.splitlines()
            return clipboard_history
        except Exception as e:
            print(f"Error occurred: {e}")
            return []


class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        # event is instance of ItemEnterEvent

        data = event.get_data()
        print("Image path:")
        print(data)
        self.inner_action(data)

        # do additional actions here...

        # you may want to return another list of results

    def inner_action(self, image_path):
        try:
            print("Copying image to clipboard: " + image_path)
            # Use xclip or xsel to copy image to clipboard
            subprocess.run(
                [
                    "xclip",
                    "-selection",
                    "clipboard",
                    "-t",
                    "image/png",
                    "-i",
                    image_path,
                ]
            )
        except Exception as e:
            print(f"Error copying image to clipboard: {e}")


if __name__ == "__main__":
    GreenClip().run()
