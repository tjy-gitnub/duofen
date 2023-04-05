from .terminal import *
from os import get_terminal_size as gts
from time import sleep

bg_color=white
text_color=black
theme_bold=False
def settheme(text=black,bg=white,bold=False):
    global bg_color,text_color,theme_bold
    text_color=text
    bg_color=bg
    theme_bold=bold


def chooseinlist(li,head='',tail='',fm='{}',focm='{}',foc=0):
    if focm=='{}':focm=fm
    set_cursor(False)
    ot=+len(head.split('\n'))+1
    while 1:
        print(clear_c+head)
        if gts().lines>=len(li)+ot:
            for i in range(len(li)):
                if i==foc:
                    print(color(focm.format(li[i]),text_color,bg_color,bold=theme_bold))
                else:
                    print(fm.format(li[i]))
        else:
            if foc+1+ot<=gts().lines:
                for i in range(gts().lines-ot):
                    if i==foc:
                        print(color(focm.format(li[i]),text_color,bg_color,bold=theme_bold))
                    else:
                        print(fm.format(li[i]))
            else:
                for i in range(foc-(gts().lines-ot)+1,foc+1):
                    if i==foc:
                        print(color(focm.format(li[i]),text_color,bg_color,bold=theme_bold))
                    else:
                        print(fm.format(li[i]))
        print(tail,end='')
        ge=getch()
        if ge==b'\xe0' or ge==b'\x00':
            ge=getch()
            if ge==b'H':
                foc+=(-1 if foc>0 else 0)
            elif ge==b'P':
                foc+=(1 if foc<len(li)-1 else 0)
        elif ge==b'\r':
            set_cursor(True)
            return foc
        elif ge==b'\x03':
            exit()

def fade_print(s,t,fm='{}',focm='{}',end='\n'):
    l=len(s)
    if focm=='{}':focm=fm
    for i in range(l-1,-1,-1):
        print('\r'+fm.format(f'{s[i:]}'),end='')
        sleep(t)
    print('\r'+focm.format(s),end=end)