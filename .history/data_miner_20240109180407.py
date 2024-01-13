from dataset_mining import DataMining


def main():

    data_miner = DataMining()
#   data_miner.create_table() already created
#    current_binary_image = data_miner.current_binary_image
#    current_image = data_miner.current_image
    trend, phase = data_miner.label1()
    data_miner.move100bars()
#    data_miner.insert_label1(current_binary_image, trend, phase)

if __name__== "__main__":
    main()