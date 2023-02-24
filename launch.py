from data_collection import data_collection
from data_deal import getTotalTable
from data_deal import getTableInfo
from data_deal import DataCleaning
from data_deal import catBusinessScope
from visualization import businessInfoDisplay
from visualization import investAbroadDisplay
from visualization import owingTaxInfoDisplay
from visualization import taxLevelDisplay
from visualization import totalTableDisplay

if __name__ == '__main__':
    tables = ['business_info', 'invest_abroad', 'owing_tax_info', 'tax_level']

    # 获取数据
    # data_collection.DataCollection(tables)

    # 各表 数据清洗
    clearing = DataCleaning.DataCleaning(tables)
    clearing.readCSV()
    clearing.data_cleaning()
    print(clearing.business_info.shape)
    print(clearing.invest_abroad.shape)
    print(clearing.owing_tax_info.shape)
    print(clearing.tax_level.shape)

    # 各表各字段信息
    tables = [clearing.business_info, clearing.invest_abroad, clearing.owing_tax_info, clearing.tax_level]
    tables = getTableInfo.getTableInfo(tables)

    # 分表可视化
    # business_info
    businessInfoDisplay.topTenEnterprisesInTheProvince1(clearing.business_info)
    businessInfoDisplay.topTenEnterprisesInTheProvince2(clearing.business_info)
    businessInfoDisplay.companyYearComparison1(clearing.business_info)
    businessInfoDisplay.companyYearComparison2(clearing.business_info)
    businessInfoDisplay.totalNumberOfRegisteredCompanies(clearing.business_info)
    businessInfoDisplay.companyOperatingStatus(clearing.business_info)
    # invest_abroad
    investAbroadDisplay.investmentAmountInvestmentOfTheTop20Companies(clearing.invest_abroad)
    # owing_tax_info
    owingTaxInfoDisplay.numberOfEnterprisesByProvince(clearing.owing_tax_info)
    owingTaxInfoDisplay.totalTaxPaymentByEnterprises(clearing.owing_tax_info)
    owingTaxInfoDisplay.taxAuthority(clearing.owing_tax_info)
    owingTaxInfoDisplay.numberOfCompaniesByProvince(clearing.owing_tax_info)
    owingTaxInfoDisplay.Top10CompaniesWithOutstandingBalances(clearing.owing_tax_info)
    # tax_level
    taxLevelDisplay.proportionOfTaxpayersAtAllLevels()

    # 合成总表
    total_table = getTotalTable.getTotalTable(tables).total_table

    # 探索分析
    totalTableDisplay.numberOfIndustryTaxpayers(total_table)
    totalTableDisplay.distributionOfTheNumberOfTaxpayersAtAllLevelsInEachProvince(total_table)
    totalTableDisplay.industryTaxpayerGradeDistribution(total_table)
    totalTableDisplay.enterpriseInvestmentEfficiencyAndRating(total_table)
    totalTableDisplay.distributionOfTaxesByLevel()
