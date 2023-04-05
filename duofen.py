import requests as r
from functools import cmp_to_key
from t.terminal import *
from webbrowser import open as open_inb
from t import pyui
init(autoreset=True)
pyui.settheme(blue,0,True)

def err(a,b):
    pyui.fade_print(a,0.03,fm=' |'+color('{}',red,bold=True),focm=color(' |',red,bold=True)+color('{}',red))
    print('   '+b)
    print(color('   Press any key to exit...',blue,bold=True),end='')
    getch()
    exit()

def bjpm(d):
    u = 'http://www.moofen.net/student/xqfx/kq/paper/aoq/list/{}/{}/{}/{}/{}/{}/{}'.format(
        d['schCode'], d['yearIn'], d['clzCode'], d['schStuCode'], d['examCode'], d['paperCode'], d['subject']['id'])
    zf = d['examScore']/100
    print(color('\n   班级排名\n',black,bg=white))
    print(color(' |',blue,bold=True)+'正在加载',end='')
    x = r.get(u, cookies=cook).json()
    clear()
    print(color('\n   班级排名\n',black,bg=white))
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
                    print(' '+color(str(i+1)+'\t'+str(tmp if tmp!=int(tmp) else int(tmp)),bg=red,bold=True))
                    continue
                print(' '+color(str(i+1),yellow,bold=True), end='')
        else:
            if p[0][1] == x['data']['min'][0][1]:
                print(' '+color('1\t'+str(tmp if tmp!=int(tmp) else int(tmp)),bg=red,bold=True))
                continue
            print(' '+color('1',yellow,bold=True), end='')
        print('\t'+str(tmp if tmp!=int(tmp) else int(tmp)))
    print(color(' Press any key to go back...',blue,bold=True),end='')
    getch()

def yj(d):
    u = 'http://www.moofen.net/student/xqfx/kq/paper/raw/get/{}/{}/{}/{}/{}/{}/{}'.format(
        d['schCode'], d['clzCode'], d['schStuCode'], d['examCode'], d['examDate'], d['subject']['id'], d['paperCode'])
    print(color('\n   原卷\n',black,bg=white))
    print(color(' |',blue,bold=True)+'正在加载',end='')
    x = r.get(u, cookies=cook).json()
    while 1:
        c=pyui.chooseinlist(list(range(1,len(x['data'])+1))+['返回'],color('\n   原卷\n',black,bg=white)+f'\n 共 {len(x["data"])} 张',fm='  {}',focm=' |{}')
        if c==len(x['data']):
            break
        else:
            open_inb(x['data'][c])
def tm(d):
    u = 'http://www.moofen.net/student/xqfx/kq/paper/aoq/get/{}/{}/{}/{}/{}/{}/{}'.format(
        d['schCode'], d['yearIn'],d['clzCode'],d['schStuCode'],d['examCode'], d['paperCode'],d['subject']['id'])
    print(color('\n   所有题目\n',black,bg=white))
    print(color(' |',blue,bold=True)+'正在加载',end='')
    x = r.get(u, cookies=cook).json()
    while 1:
        clear()
        print(color('\n   所有题目\n',black,bg=white))
        p=x['data']['items']
        for i in range(len(p)):
            if p[i]['isCorrect']:
                print(color(' '+p[i]['scoreNo'],green))
            else:
                _t='\t'
                print(color(f" {p[i]['scoreNo']}\t-{(p[i]['itemScore']-p[i]['stuScore'])/100}分\t{p[i]['stuScore']/100}/{p[i]['itemScore']/100}{_t+'标答:'+p[i]['answer'] if len(p[i]['answer']) else ''}",red))
        print(f" {color('|',blue,bold=True)}按 {color('d',underline=True,bold=True)} 查看详细,按 其它任意键 返回")
        print(color(' >',blue,bold=True),end='')
        t=getch()
        if t==b'd':
            clear()
            print(color('\n   所有题目\n',black,bg=white))
            p=x['data']['items']
            for i in range(len(p)):
                if p[i]['isCorrect']:
                    print(f"{color(' '+p[i]['scoreNo'],green)} 得分{p[i]['stuScore']/100}/{p[i]['itemScore']/100} 班级平均{p[i]['clzScore']/100}分,{p[i]['clzRatio']/100}%  年级平均{p[i]['grdScore']/100}分,{p[i]['grdRatio']/100}% {'标答 '+p[i]['answer'] if p[i]['type']['id']=='C' else p[i]['type']['name']}")
                else:
                    print(f"{color(' '+p[i]['scoreNo'],red)} 得分{p[i]['stuScore']/100}/{p[i]['itemScore']/100} 班级平均{p[i]['clzScore']/100}分,{p[i]['clzRatio']/100}%  年级平均{p[i]['grdScore']/100}分,{p[i]['grdRatio']/100}% {'标答 '+p[i]['answer']+',实答'+p[i]['choice'] if p[i]['type']['id']=='C' else p[i]['type']['name']}")
            print(f" {color('|',blue,bold=True)}按 {color('d',underline=True,bold=True)} 隐藏详细,按 其它任意键 返回")
            print(color(' >',blue,bold=True),end='')
            t=getch()
            if t==b'd':
                continue
        break


print(f"""
   {color('多分破解版',bold=True)}
   Developed by {color('谭景元',blue,bold=True)}
   {color('禁止外传',red,bold=True)}
""")
pyui.sleep(3)
clear()
print(color('\n   登录\n',black,bg=white))
pyui.fade_print('输入Cookies',0.03,fm=' |'+color('{}',blue,bold=True),focm=color(' |',blue,bold=True)+color('{}',bold=True))
yi = input('  ')
cook = eval('{"'+yi.replace('=', '":"').replace(';', '","')+'"}')
clear()
print(color('\n   登录\n',black,bg=white))
pyui.fade_print('输入schStuCode:',0.03,fm=' |'+color('{}',blue,bold=True),focm=color(' |',blue,bold=True)+color('{}',bold=True))
scst = input('  ')
# scst='2094763655660000'
clear()
print(color('\n |',blue,bold=True)+'正在加载',end='')
try:
    # 请求考试列表
    xi = r.get(
        'http://www.moofen.net/student/xqfx/kq/exam/list/280011/21/'+scst,
        cookies=cook).json()
except r.exceptions.JSONDecodeError:
    clear()
    err('高级错误','登录失败，请检查Cookie')

focbf=0
while True:
    testid=pyui.chooseinlist(xi['data'],color('   考试列表\n',black,bg=white),fm='  {[examName]}',focm=' |{[examName]}',foc=focbf)
    focbf=testid
    testname=xi['data'][testid]['examName']
    d = xi['data'][testid]
    if len(d['subjects']) > 1:
        # 有多个学科
        d = xi['data'][testid]['subjects'][pyui.chooseinlist(d['subjects'],color('\n   '+testname+'\n\n',black,bg=white)+f" {color(str(d['stuScore']/100),yellow)} 分   {d['scoreLevel']}\n\
 班排 {color(str(d['clzRankPosition']),yellow)} 名   年排 {color(str(d['grdRankPosition']),yellow)} 名\n",fm='  {[paperName]}',focm=' |{[paperName]}')]
        testname=d['paperName']
    while True:
        clear()
        tmp=pyui.chooseinlist(['成绩趋势(不可用)','班级成绩分布(不可用)','班级排名','所有题目','原卷','返回考试列表'],
            color('\n   '+testname+'\n\n',black,bg=white)+f" {color(str(d['stuScore']/100),yellow)} 分   {d['scoreLevel']}\n\
 班排 {color(str(d['clzRankPosition']),yellow)} 名   年排 {color(str(d['grdRankPosition']),yellow)} 名\n",fm='  {}',focm=' |{}')
        clear()
        if tmp==5:break
        [lambda x:None,lambda x:None,bjpm,tm,yj][tmp](d)