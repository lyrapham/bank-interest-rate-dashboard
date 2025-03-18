import pandas as pd
import numpy as np
from datetime import datetime

def generate_sample_data():
    # Generate dates for the last 12 months
    dates = pd.date_range(end=datetime.now(), periods=12, freq='M')
    
    banks = {
        'Vietnam': [
            'Techcombank', 'Vietcombank', 'BIDV', 'Vietinbank',
            'Agribank', 'VPBank', 'MB Bank', 'ACB',
            'Sacombank', 'TPBank'
        ],
        'Canada': ['RBC', 'TD Bank', 'Scotiabank', 'BMO']
    }
    
    # Base rates for different term periods (in months)
    term_rates = {
        1: 3.8, 3: 4.0, 6: 4.7, 9: 5.1,
        12: 5.5, 18: 5.7, 24: 5.9, 36: 6.1
    }
    
    data = []
    for country, country_banks in banks.items():
        for bank in country_banks:
            # Different base rate adjustment for each bank
            bank_adjustment = {
                'Techcombank': 0.3, 'Vietcombank': 0.0, 'BIDV': 0.2,
                'Vietinbank': 0.1, 'VPBank': 0.4, 'MB Bank': 0.25,
                'ACB': 0.35, 'Sacombank': 0.3, 'TPBank': 0.35,
                'Agribank': 0.1
            }.get(bank, 0)
            
            # Generate rates for each term
            for term, base_rate in term_rates.items():
                if country == 'Vietnam':
                    rate = base_rate + bank_adjustment
                else:
                    rate = (base_rate - 2.0) + np.random.normal(0, 0.1)
                
                # Add historical data points with slight variations
                for date in dates:
                    historical_adjustment = np.random.normal(0, 0.05)
                    data.append({
                        'Date': date,
                        'Country': country,
                        'Bank': bank,
                        'Term_Months': term,
                        'Interest_Rate': round(rate + historical_adjustment, 2)
                    })
    
    return pd.DataFrame(data)

def get_real_time_rates():
    return generate_sample_data() 