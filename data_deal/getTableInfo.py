import pandas as pd


def readCSV(business_info, invest_abroad, owing_tax_info, tax_level):
    business_info = pd.read_csv(f'data_tables/{business_info}.csv')
    invest_abroad = pd.read_csv(f'data_tables/{invest_abroad}.csv')
    owing_tax_info = pd.read_csv(f'data_tables/{owing_tax_info}.csv')
    tax_level = pd.read_csv(f'data_tables/{tax_level}.csv')
    tables = [business_info, invest_abroad, owing_tax_info, tax_level]
    return tables


def getTableInfo(tables):
    business_info = tables[0]
    invest_abroad = tables[1]
    owing_tax_info = tables[2]
    tax_level = tables[3]
    # 缺失值占比
    business_info_lost = ((business_info.isnull().sum()) / business_info.shape[0]).sort_values(ascending=False).map(
        lambda x: "{:.2%}".format(x))
    invest_abroad_lost = ((invest_abroad.isnull().sum()) / invest_abroad.shape[0]).sort_values(ascending=False).map(
        lambda x: "{:.2%}".format(x))
    owing_tax_info_lost = ((owing_tax_info.isnull().sum()) / owing_tax_info.shape[0]).sort_values(ascending=False).map(
        lambda x: "{:.2%}".format(x))
    tax_level_lost = ((tax_level.isnull().sum()) / tax_level.shape[0]).sort_values(ascending=False).map(
        lambda x: "{:.2%}".format(x))
    print(business_info_lost)
    print(invest_abroad_lost)
    print(owing_tax_info_lost)
    print(tax_level_lost)

    # 四表维度
    print("四表维度")
    print(business_info.shape, invest_abroad.shape, owing_tax_info.shape, tax_level.shape)
    # 四表字段
    print("四表字段")
    print(business_info.columns, invest_abroad.columns, owing_tax_info.columns, tax_level.columns)


if __name__ == '__main__':
    tables = ['business_info', 'invest_abroad', 'owing_tax_info', 'tax_level']
    tables = readCSV(tables[0], tables[1], tables[2], tables[3])
    getTableInfo(tables)
