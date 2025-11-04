from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for ratios
categories = {
    'profitability': [
        ('Gross Profit Ratio', 'gross_profit_ratio'),
        ('Return on Assets', 'return_on_assets'),
        ('Return on Equity', 'return_on_equity'),
        ('Return on Capital Employed', 'return_on_capital_employed')
    ],
    'efficiency': [
        ('Fixed Asset Turnover', 'fixed_asset_turnover'),
        ('Asset Turnover Ratio', 'asset_turnover_ratio'),
        ('Current Asset Turnover Ratio', 'current_asset_turnover_ratio'),
        ('Working Capital Turnover Ratio', 'working_capital_turnover_ratio'),
        ('Receivable Turnover Ratio', 'receivable_turnover_ratio'),
        ('Inventory Turnover Ratio', 'inventory_turnover_ratio'),
        ('Payable Turnover Ratio', 'payable_turnover_ratio')
    ],
    'solvency': [
        ('Current Ratio', 'current_ratio'),
        ('Quick Ratio', 'quick_ratio'),
        ('Debt-Equity Ratio', 'debt_equity_ratio'),
        ('Liability to Equity Ratio', 'liability_to_equity_ratio'),
        ('Interest Coverage Ratio', 'interest_coverage_ratio'),
        ('Debt Service Coverage Ratio', 'debt_service_coverage_ratio')
    ],
    'other': [
        ('Payout and Retention Ratio', 'payout_retention_ratio'),
        ('Price to Earnings & Book Ratios', 'price_to_earnings_book_ratio')
    ]
}

@app.route('/')
def home():
    return render_template('home.html', categories=categories)

@app.route('/category/<name>')
def show_ratios(name):
    ratios = categories.get(name)
    return render_template('ratios.html', category_name=name, ratios=ratios)

@app.route('/ratio/<ratio_name>', methods=['GET', 'POST'])
def ratio_input(ratio_name):
    ratio_labels = {
        'gross_profit_ratio': ('Gross Profit', 'Sales'),
        'return_on_assets': ('Net Income', 'Total Assets'),
        'return_on_equity': ('Net Income', 'Shareholders Equity'),
        'return_on_capital_employed': ('Net Operating Profit', 'Capital Employed'),
        'fixed_asset_turnover': ('Sales', 'Fixed Assets'),
        'asset_turnover_ratio': ('Sales', 'Total Assets'),
        'current_asset_turnover_ratio': ('Sales', 'Current Assets'),
        'working_capital_turnover_ratio': ('Sales', 'Working Capital'),
        'receivable_turnover_ratio': ('Net Credit Sales', 'Average Accounts Receivable'),
        'inventory_turnover_ratio': ('Cost of Goods Sold', 'Average Inventory'),
        'payable_turnover_ratio': ('Purchases', 'Average Accounts Payable'),
        'current_ratio': ('Current Assets', 'Current Liabilities'),
        'quick_ratio': ('(Current Assets - Inventory)', 'Current Liabilities'),
        'debt_equity_ratio': ('Total Debt', 'Shareholders Equity'),
        'liability_to_equity_ratio': ('Total Liabilities', 'Shareholders Equity'),
        'interest_coverage_ratio': ('EBIT', 'Interest Expenses'),
        'debt_service_coverage_ratio': ('Net Operating Income', 'Total Debt Service'),
        'payout_retention_ratio': ('Dividends Paid', 'Net Income'),
        'price_to_earnings_book_ratio': ('Market Price per Share', 'Earnings per Share or Book Value')        
    }
    if request.method == 'POST':
        numerator = float(request.form['numerator'])
        denominator = float(request.form['denominator'])
        if denominator == 0:
            result = 'Denominator cannot be zero!'
        else:
            result = numerator / denominator
        return render_template('result.html', result=result, ratio_name=ratio_name)
    label1, label2 = ratio_labels.get(ratio_name, ('Numerator', 'Denominator'))
    return render_template('ratio_input.html', ratio_name=ratio_name, label1=label1, label2=label2)

if __name__ == '__main__':
    app.run(debug=True)

