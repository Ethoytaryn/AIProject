from PIL import Image
import numpy as np


def load_img(file_name):
    return Image.open(file_name, mode='r').convert('L')


def resized(image, shape):
    return image.resize(shape, Image.ANTIALIAS)


def pil2array(img, pixel_count):
    return np.array(img.getdata(),
                    np.float32).reshape(pixel_count)


def load_array_img(images_filenames, directory_name):
    array_imgs = []
    for filename in images_filenames:
        grey_img = load_img(directory_name+'/'+filename)
        grey_img_resized = resized(grey_img,[28, 28])
        array_img = pil2array(grey_img_resized, 784)
        array_imgs.append(array_img)
    return array_imgs


def print_response(filenames, response):
    for filename in filenames:
        index = filenames.index(filename)
        print("L'image " + filename + " représente un " + str(response[index]) + ".")
