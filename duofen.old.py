import requests as r
from functools import cmp_to_key
from t.terminal import *
from webbrowser import open as open_inb
from t import pyui
init(autoreset=True)
pyui.settheme(0,green)

def bjpm(d):
    u = 'http://www.moofen.net/student/xqfx/kq/paper/aoq/list/{}/{}/{}/{}/{}/{}/{}'.format(
        d['schCode'], d['yearIn'], d['clzCode'], d['schStuCode'], d['examCode'], d['paperCode'], d['subject']['id'])
    zf = d['examScore']/100
    print(color('班级排名',bg=green))
    print(color('正在加载...',bg=blue))
    x = r.get(u, cookies=cook).json()
    clear()
    print(color('班级排名',bg=green))
    x['data']['others'].insert(0, x['data']['min'][0])
    def _cmp(r, u):
        # cmp func(in sort)
        if r[1] > u[1]:
            return -1
        elif r[1] < u[1]:
            return 1
        else:
            return 0
    p = sorted(x['data']['others'], key=cmp_to_key(_cmp))
    for i in range(len(p)):
        # 不并列显示排名
        tmp=round(zf*p[i][1]*2)/2
        if i!=0:
            if p[i][1] != p[i-1][1]:
                if p[i][1] == x['data']['min'][0][1]:
                    print(color(str(i+1)+'\t'+str(tmp if tmp!=int(tmp) else int(tmp)),bg=red,bold=True))
                    continue
                print(color(str(i+1),yellow,bold=True), end='')
        else:
            print(color('1',yellow,bold=True), end='')
        print('\t'+str(tmp if tmp!=int(tmp) else int(tmp)))
    input()

def yj(y):
    u = 'http://www.moofen.net/student/xqfx/kq/paper/raw/get/{}/{}/{}/{}/{}/{}/{}'.format(
        d['schCode'], d['clzCode'], d['schStuCode'], d['examCode'], d['examDate'], d['subject']['id'], d['paperCode'])
    print(color('原卷',bg=green))
    print(color('正在加载...',bg=blue))
    x = r.get(u, cookies=cook).json()
    while 1:
        c=pyui.chooseinlist(list(range(1,len(x['data'])+1))+['退出'],color('原卷',bg=green)+f'\n 共 {len(x["data"])} 张')
        if c==len(x['data']):
            break
        else:
            open_inb(x['data'][c])


clear()
print(color('输入Cookies: ',bg=green))
yi = input()
cook = eval('{"'+yi.replace('=', '":"').replace(';', '","')+'"}')
clear()
print(color('输入schStuCode: ',bg=green))
# scst='2094763655660000'
scst = input()
clear()
print(color('正在加载...',bg=green))
try:
    # 请求考试列表
    xi = r.get(
        'http://www.moofen.net/student/xqfx/kq/exam/list/280011/21/'+scst,
        cookies=cook).json()
except r.exceptions.JSONDecodeError:
    clear()
    error('高级错误',
          '登录失败，请检查Cookie')
    exit()

focbf=0
while True:
    testid=pyui.chooseinlist(xi['data'],color('考试列表',bg=green),fm='{[examName]}',foc=focbf)
    focbf=testid
    testname=xi['data'][testid]['examName']
    d = xi['data'][testid]
    if len(d['subjects']) > 1:
        # 有多个学科
        d = xi['data'][testid]['subjects'][pyui.chooseinlist(d['subjects'],color(testname,bg=green)+ color(' > ',green) +color('学科',bg=green),fm='{[paperName]}')]
        testname=d['paperName']
    while True:
        clear()
        tmp=pyui.chooseinlist(['成绩趋势(不可用)','班级成绩分布(不可用)','班级排名','错题(不可用)','原卷','返回考试列表'],
            f"{color(testname,bg=green)}\n\
{color(str(d['stuScore']/100),yellow)} 分   {d['scoreLevel']}\n\
班排 {color(str(d['clzRankPosition']),yellow)} 名   年排 {color(str(d['grdRankPosition']),yellow)} 名")
        clear()
        if tmp==5:break
        [lambda x:None,lambda x:None,bjpm,lambda x:None,yj][tmp](d)