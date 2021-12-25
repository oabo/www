



a = {'a':1,'b':2}

for x in a.items():
    print (x[1])

for x,e in enumerate



    { %
    for foo in all[stks] %}
    < td > {{foo.symbol}}, {{foo.次数}}, {{foo.市值.replace('亿', '')}} < / td >
{ % endfor %}

{ % set
this = foo.symbol + foo.次数 + foo.市值.replace('亿', '') %}

< tr >
< td > stocks < / td >
{ %
for ss in stocks %}
< td > {{ss}} < / td >
{ % endfor %}
< / tr >

{ %
for stks in all.keys() %}
< tr >

< td > {{stks.replace('-', '')}} < / td >

{ %
for ss in stocks %}
{ % set
this = 'no' %}
{ %
for foo in all[stks] %}
{ % if foo.symbol == ss %}
{ % set
this = foo.symbol + foo.次数 + foo.市值.replace('亿', '') %}
{ % endif %}
{ % endfor %}
< td > {{this}} < / td >
{ % endfor %}

< / tr >
{ % endfor %}