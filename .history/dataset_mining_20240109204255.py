from PIL import Image
import pyautogui
import sqlite3
import io


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




    # creates the table for the database
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
        image = pyautogui.screenshot(region = (x, y, width, height))
        self.current_image = image

        return image


    # takes the image obtained from the screenshot function and turns it into a BLOB for storage
    def binary_image(self, image):
        image_bytes = io.BytesIO()
        image.save(image_bytes, format = 'PNG')
        binary_image = image_bytes.getvalue()

        return binary_image

    # after screen shot is taken, take user keyboard input to label image
    # labels cover:
        # trend: [up, down, none]
        # phase: [push, pull, consolidation]  
        
    def label1(self):
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
    def label2(self):
        after_input = input("""
                            Enter 1 for 'pulled back then pushed', 2 for 'reversed', 3 for 'continued to push',
                            4 for 'pushed then pulled back', 5 for 'consolidated'
                            """)
        after_labels = {
            '1': 'pulled back then pushed',
            '2': 'reversed',
            '3': 'continued to push',
            '4': 'pushed then pulled back',
            '5': 'consolidated'
            }
        after_label = after_labels.get(after_input)

        return after_label


    # function to move 100 bars to prepare for screenshots

    def move100bars():
        pyautogui.moveTo(1000, 500)
        pyautogui.click
        pyautogui.press('left', presses = 100)
 


    # function to save image and all labels to table
    def insert_label(self, image, trend, phase, after):

        insert_query = "INSERT INTO trading_data (image_data, trend, phase, after) VALUES (?, ?, ?, ?)"
        self.db_cursor.execute(insert_query, (image, trend, phase, after))
        self.db_connection.commit()                       


