
import mechanize
import random
import time


class Transaction(object):
    def __init__(self):
        self.custom_timers = {}
        self.base_url = 'http://www.aliceandolivia.com'
#        pass

    def run(self):
        br = mechanize.Browser()
        br.set_handle_robots(False)

        start_timer = time.time()
        resp = br.open(self.base_url)
#        resp = br.open(self.base_url + '/r/all/')
        resp.read()
        print br.form
        latency = time.time() - start_timer
        
        self.custom_timers['All_Items'] = latency
        assert (resp.code == 200), 'Bad HTTP Response'

#        assert (resp.code == 200), 'Bad Response: HTTP %s' % resp.code
#        assert ('Example Web Page' in resp.get_data())

#        r = random.uniform(1, 2)
#        time.sleep(r)
#        self.custom_timers['Example_Timer'] = r


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
