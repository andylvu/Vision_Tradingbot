from dataset_mining import DataMining
from PIL import Image
import matplotlib.pyplot as plt

def main():

    data_miner = DataMining()
#   data_miner.create_table() already created
    
    for _ in range(105):
    
        current_image = data_miner.screenshot()
        plt.imshow(current_image)
        plt.show()
        current_binary_image = data_miner.binary_image(current_image)
        trend, phase = data_miner.label1()

        data_miner.move100bars()
        next_image = data_miner.screenshot()
        plt.imshow(next_image)
        plt.show()
        after = data_miner.label2()
    #    data_miner.insert_label(current_binary_image, trend, phase, after)

    data_miner.db_connection.close()


if __name__== "__main__":
    main()