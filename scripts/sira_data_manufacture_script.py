import argparse

import pandas as pd

from scripts.feeds.sira_asm_data_generate import *


def generate_data(x):
    sira_asm_data = {}

    sira_asm_data_path = args.out_path + "sira_asm_src_data.txt"

    for i in range(0, x):
        maptyid = str(random.randint(1000, 9999)).rjust(10, '0')
        japtyid = str(random.randint(1000, 9999)).rjust(10, '0')
        asm_src_data(i, sira_asm_data, maptyid,japtyid)

    sira_asm_data_df = pd.DataFrame(sira_asm_data).transpose()

    sira_asm_data_df.to_csv(sira_asm_data_path, sep='|', encoding='utf-8', index=False, header=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_path', dest='out_path', required=True, help='outfile')
    args = parser.parse_args()
    generate_data(100)
