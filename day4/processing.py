import os
import threading
import time

from matplotlib import image as mpimg, pyplot as plt

from day2.percentile_image import rgb2gray, get_image_segmented
from day4.queue_thread_safe import Queue

queue_a = Queue()
queue_b = Queue()


def watch_directory(dir_path):
    global queue_a
    while True:
        onlyfiles = os.listdir(dir_path)
        for name in onlyfiles:
            full_path = os.path.join(dir_path, name)
            x = mpimg.imread(full_path)
            queue_a.push({'image': x, 'name': name})
            os.remove(full_path)
            print(f'I just removed the file {full_path}')
        time.sleep(5)


def processing():
    global queue_a, queue_b
    while True:
        dict = queue_a.b_pop()
        x = dict['image']
        gray = rgb2gray(x)
        after_processing = get_image_segmented(gray)
        new_dict = {'image': after_processing, 'name': dict['name']}
        queue_b.push(new_dict)
        time.sleep(5)


def saving_bla(output_path):
    global queue_b
    while True:
        dict = queue_b.b_pop()
        save_path = os.path.join(output_path, dict['name'])
        plt.imsave(save_path, dict['image'], cmap='gray')
        time.sleep(5)


input_path = r'C:\Users\IITC\PycharmProjects\pythonProject\input'
output_path = r'C:\Users\IITC\PycharmProjects\pythonProject\output'
threading.Thread(target=watch_directory, args=(input_path,)).start()
threading.Thread(target=processing).start()
threading.Thread(target=saving_bla, args=(output_path,)).start()
