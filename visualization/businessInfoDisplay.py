import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Timeline, Grid, Bar, Map, Line, Pie
from pyecharts.globals import ThemeType
from collections import Counter
import matplotlib.pyplot as plt
import os


def topTenEnterprisesInTheProvince1(business_info):
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 观察省份占比
    relation1 = business_info.PROVINCE
    relation2 = Counter(relation1).most_common(10)
    x = ['广东', '浙江', '山东', '江苏', '河南', '四川', '安徽', '河北', '云南', '上海']
    y = [i[1] for i in relation2]
    pie = (
        Pie(init_opts=opts.InitOpts())
            .add("", [list(i) for i in zip(x, y)])
            .set_global_opts(title_opts=opts.TitleOpts(title="省份企业数前十"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    )
    # pie.render_notebook()
    pie.render("charts/省份企业数前十1.html")


def topTenEnterprisesInTheProvince2(business_info):
    data = business_info
    # 字段全部输出
    pd.set_option('display.max_columns', 35)
    data['REG_CAPITAL_NUM'] = data['REG_CAPITAL_NUM'].astype('object')
    # 滤除元素都是NaN值的行和列
    data.dropna(axis=0, how="all")
    data.dropna(axis=1, how="all")
    # 删除ID,公司名称重复项，保留最后一项
    data.drop_duplicates(subset=["ID"], keep="last")
    # 查看缺失值占比，删除占比高，数据意义不大的字段
    missing = ((data.isnull().sum()) / data.shape[0]).sort_values(ascending=False).map(lambda x: "{:.2%}".format(x))
    # (例如：实收注册资金，上市代码，组织机构批准单位，对应的新公司ID，公司英文名称,营业期限终止日期)
    datas = data.drop(["ACTUAL_CAPITAL", "LIST_CODE", "FORMER_NAME",
                       "ORG_APPROVED_INSTITUTE", "NEW_COM_ID", "COMPANY_ENNAME",
                       "TO_TIME"], axis=1)
    # 中文省份替换英文缩写
    datas = datas.mask(datas == 'BJ', '北京')
    datas = datas.mask(datas == 'HEN', '河南')
    datas = datas.mask(datas == 'TJ', '天津')
    datas = datas.mask(datas == 'HLJ', '黑龙江')
    datas = datas.mask(datas == 'GD', '广东')
    datas = datas.mask(datas == 'LN', '辽宁')
    datas = datas.mask(datas == 'SH', '上海')
    datas = datas.mask(datas == 'SC', '四川')
    datas = datas.mask(datas == 'ZJ', '浙江')
    datas = datas.mask(datas == 'JS', '江苏')
    datas = datas.mask(datas == 'JX', '江西')
    datas = datas.mask(datas == 'XZ', '西藏')
    datas = datas.mask(datas == 'SX', '山西')
    datas = datas.mask(datas == 'SD', '山东')
    datas = datas.mask(datas == 'GS', '甘肃')
    datas = datas.mask(datas == 'GJ', '香港')
    datas = datas.mask(datas == 'HUB', '湖北')
    datas = datas.mask(datas == 'HEB', '河北')
    datas = datas.mask(datas == 'CQ', '重庆')
    datas = datas.mask(datas == 'OTHER', '澳门')
    datas = datas.mask(datas == 'SNX', '陕西')
    datas = datas.mask(datas == 'XJ', '新疆')
    datas = datas.mask(datas == 'NMG', '内蒙古')
    datas = datas.mask(datas == 'FJ', '福建')
    datas = datas.mask(datas == 'AH', '安徽')
    datas = datas.mask(datas == 'GX', '广西')
    datas = datas.mask(datas == 'HUN', '湖南')
    datas = datas.mask(datas == 'GZ', '贵州')
    datas = datas.mask(datas == 'JL', '吉林')
    datas = datas.mask(datas == 'QH', '青海')
    datas = datas.mask(datas == 'NX', '宁夏')
    datas = datas.mask(datas == 'HAN', '海南')
    datas = datas.mask(datas == 'YN', '云南')
    datas = datas.mask(datas == 'TW', '台湾')
    city = datas['PROVINCE'].values.tolist()
    dict1 = {}
    for key in city:
        dict1[key] = dict1.get(key, 0) + 1
    provice = list(dict1.keys())
    values = list(dict1.values())
    china = (
        Map(init_opts=opts.InitOpts(width="900px", height="500px"))
            .add("", [list(z) for z in zip(provice, values)], zoom=0.7, )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="全国各省份注册公司总数",
                                      pos_left="left",
                                      pos_top="5%"),
            visualmap_opts=opts.VisualMapOpts(
                is_show=True,
                type_='color', max_=30000,
                range_text=['高', '低'],
            )
        )
    )
    relation1 = data.PROVINCE
    relation2 = Counter(relation1).most_common(10)
    x = ['广东', '浙江', '山东', '江苏', '河南', '四川', '安徽', '河北', '云南', '上海']
    y = [i[1] for i in relation2]
    pie = (
        Pie(init_opts=opts.InitOpts(width="900px", height="500px"))
            .add("", [list(i) for i in zip(x, y)],
                 radius=["", "55%"],
                 center=["25%", "50%"]
                 )
            .set_global_opts(title_opts=opts.TitleOpts(title="省份企业数前十"),
                             legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='1400px')
             )

            .add(
            china,
            grid_opts=opts.GridOpts(pos_bottom="", pos_right="50%")
        )
            .add(
            pie,
            grid_opts=opts.GridOpts()
        )
    )
    # grid.render_notebook()
    grid.render("charts/省份企业数前十2.html")


def companyYearComparison1(business_info):
    a = business_info
    # a['ESTIBLISH_TIME']
    a['ESTIBLISH_TIME'] = pd.to_datetime(a['ESTIBLISH_TIME'], errors='coerce')
    a['Years'] = a['ESTIBLISH_TIME'].dt.year
    b = Counter(a['Years']).most_common(20)[::-1]
    x = [i[0] for i in b]
    y = [i[1] for i in b]
    bar = (
        Bar()
            .add_xaxis(x)
            .add_yaxis("公司数量", y)
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .set_global_opts(title_opts=opts.TitleOpts(title="公司年份对比图"))
    )
    # bar.render_notebook()
    bar.render("charts/表一可视化（成立年份）.html")


def companyYearComparison2(business_info):
    a = business_info
    a['ESTIBLISH_TIME']
    a['ESTIBLISH_TIME'] = pd.to_datetime(a['ESTIBLISH_TIME'], errors='coerce')
    a['Years'] = a['ESTIBLISH_TIME'].dt.year
    b = Counter(a['Years']).most_common(20)[::-1]
    b.sort()
    x = [i[0] for i in b]
    y = [i[1] for i in b]
    bar = (
        Bar()
            .add_xaxis(x)
            .add_yaxis("公司数量", y)
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .set_global_opts(title_opts=opts.TitleOpts(title="公司年份对比图", pos_left='30%'))
    )
    pie = (
        Pie(init_opts=opts.InitOpts())
            .add("", b,
                 radius=["78%", "0%"],
                 center=["35%", "50%"])
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
            .set_global_opts(
            title_opts=opts.TitleOpts(title=" "),
            legend_opts=opts.LegendOpts(type_="scroll", pos_left="left", orient="vertical"),
        )

    )
    grid = (
        Grid()
            .add(
            bar,
            grid_opts=opts.GridOpts(pos_left="65%")
        )
            .add(
            pie,
            grid_opts=opts.GridOpts(pos_right="75%")
        )
    )
    grid.render_notebook()
    grid.render('charts/表一可视化（成立年份）2.html')


def totalNumberOfRegisteredCompanies(business_info):
    data = business_info
    # 字段全部输出
    pd.set_option('display.max_columns', 35)
    data['REG_CAPITAL_NUM'] = data['REG_CAPITAL_NUM'].astype('object')
    # 滤除元素都是NaN值的行和列
    data.dropna(axis=0, how="all")
    data.dropna(axis=1, how="all")
    # 删除ID,公司名称重复项，保留最后一项
    data.drop_duplicates(subset=["ID"], keep="last")
    # 查看缺失值占比，删除占比高，数据意义不大的字段
    missing = ((data.isnull().sum()) / data.shape[0]).sort_values(ascending=False).map(lambda x: "{:.2%}".format(x))
    # (例如：实收注册资金，上市代码，组织机构批准单位，对应的新公司ID，公司英文名称,营业期限终止日期)
    datas = data.drop(["ACTUAL_CAPITAL", "LIST_CODE", "FORMER_NAME",
                       "ORG_APPROVED_INSTITUTE", "NEW_COM_ID", "COMPANY_ENNAME",
                       "TO_TIME"], axis=1)
    # 中文省份替换英文缩写
    datas = datas.mask(datas == 'BJ', '北京')
    datas = datas.mask(datas == 'HEN', '河南')
    datas = datas.mask(datas == 'TJ', '天津')
    datas = datas.mask(datas == 'HLJ', '黑龙江')
    datas = datas.mask(datas == 'GD', '广东')
    datas = datas.mask(datas == 'LN', '辽宁')
    datas = datas.mask(datas == 'SH', '上海')
    datas = datas.mask(datas == 'SC', '四川')
    datas = datas.mask(datas == 'ZJ', '浙江')
    datas = datas.mask(datas == 'JS', '江苏')
    datas = datas.mask(datas == 'JX', '江西')
    datas = datas.mask(datas == 'XZ', '西藏')
    datas = datas.mask(datas == 'SX', '山西')
    datas = datas.mask(datas == 'SD', '山东')
    datas = datas.mask(datas == 'GS', '甘肃')
    datas = datas.mask(datas == 'GJ', '香港')
    datas = datas.mask(datas == 'HUB', '湖北')
    datas = datas.mask(datas == 'HEB', '河北')
    datas = datas.mask(datas == 'CQ', '重庆')
    datas = datas.mask(datas == 'OTHER', '澳门')
    datas = datas.mask(datas == 'SNX', '陕西')
    datas = datas.mask(datas == 'XJ', '新疆')
    datas = datas.mask(datas == 'NMG', '内蒙古')
    datas = datas.mask(datas == 'FJ', '福建')
    datas = datas.mask(datas == 'AH', '安徽')
    datas = datas.mask(datas == 'GX', '广西')
    datas = datas.mask(datas == 'HUN', '湖南')
    datas = datas.mask(datas == 'GZ', '贵州')
    datas = datas.mask(datas == 'JL', '吉林')
    datas = datas.mask(datas == 'QH', '青海')
    datas = datas.mask(datas == 'NX', '宁夏')
    datas = datas.mask(datas == 'HAN', '海南')
    datas = datas.mask(datas == 'YN', '云南')
    datas = datas.mask(datas == 'TW', '台湾')

    a = datas
    a['ESTIBLISH_TIME'] = pd.to_datetime(a['ESTIBLISH_TIME'], errors='coerce')
    a['Years'] = a['ESTIBLISH_TIME'].dt.year
    # 把注册时间以xxxx年的格式插入datas中
    datas['year'] = a['Years'].tolist()
    # 根据省份分组，得到各省份注册公司数量（Serise类型）
    c = datas.groupby('PROVINCE').size()
    # 省份名称
    d_province = c.index.tolist()
    # 各省份注册公司数
    d_count = c.values.tolist()
    # 注册公司数最值
    max_count = c.max()
    min_count = c.min()
    # 1995-2019每年的注册公司数
    dd = datas.groupby('year').size().sort_index()
    dd = dd.iloc[-25:-1]
    # 把年份转成字符型
    # years=list(map(str,dd.index.tolist()))
    years = []
    data_mark = []
    for i in range(len(dd.index.tolist())):
        y = str(int(dd.index.tolist()[i]))
        years.append(y)

    tl = Timeline(init_opts=opts.InitOpts(width="1400px", height="700px"))
    for i, j in zip(range(1995, 2020), dd.values.tolist()):
        d = datas.groupby('year').get_group(i)
        df_province = d.groupby('PROVINCE').size()
        df_province = df_province.sort_values(ascending=False)
        province = df_province.index.tolist()
        counts = df_province.values.tolist()

        map = (
            Map()
                .add(
                series_name='',
                data_pair=list(zip(province, counts)),
                maptype="china",
                is_map_symbol_show=False,
                center=[119.5, 34.5]
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="{}年全国地区注册公司情况".format(i),
                    pos_left="center",
                    pos_top="top",
                ),
                visualmap_opts=opts.VisualMapOpts(
                    is_calculable=True,  # 是否显示拖拽用的手柄（手柄能拖拽调整选中范围）
                    dimension=0,  # 是否显示拖拽用的手柄（手柄能拖拽调整选中范围）
                    pos_left="30",
                    pos_top="center",
                    range_text=["High", "Low"],
                    range_color=["lightskyblue", "yellow", "orangered"],
                    textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                    max_=df_province.max(),
                    min_=df_province.mean()),
            )
        )

        bar = (
            Bar(init_opts=opts.InitOpts(width="30%", height="50%"))
                .add_xaxis(xaxis_data=province)
                .add_yaxis(
                series_name="",
                y_axis=counts,
                label_opts=opts.LabelOpts(
                    is_show=True, position="right", formatter="{b} : {c}"  # 标签显示数据名，数据值
                ),
            )
                .reversal_axis()
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    max_=df_province.max(), axislabel_opts=opts.LabelOpts(is_show=False)
                ),
                yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
                #             xaxis_opts=opts.AxisTickOpts(length=100),
                tooltip_opts=opts.TooltipOpts(is_show=False),
                visualmap_opts=opts.VisualMapOpts(  # 视觉映射配置
                    is_calculable=True,  # 是否显示拖拽用的手柄（手柄能拖拽调整选中范围）
                    dimension=0,  # 是否显示拖拽用的手柄（手柄能拖拽调整选中范围）
                    pos_left="10",
                    pos_top="top",
                    range_text=["High", "Low"],  # 两端的文本
                    #                 range_color=["lightskyblue", "yellow", "orangered"],  # visualMap 组件过渡颜色
                    textstyle_opts=opts.TextStyleOpts(color="#ddd"),  # 文字样式配置项
                    min_=df_province.min(),
                    max_=df_province.max(),
                ),
            )

        )

        data_mark.append(j)
        line = (
            Line()
                .add_xaxis(years)
                .add_yaxis("", dd.values.tolist())
                .add_yaxis("", data_mark, markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]))
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="1995-2019年全国注册公司总数", pos_left="72%", pos_top="50%"
                )
            )
        )

        grid = (
            Grid()
                .add(
                bar,
                grid_opts=opts.GridOpts(
                    pos_left="10", pos_right="45%", pos_top="50%", pos_bottom="5"
                ),
            )
                .add(
                line,
                grid_opts=opts.GridOpts(
                    pos_left="65%", pos_right="80", pos_top="60%"
                ),
            )
                .add(map, grid_opts=opts.GridOpts())
        )

        tl.add(grid, time_point="{} 年".format(i))
    tl.add_schema(
        orient="vertical",
        is_auto_play=True,
        is_inverse=True,
        play_interval=1000,  # 自动播放，跳动的间隔为1000ms
        pos_left="null",
        pos_right="5",
        pos_top="20",
        pos_bottom="20",
        width="60",
        label_opts=opts.LabelOpts(is_show=True, color="#fff"),
    )
    # tl.render_notebook()
    tl.render('charts/1995-2019年全国注册公司总数.html')


def companyOperatingStatus(business_info):
    a = business_info['REG_STATUS'].str.strip()
    a = a.replace('存续(在营、开业、在册)', '存续（在营、开业、在册）')
    a = a.replace('存续', '存续（在营、开业、在册）')
    a = a.replace('在营（开业）企业', '存续（在营、开业、在册）')
    a = a.replace('正常', '存续（在营、开业、在册）')
    a = a.replace('开业', '存续（在营、开业、在册）')
    a = a.replace('在营', '存续（在营、开业、在册）')
    a = a.replace('在营（开业）', '存续（在营、开业、在册）')
    a = a.replace('登记成立', '存续（在营、开业、在册）')
    a = a.replace('正常执业', '存续（在营、开业、在册）')
    a = a.replace('登记', '存续（在营、开业、在册）')
    a = a.replace('吊销，未注销', '吊销未注销')
    a = a.replace('吊销,未注销', '吊销未注销')
    a = a.replace('吊销企业', '吊销未注销')
    a = a.replace('吊销', '吊销未注销')
    a = a.replace('已吊销', '吊销未注销')
    a = a.replace('注销企业', '注销')
    a = a.replace('吊销，已注销', '注销')
    a = a.replace('吊销并注销', '注销')
    a = a.replace('已废止', '注销')
    a = a.replace('吊销,已注销', '注销')
    a = a.replace('吊销后注销', '注销')
    a = a.replace('已迁出企业', '迁出')
    a = a.replace('迁往市外', '迁入')
    a = a.replace('--', '其他')
    a = a.replace('暂无', '其他')
    a = a.fillna('其他')
    b = Counter(a).most_common()
    pie = (
        Pie()
            .add("", b)
            .set_global_opts(
            title_opts=opts.TitleOpts(title=" "),
            legend_opts=opts.LegendOpts(type_="scroll", pos_left="left", orient="vertical"),
        )
    )
    # pie.render_notebook()
    pie.render("charts/公司经营状态图.html")


if __name__ == '__main__':
    business_info = pd.read_csv('data_tables/business_info.csv')
    topTenEnterprisesInTheProvince1(business_info)
    topTenEnterprisesInTheProvince2(business_info)
    companyYearComparison1(business_info)
    companyYearComparison2(business_info)
    totalNumberOfRegisteredCompanies(business_info)
    companyOperatingStatus(business_info)
