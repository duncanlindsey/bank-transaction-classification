'''
Collection of functions for transaction ETL/parsing and machine learning
'''

import re
import numpy as np
import pandas as pd

class Ledger:

    def __init__(self):
        self.ledger = None
        self.date_from = None
        self.date_to = None

    # --- I/O and utility functions

    def add_transactions(self, filepath, filetype):
        methods = {'csv': self.read_data_csv,
                    'text': self.read_data_text}
        df = methods[filetype](filepath)
        df['Account'] = filepath[filepath.find('/')+1:filepath.find(' ')]
        df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format = True)
        if self.ledger is not None:
            self.ledger = pd.concat([self.ledger, df])
        else:
            self.ledger = df
        self.update_meta_data()

    def read_data_csv(self, filepath):
        df = pd.read_csv(filepath)
        return df
    
    def read_data_text(self, filepath):
        values = {'Date': [],
            'Description': [],
            'Amount': [],
            'Balance': []}
        for line in open(filepath):
            if len(line) < 1:
                continue
            sep = ":"
            line = line.replace(u'\n', '')
            line = line.replace(u'\xa0', '')
            line = line.replace(u'\t', '')
            linVec = line.split(sep)
            if linVec[0] not in list(values.keys()):
                continue
            for i in range(1,len(linVec)):
                string = ' '.join(linVec[1:])
            values[linVec[0]].append(string)
        df = pd.DataFrame.from_dict(values)
        return df

    def update_meta_data(self):
        self.date_from = self.ledger['Date'].min()
        self.date_to = self.ledger['Date'].max()

    # --- ETL and parsing functions

    def throw_out_regex(self, col, regex):
        '''Deletes a regex-defined string from a column of the ledger'''
        self.ledger[col] = self.ledger[col].str.replace(regex, '', case = False, flags = re.IGNORECASE)

    def extract_regex(self, col_from, col_to, regex):
        '''Copies a regex-defined string from a column to a new column, before deleting instances
        of the string in the original column'''
        self.ledger[col_to] = self.ledger[col_from].str.extract(regex, flags = re.IGNORECASE, expand = True)
        self.throw_out_regex(col_from, regex)