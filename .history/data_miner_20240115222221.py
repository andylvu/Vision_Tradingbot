from dataset_mining import DataMining
import cv2
import time

def main():

    try:


        data_miner = DataMining()
#       data_miner.create_table() already created
    
        for _ in range(105):

              
            current_image = data_miner.screenshot()
            cv2.imshow('current image', current_image)

            current_binary_image = data_miner.binary_image(current_image)
            trend, phase = data_miner.label1()
            cv2.waitKey(1000)
            cv2.destroyAllWindows()

            data_miner.move100bars()
            next_image = data_miner.screenshot()
            plt.imshow(next_image)
            plt.show(block = False)
            data_miner.left_screen_click()
            after = data_miner.label2()

            plt.close()
            plt.pause(1)
             
            #data_miner.insert_label(current_binary_image, trend, phase, after)
            

        data_miner.db_connection.close()
    
    except KeyboardInterrupt:
        print("\nOperation interrupted. exiting...")
    
    finally:
        if data_miner:
            data_miner.db_connection.close()

if __name__== "__main__":
    main()