from dataset_mining import DataMining


def main():

    data_miner = DataMining()
#   data_miner.create_table() already created
    current_binary_image = data_miner.current_binary_image
    trend, phase = data_miner.pre_labels()
    data_miner.move100bars()
    data_miner.insert(current_bars, trend, phase)

if __name__== "__main__":
    main()