from PIL import Image
import pyautogui
import sqlite3

"""
The general idea behind this image and datamining script is to capture a section of the screen
on the trading view website. The criteria for this is to capture an area of 100 bars on the 1H
time frame. After every image, we then use keyboard inputs to label the image. After this,
100 bars are then passed allow us to see the after results, where more labeling can occur. 
In addition to this, this new 'after' image is a new 'before' image for another training image.
Each image will have three labels to it

"""

class DataMining:
    

    def __init__(self, db_path = 'trading_data.db'):
        self.db_connection = sqlite3.connect(db_path)
        self.db_cursor = self.db_connection.cursor()
        self.current_bars = self.screenshot()


    def create_table(self):
        self.db_cursor.execute('''
            CREATE TABLE IF NOT EXISTS trading_data (                       
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_data BLOB,                   
                trend TEXT,
                phase TEXT,
                after TEXT               
                )'''
        )               
        self.db_connection.commit()


    # function to take screenshot of the screen in a specified area with specified dimension
    # takes screenshots every hundred bars

    def screenshot(self):
        x = 100
        y = 200
        width = 500
        height = 500
        screenshot = pyautogui.screenshot(region = (x, y, width, height))
        screenshot.show()
        
        return screenshot

    def show_before(self):

        pass


    # after screen shot is taken, take user keyboard input to label image
    # labels cover:
        # trend: [up, down, none]
        # phase: [push, pull, consolidation]  
        
    def pre_labels(self):
        trend_input = input("Enter 1 for 'up', 2 for 'downn', and 3 for 'no trend'")
        trend_labels = {
            '1': 'up', 
            '2': 'down',
            '3': 'no trend'
            }
        trend_label = trend_labels.get(trend_input)
        phase_input = input("Enter 1 for 'push', 2 for 'pullback', 3 for 'consolidation'")
        phase_labels = {
            '1': 'push', 
            '2': 'pullback',
            '3': 'consolidation'
            }
        phase_label = phase_labels.get(phase_input)

        return trend_label, phase_label
    

    # for use to label what happens after
    # label will cover after:
    # [pulled back then pushed, reversed, continued to push, pushed then pulled back, consolidated]       
    def after_label(self):
        after = 1
        pass


    # function to move 100 bars to prepare for screenshots
    @staticmethod
    def move100bars():
        pyautogui.press('left', presses = 100)
 


    # function to save image and corresponding labels to sqlite3 database
    def insert(self, image, trend, phase):
        self.image = image
        self.trend = trend
        self.phase = phase
        insert_query = "INSERT INTO trading_data.db (image, trend, phase) VALUES (?, ?, ?)"
                               

    