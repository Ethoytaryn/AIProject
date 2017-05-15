import tensorflow as tf


def load_img(list_file_name):
    filename_queue = tf.train.string_input_producer(list_file_name)
    reader = tf.WholeFileReader()
    key, value = reader.read(filename_queue)
    return tf.image.decode_jpeg(value)


def transform_img_to_neuronal_network(image_tensor):
    return tf.image.resize_images(tf.image.rgb_to_grayscale(image_tensor), [28, 28])

