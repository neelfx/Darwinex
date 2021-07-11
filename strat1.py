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



