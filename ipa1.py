# This function will convert any picture object to Grayscale.
def convert_to_grayscale(picture):
  # Convert to Grayscale
  for y in range(getHeight(picture)):
    for x in range(getWidth(picture)):
      wm_image_pixel = getPixelAt(picture, x, y)
      red_color = getRed(wm_image_pixel)
      green_color = getGreen(wm_image_pixel)
      blue_color = getBlue(wm_image_pixel)
    
      # Grayscale is average of all the pixels and setting same value for R,G,B
      avg = (red_color + green_color + blue_color) / 3
      combined_color  = makeColor(avg, avg, avg)
      # Set color pixel by pixel
      setColor(wm_image_pixel,  combined_color)
  return picture

# This function will add watermark in the center.
def add_water_mark(building_picture, logo_picture):
  # Get Pixel Details in RGB format
  building_pix = getPixels(building_picture)
  logo_pix = getPixels(logo_picture)
  
  # get Height and width
  building_pic_height = getHeight(building_picture)
  building_pic_width = getWidth(building_picture)

  # get Height and width of logo image
  logo_pic_height = getHeight(logo_picture)  
  logo_pic_width = getWidth(logo_picture)

  # super impose Logo image on main image in the center
  for y in range(logo_pic_height):
    for x in range(logo_pic_width):
      x_center = x + (building_pic_width  - logo_pic_width) / 2  # Calculate X axis center
      y_center = y + (building_pic_height - logo_pic_height) / 2  # Calculate y axis center

      # fetch RGB values of both images
      logo_pixel = getPixelAt(logo_picture, x, y)
      lr = getRed(logo_pixel)
      lg = getGreen(logo_pixel)
      lb = getBlue(logo_pixel)
    
      # Get Pixel Values of Building Pic
      building_pixel = getPixelAt(building_picture, x_center, y_center)
      br = getRed(building_pixel)
      bg = getGreen(building_pixel)
      bb = getBlue(building_pixel)
    
      # Merge pixel by pixel and reducing the color of logo to look as watermark
      # 70% of main color and 30% of logo color
      combined_color  = makeColor(br * 0.7 + int(lr * 0.3), bg * 0.7 + int(lg * 0.3), bb * 0.7 + int(lb * 0.3))
      setColor(building_pixel, combined_color)
      
  # Add thin black color border (4 pixels in width)
  addRect(building_picture, 0, 0, building_pic_width - 1, building_pic_height - 1, black)
  addRect(building_picture, 1, 1, building_pic_width - 3, building_pic_height - 3, black)
  addRect(building_picture, 2, 2, building_pic_width - 5, building_pic_height - 5, black)
  addRect(building_picture, 3, 3, building_pic_width - 7, building_pic_height - 7, black)
  return building_picture

# Pick building pic
building_file = pickAFile()
building_picture = makePicture(building_file)

# Pick Logo File
logo_file = pickAFile()
logo_picture = makePicture(logo_file)

watermarked_image = add_water_mark(building_picture, logo_picture)
writePictureTo(watermarked_image , "c:\Apps\RMIT_photo_colour.jpg")
print "RMIT_photo_colour.jpg Created successfully"

watermarked_image_grayscale = duplicatePicture(watermarked_image)

watermarked_image_grayscale = convert_to_grayscale(watermarked_image_grayscale)
writePictureTo(watermarked_image_grayscale , "c:\Apps\RMIT_photo_grayscale.jpg")
print "RMIT_photo_grayscale.jpg Created successfully"

# Uncomment below lines to see the image
explore(watermarked_image)
explore(watermarked_image_grayscale)
