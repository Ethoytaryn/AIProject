import tensorflow as tf


def load_img(list_file_name):
    filename_queue = tf.train.string_input_producer(list_file_name)
    reader = tf.WholeFileReader()
    key, value = reader.read(filename_queue)
    return tf.image.decode_jpeg(value)


def adapter_img_to_neuronal_network(img_tensor, shape):
    return tf.image.resize_images(tf.image.rgb_to_grayscale(img_tensor), shape)


def adapter_response(neuronal_network_array_response):
    assert (len(neuronal_network_array_response) == 10), "La réponse du neurone doit être une Array de longeur 10"
    response = "0123456789"
    position = neuronal_network_array_response.index(1)
    return response[position]


def print_response(filename, response):
    print("L'image " + filename + " représente un " + response + ".")
