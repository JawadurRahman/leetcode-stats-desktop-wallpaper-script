import os
import ctypes
from PIL import Image, ImageDraw, ImageFont

# Function to create an image with a bulleted list
def create_bullet_list_image(image_filename, text_list, image_size=(800, 600), font_size=20):
    # Create a new image with black background
    image = Image.new('RGB', image_size, color='black')
    draw = ImageDraw.Draw(image)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
        print("Custom font not found, using default.")

    # Set starting position for text
    x, y = 50, 50
    bullet = "\u2022"  # Unicode character for bullet point

    # Draw each line of the bullet list
    for item in text_list:
        draw.text((x, y), f"{bullet} {item}", font=font, fill='white')  # White text on black background
        y += font_size + 5  # Adjust line spacing

    # Save the image
    image.save(image_filename)
    print(f"Image saved as {image_filename}")

# Function to set the image as desktop wallpaper
def set_desktop_wallpaper(image_filename):
    image_path = os.path.abspath(image_filename)  # Get full path
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
    print("Wallpaper changed successfully.")

if __name__ == "__main__":
    # List of items for the bullet list
    items = [
        "KCNA course 5 percent daily",
        "Finish Azure AI Hackathon",
        "Apply TO EY",
        "Apply TO visonconsulting",
        "Google Summer OF CODE",
        "Deploy App"
    ]

    # Define image filename
    image_filename = "bullet_list_wallpaper.png"

    # Create the bullet list image
    create_bullet_list_image(image_filename, items)

    # Set the created image as desktop wallpaper
    set_desktop_wallpaper(image_filename)
