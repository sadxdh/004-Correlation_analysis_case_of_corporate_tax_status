import pandas as pd


def count_null(invest_abroad):
    return invest_abroad.isnull().sum()
    # 得出STAKES_RATIO和INVES_CAPITAL字段整列值都为空，LEGAL_PERSON_NAME(法定代表人)字段缺失1076条


def del_line(invest_abroad: pd.DataFrame):
    invest_abroad = invest_abroad.dropna().reset_index(drop=True)  # 删除含缺失值的行
    invest = invest_abroad.loc[:, ['COMPANY_NAME', 'AMOUNT']]  # 将COMPANY_NAME,AMOUNT字段所在列提取出来
    inves = invest.groupby(['COMPANY_NAME']).sum().sort_values(by='AMOUNT', ascending=False).iloc[:20, :]
    # 将对外投资金额最高的前二十的公司统计出来
    return invest


def invest_abroad_clearing(invest_abroad: pd.DataFrame) -> pd.DataFrame:
    invest_abroad = invest_abroad.dropna(axis=1, how='all')  # 删除整列值为空的列
    invest_abroad = invest_abroad.set_index('INVES_COMPANY_NAME')
    # print(invest_abroad)
    return invest_abroad
