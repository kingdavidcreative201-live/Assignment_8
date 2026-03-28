from functools import reduce
from image_lib import Image
   
# add your blur function here
def blur(image):
    def tripleSum(triple1, triple2):
        (r1, g1, b1) = triple1
        (r2, g2, b2) = triple2
        return (r1 + r2, g1 + g2, b1 + b2)
    new = image.clone()
    for y in range(1, image.getHeight() - 1):
        for x in range(1, image.getWidth() - 1):
            oldP = image.getPixel(x, y)      # center
            left = image.getPixel(x - 1, y)  # left neighbor
            right = image.getPixel(x + 1, y) # right neighbor
            top = image.getPixel(x, y - 1)   # top neighbor
            bottom = image.getPixel(x, y + 1) # bottom neighbor
            
            # Sum all 5 pixels using reduce and tripleSum
            sums = reduce(tripleSum, [oldP, left, right, top, bottom])
            
            # Calculate average by dividing each component by 5
            # Using integer division (//) to keep values as integers
            averages = (sums[0] // 5, sums[1] // 5, sums[2] // 5)
            
            # Set the blurred pixel in the new image
            new.setPixel(x, y, averages)
    
    return new

def main():
    my_image = Image("smokey.gif")
    print("Original image:", my_image.getWidth(), "x", my_image.getHeight())
    # call the blur function here
    blurred = blur(my_image)
    # save the blurred image to a PNG file here
    blurred.save("smokey_blurred.png")
    print("Blurred image saved as smokey_blurred.png")

if __name__ == "__main__":
    main()