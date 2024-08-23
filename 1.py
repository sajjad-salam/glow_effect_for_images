import os
from PIL import Image


def convert_black_to_white(image_path, output_path):
    # Open the image
    img = Image.open(image_path).convert("RGBA")

    # Load pixel data
    pixels = img.load()

    # Get dimensions of the image
    width, height = img.size

    # Loop over each pixel and change black to white
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            # Check if the pixel is black (you can adjust the threshold if necessary)
            if r < 50 and g < 50 and b < 50:
                pixels[x, y] = (255, 255, 255, a)

    # Save the modified image
    img.save(output_path)


def process_images_in_directory():
    # Get the current working directory
    current_dir = os.getcwd()

    # Create the output directory if it doesn't exist
    output_dir = os.path.join(current_dir, "output")
    os.makedirs(output_dir, exist_ok=True)

    # Loop through all files in the current directory
    for filename in os.listdir(current_dir):
        # Check if the file is an image (you can add more extensions if needed)
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')):
            input_path = os.path.join(current_dir, filename)
            output_path = os.path.join(output_dir, filename)
            convert_black_to_white(input_path, output_path)
            print(f"Processed {filename} -> {output_path}")


# Example usage
process_images_in_directory()
