import sys
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    print("Please input exactly three command-line arguments")
    sys.exit(1)
else:
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    if "." not in input_file_name or "." not in output_file_name:
        print("Please input valid file names with dots (.)")
        sys.exit(1)
    else:
        input_splitted = input_file_name.split(".")
        output_splitted = output_file_name.split(".")

        if input_splitted[-1] != "jpg" or output_splitted[-1] != "jpg":
            print("Please input valid JPG file names")
            sys.exit(1)
        else:
            base_image = Image.open(input_file_name)
            shirt_image = Image.open("shirt.png")

            # Get size of shirt
            size = shirt_image.size

            # Resize the input image to the size of the shirt image
            resized_base_image = ImageOps.fit(base_image, size)

            # Paste the shirt image onto the new base image
            resized_base_image.paste(shirt_image, shirt_image)

            # Save the result image
            resized_base_image.save(output_file_name, "JPEG")
