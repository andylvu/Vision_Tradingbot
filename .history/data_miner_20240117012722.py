from dataset_mining import DataMining
from PIL import Image
import os
import time

def main():

    try:


        data_miner = DataMining()
#       data_miner.create_table() already created
    
        for _ in range(3):

              
            whole_image = data_miner.screenshot()
            current_image = data_miner.cut_image(whole_image)
            whole_image.show()
            data_miner.left_screen_click()
            current_binary_image = data_miner.binary_image(current_image)
            trend, phase, after = data_miner.label()


            data_miner.move100bars()


            data_miner.left_screen_click()



            os.system('taskkill /f /im PhotosApp.exe')
            time.sleep(.1)
            data_miner.insert_label(current_binary_image, trend, phase, after)
            

        data_miner.db_connection.close()
    
    except KeyboardInterrupt:
        print("\nOperation interrupted. exiting...")
    
    finally:
        if data_miner:
            data_miner.db_connection.close()

if __name__== "__main__":
    main()