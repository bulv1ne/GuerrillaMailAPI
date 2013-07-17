#!/usr/bin/env python

import requests
import time
import datetime
from urllib import urlencode

API_URL = 'http://api.guerrillamail.com/ajax.php?'

def timestamp_to_datetime(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

s = requests.Session()
def guerrilla_call(f, **kwargs):
    kwargs['f'] = f
    print f, kwargs
    return s.get(API_URL, params=urlencode(kwargs))

class GuerrillaMail(object):

    def __init__(self):
        self.sid_token = ''

    def get_email_address(self, lang='en', **kwargs):
        r = guerrilla_call('get_email_address', **kwargs)
        self.sid_token = r.json()['sid_token']
        return r.json()

    def set_email_user(self, email_user, **kwargs):
        r = guerrilla_call('set_email_user', email_user=email_user, sid_token=self.sid_token, **kwargs)
        self.sid_token = r.json()['sid_token']
        return r.json()

    def check_email(self, seq='0', **kwargs):
        return guerrilla_call('check_email', seq=str(seq), sid_token=self.sid_token, **kwargs).json()

    def get_email_list(self, offset=0, **kwargs):
        return guerrilla_call('get_email_list', offset=str(offset), sid_token=self.sid_token, **kwargs).json()

    def fetch_email(self, email_id, **kwargs):
        return guerrilla_call('fetch_email', email_id=email_id, sid_token=self.sid_token, **kwargs).json()

    def forget_me(self, email_addr, **kwargs):
        return guerrilla_call('forget_me', email_addr=email_addr, sid_token=self.sid_token, **kwargs).json()

    def del_email(self, email_ids, **kwargs):
        return guerrilla_call('del_email', email_ids=email_ids, sid_token=self.sid_token, **kwargs).json()

    def extend(self):
        return guerrilla_call('extend', sid_token=self.sid_token).json()


