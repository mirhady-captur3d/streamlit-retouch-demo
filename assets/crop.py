from PIL import Image
import os

# Function to crop an image into 4 sections

def crop_image(image_path, prefix):
    # Open the image
    image = Image.open(image_path)
    width, height = image.size

    # Calculate the middle points
    mid_width = width // 2
    mid_height = height // 2

    # Define the crop boxes
    boxes = [
        (0, 0, mid_width, mid_height),           # Top-left
        (mid_width, 0, width, mid_height),       # Top-right
        (0, mid_height, mid_width, height),      # Bottom-left
        (mid_width, mid_height, width, height)   # Bottom-right
    ]

    # Create a directory to store cropped images
    output_dir = os.path.dirname(image_path)

    # Crop and save the images
    for i, box in enumerate(boxes, 1):
        cropped_image = image.crop(box)
        output_file = os.path.join(output_dir, f"{prefix}_{i}.jpg")
        cropped_image.save(output_file)
        print(f"Saved: {output_file}")

# Paths to the input files
file1 = "11_after.jpg"
file2 = "11_upscaled.jpg"

# Crop both files
crop_image(file1, "11_after")
crop_image(file2, "11_upscaled")
