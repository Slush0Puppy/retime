###########      IMPORTING      ##########

from tkinter import Tk,Label,StringVar,END,Entry,PhotoImage,Button
#import tkinter for gui
from os import _exit,getcwd #quitting and getting directory
from decimal import Decimal as d #decimal is much more accurate than floats
from decimal import ROUND_HALF_UP

###########      IMPORTING      ##########



###########      BULK OF CODE      ##########
# everything in this section is executed every time something changes.

def my_tracer(a, b, c): # traced variables send 3 arguments to this
    global fr
    try:
        fr=d(fv.get())
    except:
        try:
            fr=frac(fv.get())
        except:
            fr=1000 #by default, no rounding happens. not recommended
    if fr==0:
        fr=1000
    
    try:
        mod=cTime(mv.get(),fr)
        #print('c',mod)
    except:     #the modifier, added to the resulting time
        try:
            mod=frac(mv.get())
            #print('f',mod)
        except:
            try:
                mod=numtime(mv.get()) # yes
                #print('n',mod)
            except:
                mod=d(0)
                #print('0',mod)

    start=getnum(sv.get())
    end=getnum(ev.get())

    try:        # if youtube debug info is entered correctly, displays time as h m s ms
        if end-start+mod < 0:
            negative=True   # if start > end, a negative is put in front of the absolute value of
                            #the result
        else:
            negative=False
        new_text = negative*"- "+realtime(abs(end-start+mod))
    except:
        new_text = ""
        
    tv.set(new_text)
    #tv.set("- 999h 59m 59s 999ms")     #test line to get longest conceivable input
###########      BULK OF CODE      ##########


###########      MISC. FUNCTIONS      ##########
def close():    # normally, pressing the close button on tkinter window doesn't terminate script
    _exit(0) # <- ends script so it doesn't keep running


def copy(r,text):
    r.clipboard_clear()
    r.clipboard_append(text)
    r.update()


def getnum(v):
    var="x"
    vtext = v.split(',') #start point

    for i in range(len(vtext)):
        if vtext[i][4:7]=='cmt':
            var=d(vtext[i].split('"')[-2]) #crops out the useless stuff
            var = d(var - var%(d(1)/fr)) #rounds down the time to the start of a frame

    if var == "x":
        try:
            var=cTime(v,fr)
        except:
            try:
                var=numtime(v)
            except:
                var="x"

    return var
                

message=open(getcwd()+"\mod message\message.txt",'r').read()
def mm(x):
    x=x.replace("<starth>",realtime(d(getnum(sv.get()))))
    x=x.replace("<start>",uTime(d(getnum(sv.get()))))
    x=x.replace("<starts>",str(getnum(sv.get())))
    x=x.replace("<endh>",realtime(d(getnum(ev.get()))))
    x=x.replace("<end>",uTime(d(getnum(ev.get()))))
    x=x.replace("<ends>",str(getnum(sv.get())))
    x=x.replace("<result>",tv.get())
    x=x.replace("<framerate>",fv.get())
    x=x.replace("<modifier>",mv.get())
    return x

def cTime(a,f): #converts x:xx:xx.xxx to xxxxxx.xxx
    x=d(0)
    n=d(1)
    if a[0]=='-':
        n=d(-1)
        a=a[1:]
    try:
        c=d(a.split(";")[1])/d(f)
    except:
        c=d(0)
    b=a.split(";")[0].split(":")
    for i in range(len(b)):
        x+=d(60)**d(i)*d(b[-(i+1)])
    return n*(d(x)+c)

def uTime(a): #inverse of cTime
    a = a.quantize(d('1.111'), rounding=ROUND_HALF_UP)
    t1, t0 = divmod(a, 1)
    t2, t1 = divmod(t1, 60)
    t3, t2 = divmod(t2, 60)
    t0= round(t0*1000)
    if t0==0:
        t4, t3 = divmod(t3,  60)
    else:
        t4=0

    if t4!=0:       #formatting :(
        return("%d:%02d:%02d:%02d" % (t4, t3, t2, t1))
    elif t3!=0 and t0!=0:   # despite similarities, realtime and uTime can't be merged into
                            #the same function because :::. and h/m/s/ms are read differently
        return("%d:%02d:%02d.%03d" % (t3, t2, t1, t0))
    elif t3!=0 and t0==0:
        return("%d:%02d:%02d" % (t3, t2, t1))
    elif t2!=0 and t0!=0:
        return("%d:%02d.%03d" % (t2, t1,t0))
    elif t2!=0 and t0==0:
        return(("%d:%02d" % (t2, t1)))
    elif t0!=0:
        return("%d.%03d" % (t1,t0))
    else:
        return(str(int(t1)))
    

def realtime(time): # turn XXXXXX.xxx into XXXh XXm XXs xxxms
    #print(time)
    time=time.quantize(d('1.111'), rounding=ROUND_HALF_UP)
    ms=(1000*time)%1000
    time-=time%1
    s=time%60
    time=(time-s)/60      #finding number of hours, minutes, etc
    m=time%60
    time=(time-m)/60
    h=time

    #print(h)
    #print(m)
    #print(s)
    #print(ms)

    ms="{:03d}".format(int(ms)) #formatting
    if ms != '000':
        if h!=0:
            h=int(h)
            m="{:02d}".format(int(m))
            s="{:02d}".format(int(s))
            return(str(h)+'h '+str(m)+'m '+str(s)+'s '+str(ms)+'ms')
        else:
            m=int(m)
            s="{:02d}".format(int(s))
            return(str(m)+'m '+str(s)+'s '+str(ms)+'ms')
    else:
        if h!=0:
            h=int(h)
            m="{:02d}".format(int(m))
            s="{:02d}".format(int(s))
            return(str(h)+'h '+str(m)+'m '+str(s)+'s')
        else:
            m=int(m)
            s="{:02d}".format(int(s))
            return(str(m)+'m '+str(s)+'s')

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def numtime(x):
    for each in x:
        if each not in ['0','1','2','3','4','5','6','7','8',
                        '9','h','m','s',' ','-','.']:
            raise

    neg=d(x[0]=='-')*d(-2)+d(1)
    if neg<0:
        x=x[1:]
        
    x=' '+x.replace('ms','n')
    sp=findOccurrences(x,' ')


    hri=x.find('h')
    for each in sp:
        if each<hri-1:
            hrs=each
    try:
        h=d(x[hrs+1:hri])*d(3600)
    except:
        h=0

    mni=x.find('m')
    for each in sp:
        if each<mni-1:
            mns=each
    try:
        m=d(x[mns+1:mni])*d(60)
    except:
        m=0

    sei=x.find('s')
    for each in sp:
        if each<sei-1:
            ses=each
    try:
        s=d(x[ses+1:sei])
    except:
        s=0

    msi=x.find('n')
    for each in sp:
        if each<msi-1:
            mss=each
    try:
        ms=d(x[mss+1:msi])*d(0.001)
    except:
        ms=0

    return(neg*(h+m+s+ms))


def frac(x):
    a,b = x.split('/')
    return d(a)/d(b)

#print(realtime(d(5.999999999999972)))
#print(realtime(d(6.000000000000072)))     # float precision tests
#print(uTime(d(5.999999999999972)))        # i hate floats :(
#print(uTime(d(6.000000000000000072)))
#print(uTime(d(0.99)))
#print(frac("12/23"))
    
###########      MISC. FUNCTIONS      ##########



###########      GUI      ##########

root = Tk()
root.title("SP's Retiming Tool")
root.iconbitmap(getcwd()+"\source\icon.ico")
root.protocol("WM_DELETE_WINDOW", close) # procedure done upon clicking X
root.wm_attributes("-topmost", 1)

Label(root,text="Video FPS",font=("Hobo Std", 16)).grid(row=0,column=0)
Label(root,text="Modifier",font=("Hobo Std", 16)).grid(row=0,column=1,columnspan=3)

fv= StringVar()
fv.trace('w', my_tracer)
# ^ All input code will look something like this, allowing my_tracer() to
#update every time any updates are made

mv = StringVar()
mv.trace('w', my_tracer)

sv = StringVar() # using StringVar means the result can
                    #dynamically change as entry values change
sv.trace('w', my_tracer) # run my_tracer if value was changed (w = write)

ev = StringVar() # or StringVar(top) 
ev.trace('w', my_tracer) # run my_tracer if value was changed (w = write)

tv = StringVar() # or StringVar(top) 

def clear(): #restores all inputs to default values and clears the output
    f.delete(0, END)
    m.delete(0, END)
    s.delete(0, END)
    e.delete(0, END)
    tv.set("")

def paste0():
    mv.set(root.clipboard_get())

def paste1():
    sv.set(root.clipboard_get())

def paste2():
    ev.set(root.clipboard_get())
    
a,b,c=0,0,1         # his code is messy, knees weak, arms are heavy
Label(root,text="Video FPS",font=("Hobo Std", 16)).grid(row=a,column=b,columnspan=c)

a,b,c=0,1,3
Label(root,text="Modifier  ",font=("Hobo Std", 16)).grid(row=a,column=b,columnspan=c)

a,b,c=1,0,1
f=Entry(root,width=5, font=("Hobo Std", 30),justify='center',textvariable=fv)
f.grid(row=a,column=b,columnspan=c)

a,b,c=1,1,2
m=Entry(root,width=17, font=("Hobo Std", 18),justify='center',textvariable=mv)
m.grid(row=a,column=b,columnspan=c)

a,b,c=1,3,1
image1=PhotoImage(file=getcwd()+"\source\\arrow.png")
a0=Button(root,width=36,height=36,image=image1,command=paste0)
a0.grid(row=a,column=b,columnspan=c)

a,b,c=2,0,4
Label(root,text="Start frame",font=("Hobo Std", 16)).grid(row=a,column=b,columnspan=c)

a,b,c=3,0,3
s=Entry(root,width=24, font=("Hobo Std", 20),textvariable=sv)###
s.grid(row=a,column=b,columnspan=c)

a,b,c=3,3,1
a1=Button(root,width=36,height=36,image=image1,command=paste1)
a1.grid(row=a,column=b,columnspan=c)

a,b,c=4,0,4
Label(root,text="End frame",font=("Hobo Std", 16)).grid(row=a,column=b,columnspan=c)

a,b,c=5,0,3
e=Entry(root,width=24, font=("Hobo Std", 20),textvariable=ev)###
e.grid(row=a,column=b,columnspan=c)

a,b,c=5,3,1
a2=Button(root,width=36,height=36,image=image1,command=paste2)
a2.grid(row=a,column=b,columnspan=c)

a,b,c=6,0,3
t = Label(root,width=18, font=("Hobo Std", 30),background="white",textvariable=tv)
t.grid(row=a,column=b,columnspan=c,pady=(10,5))

a,b,c=6,3,1
image2=PhotoImage(file=getcwd()+"\source\clipboard.png")
cb = Button(root,width=40,height=58,image=image2, command=lambda: copy(root,tv.get()))
cb.grid(row=a,column=b,columnspan=c,pady=(5,0))

a,b,c=7,0,3
clb=Button(root,width=15, text="Clear",font=("Hobo Std", 30),command=clear)
clb.grid(row=a,column=b,columnspan=c,pady=5,padx=(10,0))

a,b,c=7,3,1
image3=PhotoImage(file=getcwd()+"\source\message.png")
mb = Button(root,width=66,height=66,image=image3, command=lambda: copy(root,mm(message)))
mb.grid(row=a,column=b,columnspan=c,pady=(5,0))



root.mainloop() #executes the code

###########      GUI      ##########
