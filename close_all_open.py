# Open 5 trades

_zmq._DWX_MTX_NEW_TRADE_()
{'_action': 'EXECUTION', '_magic': 123456, '_ticket': 85090920, '_open_price': 1.15379, '_sl': 500, '_tp': 500}

_zmq._DWX_MTX_NEW_TRADE_()
{'_action': 'EXECUTION', '_magic': 123456, '_ticket': 85090921, '_open_price': 1.15379, '_sl': 500, '_tp': 500}

_zmq._DWX_MTX_NEW_TRADE_()
{'_action': 'EXECUTION', '_magic': 123456, '_ticket': 85090922, '_open_price': 1.15375, '_sl': 500, '_tp': 500}

_zmq._DWX_MTX_NEW_TRADE_()
{'_action': 'EXECUTION', '_magic': 123456, '_ticket': 85090926, '_open_price': 1.15378, '_sl': 500, '_tp': 500}

_zmq._DWX_MTX_NEW_TRADE_()
{'_action': 'EXECUTION', '_magic': 123456, '_ticket': 85090927, '_open_price': 1.15378, '_sl': 500, '_tp': 500}

# Close all open trades
_zmq._DWX_MTX_CLOSE_ALL_TRADES_()

# MetaTrader response (JSON):
{'_action': 'CLOSE_ALL',
 '_responses': {85090927: {'_symbol': 'EURUSD',
   '_magic': 123456,
   '_close_price': 1.1537,
   '_close_lots': 0.01,
   '_response': 'CLOSE_MARKET'},
  85090926: {'_symbol': 'EURUSD',
   '_magic': 123456,
   '_close_price': 1.1537,
   '_close_lots': 0.01,
   '_response': 'CLOSE_MARKET'},
  85090922: {'_symbol': 'EURUSD',
   '_magic': 123456,
   '_close_price': 1.1537,
   '_close_lots': 0.01,
   '_response': 'CLOSE_MARKET'},
  85090921: {'_symbol': 'EURUSD',
   '_magic': 123456,
   '_close_price': 1.15369,
   '_close_lots': 0.01,
   '_response': 'CLOSE_MARKET'},
  85090920: {'_symbol': 'EURUSD',
   '_magic': 123456,
   '_close_price': 1.15369,
   '_close_lots': 0.01,
   '_response': 'CLOSE_MARKET'}},
 '_response_value': 'SUCCESS'}