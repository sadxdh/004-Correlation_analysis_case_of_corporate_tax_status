import pandas as pd
from pyecharts.charts import Bar
from pyecharts.charts import WordCloud
from pyecharts.charts import PictorialBar
from pyecharts.charts import Funnel
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType
from pyecharts import options as opts
from pyecharts.faker import Faker


def numberOfEnterprisesByProvince(owing_tax_info):
    # 以省份分组统计各个参数出现的次数
    df3 = owing_tax_info.groupby('PROVINCE').count()
    x = df3.index
    y = list(df3['OWING_TAX_BALANCE'])

    bar = (
        Bar(init_opts=opts.InitOpts(width='1000px', height='300px',
                                    theme=ThemeType.WESTEROS,
                                    bg_color='#fff'))
            .add_xaxis(list(x))
            .add_yaxis('各省份企业数量', y)
        #     .set_global_opts(

        #                     )

    )
    # bar.render_notebook()
    bar.render("charts/各省份企业数量.html")


def totalTaxPaymentByEnterprises(owing_tax_info):
    # 各个企业纳税的总额
    # 以省份分组并求和
    df4 = owing_tax_info.groupby('PROVINCE').sum()
    x = df4.index
    y1 = list(df4['OWING_TAX_BALANCE'])
    # 保留小数后两位
    y1 = df4['OWING_TAX_BALANCE']
    a = []
    for i in y1:
        a.append(round(i, 2))
    y1 = list(a)

    bar = (
        Bar(init_opts=opts.InitOpts(width='1000px', height='300px',
                                    theme=ThemeType.LIGHT,
                                    bg_color='#fff'))
            .add_xaxis(list(x))
            .add_yaxis('各省份企业纳税总额(万元)', y1)

    )
    # bar.render_notebook()
    bar.render("charts/各省份企业纳税总额(万元).html")


def taxAuthority(owing_tax_info):
    # 根据税务机关分组统计其数量
    df_kinds = owing_tax_info.groupby('TAX_AUTHORITY').size()
    # 将数量转成列表元素是字符类型
    counts = []
    for i in range(len(df_kinds.values.tolist())):
        counts.append(str(df_kinds.values.tolist()[i]))
    # 将税务机关及其数量的列表转成元组
    df_kinds = list(zip(df_kinds.index, counts))

    b = (
        WordCloud()
            .add(series_name="税务机关", data_pair=df_kinds, word_size_range=[6, 66])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="税务机关", title_textstyle_opts=opts.TextStyleOpts(font_size=23),
                subtitle="结论：最常用税务机关：广东国家税务局、浙江国家税务局、山东国家税务局、河南国家税务局"
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    # b.render_notebook()
    b.render("charts/税务机关.html")


def numberOfCompaniesByProvince(owing_tax_info):
    df_provnce = owing_tax_info.groupby('PROVINCE').size()
    c = (
        PictorialBar()
            .add_xaxis(df_provnce.index.tolist())
            .add_yaxis(
            "",
            df_provnce.values.tolist(),
            label_opts=opts.LabelOpts(is_show=False),
            symbol_size=10,
            symbol_repeat="fixed",
            symbol_offset=[0, 0],
            is_symbol_clip=True,
            #         symbol=SymbolType.ROUND_RECT,
            symbol=SymbolType.ARROW,
        )
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title="owing_tax_info各省公司的数量"),
            xaxis_opts=opts.AxisOpts(is_show=False),
            yaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(opacity=0)
                ),
            ),
        )
    )
    # c.render_notebook()
    c.render("charts/各省公司的数量.html")


def Top10CompaniesWithOutstandingBalances(owing_tax_info):
    df_company = owing_tax_info.groupby(['COMPANY_ID', 'COMPANY_NAME'])['OWING_TAX_BALANCE'].sum()
    df_company = df_company.sort_values(ascending=False)[:10]
    company_name = []
    for i in range(10):
        company_name.append(df_company.index[i][1])
    c = (
        Funnel(init_opts=opts.InitOpts(width="700px"))
            .add(
            "公司",
            [list(z) for z in zip(company_name, df_company.values)],
            sort_="descending",
            label_opts=opts.LabelOpts(position="inside"),
            #         is_selected=True
        )
            .set_global_opts(title_opts=opts.TitleOpts(title='欠款余额前十的公司'),
                             legend_opts=opts.LegendOpts(is_show=False), )
    )
    # c.render_notebook()
    c.render('charts/欠款余额前十的公司.html')


if __name__ == '__main__':
    owing_tax_info = pd.read_csv('data_tables/owing_tax_info.csv')
    numberOfEnterprisesByProvince(owing_tax_info)
    totalTaxPaymentByEnterprises(owing_tax_info)
    taxAuthority(owing_tax_info)
    numberOfCompaniesByProvince(owing_tax_info)
    Top10CompaniesWithOutstandingBalances(owing_tax_info)