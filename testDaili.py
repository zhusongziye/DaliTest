from PIL import Image
import math
import operator
from functools import reduce
from time import sleep
import os
import time
import logging
from PIL import ImageGrab
import ctypes

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='C:\\autotest\\log\\Dali_Test.log',
                    filemode='w')

# logging.info("------------ Start test Dali102 --------------")


def test102():
    time.sleep(3)
    # os.system("C:\\autotest\\run-button.exe")  # run test by autoit3(Nunit-x86)
    os.system("C:\\autotest\\Dali102.exe")  # run dali102 test by autoit3(Nunit-x86)
    logging.info("Open test case success!")

    time.sleep(3)
    while True:
        time.sleep(36000)      # this time according Dali102 test time can setting longer
        # detect the test is or not stop
        os.system("C:\\autotest\\Dali102_stopget.exe")  # get new stop btn pic by autoit3
        logging.info("get new stop btn pic ok!")
        time.sleep(3)

        image1 = Image.open('C:\\autotest\\pic\\Dali102.jpg')
        image2 = Image.open('C:\\autotest\\pic\\stopBtnImage.jpg')  # use for compare with the image1
        logging.info("ready image compare!")

        h1 = image1.histogram()
        h2 = image2.histogram()
        result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))  # Image matching
        # print(result)
        value = int(result)
        # print(value)
        logging.info("get image matching result")

        if value == 0:
            # if is same, save log
            os.system("C:\\autotest\\Dali102_copylog.exe")  # copy test log
            print("copy log successed!")
            os.system("C:\\autotest\\Dali102_savelog.exe")  # paste test log
            print("paste log successed!")
            logging.info("Image are same, save log ok!")
            break

        if value != 0:
            # print("no same,will next cycle")
            logging.info("the image are not same, will compare in next cycle")
            time.sleep(600)

    # shotScreen
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)
        ctypes.windll.kernel32.CloseHandle(whnd)
    img = ImageGrab.grab()
    img.save('C:\\autotest\\pic\\102_result.bmp')  # save shot screen

    os.system("C:\\autotest\\Dali102_close.exe")  # close test
    # print("paste log success!")
    logging.info("close test ok")
    sleep(2)

# logging.info("------------ Start test DaliSRS --------------")


def testSrs():
    time.sleep(3)
    # os.system("C:\\autotest\\run-button.exe")  # run test by autoit3(Nunit-x86)
    os.system("C:\\autotest\\DaliSRS.exe")  # run dali102 test by autoit3(Nunit-x86)
    logging.info("Open test case success!")
    time.sleep(3)

    while True:
        time.sleep(18000)  # # this time according SRS test time can setting longer
        # detect the test is or not stop
        os.system("C:\\autotest\\DaliSRS_stopget.exe")  # get new stop btn pic by autoit3
        logging.info("get new stop btn pic ok!")
        time.sleep(3)

        image1 = Image.open('C:\\autotest\\pic\\DaliSRS.jpg')
        image2 = Image.open('C:\\autotest\\pic\\stopBtnImage.jpg')  # use for compare with the image1
        logging.info("ready image compare!")

        h1 = image1.histogram()
        h2 = image2.histogram()
        result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))  # Image matching
        # print(result)
        value = int(result)
        # print(value)
        logging.info("get image matching result")

        if value == 0:
            # if is same, save log
            os.system("C:\\autotest\\DaliSRS_copylog.exe")  # copy test log
            print("copy log successed!")
            os.system("C:\\autotest\\DaliSRS_savelog.exe")  # paste test log
            print("paste log successed!")
            logging.info("Image are same, save log ok!")
            break

        if value != 0:
            # print("no same,will next cycle")
            logging.info("the image are not same, will compare in next cycle")
            time.sleep(300)

    # shotScreen
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)
        ctypes.windll.kernel32.CloseHandle(whnd)
    img = ImageGrab.grab()
    img.save('C:\\autotest\\pic\\SRS_Result.bmp')  # save shot screen

    os.system("C:\\autotest\\DaliSRS_close.exe")  # close test
    # print("paste log success!")
    logging.info("close test ok")
    sleep(2)

# logging.info("------------ Start test DaliSRS2 --------------")


def testSrs2():
    time.sleep(3)
    # os.system("C:\\autotest\\run-button.exe")  # run test by autoit3(Nunit-x86)
    os.system("C:\\autotest\\DaliSRS2.exe")  # run dali102 test by autoit3(Nunit-x86)
    logging.info("Open test case success!")
    time.sleep(3)

    while True:
        time.sleep(600)   # # this time according SRS2 test time can setting longer
        # detect the test is or not stop
        os.system("C:\\autotest\\DaliSRS2_stopget.exe")  # get new stop btn pic by autoit3
        logging.info("get new stop btn pic ok!")
        time.sleep(3)

        image1 = Image.open('C:\\autotest\\pic\\DaliSRS2.jpg')
        image2 = Image.open('C:\\autotest\\pic\\stopBtnImage.jpg')  # use for compare with the image1
        logging.info("ready image compare!")

        h1 = image1.histogram()
        h2 = image2.histogram()
        result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))  # Image matching
        # print(result)
        value = int(result)
        # print(value)
        logging.info("get image matching result")

        if value == 0:
            # if is same, save log
            os.system("C:\\autotest\\DaliSRS2_copylog.exe")  # copy test log
            print("copy log successed!")
            os.system("C:\\autotest\\DaliSRS2_savelog.exe")  # paste test log
            print("paste log successed!")
            logging.info("Image are same, save log ok!")
            break

        if value != 0:
            # print("no same,will next cycle")
            logging.info("the image are not same, will compare in next cycle")
            time.sleep(300)

    # shotScreen
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)
        ctypes.windll.kernel32.CloseHandle(whnd)
    img = ImageGrab.grab()
    img.save('C:\\autotest\\pic\\SRS2_Result.bmp')  # save shot screen

    os.system("C:\\autotest\\DaliSRS2_close.exe")  # close test
    # print("paste log success!")
    logging.info("close test ok")
    sleep(2)

# logging.info("------------ Start test DaliSRS2 --------------")
if __name__ == "__main__":
    logging.info("------------ Start test Dali102 --------------")
    test102()
    logging.info("------------ Start test DaliSRS --------------")
    testSrs()
    logging.info("------------ Start test DaliSRS2 --------------")
    testSrs2()
    cmd = "taskkill /F /IM cmd.exe"  # kill all cmd process
    os.system(cmd)
    logging.info("kill all cmd process ok!")



