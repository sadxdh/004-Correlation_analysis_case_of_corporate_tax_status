import pandas as pd
from pyecharts.charts import Bar, Grid
from pyecharts import options as opts


def investmentAmountInvestmentOfTheTop20Companies(invest_abroad):
    invest_abroad = invest_abroad.dropna(axis=1, how='all')
    invest_abroad = invest_abroad.dropna().reset_index(drop=True)
    invest = invest_abroad.loc[:, ['COMPANY_NAME', 'AMOUNT']]
    inves = invest.groupby(['COMPANY_NAME']).sum().sort_values(by='AMOUNT', ascending=False).iloc[:20, :]
    x = inves.index.tolist()
    y = inves['AMOUNT'].tolist()
    bar = (Bar(init_opts=opts.InitOpts(height="1000px"))
        .add_xaxis(x)
        .add_yaxis("投资金额", y, color='#2f4414')
        .set_global_opts(
        title_opts=opts.TitleOpts(title="投资金额前二十家公司投资情况", pos_left='60%', pos_top='4%'),
        xaxis_opts=opts.AxisOpts(name="公司名称", axislabel_opts={"interval": "0", "rotate": "60"}),
        yaxis_opts=opts.AxisOpts(name='投资金额'),
        datazoom_opts=opts.DataZoomOpts()
        )
    )

    grid = Grid()
    grid.add(bar, grid_opts=opts.GridOpts(pos_bottom="50%"))
    # grid.render_notebook()
    grid.render("charts/投资金额前二十家公司投资情况.html")


if __name__ == '__main__':
    invest_abroad = pd.read_csv("data_tables/invest_abroad.csv", encoding='utf-8')
    investmentAmountInvestmentOfTheTop20Companies(invest_abroad)
