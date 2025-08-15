#!/usr/bin/env python3

import os
from PIL import Image


def main(images_dir):
    # Iterate through all files in the input directory
    for image in os.listdir(images_dir):
        name, ext = os.path.splitext(image)
        image_path = os.path.join(images_dir, image)
        # Check if it's a file, not hidden, and has a supported image extension
        if os.path.isfile(image_path) and not name.startswith('.') and ext.lower().endswith('.tiff'):
            try:
                # Open the image file
                with Image.open(image_path) as im:
                    # The raw images contains alpha transparency layers.
                    # So, it is better to first convert RGBA 4-channel format to RGB 3-channel format before processing the images.
                    # Resize it to 600x400 pixels
                    processed = im.convert('RGB').resize((600, 400))

                    # Create a new filename with .jpeg extension
                    new_name = name + '.jpeg'

                    # Build the full path for the output file
                    output_path = os.path.join(images_dir, new_name)

                    # Save the processed image in JPEG format
                    processed.save(output_path, format='JPEG')

            # Handle any image processing errors (e.g., corrupted files)
            except Exception as e:
                print(f'Failed to process {name}: {e}')


if __name__ == "__main__":
    main("./supplier-data/images/")
