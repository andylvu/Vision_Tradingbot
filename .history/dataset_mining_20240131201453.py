from PIL import Image, ImageDraw
import pyautogui
import sqlite3
import io
import time

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
        self.db_path = db_path
        self.db_connection = sqlite3.connect(db_path)
        self.db_cursor = self.db_connection.cursor()




    # creates the table for the database
    def create_table(self):
        self.db_cursor.execute('''
            CREATE TABLE IF NOT EXISTS trading_data (                       
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_data BLOB,
                tradable TEXT,                   
                trend TEXT,
                phase TEXT,
                after TEXT               
                )'''
        )               
        self.db_connection.commit()


    # function to take screenshot of the screen in a specified area with specified dimension
    # takes screenshots every hundred bars

    def screenshot(self):
        x = 52
        y = 158
        width = 2061
        height = 721
        image = pyautogui.screenshot(region = (x, y, width, height))
        draw = ImageDraw.Draw(image)
        start_point = (1030, 0)
        end_point = (1030, 721)
        line_color = (255,0,0)
        draw.line([start_point, end_point], fill = line_color, width = 2)

        return image
    
    # cut the image in half only taking the left side to be saved
    def cut_image(self, image):
        left = image.crop((0, 0, 1030, 721))

        return left


    # takes the image obtained from the screenshot function and turns it into a BLOB for storage
    def binary_image(self, image):
        image_bytes = io.BytesIO()
        image.save(image_bytes, format = 'PNG')
        binary_image = image_bytes.getvalue()

        return binary_image

 
    # checks if the current live condition is favorable to trade
    def tradable(self):
        tradable_input = input("Tradable? yes = 1, no = 2")
        tradable_label = {
            '1': 'yes', 
            '2': 'no'
            }
        tradable_label = tradable_label.get(tradable_input)

        if tradable_label is None:
            print('invalid input, enter valid option')
            return self.tradable()

        return tradable_label
    

    def label(self):
        # trend
        trend_input = input("Enter 1 for 'up trend', 2 for 'downn trend', and 3 for 'no trend'")
        trend_labels = {
            '1': 'up', 
            '2': 'down',
            '3': 'no trend'
            }
        trend_label = trend_labels.get(trend_input)

        # current phase
        phase_input = input("Enter 1 for 'push', 2 for 'pullback', 3 for 'consolidation'")
        phase_labels = {
            '1': 'push', 
            '2': 'pullback',
            '3': 'consolidation'
            }
        phase_label = phase_labels.get(phase_input)

        # describe after image
        after_input = input("""
                            Enter 1 for 'continues trend', 
                            2 for 'pull back', 
                            3 for 'breaks structure and reverses',
                            4 for 'consolidates/no trend'
                            """)
        after_labels = {
            '1': 'continues trend',
            '2': 'continues pull back',
            '3': 'breaks structure and reverses',
            '4': 'consolidates/no trend'
            }
        after_label = after_labels.get(after_input)

        if trend_label is None or phase_label is None or after_label is None:
            print('invalid input, enter valid option')
            return self.label()
        
        return trend_label, phase_label, after_label
    



    # function to move 100 bars to prepare for screenshots

    def move100bars(self):
        pyautogui.moveTo(2150, 280)
        pyautogui.doubleClick()
        pyautogui.moveTo(1100, 190)
        pyautogui.dragTo(57, 190, 1, button = 'left')
 
    def left_screen_click(self):
        pyautogui.moveTo(-900, 630)
        pyautogui.click(button = 'left')


    # function to save image and all labels to table
    def insert_label(self, image, trend, phase, after):

        insert_query = "INSERT INTO trading_data (image_data, tradable, trend, phase, after) VALUES (?, ?, ?, ?)"
        self.db_cursor.execute(insert_query, (image, trend, phase, after))
        self.db_connection.commit()                       


