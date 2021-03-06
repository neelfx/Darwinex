# code for constructing a trade

_my_trade = _zmq._generate_default_order_dict()

Output: 
{'_action': 'OPEN',
 '_type': 0,
 '_symbol': 'EURUSD',
 '_price': 0.0,
 '_SL': 500,
 '_TP': 500,
 '_comment': 'DWX_Python_to_MT',
 '_lots': 0.01,
 '_magic': 123456,
 '_ticket': 0}

_my_trade['_lots'] = 0.05

_my_trade['_SL'] = 250

_my_trade['_TP'] = 750

_my_trade['_comment'] = 'nerds_rox0r'

#send trade
_zmq._DWX_MTX_NEW_TRADE_(_order=_my_trade)

# MetaTrader response (JSON):
{'_action': 'EXECUTION', 
'_magic': 123456, 
'_ticket': 85051741, 
'_open_price': 1.14414, 
'_sl': 250, 
'_tp': 750}

####################################################

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

#################################################



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

 ###########################################################

 _zmq._DWX_MTX_CLOSE_TRADE_BY_TICKET_(85051856)

# MetaTrader response (JSON):
{'_action': 'CLOSE', 
'_ticket': 85051856, 
'_close_price': 1.14378, 
'_close_lots': 0.04, 
'_response': 'CLOSE_MARKET', 
'_response_value': 'SUCCESS'}

#############################################################

_zmq._DWX_MTX_GET_ALL_OPEN_TRADES_()

# MetaTrader response (JSON):

{'_action': 'OPEN_TRADES', 
'_trades': {
    85051741: {'_magic': 123456, 
                '_symbol': 'EURUSD', 
                '_lots': 0.05, 
                '_type': 0, 
                '_open_price': 1.14414, 
                '_pnl': -0.45}
    }
}

##################################################################