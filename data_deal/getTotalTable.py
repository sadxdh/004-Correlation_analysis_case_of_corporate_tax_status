import numpy as np
import pandas as pd


class getTotalTable:
    def __init__(self, tables):
        self.table_names = tables
        self.owing_tax_info = pd.DataFrame()
        self.tax_level = pd.DataFrame()
        self.invest_abroad = pd.DataFrame()
        self.business_info = pd.DataFrame()
        self.total_table = pd.DataFrame()

        for table_name in self.table_names:
            df = pd.read_csv(f'data_tables/{table_name}.csv')
            # 删除GOOD_TAXNUM这个空字段 并更新df
            df = df.dropna(axis=1, how='all')
            if table_name == 'business_info':
                df = df.set_index('COMPANY_NAME')
                self.business_info = df
            elif table_name == 'owing_tax_info':
                df = df.set_index('COMPANY_NAME')
                self.owing_tax_info = df
            elif table_name == 'invest_abroad':
                df = df.set_index('INVES_COMPANY_NAME')
                self.invest_abroad = df
            elif table_name == 'tax_level':
                df = df.set_index('GOOD_NAME')
                self.tax_level = df
                # 343743行
        self.merge_table()
        # print(self.tax_level)

    def merge_table(self):
        self.total_table = pd.merge(self.owing_tax_info.loc[:, ['OWING_TAX_TYPE', 'OWING_TAX_BALANCE', 'OWING_TAX_BALANCE_NOW', 'PROVINCE', 'TAX_AUTHORITY']],
                                    self.tax_level['GOOD_LEVEL'],
                                    right_index=True,
                                    left_index=True)
        # print("total_table:", self.total_table)
        self.total_table = pd.merge(self.invest_abroad.loc[:, ['COMPANY_ID', 'COMPANY_NAME', 'AMOUNT']],
                                    self.total_table,
                                    right_index=True,
                                    left_index=True)
        self.total_table = pd.merge(self.business_info.loc[:, ['ID', 'COMPANY_ORG_TYPE', 'ESTIBLISH_TIME', 'BUSINESS_SCOPE', 'REG_STATUS', 'REG_CAPITAL']],
                                    self.total_table,
                                    right_index=True,
                                    left_index=True)
        print(self.total_table)
        self.total_table.to_csv("data_tables/total_table.csv", encoding='utf-8')


if __name__ == '__main__':
    tables = ['business_info', 'invest_abroad', 'owing_tax_info', 'tax_level']
    getTotalTable(tables)
