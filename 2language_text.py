import argparse
import os
import pandas as pd


def creat(path, en_file_name, ch_file_name):
    with open(os.path.join(path, en_file_name), 'r', encoding='utf-8') as fl:
        en_df = pd.read_csv(fl, sep='\n', header=None)
    with open(os.path.join(path, ch_file_name), 'r', encoding='utf-8') as fl:
        ch_df = pd.read_csv(fl, sep='\n', header=None)
    assert len(en_df) == len(ch_df), 'file length not same'

    new_df = pd.DataFrame(2 * len(en_df) * [''])
    for i in range(len(en_df)):
        new_df.iloc[2*i][0] = en_df.iloc[i][0]
        new_df.iloc[2*i + 1][0] = ch_df.iloc[i][0]

    new_df.to_csv(os.path.join(path, '2language.txt'), sep='\n', index=False, header=False)

if __name__ == '__main__':
    data_path = './data'
    args = argparse.ArgumentParser(description='Specify file name')
    args.add_argument('-e', '--en_file_name', default=None, type=str,
                      help='english file name')
    args.add_argument('-c', '--ch_file_name', default=None, type=str,
                      help='chinese file name')
    args = args.parse_args()

    for name in [args.en_file_name, args.ch_file_name]:
        temp = os.path.join(data_path, name)
        assert os.path.exists(temp), f'file {temp} do not exist'

    creat(data_path, args.en_file_name, args.ch_file_name)
