import pandas as pd
from data_deal import business_info_clearing
from data_deal import invest_abroad_clearing
from data_deal import owing_tax_info_clearing
from data_deal import tax_level_clearing


class DataCleaning:
    def __init__(self, tables):
        self.tables = tables
        self.business_info = self.tables[0]
        self.invest_abroad = self.tables[1]
        self.owing_tax_info = self.tables[2]
        self.tax_level = self.tables[3]

    def readCSV(self):
        self.business_info = pd.read_csv(f'data_tables/{self.business_info}.csv')
        self.invest_abroad = pd.read_csv(f'data_tables/{self.invest_abroad}.csv')
        self.owing_tax_info = pd.read_csv(f'data_tables/{self.owing_tax_info}.csv')
        self.tax_level = pd.read_csv(f'data_tables/{self.tax_level}.csv')

    def data_cleaning(self):
        self.business_info = business_info_clearing.business_info_cleaning(self.business_info)
        self.invest_abroad = invest_abroad_clearing.invest_abroad_clearing(self.invest_abroad)
        self.owing_tax_info = owing_tax_info_clearing.owing_tax_info_clearing(self.owing_tax_info)
        self.tax_level = tax_level_clearing.tax_level_clearing(self.tax_level)


if __name__ == '__main__':
    tables = ['business_info', 'invest_abroad', 'owing_tax_info', 'tax_level']
    clearing = DataCleaning(tables)
    clearing.readCSV()
    clearing.data_cleaning()
    print(clearing.business_info.shape)
    print(clearing.invest_abroad.shape)
    print(clearing.owing_tax_info.shape)
    print(clearing.tax_level.shape)
