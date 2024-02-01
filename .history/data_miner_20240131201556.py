from dataset_mining import DataMining
from PIL import Image
import os
import time

def main():

    try:


        data_miner = DataMining()
#        data_miner.create_table() 
    
        for _ in range(3):
            # obtain the screenshot of the trading screen and area 
            whole_image = data_miner.screenshot()
            
            # obtain the left side of the trading space 
            # represents what is currently 'live' to feed into CNN
            current_image = data_miner.cut_image(whole_image)

            # show the entire trading space
            whole_image.show()

            # use this specified left screen click to help with image tagging flow
            # deliberately click on the cmd terminal
            data_miner.left_screen_click()

            # convert the current 'live' left side of the image to bianry values 
            # store into DB as BLOB
            current_binary_image = data_miner.binary_image(current_image)

            # check if the current live condition is tradable
            tradable = data_miner.tradable()

            # if trading conditions are not favorable
            if tradable == 'no':
                trend, phase, after = 'null'
                data_miner.insert_label(current_binary_image, tradable, trend, phase, after)

            # if trading conditions are favorable
            else:

                trend, phase, after = data_miner.label()
                data_miner.insert_label(current_binary_image, tradable, trend, phase, after)

            # use mouse to move close to 100 bars for new image
            data_miner.move100bars()

            # click only to the left screen where the cmd terminal is for easy labeling
            data_miner.left_screen_click()

            # close the default microsoft image viewer 
            os.system('taskkill /f /im PhotosApp.exe')

            # sleep one second so that the image viewer animation can properly close
            time.sleep(.1)
            
            

        data_miner.db_connection.close()
    
    except KeyboardInterrupt:
        print("\nOperation interrupted. exiting...")
    
    finally:
        if data_miner:
            data_miner.db_connection.close()

if __name__== "__main__":
    main()