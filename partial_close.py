_zmq._DWX_MTX_CLOSE_PARTIAL_BY_TICKET_(85051741, 0.01)

# MetaTrader response (JSON):
{'_action': 'CLOSE', 
'_ticket': 85051741, 
'_response': 'CLOSE_PARTIAL', 
'_close_price': 1.14401, 
'_close_lots': 0.01}

# Partially closing a trade renews the ticket ID, retrieve it again.

_zmq._DWX_MTX_GET_ALL_OPEN_TRADES_()

# MetaTrader response (JSON):
{'_action': 'OPEN_TRADES', 
'_trades': {
    85051856: {'_magic': 123456, 
                '_symbol': 'EURUSD', 
                '_lots': 0.04, 
                '_type': 0, 
                '_open_price': 1.14414, 
                '_pnl': -0.36}
    }
}