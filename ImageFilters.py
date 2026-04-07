# Lab 9 – Image Processing
# Name: Valentina Rodriguez
# Date: 04/07/2026
# Assignment: Lab 9

from PIL import Image


def swapGreenBlue(img):
    """Swap the green and blue values for every pixel in the image."""
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            red, green, blue = pixel[:3]
            if len(pixel) == 4:
                pixels[x, y] = (red, blue, green, pixel[3])
            else:
                pixels[x, y] = (red, blue, green)

    img.save("swapGB.png")


def darken(img, amount):
    """Darken the image by reducing RGB values by the given amount."""
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            red, green, blue = pixel[:3]
            red = max(0, red - amount)
            green = max(0, green - amount)
            blue = max(0, blue - amount)
            if len(pixel) == 4:
                pixels[x, y] = (red, green, blue, pixel[3])
            else:
                pixels[x, y] = (red, green, blue)

    img.save("darkImg.png")


def bwFilter(img):
    """Example function: converts image to grayscale."""
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue = pixels[x, y]
            avg = (red + green + blue) // 3
            pixels[x, y] = (avg, avg, avg)

    img.save("bwImg.png")


def main():
    # Open the image file
    myImg = Image.open("durango.png")

    # Example (already completed)
    # bwFilter(myImg)

    # Uncomment each function as you complete it
    swapGreenBlue(myImg.copy())
    darken(myImg.copy(), 20)


if __name__ == "__main__":
    main()
