# Ulauncher GreenClip Extension

A Ulauncher extension to integrate with [GreenClip](https://github.com/erebe/greenclip), allowing you to access and search your clipboard history directly from Ulauncher. This extension supports both text and image entries in the clipboard.

## Features

- Access your GreenClip clipboard history from Ulauncher.
- Search through clipboard entries by typing keywords.
- Copy text and image entries back to the clipboard.
- Handles image entries by detecting GreenClip's image cache.

## Requirements

- **GreenClip**: Install GreenClip to manage your clipboard history.
  - GreenClip repository: [GreenClip on GitHub](https://github.com/erebe/greenclip)
  - Install GreenClip with:
    ```bash
    sudo pacman -S greenclip    # For Arch-based distros
    ```
    Or follow the installation instructions from the [GreenClip GitHub repository](https://github.com/erebe/greenclip).

- **xclip**: Required to copy image entries back to the clipboard.
  - Install `xclip` using:
    ```bash
    sudo apt install xclip      # For Debian-based distros
    sudo pacman -S xclip        # For Arch-based distros
    ```

## Installation

1. Install GreenClip and ensure it is configured to manage your clipboard.
2. Install xclip if you want to copy image entries from the clipboard.
3. Download or clone this Ulauncher extension repository into your Ulauncher extensions directory.
4. Restart Ulauncher.

## Configuration

The extension comes with the following configurable options:

- **Copy Keyword**: The keyword used to trigger this extension in Ulauncher (default: `copy`).
- **GreenClip Image Cache Directory**: The directory where GreenClip stores its cached images. The default is `/tmp/greenclip/`, but you can change this if your setup differs.

You can configure these options in the Ulauncher preferences.

## Usage

1. Open Ulauncher and type the keyword `copy` (or whatever you configured).
2. Start typing to search through your clipboard history.
3. Select an entry to copy it back to the clipboard.

- For **text entries**, the selected text will be copied back to the clipboard.
- For **image entries**, the image will be copied back to the clipboard using xclip.

## Developer

- **Name**: Anuragh K P
- **Email**: kpanuragh@gmail.com

## License

This extension is licensed under the MIT License.
