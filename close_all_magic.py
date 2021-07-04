# Before running the following example, 5 trades were executed using the same values as in "_my_trade" above, the magic number being 123456.

# Check currently open trades.

_zmq._DWX_MTX_GET_ALL_OPEN_TRADES_()

# MetaTrader response (JSON):
{'_action': 'OPEN_TRADES', 
    '_trades': {
        85052022: {'_magic': 123456, '_symbol': 'EURUSD', '_lots': 0.05, '_type': 0, '_open_price': 1.14353, '_pnl': 1.15}, 
        85052026: {'_magic': 123456, '_symbol': 'EURUSD', '_lots': 0.05, '_type': 0, '_open_price': 1.14354, '_pnl': 1.1}, 
        85052025: {'_magic': 123456, '_symbol': 'EURUSD', '_lots': 0.05, '_type': 0, '_open_price': 1.14354, '_pnl': 1.1}, 
        85052024: {'_magic': 123456, '_symbol': 'EURUSD', '_lots': 0.05, '_type': 0, '_open_price': 1.14354, '_pnl': 1.1}, 
        85052023: {'_magic': 123456, '_symbol': 'EURUSD', '_lots': 0.05, '_type': 0, '_open_price': 1.14356, '_pnl': 1}
    }
}

# Close all trades with magic number 123456
_zmq._DWX_MTX_CLOSE_TRADES_BY_MAGIC_(123456)

# MetaTrader response (JSON):
{'_action': 'CLOSE_ALL_MAGIC', '_magic': 123456, 
'_responses': {
    85052026: {'_symbol': 'EURUSD', '_close_price': 1.14375, '_close_lots': 0.05, '_response': 'CLOSE_MARKET'}, 
    85052025: {'_symbol': 'EURUSD', '_close_price': 1.14375, '_close_lots': 0.05, '_response': 'CLOSE_MARKET'}, 
    85052024: {'_symbol': 'EURUSD', '_close_price': 1.14375, '_close_lots': 0.05, '_response': 'CLOSE_MARKET'}, 
    85052023: {'_symbol': 'EURUSD', '_close_price': 1.14375, '_close_lots': 0.05, '_response': 'CLOSE_MARKET'}, 
    85052022: {'_symbol': 'EURUSD', '_close_price': 1.14375, '_close_lots': 0.05, '_response': 'CLOSE_MARKET'}}, 
'_response_value': 'SUCCESS'}