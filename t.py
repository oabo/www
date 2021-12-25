

import pickle as pk
import redis
r = redis.Redis(host='192.168.0.221', port=6379, db=3,decode_responses=True,password='!QAZ2wsx')
import traceback
#from base import  *
def redis_to_pk(name, key):
    try:
        return pk.loads(r.hget(name, key).encode('latin1'))
    except:
        traceback.print_exc()

def get_221_data(day):
    the_msg ='[]'
    try:
        the_msg = redis_to_pk('wx_send_message', day)
    except:
        pass
    return the_msg

data = get_221_data('0')["stocks"]
for x in data :
    print (x.symbol,x.次数,x.市值)


days=r.hkeys('wx_send_message')
days = sorted(days)
print(hs)

