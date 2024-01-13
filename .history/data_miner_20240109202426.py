from dataset_mining import DataMining
from PIL import Image


def main():

    data_miner = DataMining()
#   data_miner.create_table() already created
    
    current_image = data_miner.screenshot()
    current_image.show()
    current_binary_image = data_miner.binary_image(current_image)
    trend, phase = data_miner.label1()
    data_miner.move100bars()
    next_image = data_miner.screenshot()
    next_image.show()
    after = data_miner.label2
    data_miner.insert_label1(current_binary_image, trend, phase)
    data_miner.insert_label2(after)


if __name__== "__main__":
    main()