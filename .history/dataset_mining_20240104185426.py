from PIL import Image
import pyautogui

"""
The general idea behind this image and datamining script is to capture a section of the screen
on the trading view website. The criteria for this is to capture an area of 100 bars on the 1H
time frame. After every image, we then use keyboard inputs to label the image. After this,
100 bars are then passed allow us to see the after results, where more labeling can occur. 
In addition to this, this new 'after' image is a new 'before' image for another training image.
Each image will have three labels to it

"""

class DataMining:
    

    def __init__(self):


        pass


    # function to take screenshot of the screen in a specified area with specified dimension
    # takes screenshots every hundred bars
    @staticmethod
    def screenshot():
        x = 100
        y = 200
        width = 500
        height = 500
        screenshot = pyautogui.screenshot(region = (x, y, width, height))


        return screenshot




    # after screen shot is taken, take user keyboard input to label image
    # labels cover:
        # trend: [up, down, none]
        # phase: [push, pull, consolidation]
        # after: [pulled back then pushed, reversed, continued to push, pushed then pulled back, consolidated]     
    def labels(self):
        
        pass
        

    # function to move 100 bars to prepare for screenshots
    def move100bars(self):

        pass


    # function to save image and corresponding labels to sqlite3 database
    def insert(self):

        pass