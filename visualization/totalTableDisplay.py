import pandas as pd
import numpy as np
import jieba
from collections import Counter
from pyecharts.charts import Bar, Pie, Grid, Map, Line, Timeline, Page
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import *
from pyecharts.globals import *
from pyecharts.faker import *


def numberOfIndustryTaxpayers(total_table):
    tt = total_table[total_table['GOOD_LEVEL'] == "B级纳税人"].drop_duplicates(
        ['Unnamed: 0']).reset_index().drop(columns='index')
    df = tt['BUSINESS_SCOPE']
    b = []
    x = df.shape[0]
    for i in range(x):
        b.append(jieba.lcut(str(df[i]), cut_all=False)[0])
    c = Counter(b).most_common(80)
    c1 = dict(c)
    d = ['生产', '吸收', '许可', '为', '普通', '办理', '经营', '在', '道路', '一般', '从事', '企业', '财产损失', '从事', 'nan', '对', '研发', '国内',
         '室内外', '预', '负责', '房屋', '商品', '农业', '以', '产销', '按', '实施', '实业', '组织', '项目', '（', '市政', '提供', '资产', '混凝土',
         '货物', '文化', '承担', '承接', '融资', '城市']
    e = {}
    for i in dict(c):
        if i in d:
            c1.pop(i)
    x3 = c1.keys()
    y3 = c1.values()
    bar = (
        Bar()
            .add_xaxis(list(x3)[::-1])
            .add_yaxis("", list(y3)[::-1])
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .set_global_opts(title_opts=opts.TitleOpts(title="", pos_left='30%'))
    )
    # bar.render_notebook()
    bar.render("charts/行业纳税人数量.html")


def distributionOfTheNumberOfTaxpayersAtAllLevelsInEachProvince(total_table):
    pd.set_option('display.unicode.east_asian_width', True)
    datas = total_table.loc[:, ['GOOD_LEVEL', 'PROVINCE']]
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

    line_province = datas.groupby("PROVINCE").size().index
    x_data = line_province.tolist()
    count = []
    for level, group in datas.groupby("GOOD_LEVEL"):
        count.append(group.groupby('PROVINCE').size().values.tolist())
    c = (
        Line(init_opts=opts.InitOpts(width="1000px", height="600px"))
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            series_name="A级纳税人",
            y_axis=count[0],
            symbol='circle',
            label_opts=opts.LabelOpts(is_show=False),
        )
            .add_yaxis(
            series_name="B级纳税人",
            y_axis=count[1],
            symbol='rect',
            label_opts=opts.LabelOpts(is_show=False),
        )
            .add_yaxis(
            series_name="C级纳税人",
            y_axis=count[2],
            symbol='arrow',
            label_opts=opts.LabelOpts(is_show=False),
        )
            .add_yaxis(
            series_name="D级纳税人",
            y_axis=count[3],
            symbol='diamond',
            label_opts=opts.LabelOpts(is_show=False),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="各级纳税人在各省份的人数分布"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=False),
                min_='dataMin',
                max_='dataMax'
            ),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,
                                     axislabel_opts={"interval": "0", "rotate": "-30"}),
        )
    )
    # c.render_notebook()
    c.render('charts/各级纳税人在各省份的人数分布.html')


def industryTaxpayerGradeDistribution(total_table):
    # 各行业总数排名
    df = total_table['BUSINESS_SCOPE']
    b = []
    x = df.shape[0]
    for i in range(x):
        b.append(jieba.lcut(str(df[i]), cut_all=False)[0])
    c = Counter(b).most_common(80)
    c1 = dict(c)
    d = ['生产', '吸收', '许可', '为', '普通', '办理', '经营', '在', '道路', '一般', '从事', '企业', '财产损失', '从事', 'nan', '对', '研发', '国内',
         '室内外', '预', '负责', '房屋', '商品', '农业', '以', '产销', '按', '实施', '实业', '组织', '项目', '（', '市政', '提供', '资产', '混凝土',
         '货物', '文化', '承担', '承接', '融资', '城市']
    e = {}
    for i in dict(c):
        if i in d:
            c1.pop(i)
    x3 = c1.keys()
    y3 = c1.values()
    bar = (
        Bar()
            .add_xaxis(list(x3)[::-1])
            .add_yaxis("", list(y3)[::-1])
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .set_global_opts(title_opts=opts.TitleOpts(title="", pos_left='30%'))
    )
    # bar.render_notebook()

    # 数量最多的20个行业与纳税人评级表合并
    m1 = pd.DataFrame(data=b, columns=['BUSINESS_SCOPE'])
    m2 = pd.concat([m1, total_table['GOOD_LEVEL']], axis=1)
    # 对20个行业的各个评级分类
    Industries = ['房地产', '销售', '物业管理', '房屋建筑', '汽车', '建筑', '法律', '批发', '加工', '投资', '制造', '建筑工程', '煤炭', '服务', '计算机',
                  '餐饮', '服装', '建筑材料', '技术开发', '设计']
    data = [m2.groupby('BUSINESS_SCOPE').get_group(i).value_counts() for i in Industries]
    # 20个行业的数据提取
    x = [i.index.tolist() for i in data]
    y = [i.values.tolist() for i in data]

    bar = [
        (
            Bar()
                .add_xaxis(a)
                .add_yaxis("分布情况", b)
                .set_series_opts(label_opts=opts.LabelOpts(position="right"))
                .set_global_opts(title_opts=opts.TitleOpts(title=f"{c}纳税人等级分布", pos_left='10%'))
        )
        for a, b, c in zip(x, y, Industries)
    ]
    timeline = Timeline()
    for i in range(len(Industries)):
        timeline.add(bar[i], f"{Industries[i]}")
    # timeline.render_notebook()
    timeline.render('charts/行业纳税人等级分布.html')


def counter(conpany_level):
    return Counter(conpany_level)


def enterpriseInvestmentEfficiencyAndRating(total_table):
    data = total_table
    # 查询各个企业投资公司数量
    company = data['Unnamed: 0'].values.tolist()
    dict1 = {}
    for key in company:
        dict1[key] = dict1.get(key, 0) + 1

        # 投资数量最多的前十家公司：conpany_top_tan
    dict2 = sorted(dict1.items(), key=lambda d: d[1], reverse=True)
    dict3 = dict2[:20]
    conpany_top_tan = {}
    for i in dict3:
        conpany_top_tan[i[0]] = i[1]

    # #前二十家企业投资公司数量数据
    conpany_name_list = list(conpany_top_tan.keys())
    top_tan = data[data['Unnamed: 0'].isin(conpany_name_list)]
    top_tan['OWING_TAX_BALANCE'] = pd.to_numeric(top_tan['OWING_TAX_BALANCE'], errors='coerce')

    # #重新前二十公司排列顺序
    company_Tan = top_tan['Unnamed: 0'].values.tolist()
    tan = {}
    for key in company_Tan:
        tan[key] = tan.get(key, 0) + 1

        # #企业所占行业需纳税的总情况
    # top_tans = top_tan.drop_duplicates(subset=['TAX_NUMBER'], keep="last")
    top_tans_money = dict(top_tan.groupby('ID')['OWING_TAX_BALANCE'].agg('sum'))  # sum要加单引号
    # print(top_tans.groupby('ID')['OWING_TAX_BALANCE'].agg('sum'))

    # # #公司情况单列表单
    df2 = top_tan.loc[:, ['Unnamed: 0', 'GOOD_LEVEL']]
    df3 = df2.drop_duplicates(subset=['Unnamed: 0', 'GOOD_LEVEL'], keep="last")
    conpany_level = list(df3['GOOD_LEVEL'].values.tolist())
    conpany_name = list(top_tans_money.keys())
    conpany_Tax_arrears = list(top_tans_money.values())
    conpany_number = list(tan.values())

    conpany_Tax_arrears = [int(a) for a in conpany_Tax_arrears]

    bar = (
        Bar(init_opts=opts.InitOpts(width="1000px",
                                    height="500px",
                                    ))
            .add_xaxis(conpany_name)
            .add_yaxis("企业涉及行业总欠税金额", conpany_Tax_arrears)
            .extend_axis(
            yaxis=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} 个"), interval=5
            )
        )
            .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-10, interval=0)))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="单个企业投资效益情况"),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} 万元")),

        )
    )

    line = Line().add_xaxis(conpany_name).add_yaxis("单个企业投资公司总个数", conpany_number, yaxis_index=1)
    bar.overlap(line)  # 在柱状图上叠加折线图
    # bar.render("企业投资效益与评级情况.html")

    level = ['A级纳税人', 'B级纳税人', 'C级纳税人', 'D级纳税人']

    ss = dict(counter(conpany_level))
    new_ss = dict(sorted(ss.items(), key=lambda d: d[0], reverse=False))
    level_number = list(new_ss.values())

    pie = Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    pie.add("", [list(z) for z in zip(level, level_number)], radius=["50%", "75%"], center=["45%", "60%"],
            rosetype="radius", )
    pie.set_series_opts(label_opts=opts.
                        LabelOpts(is_show=True)
                        )
    pie.set_global_opts(title_opts=opts.TitleOpts(title="企业信用评分", pos_left="32%"),
                        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="5%"))
    pie.set_colors(["green", "blue", "red"])  # 改变颜色
    page1 = Page(layout=Page.DraggablePageLayout)
    page1.add(
        bar,
        pie, )
    # page1.render_notebook()
    page1.render('charts/企业投资效益与评级情况.html')


def distributionOfTaxesByLevel():
    name = ['增值税', '企业所得税']
    page = Page()

    num = [55583, 55742]
    piea = Pie()
    piea.add("", [list(z) for z in zip(name, num)])  # 设置圆环的粗细和大小
    piea.set_global_opts(title_opts=opts.TitleOpts(title="A级纳税人"))
    piea.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))

    num = [14712, 14659]
    pieb = Pie()
    pieb.add("", [list(z) for z in zip(name, num)])  # 设置圆环的粗细和大小
    pieb.set_global_opts(title_opts=opts.TitleOpts(title="B级纳税人"))
    pieb.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))

    num = [7074, 6993]
    piec = Pie()
    piec.add("", [list(z) for z in zip(name, num)])  # 设置圆环的粗细和大小
    piec.set_global_opts(title_opts=opts.TitleOpts(title="C级纳税人"))
    piec.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))

    num = [3888, 3819]
    pied = Pie()
    pied.add("", [list(z) for z in zip(name, num)])  # 设置圆环的粗细和大小
    pied.set_global_opts(title_opts=opts.TitleOpts(title="D级纳税人"))
    pied.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))

    timeline = Timeline()
    timeline.add(piea, 'A级纳税人')
    timeline.add(pieb, 'B级纳税人')
    timeline.add(piec, 'B级纳税人')
    timeline.add(pied, 'B级纳税人')
    # timeline.render_notebook()
    timeline.render('charts/各等级税种分布.html')


if __name__ == '__main__':
    total_table = pd.read_csv('data_tables/total_table.csv')
    numberOfIndustryTaxpayers(total_table)
    distributionOfTheNumberOfTaxpayersAtAllLevelsInEachProvince(total_table)
    industryTaxpayerGradeDistribution(total_table)
    enterpriseInvestmentEfficiencyAndRating(total_table)
    distributionOfTaxesByLevel()
