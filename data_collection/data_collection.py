import pymysql
import pandas as pd
import os


class DataCollection:
    def __init__(self, tables):

        if not os.path.exists("data_tables"):
            os.mkdir("data_tables")
        for table_name in tables:
            self.table_name = table_name

            connect = pymysql.connect(host='10.102.52.248', port=3306, user='root', password='root', database='casepro',
                                      charset='utf8')
            cursor = connect.cursor()
            cursor.execute(f'select * from {self.table_name}')
            result = cursor.fetchall()  # 全量查询结果

            des = cursor.description
            title = [each[0] for each in des]
            cursor.close()
            connect.close()

            # 拿到数据库查询的内容
            result_list = []
            for each in result:
                result_list.append(list(each))

            # 保存成dataframe
            df_dealed = pd.DataFrame(result_list, columns=title)
            # 保存成csv 这个编码是为了防止中文没法保存，index=None的意思是没有行号
            df_dealed.to_csv(f'data_tables/{self.table_name}.csv', index=False, encoding='utf-8')
            print(f'{self.table_name}数据表转存完毕')


if __name__ == '__main__':
    tables = ['business_info', 'invest_abroad', 'owing_tax_info', 'tax_level']
    DataCollection(tables)
