import re
import subprocess
import time
import os


CAPTURE_FILTER = re.compile(".*YUAN.*", re.IGNORECASE)
STRING_ENCODING = "utf-8"


def verify_capture_board():
    lsmod_proc = subprocess.Popen(['lsusb'], stdout=subprocess.PIPE)
    binary_string = lsmod_proc.communicate()[0]
    string = binary_string.decode(STRING_ENCODING)
    return bool(re.search(CAPTURE_FILTER, string))


def waiting_capture_board():
    while not verify_capture_board():
        print('Waiting Capture Board to be connected')
        time.sleep(10)

    os.system('v4l2-ctl --set-fmt-video=width=3840,height=2160,pixelformat=YU12')
    print('Capture Board was connect')
