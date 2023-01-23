import os
import cv2
import numpy as np
import time
import keyboard



image_folder = 'C:/Users/benth/Documents/Programming Projects/key-display/images/JPG/'
save_folder = 'C:/Users/benth/Documents/Programming Projects/key-display/images/JPG/'
image_filenames = os.listdir(image_folder)

try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicornhathd

char_grid = [[0 for x in range(8)] for y in range(8)]
# for row in char_grid:
    # print(row)

mapping_dict = {}

for i in range(len(image_filenames)):

    char_grid = [[0 for x in range(8)] for y in range(8)]

    # print("Reading image from " + image_folder + image_filenames[i])

    image = cv2.imread(image_folder + image_filenames[i])

    # cv2.imshow(image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to make the image binary
    _, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    binary_image = cv2.rotate(binary_image, cv2.ROTATE_90_CLOCKWISE)
    # Ensure all images are put into an 8x8 grid
    for row_index in range(len(char_grid)):
        for column_index in range(len(char_grid)):
            # Just as some images are smaller than the grid it will be put in
            try:
                char_grid[row_index][column_index] = binary_image[row_index][column_index]
            except:
                pass

    mapping_dict[image_filenames[i][:-4]] = char_grid


# Show number 2

# two = mapping_dict['two']
# unicornhathd.rotation(210)

# for row in range(8):
#     for column in range(8):
#         unicornhathd.set_pixel(column, row, two[column][row], two[column][row], two[column][row])


# unicornhathd.show()
# time.sleep(10)  


def on_press(key):
    unicornhathd.clear()
    if str(key) in mapping_dict.keys():
        char = mapping_dict[key]
        unicornhathd.rotation(210)

        for row in range(8):
            for column in range(8):
                unicornhathd.set_pixel(column, row, char[column][row], char[column][row], char[column][row])

        unicornhathd.show()

# unicornhathd.show()
# time.sleep(10)  

def on_release(key):
    print(f'{key} released')


keyboard.on_press(on_press)
# keyboard.on_release(on_release, keys)

# Run the event loop indefinitely
keyboard.wait(1)



