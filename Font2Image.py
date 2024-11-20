import os
from PIL import Image, ImageDraw, ImageFont

def hex_to_rgb(hex_color: str) -> tuple:
    """
    Converts a hex color code to an RGB tuple.
    """
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def list_fonts_in_directory():
    """
    Lists all .ttf and .otf font files in the current directory.
    """
    return [f for f in os.listdir() if f.lower().endswith(('.ttf', '.otf'))]

def convert_font_to_images(font_path: str, output_color: tuple = (0, 0, 0)):
    """
    Converts a font file to individual letter images.
    """
    img_size = (400, 400)
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!?.,:;"
    
    try:
        font_name = os.path.splitext(os.path.basename(font_path))[0]
        font = ImageFont.truetype(font_path, size=300)
    except Exception as e:
        print(f"Error loading font: {e}")
        return

    output_dir = f"{font_name}_images"
    os.makedirs(output_dir, exist_ok=True)
    
    for char in characters:
        img = Image.new("RGBA", img_size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        
        # Calculate text bounding box to center the character
        bbox = font.getbbox(char)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        position = ((img_size[0] - text_width) // 2, (img_size[1] - text_height) // 2)

        draw.text(position, char, fill=output_color, font=font)

        img_path = os.path.join(output_dir, f"{char}.png")
        img.save(img_path)
        print(f"Saved: {img_path}")
    
    print(f"All images saved in folder: {output_dir}")

def main():
    fonts = list_fonts_in_directory()
    if not fonts:
        print("No font files (.ttf, .otf) found in the current directory.")
        return

    print("Enter font choice to turn into images:")
    for idx, font in enumerate(fonts, start=1):
        print(f"{idx}. {font}")

    try:
        choice = int(input("Enter the number corresponding to your font choice: "))
        if choice < 1 or choice > len(fonts):
            raise ValueError
    except ValueError:
        print("Invalid choice. Please enter a number from the list.")
        return

    selected_font = fonts[choice - 1]
    print(f"Selected font: {selected_font}")

    try:
        hex_color = input("Enter hex code color for the font's images (e.g., #FF5733 or press Enter for black): ")
        output_color = hex_to_rgb(hex_color) if hex_color else (0, 0, 0)
    except Exception as e:
        print(f"Invalid hex color. Defaulting to black. Error: {e}")
        output_color = (0, 0, 0)

    convert_font_to_images(selected_font, output_color)

if __name__ == "__main__":
    main()
