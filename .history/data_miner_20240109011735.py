from dataset_mining import DataMining


def main():

    data_miner = DataMining()
#   data_miner.create_table() already created
    current_bars = data_miner.screenshot()
    trend, phase = data_miner.pre_labels()
    data_miner.move100bars()
#    data_miner.insert(current_bars, trend, phase)

if __name__== "__main__":
    main()