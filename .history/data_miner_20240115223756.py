from dataset_mining import DataMining
from PIL import Image
import os
import time

def main():

    try:


        data_miner = DataMining()
#       data_miner.create_table() already created
    
        for _ in range(105):

              
            current_image = data_miner.screenshot()
            current_image.show()

            current_binary_image = data_miner.binary_image(current_image)
            trend, phase = data_miner.label1()
            current_image.close()

            data_miner.move100bars()
            next_image = data_miner.screenshot()
            next_image.show()
            data_miner.left_screen_click()
            after = data_miner.label2()


            next_image.close()
            time.sleep(2)
            #data_miner.insert_label(current_binary_image, trend, phase, after)
            

        data_miner.db_connection.close()
    
    except KeyboardInterrupt:
        print("\nOperation interrupted. exiting...")
    
    finally:
        if data_miner:
            data_miner.db_connection.close()

if __name__== "__main__":
    main()