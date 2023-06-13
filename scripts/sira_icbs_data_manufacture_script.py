import argparse
import pandas as pd

from scripts.feeds.sira_icbs_data_generate import *

def generate_data(x):
    sira_icbs_data = {}
    sira_icbs_data_path = args.out_path + "sira_icbs_src_data.txt"
    for i in range(0, x):
        sira_icbs_src_data(i, sira_icbs_data)

    sira_icbs_data_df = pd.DataFrame(sira_icbs_data).transpose()
    sira_icbs_data_df.to_csv(sira_icbs_data_path, sep='|', encoding='utf-8', index=False, header=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_path', dest='out_path', required=True, help='outfile')
    args = parser.parse_args()
    generate_data(100)
