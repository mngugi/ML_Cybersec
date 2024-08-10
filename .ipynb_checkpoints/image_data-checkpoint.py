from PIL import Image

def calculate_image_size(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Get image dimensions
        width, height = img.size
        # Calculate the number of pixels
        num_pixels = width * height
        # Determine the number of color channels (assuming RGB format)
        num_channels = len(img.getbands())  # Typically 3 for RGB
        # Calculate the total number of bytes
        total_bytes = num_pixels * num_channels
        
        return width, height, num_pixels, num_channels, total_bytes

# Specify the path to your image file
image_path = '/####/xxxxx/Pictures/faketwitter.png'

# Get the image size information
width, height, num_pixels, num_channels, total_bytes = calculate_image_size(image_path)

print(f"Image dimensions: {width}x{height}")
print(f"Number of pixels: {num_pixels}")
print(f"Number of color channels: {num_channels}")
print(f"Total number of bytes: {total_bytes}")
