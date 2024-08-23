# GLOW EFFECT FOR PNG IMAGES

=============================

This is a Python script that converts black pixels to white pixels in images. It processes all image files (png, jpg, jpeg, bmp, tiff, gif) in the current working directory and saves the modified images in a new "output" directory.

## How to Use

1. Save this script as a Python file (e.g., `image_converter.py`).
2. Place the script in the directory containing the images you want to process.
3. Run the script using Python (e.g., `python image_converter.py`).
4. The script will create a new "output" directory and save the modified images there.

## Script Explanation

The script consists of two functions:

- `convert_black_to_white(image_path, output_path)`: This function takes an image file path as input, converts black pixels to white, and saves the modified image to the specified output path.
- `process_images_in_directory()`: This function loops through all files in the current working directory, checks if they are image files, and applies the `convert_black_to_white` function to each image.

The script uses the Python Imaging Library (PIL) to manipulate the images.

## Note

You can adjust the threshold value in the `convert_black_to_white` function to change the definition of "black" pixels. Currently, it considers pixels with RGB values less than 50 as black.
<img src="https://img.shields.io/badge/PYTHON-black?style=for-the-badge&logo=python&logoColor=gold"/>
