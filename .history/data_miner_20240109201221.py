from dataset_mining import DataMining
from PIL import Image


def main():

    data_miner = DataMining()
#   data_miner.create_table() already created
    
    data_miner.screenshot()
    data_miner.current_image.show()
    trend, phase = data_miner.label1()
    data_miner.move100bars()
    

#    data_miner.insert_label1(current_binary_image, trend, phase)

if __name__== "__main__":
    main()