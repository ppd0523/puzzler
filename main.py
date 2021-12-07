import os, sys
if getattr(sys, 'frozen', False):
    _path = sys.executable
else:
    _path = __file__

os.chdir(os.path.dirname(os.path.abspath(_path)))

import tkinter as tk
import threading
import glob
from sslog.logger import SimpleLogger
from functools import partial
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchWindowException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

log = SimpleLogger()
driver = None
init_url = 'https://www.google.co.kr'


def open_browser():
    def task():
        global driver
        try:
            windows = driver.window_handles
            if windows:
                return
        except AttributeError as e:
            if driver:
                return

        opt = webdriver.ChromeOptions()
        files = glob.glob('./extensions/*')
        [opt.add_extension(file) for file in files if file.endswith('.crx')]

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=opt)
        driver.get(url=init_url)

    threading.Thread(target=task).start()


def on_text():
    global driver
    log.info(driver.title)


def on_destroy(_root):
    global driver
    if driver:
        try:
            driver.quit()
        except NoSuchWindowException:
            pass
        except WebDriverException:
            pass
    _root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.wm_attributes('-topmost', True)  # Top only
    root.wm_attributes('-transparent', True)  # Allowed transparent

    root.title("Web Controller")
    root.geometry("480x320+100+100")
    # root.attributes('-alpha', 1)
    root.resizable(True, True)

    ########################### Button Frame ###########################
    btn_frame = tk.Frame(root)
    btn_frame.pack(side=tk.LEFT, )

    btn_frame_opt = {
        'master': btn_frame,
        'height': 2,
    }
    btn_pack_opt = {
        'pady': 10,
    }
    btn_open = tk.Button(**btn_frame_opt, text='Open', command=open_browser)
    btn_open.pack(btn_pack_opt)
    btn_start = tk.Button(**btn_frame_opt, text='start', command=open_browser)
    btn_start.pack(btn_pack_opt)
    btn_stop = tk.Button(**btn_frame_opt, text='stop')
    btn_stop.pack(btn_pack_opt)
    ####################################################################

    screen_frame = tk.Frame(root, bg='red')
    screen_frame.pack(side=tk.LEFT, expand=True, fill='both')

    canvas = tk.Canvas(screen_frame, bg='systemTransparent')
    canvas.pack(expand=True, fill='both', padx=5, pady=5)


    ####################################################################
    root.protocol("WM_DELETE_WINDOW", partial(on_destroy, root))
    root.mainloop()