import os
from PIL import Image, ImageFilter


def add_glow(image_path, output_path, glow_radius=30, glow_intensity=1):
    # Open the image
    img = Image.open(image_path).convert("RGBA")

    # Create a white background image
    white_bg = Image.new("RGBA", img.size, (255, 255, 255, 0))

    # Create the glow effect by blurring the original image
    glow = img.copy().filter(ImageFilter.GaussianBlur(glow_radius))

    # Composite the glow with the white background
    for _ in range(glow_intensity):
        white_bg = Image.alpha_composite(white_bg, glow)

    # Composite the original image on top of the glow effect
    final_img = Image.alpha_composite(white_bg, img)

    # Save the final image
    final_img.save(output_path)


def process_images_for_glow():
    # Get the current working directory
    current_dir = os.getcwd()

    # Create the output_glow directory if it doesn't exist
    output_glow_dir = os.path.join(current_dir, "output_glow")
    os.makedirs(output_glow_dir, exist_ok=True)
    # output_path = os.path.join(current_dir, "Output")

    # Loop through all files in the current directory
    for filename in os.listdir(current_dir):
        # Check if the file is an image (you can add more extensions if needed)
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')):
            input_path = os.path.join(current_dir, filename)
            output_path = os.path.join(output_glow_dir, filename)
            add_glow(input_path, output_path)
            print(f"Processed {filename} -> {output_path}")


# Example usage
process_images_for_glow()
