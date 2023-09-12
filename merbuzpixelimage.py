from PIL import Image

def merbuzPixelCreate(path_to_image: str, width: int, height: int):
    filename = f'merbuzpixelfile_{path_to_image.split(".")[0]}.merbuzpixel'
    
    base_image = Image.open(path_to_image).convert('RGB') # Convert base image to RGB
    
    rgbImage = base_image.resize((width,height), resample=Image.Resampling.BILINEAR) # Change size to 16 on 16
    
    # Create file for encoding image
    with open(filename, 'w') as file:
        file.write('')
        file.close()
    
    # Write data to file
    with open(filename, 'a') as file:
        index = 0 # Create index of pixels
        for y in range(0, width): 
            for x in range(0, height):
                RGB = rgbImage.getpixel((x,y)) # Get RGB code of pixel
                R,G,B = RGB
                if not (R,G,B) == (0,0,0):
                    file.write(f'{R, G, B, index}') # Write RGB and index to file
                index += 1 
        
        print(f'File succesfly created. Filename: {filename}')
        file.close()
                



