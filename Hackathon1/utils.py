import pandas as pd

def safe_date(val):
    import numpy as np
    if pd.isna(val) or str(val).lower() in ['nan', 'nat', 'none', '']:
        return None
    return str(val)
