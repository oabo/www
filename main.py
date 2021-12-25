# coding:utf-8
from flask import Flask,render_template,request,url_for
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
import redis
import pickle as pk
import traceback
import time

r = redis.Redis(host='192.168.0.221', port=6379, db=3,decode_responses=True,password='!QAZ2wsx')

def redis_to_pk(name, key):
    try:
        return pk.loads(r.hget(name, key).encode('latin1'))
    except:
        traceback.print_exc()
def get_221_data(day):
    the_msg ='[]'
    try:
        the_msg = redis_to_pk('wx_send_message', day)
        stocks = the_msg['stocks']
        计算时间 =the_msg['计算时间']
    except:
        pass

    return stocks,计算时间

def get_221_all_days(days):
    all = {}

    #day0 = redis_to_pk('wx_send_message', '0')
    #all['最新'] = day0['stocks']

    for day in days:
        if day  == '0':
            continue
        a_day = redis_to_pk('wx_send_message', day)
        all[day] = a_day['stocks']

    stocks = []
    for day in all.keys():
        for x in all[day]:
            if x.symbol not in stocks:
                stocks.append(x.symbol)
    #print('stocks:',stocks)

    rtl =    [['stocks']+stocks]
    for x in all.keys():
        rtlx =[x.replace('-','.')]
        for sks in stocks:
            for s in all[x]:
                if s.symbol == sks:
                    rtlx .append( s.次数 + ', '+ s.市值.replace('亿', ''))
                    break
            else:
                rtlx.append('')
                #print(s.symbol)

        #print(rtlx)
        rtl.append(rtlx)
    return rtl


app = Flask(__name__)
buyed = ['300451',"600715",'603023','603183','000413','002370','300869']
@app.route('/pppppooooossssstttttt',methods=["POST"])
def pppppooooossssstttttt():
    if request.method == 'POST':
        try:
            print(request.stream.read().decode(),"IP:",request.remote_addr)

        except:
            print("except")
    return '.'


@app.route('/')
def home():

    days = r.hkeys('wx_send_message')
    days = sorted(days,reverse=True)
    all = get_221_all_days(days)


    #print(all)


    #stocks,计算时间  =  get_221_data('0')
    day = time.strftime('%Y-%m-%d')
    #return 'test'
    return render_template('home.html',Title = day + '选股' ,all = all,buyed = buyed)




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)

