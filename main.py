import os
from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image
from io import BytesIO

# Create a directory to save the bar code
output_dir = 'images'
os.makedirs(output_dir, exist_ok=True)

# Sets the width and height of the image
image_width = 600
image_height = 400

# Open and read the contents of the main.txt file
with open('main.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Process each line and generate a barcode
for idx, line in enumerate(lines):
    content = line.strip()
    
    # Generate a barcode and save it to memory
    barcode = Code128(content, writer=ImageWriter())
    buffer = BytesIO()
    barcode.write(buffer)
    buffer.seek(0)
    
    # Open the generated barcode image
    barcode_image = Image.open(buffer)
    
    barcode_image = barcode_image.resize((image_width, image_height), Image.LANCZOS)

    new_image = Image.new('RGB', (image_width, image_height), 'white')
    
    # Paste barcode image into new image
    new_image.paste(barcode_image, (0, 0))

    # Save the final image
    final_image_path = os.path.join(output_dir, f'final_barcode_{idx}.png')
    new_image.save(final_image_path)

    # Close the image in memory
    buffer.close()

print ("Done.")
