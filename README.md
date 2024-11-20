# Font2Image

Font2Image is a Python-based tool designed to convert font files (`.ttf` or `.otf`) into high-quality 400x400 transparent background images for each character. This tool is ideal for creating custom emojis, typography assets, or character-based design elements.

---

## Features
- **Supported Formats**: Converts `.ttf` and `.otf` font files.
- **Custom Colors**: Customize character colors using HEX codes (e.g., `#FF0000` for red).
- **Transparent Backgrounds**: Rendered images have a fully transparent background.
- **Simple Wizard Interface**: User-friendly terminal-based wizard for selecting fonts and colors.
- **Batch Processing**: Automatically generates images for uppercase, lowercase, numbers, and basic punctuation.

---

## Installation

### Prerequisites
1. **Python**:
   - Install Python from the [official Python website](https://www.python.org/downloads/).
   - Add Python to your system PATH during installation.

2. **Git**:
   - Install Git from [git-scm.com](https://git-scm.com/) to clone repositories.

### Clone the Repository
To download Font2Image, clone the repository using Git:
```bash
git clone https://github.com/your-username/Font2Image.git
cd Font2Image
```

## Install Dependencies
### Install the required Python libraries:

```bash
pip install -r requirements.txt
```
**Usage**

__Step 1__: Prepare Font Files

Place your `.ttf` or `.otf` font files in the same directory as the script.

__Step 2__: Run the Script
Run the script with:

```bash
python font_to_images_wizard_hex.py
```

__Note__: Use python3 or py instead of python if necessary.

__Step 3__: Follow the Wizard

The script will list all available font files in the directory.

Select a font by typing its corresponding number.

Enter a HEX color code for the text (e.g., `#123ABC`) or press Enter for the default black (`#000000`).

__Step 4__: Check Output

The script will create a folder named `<FontName>`_images containing `.png` files for each character.

## Example Workflow
### Input

Font file: `ExampleFont.ttf`

Color: `#FF5733 (orange)`

### Output

The script will generate:

```css
ExampleFont_images/
  ├── A.png
  ├── B.png
  ├── ...
  ├── 9.png
  ├── !.png
  └── ?.png
  ```
