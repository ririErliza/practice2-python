import PIL.Image

# ascii characters used to build the output text
ASCII_CHARS = ["0", "1", ".", ","]

# resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio=height/width
    new_height = int(new_width*ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grafify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

# convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixels//25] for pixel in pixels])
    return (characters)

def main():
    path=input("Enter a valid pathname to an image:\n")
    try:
        image=PIL.Image.open(path)
    except:
        print(path,"is not a valid pathname to an image")

main()