import datetime
import requests
import queue
import time


# cookie = 'perm=0E07A57D1F6381A694278FA3702C9A67; closesettings=2048; __cfduid=d8104becfc6f68664245db364a5e7b5801507877774; tradetype=0; language=0; leverRate=20; locale=zh_CN; treatyType_Btc=201802090000012; future_contract_type_BTC=this_week; open-base-currency=cny; first_ref="https://www.okex.com/future/future.do?symbol=0"; lp="https://www.okex.com/intro_apiOverview.html"; open-trade-currency=btc; coin_session_logininfo=""; SHOW_NOTIFY=0; coin_session_id_o=2d155b7b-dbef-4922-928e-0447143a21e603ade0839fc31626; coin_session_nikename=157****6219; coin_session_user_id=2d155b7b-dbef-4922-928e-0447143a21e603ade0839fc31626; symbol=btc_usdt; ref="https://www.okex.com/c2c/trade/openTrade.do"; JSESSIONID=2C73CF7A29FDD9426FCBBAC0E38EDC15'
cookie = {'perm': '0E07A57D1F6381A694278FA3702C9A67',
          ' closesettings': '2048',
          ' __cfduid': 'd8104becfc6f68664245db364a5e7b5801507877774',
          ' tradetype': '0',
          ' language': '0',
          ' leverRate': '20',
          ' locale': 'zh_CN',
          ' treatyType_Btc': '201802090000012',
          ' future_contract_type_BTC': 'this_week',
          ' open-base-currency': 'cny',
          ' first_ref': "https://www.okex.com/future/future.do?symbol=0",
          ' lp': "https://www.okex.com/intro_apiOverview.html",
          ' open-trade-currency': 'btc', ' coin_session_logininfo': "",
          ' SHOW_NOTIFY': '0',
          ' coin_session_id_o': '2d155b7b-dbef-4922-928e-0447143a21e603ade0839fc31626',
          ' coin_session_nikename': '157****6219',
          ' coin_session_user_id': '2d155b7b-dbef-4922-928e-0447143a21e603ade0839fc31626',
          ' symbol': 'btc_usdt',
          ' ref': "https://www.okex.com/c2c/trade/openTrade.do",
          ' JSESSIONID': '2C73CF7A29FDD9426FCBBAC0E38EDC15'}
# print(type(cookie))

url = 'https://www.okex.com/v2/c2c-open/tradingOrders/group?digitalCurrencySymbol=btc&legalCurrencySymbol=cny'
t0 = time.time()
r = requests.get(url, cookies=cookie)
t1 = time.time()
print(t1-t0,'耗时')
print(r.status_code)
print(r.text)
data = r.text
q = queue.Queue()
today = datetime.date.today()
print(today)
q.put(today)
q.put(data)
print('**************')
print(q.get())















