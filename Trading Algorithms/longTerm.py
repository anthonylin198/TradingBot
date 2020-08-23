from zipline.api import symbol, order_target_percent

# initialize just runs some of the code


def initialize(context):
    """
        called once at the start of the run.
    """
    # convert the symbol string to asset and store a reference to it
    # universe selection, pick the various symbols
    context.long_portfolio = [
        symbol('TWTR'),
        symbol('FDX'),
        symbol('ETFC')
    ]


# handle data is the actual trading
def handle_data(context, data):

    # order to target 90% of portfolio value in the asset, orders by the minute, 30% each
    for security in context.long_portfolio:
        order_target_percent(security, 0.25)
