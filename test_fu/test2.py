import queue
import threading
import requests

class MyThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.q = queue.Queue()
        self.name = name

    def get_q(self):
        return self.q

    # 重写线程中的run方法，使其在自己的线程中运行
    def run(self):
        currentThreadname = threading.current_thread()
        print('running in', currentThreadname)
        while True:
            r = requests.get(url, cookies=cookie)
            data = r.text
            print(data)
            self.q.put(data)

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
thread1 = MyThread(11, 'mythread')
thread1.start()
# thread.json_data(url, cookie)
q = thread1.get_q()
while True:
    if q.not_empty:
        print(q.get())
