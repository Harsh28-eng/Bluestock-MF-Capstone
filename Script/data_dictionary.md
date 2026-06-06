# Data Dictionary

# 01_fund_master.csv

| Column      | Type    | Description              |
| ----------- | ------- | ------------------------ |
| amfi_code   | Integer | Unique AMFI Scheme Code  |
| scheme_name | Text    | Mutual Fund Scheme Name  |
| fund_house  | Text    | Asset Management Company |
| category    | Text    | Fund Category            |

# 02_nav_history.csv

| Column    | Type    | Description     |
| --------- | ------- | --------------- |
| amfi_code | Integer | Scheme Code     |
| date      | Date    | NAV Date        |
| nav       | Float   | Net Asset Value |

# 08_investor_transactions.csv

| Column           | Type  | Description             |
| ---------------- | ----- | ----------------------- |
| investor_id      | Text  | Investor Identifier     |
| transaction_date | Date  | Transaction Date        |
| amount_inr       | Float | Transaction Amount      |
| transaction_type | Text  | SIP/Lumpsum/Redemption  |
| kyc_status       | Text  | KYC Verification Status |
