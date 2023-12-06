from pynput.keyboard import Key, Controller
import time

def file_upload():
    upload_file = 'C:\\Users\\M Ibrahim Dar\\Downloads\\com.afwsamples.testdpc_9.0.1-9001_minAPI21(nodpi)_apkmirror.com.apk'

    keyboard = Controller()
    time.sleep(2)
    keyboard.type(upload_file)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(2)
