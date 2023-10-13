from PIL import Image

def divide_image(image_path, num_rows, num_cols):
    img = Image.open(image_path)
    width, height = img.size

    if num_rows * num_cols != 100:
        raise ValueError("Number of rows times number of columns should be 100")

    part_width = width // num_cols
    part_height = height // num_rows

    parts = []

    for i in range(num_rows):
        for j in range(num_cols):
            left = j * part_width
            upper = i * part_height
            right = left + part_width
            lower = upper + part_height
            part = img.crop((left, upper, right, lower))
            parts.append(part)

    return parts

if __name__ == "__main__":
    image_path = "path_to_your_image.jpg"  # Replace with your image path
    num_rows = 10
    num_cols = 10

    try:
        parts = divide_image(image_path, num_rows, num_cols)
        for i, part in enumerate(parts):
            part.save(f"part_{i}.jpg")
    except Exception as e:
        print(f"Error: {e}")
