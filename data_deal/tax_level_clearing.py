import pandas as pd


def tax_level_clearing(tax_level: pd.DataFrame) -> pd.DataFrame:
    tax_level = tax_level.dropna(axis=1, how='all')
    tax_level = tax_level.set_index('GOOD_NAME')
    return tax_level
