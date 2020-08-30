# Overview: Buy and hold strategy -- rebalances portfolio at the start of every month. 5 companies with 15% in to keep some cash on hand

# imports
from zipline.api import(symbol,
                        order_target_percent,
                        schedule_function,
                        date_rules,
                        time_rules,
                        )

# Initialize Companies to trade


def initialize(context):
    # Company Selection -- NYSE
    context.long_portfolio = [
        symbol('MSFT'),
        symbol('AAPL'),
        symbol('FB')
    ]

    # Call rebalance function on the first trading day of each month after 2.5 hours from market open
    schedule_function(rebalance,
                      date_rules.month_start(days_offset=0),
                      time_rules.market_close(hours=2, minutes=30))

# Rebalance The Portfolio


def rebalance(context, data):
    # Invest 80% of portfolio split amongst companies
    portfolioLength = len(context.long_portfolio)
    orderTarget = 0.8/portfolioLength
    for security in context.long_portfolio:
        order_target_percent(security, orderTarget)
