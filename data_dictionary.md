# Data Dictionary

# 01_fund_master.csv

amfi_code
- Type: Integer
- Description: Unique AMFI Scheme Code

scheme_name
- Type: Text
- Description: Mutual Fund Scheme Name

fund_house
- Type: Text
- Description: Asset Management Company

category
- Type: Text
- Description: Fund Category

------------------------------------------------

# 02_nav_history.csv

amfi_code
- Type: Integer
- Description: Scheme Identifier

date
- Type: Date
- Description: NAV Date

nav
- Type: Float
- Description: Net Asset Value

------------------------------------------------

# 08_investor_transactions.csv

investor_id
- Type: Text
- Description: Investor ID

transaction_date
- Type: Date
- Description: Transaction Date

amount_inr
- Type: Float
- Description: Investment Amount

transaction_type
- Type: Text
- Description: SIP / Lumpsum / Redemption