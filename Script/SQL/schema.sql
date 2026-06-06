CREATE TABLE dim_fund(
    fund_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT
);

CREATE TABLE dim_date(
    date_id INTEGER PRIMARY KEY,
    full_date DATE
);

CREATE TABLE fact_nav(
    nav_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    date_id INTEGER,
    nav REAL,
    FOREIGN KEY(fund_id) REFERENCES dim_fund(fund_id)
);

CREATE TABLE fact_transactions(
    transaction_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    amount REAL,
    FOREIGN KEY(fund_id) REFERENCES dim_fund(fund_id)
);

CREATE TABLE fact_performance(
    performance_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    FOREIGN KEY(fund_id) REFERENCES dim_fund(fund_id)
);

CREATE TABLE fact_aum(
    aum_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    aum REAL,
    FOREIGN KEY(fund_id) REFERENCES dim_fund(fund_id)
);