import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def proportionOfTaxpayersAtAllLevels():
    tax_level = pd.read_csv('data_tables/tax_level.csv')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    # 分组统计
    df = tax_level.groupby('GOOD_LEVEL')['GOOD_NAME'].agg(['count'])
    # 每个级别纳税人总数
    index = list(df.index)
    res = list(df['count'])
    # 画图
    plt.figure(figsize=(16, 14))
    plt.title('各级别纳税人占比', fontdict={'weight': 'normal', 'size': 28})  # 改变图标题字体
    plt.axis('equal')
    plt.pie(res,
            labels=index,
            autopct='%1.1f%%',
            startangle=60,
            textprops={'fontsize': 20},
            #         wedgeprops={'width':0.4,'edgecolor':'k'},
            shadow=True,
            explode=(0.06, 0, 0, 0),
            )
    plt.savefig('charts/各级别纳税人占比.jpg')
    plt.show()


if __name__ == '__main__':
    tax_level = pd.read_csv('data_tables/tax_level.csv')
    proportionOfTaxpayersAtAllLevels(tax_level)
