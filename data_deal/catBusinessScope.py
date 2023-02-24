import pandas as pd


# 查看总表 经营范围
def cat(total_table):
    A_point = total_table[total_table['GOOD_LEVEL'] == "A级纳税人"].drop_duplicates(['Unnamed: 0']).reset_index().drop(
        columns='index').reindex()
    B_point = total_table[total_table['GOOD_LEVEL'] == "B级纳税人"].drop_duplicates(['Unnamed: 0']).reset_index().drop(
        columns='index').reindex()
    C_point = total_table[total_table['GOOD_LEVEL'] == "C级纳税人"].drop_duplicates(['Unnamed: 0']).reset_index().drop(
        columns='index').reindex()
    D_point = total_table[total_table['GOOD_LEVEL'] == "C级纳税人"].drop_duplicates(['Unnamed: 0']).reset_index().drop(
        columns='index').reindex()
    print(A_point)
    print(B_point)
    print(C_point)
    print(D_point)


if __name__ == '__main__':
    df = pd.read_csv("data_tables/total_table.csv")
    cat(df)
