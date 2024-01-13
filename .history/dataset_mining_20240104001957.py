from PIL import Image

"""The general idea behind this image and datamining script is to capture a section of the screen
on the trading view website. The criteria for this is to capture an area of 100 bars on the 1H
time frame. After every image, we then use keyboard inputs to label the image. After this,
100 bars are then passed allow us to see the after results, where more labeling can occur. 
In addition to this, this new 'after' image is a new 'before' image for another training image."""

class DataMining:
    

    # function to take screenshot of the screen in a specified area with specified dimension
    # takes screenshots every hundred bars
    def screenshot():

        pass


    # after screen shot is taken, take user keyboard input to label image
    # labels cover:
        # trend: [up, down, none]
        # phase: [push, pull, consolidation]
        # after: [continues trend, pulls back, breaks trend, consolidates]     
    def labels():
        
        pass
        
    # function to move 100 bars to prepare for screenshots
    def move100bars():


    def insert():

        pass