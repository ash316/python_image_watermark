from PIL import Image, ImageOps

border_color = 'black'


def read_image():

    # src_image = "/home/ashish/python/download.jpg"
    # wmImage = "/home/ashish/python/logo.jpg"

    src_image = input('Enter building image path: ')
    wm_image = input('Enter logo image path: ')

    jpeg_image = Image.open(src_image)
    logo_image = Image.open(wm_image)
    
    # Add border
    jpeg_image = ImageOps.expand(jpeg_image, border=4, fill=border_color)

    # Get Pixel Tuple for original Image
    pix = jpeg_image.load()

    # get Height and width
    w1, h1 = jpeg_image.size

    # get Height and width of logo image
    w, h = logo_image.size

    # get pixel object for Logo image
    logo_pix = logo_image.load()

    # superImpose Logo image on main image in the center
    for y in range(h):
        for x in range(w):
            x_center = x + (w1-w) / 2  # Calculate X axis center
            y_center = y + (h1-h) / 2  # Calculate y axis center

            # Add pixels on main image
            pix[x_center, y_center] = logo_pix[x, y]

    # Save the coloured image
    jpeg_image.save("RMIT_photo_colour.jpg")
    print("RMIT_photo_colour.jpg created in home directory with LOGO watermark")

    # Save the Gray scale image
    Image.open("RMIT_photo_colour.jpg").convert('L').save("RMIT_photo_grayscale.jpg")
    print("RMIT_photo_grayscale.jpg created in grayscale mode")


read_image()




