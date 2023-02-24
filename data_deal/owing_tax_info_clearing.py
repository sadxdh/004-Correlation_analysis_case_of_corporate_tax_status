import pandas as pd


def count_null(owing_tax_info):
    # print('缺失值个数：\n{}'.format(owing_tax_info))
    return owing_tax_info.isnull().sum()


def del_line(owing_tax_info):
    null_sum = count_null(owing_tax_info)
    for i in owing_tax_info.index.tolist():
        if null_sum[i] >= len(owing_tax_info.index.tolist()) / 2:  # 删除整列都是空值的列
            del owing_tax_info[i]
    return owing_tax_info


def owing_tax_info_clearing(owing_tax_info: pd.DataFrame) -> pd.DataFrame:
    owing_tax_info = owing_tax_info.dropna(axis=1, how='all')  # 删除整列值为空的列
    owing_tax_info = owing_tax_info.drop_duplicates(keep='first')  # 删除重复行
    return owing_tax_info
