import pandas as pd


def count_null(business_info):
    return business_info.isnull().sum()
    # 得出STAKES_RATIO和INVES_CAPITAL字段整列值都为空，LEGAL_PERSON_NAME(法定代表人)字段缺失1076条


def business_info_cleaning(business_info: pd.DataFrame) -> pd.DataFrame:
    business_info = business_info.dropna(axis=1, how='all')  # 删除整列值为空的列
    business_info = business_info.set_index('COMPANY_NAME')
    # print(business_info)
    return business_info
