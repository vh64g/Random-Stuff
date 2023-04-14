from pynput.mouse import Listener
import logging
import time

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_scroll(x, y, dx, dy):
    print('Mouse scrolled at ({0}, {1})({2}, {3}) {4}'.format(x, y, dx, dy, time.asctime()))
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3}) {4}'.format(x, y, dx, dy, time.asctime()))

with Listener(on_scroll=on_scroll) as listener:
    listener.join()
