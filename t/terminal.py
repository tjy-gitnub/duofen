from msvcrt import getch
from colorama import init
init(autoreset=True)
black=30
red=31
green=32
yellow=33
blue=34
pink=35
cyan=36
white=37
def color(what,text=None,bg=None,bold=False,underline=False,blink=False,fanxian=False,disnone=False):
    clist=[]
    clist.append(str(text)) if text else None
    clist.append(str(bg+10)) if bg else None
    clist.append('1') if bold else None
    clist.append('4') if underline else None
    clist.append('5') if blink else None
    clist.append('7') if fanxian else None
    clist.append('8') if disnone else None
    return '\033['+';'.join(clist)+'m'+what+'\033[0m'


def setcolor(text=None,bg=None,bold=False,underline=False,blink=False,fanxian=False,disnone=False):
    clist=[]
    clist.append(str(text)) if text else None
    clist.append(str(bg+10)) if bg else None
    clist.append('1') if bold else None
    clist.append('4') if underline else None
    clist.append('5') if blink else None
    clist.append('7') if fanxian else None
    clist.append('8') if disnone else None
    print('\033['+';'.join(clist)+'m',end='\0')

def defcolor():
    print('\033[0m',end='')


def clear():
    print("\x1b[2J",end='')


def error(ty, msg):
    print(color("> ",red),end='')
    print(color(ty,white,red),end=' : ')
    print(color(msg,red,bold=True))
    print(color('Press any key to continue...',green))
    getch()
    return ''