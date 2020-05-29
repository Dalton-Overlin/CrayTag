"""
##############################
    CrayTag. Version 1.0
##############################
    Coded by: Dalton Overlin
##########################################################
    This is freeware! FREEWARE!
    So if someone asked you to pay for this program
    then they are a crook and you've been scammed!
    I am releasing this program for use at no cost.
    I will not be giving anyone, any form
    of authorization to sell this program (unmodified) for
    a price. Just be aware of this, this code is open source
    and is Freeware! Don't be tricked into paying for free software.
##########################################################
MIT License
-----------

Copyright (c) 2020 Dalton Overlin https://github.com/Dalton-Overlin/CrayTag
Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""
def installer(x):
    print(('\n'*2)+'This module: ( '+x+' ) is not installed.\n\nIf you type yes & press enter I will try and install it for you.\nIf not, just press enter and the program will exit.\nNote, here are two commands you can run to install the missing module.\n\n'+'python -m pip install '+x+'pip install '+x)
    c=str(input())
    if 'yes' in c.lower() or 'y' in c.lower():
        vue=os.system('python -m pip install '+str(x))
        if vue==0:
            return
        else:
            print('\n\nThis module: ',str(x),' could not be automatically installed, please install it manually.')
            input()
            exit()
    else:
        print('Exiting, Goodbye:)')
        exit()
try:
    import os
except:
    installer('os')
    import os
try:
    import string
except:
    installer('string')
    import string
try:
    import tkinter
    from tkinter import *
    from tkinter import filedialog
    from tkinter import PhotoImage
    import tkinter.font as tkFont
    import tkinter as tk
except:
    installer('tkinter')
    import tkinter
    from tkinter import *
    from tkinter import filedialog
    from tkinter import PhotoImage
    import tkinter.font as tkFont
    import tkinter as tk
try:
    import shutil
except:
    installer('shutil')
    import shutil
try:
    import time
except:
    installer('time')
    import time
try:
    import datetime
except:
    installer('datetime')
    import datetime
try:
    import eyed3
except:
    installer('eyed3')
    import eyed3
try:
    import tinytag
    from tinytag import TinyTag
except:
    installer('tinytag')
    import tinytag
    from tinytag import TinyTag

try:
    from PIL import ImageTk, Image
except:
    installer('pillow')
    from PIL import ImageTk, Image
eyed3.log.setLevel("ERROR")
class ex:
    thisOS = os.name
    tide = os.getcwd()
    activebackground="dark green"
    activeforeground="lawn green"
    fg="white"
    v='/'
    fold=None
    darkgreen='chartreuse4' # ex.darkgreen
    white='white' # ex.white
    black='dark green' # ex.black
    green4='green4' # ex.green4
    green3='green3' # ex.green3
    lime='lawn green' # ex.lime
    seagreen='SpringGreen4' # ex.seagreen For the editor window bg.
    forestgreen='forest green' # ex.forestgreen
if "nt" in ex.thisOS: ex.v = "/"
else: ex.v = "/"
if os.path.isfile(ex.tide+ex.v+'temp-vox-O.jpg'):
    os.remove(ex.tide+ex.v+'temp-vox-O.jpg')
if os.path.isfile(ex.tide+ex.v+'temp-vox.jpg'):
    os.remove(ex.tide+ex.v+'temp-vox.jpg')
def browse_button():
    filename = filedialog.askdirectory(initialdir = ex.tide)
    return filename
def browseFile():
    filename =  filedialog.askopenfilename(initialdir = ex.tide,title = "Select Image File",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    return filename
class maxx:
    div=' - ' # This can be anything like ' ', ' - ', etc.  maxx.div
def reno(Input):
    if type(Input)!=list:
        print('Input must be list!')
        return None
    else:
        if Input==[]:
            print('Cant send empty list for sorting!')
    newHold=[]
    Input.sort()
    for tv in Input: # This primes the data.
        t=str(tv)
        while t[0]==' ':
            t=t[1:]
        kpop=True
        try:
            if t[:2]=='NA' and t[2:3] in [' ','-','_','+','=','~','.']:
                temp = str(t)
                temp=temp.strip()
                if temp[:2]=='NA':
                    temp=temp[2:]
                temp=temp.strip()
                if temp[0] in ['-','_','+','=','~','.']:
                    cake=str(temp)
                    nun=temp[0]
                    temp=temp[1:]
                    temp=temp.strip()
                    if temp=='':
                        temp=maxx.div+cake
                    else:
                        temp=maxx.div+temp
                else:
                    temp=maxx.div+temp
                newHold.append(temp)
            elif t.replace(' ','')[0] in ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']:
                temp = str(t)
                temp=temp.strip()
                con=0
                for v in temp:
                    if v in ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        con+=1
                    else:
                        break
                temp=temp[con:]
                temp=temp.strip()
                if temp[0] in ['-','_','+','=','~','.']:
                    cake=str(temp)
                    nun=temp[0]
                    temp=temp[1:]
                    temp=temp.strip()
                    if temp=='':
                        temp=maxx.div+cake
                    else:
                        temp=maxx.div+temp
                else:
                    temp=maxx.div+temp
                newHold.append(temp)
            else:
                temp = str(t)
                temp=temp.strip()
                if temp[0] in ['-','_','+','=','~','.']:
                    cake=str(temp)
                    nun=temp[0]
                    temp=temp[1:]
                    temp=temp.strip()
                    if temp=='':
                        temp=maxx.div+cake
                    else:
                        temp=maxx.div+temp
                else:
                    temp=maxx.div+temp
                newHold.append(temp)
        except:
            temp = str(t)
            temp=temp.strip()
            newHold.append(maxx.div+temp)
    tim=len(str(len(newHold)))
    if tim==1:
        tim=2
    cova=1
    holder=[]
    for t in newHold:
        temp=str(cova)
        while len(temp) != tim:
            temp='0'+temp
        holder.append(temp+t)
        cova+=1
    return holder
class taffy:
    dataToReturn=None
def handler(available,issue): # This will handle missing album art and additional info.
    taffy.dataToReturn=None
    roota = tkinter.Tk()
    w = 270
    h = 257
    ws = roota.winfo_screenwidth()
    hs = roota.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    roota.geometry('%dx%d+%d+%d' % (w, h, x, y))
    roota.configure(background=ex.forestgreen)
    roota.title('Missing Data.')
    donna=400
    class zat:
        canva=None
    def quitt():
            roota.destroy()
            print('Good Data: ',taffy.dataToReturn)
    acv = tkinter.Button(roota,text ="Done",command=quitt, anchor='c',bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 14, 'bold'),activebackground=ex.activebackground,activeforeground='lime')
    acv.pack()
    acv.place(bordermode=OUTSIDE, height=27, width=donna,relx=0.5, rely=1.0, anchor=S)
    if issue=='cover': # This means mising cover art.
        w = 400
        h = 257
        ws = roota.winfo_screenwidth()
        hs = roota.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        roota.geometry('%dx%d+%d+%d' % (w, h, x, y))
        msa = Label(roota, text="Missing Album Art",bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 14, 'bold'),anchor='w')
        msa.place(bordermode=OUTSIDE, height=27, width=400,relx=0.5, rely=0.0, anchor=N)
        msa3 = Label(roota, text="Album Information",bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 14, 'bold'),anchor='w')
        msa3.place(bordermode=OUTSIDE, height=27, width=241,relx=0.697, rely=0.1, anchor=N)
        zat.canva=tkinter.Canvas(roota, bg=ex.green3, height=150, width=150)
        zat.canva.pack()
        zat.canva.place(bordermode=OUTSIDE,height=150,width=150,relx=0.2,rely=0.12,anchor=N)
        msa4 = Label(roota, text="Please Select Album Art.",bg=ex.forestgreen,fg=ex.activeforeground,font=('Helvetica', 8, 'bold'),anchor='w')
        msa4.place(bordermode=OUTSIDE, height=23, width=150,relx=0.20, rely=0.705, anchor=N)
        def upd():
            fbi=browseFile()
            if os.path.isfile(fbi)==False:
                a.config('Must Choose JPG/JPEG Image')
                return
            if fbi[-4:].lower()=='.jpg' or fbi[-5:].lower()=='.jpeg':
                pass
            else:
                a.config('Must Choose JPG/JPEG Image')
                return
            try:
                zat.canva.destroy()
                im = Image.open(fbi)
                image = Image.open(fbi)
                size = 150, 150
                image.thumbnail(size,Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)
                zat.canva=tkinter.Canvas(roota,bg=ex.green3, height=150, width=150)
                zat.canva.pack()
                zat.canva.place(bordermode=OUTSIDE,height=150,width=150,relx=0.2,rely=0.12,anchor=N)
                label = Label(zat.canva,image=photo)
                label.image = photo
                label.place(bordermode=OUTSIDE,relx=0,rely=0,width=150,height=150)
                flip=fbi.split('\\')
                flip=flip[-1]
                flip=fbi.split('/')
                flip=flip[-1]
                msa4.config(text=str(flip))
                taffy.dataToReturn=str(fbi)
            except:
                try:
                    zat.canva.destroy()
                except:
                    pass
                acv.config('Must Choose JPG/JPEG Image')
                zat.canva=tkinter.Canvas(roota, bg=ex.green3, height=150, width=150)
                zat.canva.pack()
                zat.canva.place(bordermode=OUTSIDE,height=150,width=150,relx=0.2,rely=0.12,anchor=N)
        a = tkinter.Button(roota,text ="Open Cover Selector",command=upd, anchor='c',bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 14, 'bold'),activebackground=ex.activebackground,activeforeground='lime')
        a.pack()
        a.place(bordermode=OUTSIDE, height=27, width=400,relx=0.5, rely=0.9, anchor=S)
        donna=400
        red = tkinter.Text(roota,font=('Helvetica', 12),bg=ex.activebackground,fg='lime')
        red.pack()
        red.place(bordermode=OUTSIDE, height=153, width=241,relx=0.697, rely=0.20, anchor=N)
        cod=True
        fix=True
        taft=''
        for t in available:
            if cod:
                cod=False
                taft+='Album: '+t+'\n'
            else:
                if fix:
                    taft+='Artist: '+t+'\n'
                    fix=False
                else:
                    taft+=t+'\n'
        red.insert("1.0", taft)
        red.config(state=DISABLED)
    elif issue=='album': # This means missing album name.
        msa = Label(roota, text="Missing Album Name",bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 14, 'bold'))
        msa.place(bordermode=OUTSIDE, height=27, width=400,relx=0.5, rely=0.0, anchor=N)
        w = 400
        h = 257
        ws = roota.winfo_screenwidth()
        hs = roota.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        roota.geometry('%dx%d+%d+%d' % (w, h, x, y))
        msa3 = Label(roota, text="Album Information",bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 14, 'bold'),anchor='e')
        msa3.place(bordermode=OUTSIDE, height=27, width=241,relx=0.697, rely=0.1, anchor=N)
        def leaveBlank():
            taffy.dataToReturn=None
            roota.destroy()
            return
        a = tkinter.Button(roota,text ="Leave Blank",command=leaveBlank, anchor='c',bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 14, 'bold'),activebackground=ex.activebackground,activeforeground='lime')
        a.pack()
        a.place(bordermode=OUTSIDE, height=27, width=400,relx=0.5, rely=0.9, anchor=S)
        donna=400
        red = tkinter.Text(roota,font=('Helvetica', 12),bg=ex.activebackground,fg='lime')
        red.pack()
        red.place(bordermode=OUTSIDE, height=153, width=241,relx=0.697, rely=0.20, anchor=N)
        fix=True
        taft=''
        for t in available:
            if fix:
                taft+='Artist: '+t+'\n'
                fix=False
            else:
                taft+=t+'\n'
        red.insert("1.0", taft)
        red.config(state=DISABLED)
        msa3g = Label(roota, text="Enter Below",bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 14, 'bold'),anchor='w')
        msa3g.place(bordermode=OUTSIDE, height=27, width=159,relx=0.198, rely=0.1, anchor=N)
        class jig:
            fig=True
        red2 = tkinter.Text(roota,wrap=WORD,font=('Helvetica', 12),bg='black',fg='lime',insertbackground='gold')
        red2.pack()
        red2.place(bordermode=OUTSIDE, height=153, width=159,relx=0.198, rely=0.20, anchor=N)
        red2.insert('1.0','Type Album Name Here')
        def jan(k):
            if jig.fig:
                red2.delete('1.0', END)
                jig.fig=False
        red2.bind('<Button-1>',jan)
        red2.bind('<Button-2>',jan)
        red2.bind('<Button-3>',jan)
        class aloe:
            vera=True
        def quitt2():
            yum=red2.get('1.0',END)
            if yum.replace(' ','').replace('\n','').replace('\t','')=='' or yum.replace(' ','').replace('\n','').replace('\t','')=='TypeAlbumNameHere':
                acv.config(text='No Text: Click Again To Skip',font=('Helvetica', 13, 'bold'))
                if aloe.vera==False:
                    taffy.dataToReturn=None
                    roota.destroy()
                    print('Bad Data')
                    return
                aloe.vera=False
            else:
                taffy.dataToReturn=yum.replace('\n','').replace('\t','')
                roota.destroy()
                print('Good Data: ',taffy.dataToReturn)
        acv.config(command=quitt2)
    elif issue=='artist': # This means no files for the album has an artist to fill the gap.
        msa = Label(roota, text="Missing Artist Name",bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 14, 'bold'))
        msa.place(bordermode=OUTSIDE, height=27, width=400,relx=0.5, rely=0.0, anchor=N)
        w = 400
        h = 257
        ws = roota.winfo_screenwidth()
        hs = roota.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        roota.geometry('%dx%d+%d+%d' % (w, h, x, y))
        msa3 = Label(roota, text="Album Information",bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 14, 'bold'),anchor='e')
        msa3.place(bordermode=OUTSIDE, height=27, width=241,relx=0.697, rely=0.1, anchor=N)
        def leaveBlank():
            taffy.dataToReturn=None
            roota.destroy()
            return
        a = tkinter.Button(roota,text ="Leave Blank",command=leaveBlank, anchor='c',bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 14, 'bold'),activebackground=ex.activebackground,activeforeground='lime')
        a.pack()
        a.place(bordermode=OUTSIDE, height=27, width=400,relx=0.5, rely=0.9, anchor=S)
        donna=400
        red = tkinter.Text(roota,font=('Helvetica', 12),bg=ex.activebackground,fg='lime')
        red.pack()
        red.place(bordermode=OUTSIDE, height=153, width=241,relx=0.697, rely=0.20, anchor=N)
        fix=True
        taft=''
        for t in available:
            if fix:
                taft+='Album: '+t+'\n'
                fix=False
            else:
                taft+=t+'\n'
        red.insert("1.0", taft)
        red.config(state=DISABLED)
        msa3g = Label(roota, text="Enter Below",bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 14, 'bold'),anchor='w')
        msa3g.place(bordermode=OUTSIDE, height=27, width=159,relx=0.198, rely=0.1, anchor=N)
        class jig:
            fig=True
        red2 = tkinter.Text(roota,wrap=WORD,font=('Helvetica', 12),bg='black',fg='lime',insertbackground='gold')
        red2.pack()
        red2.place(bordermode=OUTSIDE, height=153, width=159,relx=0.198, rely=0.20, anchor=N)
        red2.insert('1.0','Type Artist Name Here')
        def jan(k):
            if jig.fig:
                red2.delete('1.0', END)
                jig.fig=False
        red2.bind('<Button-1>',jan)
        red2.bind('<Button-2>',jan)
        red2.bind('<Button-3>',jan)
        class aloe:
            vera=True
        def quitt2():
            yum=red2.get('1.0',END)
            if yum.replace(' ','').replace('\n','').replace('\t','')=='' or yum.replace(' ','').replace('\n','').replace('\t','')=='TypeArtistNameHere':
                acv.config(text='No Text: Click Again To Skip',font=('Helvetica', 13, 'bold'))
                if aloe.vera==False:
                    taffy.dataToReturn=None
                    roota.destroy()
                    print('Bad Data')
                    return
                aloe.vera=False
            else:
                taffy.dataToReturn=yum.replace('\n','').replace('\t','')
                roota.destroy()
                print('Good Data: ',taffy.dataToReturn)
        acv.config(command=quitt2)
    else:
        try:
            roota.destroy()
        except:
            pass
        print('You sent a bad issue value.')
        return None
    roota.resizable(0, 0)
    roota.mainloop()
class origami:
    alert=True
    files=0
    size=480, 480
    genre=None # origami.genre
    setGen=False # origami.setGen
def masterLoop(path,alert):
    # alert will be true if alert user to correct issues. False if do nothing.
    origami.alert=alert
    origami.files=0
    def crawler(path): # This will be called recursively to handle sub folders.
        if os.path.isdir(path)==False:
            return
        files=os.listdir(path)
        if files==[]:
            return
        files.sort()
        trx=True
        mp3s=[]
        covers=[]
        for t in files:
            try:
                if t.lower().endswith('.mp3'):
                    trx=False
                    mp3s.append(t)
                else:
                    if t.lower().endswith('.jpg') or t.lower().endswith('.jpeg'):
                        covers.append(t)
            except:
                pass
            if os.path.isdir(path+ex.v+t):
                try:
                    crawler(path+ex.v+t) # This specifies recursive sub folder calls.
                except:
                    pass
        if trx or mp3s==[]:
            return
        cover=None
        cola=False
        if covers==[]: # This will try to extract album art from mp3s.
            cola=True
        else: # This will try to find cover as preferable, but use any image file as cover.
            cam=True
            for t in covers:
                if t.lower().startswith('cover'):
                    cover=path+ex.v+t
                    cam=False
                    break
            if cam:
                for t in covers:
                    if t.lower().startswith('folder'):
                        cover=path+ex.v+t
                        break
            if cover==None:
                cover=path+ex.v+covers[0]
        albums=[]
        data=[] # Meaning Filenames.
        artists=[]
        for t in mp3s:
            aus=eyed3.load(path+ex.v+t)
            alb=str(aus.tag.album)
            if alb in albums:
                c=albums.index(alb)
                data[c].append(t)
                artists[c].append(str(aus.tag.artist))
            else:
                albums.append(alb)
                data.append([t])
                artists.append([aus.tag.artist])
        c=0
        for t in data:
            data[c].sort()
            c+=1
        print('Albums: ','\n'.join(albums))
        if len(albums)==[]:
            return
        if len(albums)!=1:
            thebes=True
        else:
            thebes=False
        c=0
        newFnames=[]
        for t in data:
            egypt=t
            egypt.sort()
            if egypt==[]:
                print('Error: Nimue')
                return
            faith=reno(egypt)
            cv=0
            for b in egypt:
                os.rename(path+ex.v+b,path+ex.v+faith[cv])
                if os.path.isfile(path+ex.v+faith[cv]) == False:
                    print('Issue H2O',path+ex.v+faith[cv])
                    return
                cv+=1
            newFnames.append(faith)
        c=0
        if origami.alert:
            for t in albums:
                if t=='None' or t==None:
                    handler([artists[c][0],'\n'.join(data[c])],'album')
                    gdi=taffy.dataToReturn
                    if gdi==None or gdi=='' or gdi=='None':
                        pass
                    else:
                        albums[c]=str(gdi)
                c+=1
        c=0
        if origami.alert:
            for t in artists:
                check=True
                for v in t:
                    if v!='None' and v!= None:
                        check=False
                if check:
                    handler([albums[c],'\n'.join(data[c])],'artist')
                    gdi=taffy.dataToReturn
                    if gdi==None or gdi=='' or gdi=='None':
                        pass
                    else:
                        artists[c]=[str(gdi)]
                c+=1
        c=0
        print('Cover: ',cover)
        for t in newFnames:
            found=None # Will hold album cover path
            addCover=True # This will determine if cover was found or not.
            if thebes: # This means more than one album, so individual covers must be extracted.
                for v in t:
                    try:
                        tag = TinyTag.get(path+ex.v+v,image=True)
                        photor=tag.get_image()
                        if photor == '' or photor == None or len(photor) < 10:
                            found=None
                        else:
                            found=photor
                            break
                    except:
                        found=None
                if found==None and origami.alert: # This should call the missing data setter if checked.
                    handler([albums[c],artists[c][0],'\n'.join(t)],'cover')
                    found=taffy.dataToReturn
                else:
                    try:
                        grey=open(path+ex.v+'cover.jpg','wb')
                        grey.write(found)
                        grey.close()
                        found=path+ex.v+'cover.jpg'
                    except:
                        found=None
                if os.path.isfile(str(found)):
                    try:
                        im = Image.open(found)
                        im.save(path+ex.v+'cover.jpg','JPEG')
                        addCover=True
                    except:
                        addCover=False
                else:
                    addCover=False
            else: # This is for singular albums.
                if cover==None or os.path.isfile(cover)==False:
                    for v in t:
                        try:
                            tag = TinyTag.get(path+ex.v+v,image=True)
                            photor=tag.get_image()
                            if photor == '' or photor == None or len(photor) < 10:
                                found=None
                            else:
                                found=photor
                                break
                        except:
                            found=None
                    if found==None and origami.alert: # This should call the missing data setter if checked.
                        handler([albums[c],artists[c][0],'\n'.join(t)],'cover')
                        found=taffy.dataToReturn
                    else:
                        try:
                            grey=open(path+ex.v+'cover.jpg','wb')
                            grey.write(found)
                            grey.close()
                            found=path+ex.v+'cover.jpg'
                        except:
                            found=None
                    if os.path.isfile(str(found)):
                        print('con')
                        try:
                            im = Image.open(found)
                            im.save(path+ex.v+'cover.jpg','JPEG')
                            addCover=True
                        except:
                            addCover=False
                    else:
                        addCover=False
                else:
                    found=cover
                    addCover=True
            ''' < This should set the new Data > '''
            trackC=1 # Track count.
            for F in t: # F == filename.
                origami.files+=1
                try:
                    aus=eyed3.load(path+ex.v+F)
                    if addCover: # For cover.
                        try:
                            im = Image.open(found)
                            size = origami.size
                            im.thumbnail(size, Image.ANTIALIAS)
                            im.save(ex.tide+ex.v+'temp-vox.jpg','JPEG')
                            imagedata = open(ex.tide+ex.v+'temp-vox.jpg',"rb").read()
                            for t in [y.description for y in aus.tag.images]:
                                aus.tag.images.remove(t)
                            aus.tag.images.set(3,imagedata,"image/jpeg")
                        except:
                            print('Erra: JING')
                    aus.tag.album=str(albums[c])
                    try:
                        if artists[c][0]=='None' or artists[c][0]==None or artists[c][0]=='':
                            aus.tag.comments.set(str(albums[c]))
                        else:
                            aus.tag.comments.set(str(artists[c][0]))
                    except:
                        print('Erra Mohigo')
                    if str(aus.tag.artist)=='None' or str(aus.tag.artist)=='':
                        vin = 'None'
                        for k in artists[c]:
                            if k=='None' or k=='' or k==None:
                                pass
                            else:
                                vin=str(k)
                                break
                        try:
                            aus.tag.album_artist=vin
                            aus.tag.artist=vin
                            aus.tag.composer=vin
                            aus.tag.original_artist=vin
                            aus.tag.publisher=vin
                            aus.tag.copyright=vin
                        except:
                            print('Erra kiosk')
                    else:
                        vin = 'None'
                        for k in artists[c]:
                            if k=='None' or k=='' or k==None:
                                pass
                            else:
                                vin=str(k)
                                break
                        try:
                            aus.tag.publisher=vin
                            aus.tag.copyright=vin
                        except:
                            print('Erra vinmo')
                    if origami.setGen:
                        try:
                            aus.tag.genre=str(origami.genre)
                            aus.tag.non_std_genre=str(origami.genre)
                        except:
                            print('Erra halo')
                    aus.tag.track_num = trackC
                    trackC+=1
                    aus.tag.save()
                except:
                    print('Erra Shim')
            c+=1 # This must go to end of this for loop.
    try:
        crawler(path) # This always at end of masterLoop(). Above return statement.
    except:
        print('Bad')
        return 'Bad Path!'
    return str(origami.files)+' Files Done!'
class image:
    imageA="""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"""
    imageC="""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Ij8+Cjx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDQuNC4wLUV4aXYyIj4KIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgIHhtbG5zOmlwdGNFeHQ9Imh0dHA6Ly9pcHRjLm9yZy9zdGQvSXB0YzR4bXBFeHQvMjAwOC0wMi0yOS8iCiAgICB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIKICAgIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiCiAgICB4bWxuczpwbHVzPSJodHRwOi8vbnMudXNlcGx1cy5vcmcvbGRmL3htcC8xLjAvIgogICAgeG1sbnM6R0lNUD0iaHR0cDovL3d3dy5naW1wLm9yZy94bXAvIgogICAgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIgogICAgeG1sbnM6ZXhpZj0iaHR0cDovL25zLmFkb2JlLmNvbS9leGlmLzEuMC8iCiAgICB4bWxuczpwaG90b3Nob3A9Imh0dHA6Ly9ucy5hZG9iZS5jb20vcGhvdG9zaG9wLzEuMC8iCiAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIKICAgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpjODc0MGVkNy1lMzFmLWM0NDItOTY2NS1kYWYzYzMyNzkxOWEiCiAgIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6NTk3ZTU1MTEtYmJiOC00YjZhLTljMWYtZWI0YmZlNTdhZWJmIgogICB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6Yzg3NDBlZDctZTMxZi1jNDQyLTk2NjUtZGFmM2MzMjc5MTlhIgogICBHSU1QOkFQST0iMi4wIgogICBHSU1QOlBsYXRmb3JtPSJXaW5kb3dzIgogICBHSU1QOlRpbWVTdGFtcD0iMTU4NzM0NDM4NzUyMDc2MCIKICAgR0lNUDpWZXJzaW9uPSIyLjEwLjE4IgogICBkYzpGb3JtYXQ9ImltYWdlL3BuZyIKICAgZXhpZjpDb2xvclNwYWNlPSIxIgogICBleGlmOlBpeGVsWERpbWVuc2lvbj0iNTEyIgogICBleGlmOlBpeGVsWURpbWVuc2lvbj0iNTEyIgogICBwaG90b3Nob3A6Q29sb3JNb2RlPSIzIgogICB0aWZmOk9yaWVudGF0aW9uPSIxIgogICB0aWZmOlJlc29sdXRpb25Vbml0PSIyIgogICB0aWZmOlhSZXNvbHV0aW9uPSI3MjAwMDAvMTAwMDAiCiAgIHRpZmY6WVJlc29sdXRpb249IjcyMDAwMC8xMDAwMCIKICAgeG1wOkNyZWF0ZURhdGU9IjIwMTQtMTItMTBUMDQ6MDc6MTQrMDE6MDAiCiAgIHhtcDpDcmVhdG9yVG9vbD0iR0lNUCAyLjEwIgogICB4bXA6TWV0YWRhdGFEYXRlPSIyMDE0LTEyLTEyVDExOjUxOjI2KzAxOjAwIgogICB4bXA6TW9kaWZ5RGF0ZT0iMjAxNC0xMi0xMlQxMTo1MToyNiswMTowMCI+CiAgIDxpcHRjRXh0OkxvY2F0aW9uQ3JlYXRlZD4KICAgIDxyZGY6QmFnLz4KICAgPC9pcHRjRXh0OkxvY2F0aW9uQ3JlYXRlZD4KICAgPGlwdGNFeHQ6TG9jYXRpb25TaG93bj4KICAgIDxyZGY6QmFnLz4KICAgPC9pcHRjRXh0OkxvY2F0aW9uU2hvd24+CiAgIDxpcHRjRXh0OkFydHdvcmtPck9iamVjdD4KICAgIDxyZGY6QmFnLz4KICAgPC9pcHRjRXh0OkFydHdvcmtPck9iamVjdD4KICAgPGlwdGNFeHQ6UmVnaXN0cnlJZD4KICAgIDxyZGY6QmFnLz4KICAgPC9pcHRjRXh0OlJlZ2lzdHJ5SWQ+CiAgIDx4bXBNTTpIaXN0b3J5PgogICAgPHJkZjpTZXE+CiAgICAgPHJkZjpsaQogICAgICBzdEV2dDphY3Rpb249ImNyZWF0ZWQiCiAgICAgIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6Yzg3NDBlZDctZTMxZi1jNDQyLTk2NjUtZGFmM2MzMjc5MTlhIgogICAgICBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgQ0MgKFdpbmRvd3MpIgogICAgICBzdEV2dDp3aGVuPSIyMDE0LTEyLTEwVDA0OjA3OjE0KzAxOjAwIi8+CiAgICAgPHJkZjpsaQogICAgICBzdEV2dDphY3Rpb249InNhdmVkIgogICAgICBzdEV2dDpjaGFuZ2VkPSIvIgogICAgICBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOmJiNjBiMjY5LWRkYzAtYWE0OC1iNDIyLWQyNjMwZjMwNTY5MCIKICAgICAgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIENDIChXaW5kb3dzKSIKICAgICAgc3RFdnQ6d2hlbj0iMjAxNC0xMi0xMlQxMTo1MToyNiswMTowMCIvPgogICAgIDxyZGY6bGkKICAgICAgc3RFdnQ6YWN0aW9uPSJzYXZlZCIKICAgICAgc3RFdnQ6Y2hhbmdlZD0iLyIKICAgICAgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDpmNTM2NTY5Yi1iMmNiLTRiMjctYTgwZS00Y2JlNzliYzgyOTkiCiAgICAgIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkdpbXAgMi4xMCAoV2luZG93cykiCiAgICAgIHN0RXZ0OndoZW49IjIwMjAtMDQtMTlUMTg6NTk6NDciLz4KICAgIDwvcmRmOlNlcT4KICAgPC94bXBNTTpIaXN0b3J5PgogICA8cGx1czpJbWFnZVN1cHBsaWVyPgogICAgPHJkZjpTZXEvPgogICA8L3BsdXM6SW1hZ2VTdXBwbGllcj4KICAgPHBsdXM6SW1hZ2VDcmVhdG9yPgogICAgPHJkZjpTZXEvPgogICA8L3BsdXM6SW1hZ2VDcmVhdG9yPgogICA8cGx1czpDb3B5cmlnaHRPd25lcj4KICAgIDxyZGY6U2VxLz4KICAgPC9wbHVzOkNvcHlyaWdodE93bmVyPgogICA8cGx1czpMaWNlbnNvcj4KICAgIDxyZGY6U2VxLz4KICAgPC9wbHVzOkxpY2Vuc29yPgogIDwvcmRmOkRlc2NyaXB0aW9uPgogPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgIAo8P3hwYWNrZXQgZW5kPSJ3Ij8+Rb4XKwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+QEFAA7L/yZR10AAATPSURBVDgRAcQEO/sBAAAAAAAAAAAAAAAAAAAAAAAAAAAAD2MPH3QfAAAAAAAAAAAA4Yzh8Z3xAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAssCwAAAP///////wAAAAssCwAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAJKAn8+/z9/v0AAAADAgMJKAkAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAABC8EI4wj+OL477/vAAwADkoO+gn69e71+vX6AAAABgsGCxELBPcE87fzAfQBEUERCB4I3XTd/NH8AQAAACChIA42DgAAAP39/fLx8gHj7IYgMD4m3h0R/wAAAOTv/87Z9oLb+egfFxASEAMEAwAAAPLK8uBf4AMNWQ0XVxcBAgH+/v708/Ql6e13RRY6I/ofCfj//f7+/v8QCwInHAZRHwbg0O3ZCQgHCAcBAQEGGAb37/cCFE4UAQMB////+/r7AebtaEAUFg8Cwdj0ZWrtAhHsBBLsZWft2Nj6FRADiEMOCeLt////AAAAAQMBFE4UAuqq6vzy/AAAAPX09V8fCRIQA+DZ+WA25g0IAsa4Dsa4DgwLAik28NjY+hUUBIIM//z0/AAAAPzy/Oqq6gAAAAADNQMoxSgRsxGh6B+9/yJOeQpvbgT6+xX//xb//xb6+xVtbgNxcQP//xbg4BEHSwcmtiYENwQAAAAAAAAAAAAAHqceCqkKtv8mvv8jAA0AxcIN//8W//8W//8W//8WwsINAA0A6f8j5PojAA0AAAgAAAAAAAAABAAAAAAAAP///wD/AAAAAAAAAAAAAP4AAAAAAAAAAAAAAAAAAAAAAAAAAFwAIv0A/QAA3QAAAAAAAAAAAAIAAAAHQgcKHwoGCwbr6fn/AP9ObAqrrff7/P8AAAAAAAD7/P+rrPYWZBYBAAH65voAAAAABwAAAwAAAAAEC1ALIHsgAQoBDP4M3uT2HBcNT18RYzXlAwLwVVUJAP8Aqqz3k5/9OcojAAAA7sruAAAAAAkAAQ0BAOsAAhZXFgMMAwEBAQsMC6Lh9+7w/SAnB5/KGsD4CjpH8jpI8qT1DznJOQ0oDfjq+Nh+2AAEAAEGAQQIBAMUAwELVQsifiIBBAH+/v708/Qp6OpjPhUMEQeYAB/z/P4AAAADBAMAAAD46/jTedPvq+8ADAAECQQCAgL74/sD+9b7CDUICB0IAQEBBgcG6gkKsdfz/OQH4wcJBA4EAgIC9+X368DrzmTO9sP2AAsABAoEAwMD/fT9/vD+AQAAAAMuAyKKIvji+O667gQQBBhaGAMNA96G3vi8+AAAAAAAAAAAAAD9AAD5AAAEAAMQAwEHAfzk/AD+AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAltyUqyCoHQwcADQAAEQAADwAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAACDQIDCwMDjQO8c/x/uz+APwAAPsAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAPTR9AAAAAYWBiOJIwMhAwD3AAAAAAAAAAAAAAAAAAAAAAAAAAAAAF9AXI6aQo25AAAAAElFTkSuQmCC"""
class temp:
    roota=None
def mainCat(indo):
    class halo:
        nedra=True
    if os.path.isfile(ex.tide+ex.v+'temp-vox-O.jpg'):
        os.remove(ex.tide+ex.v+'temp-vox-O.jpg')
    if os.path.isfile(ex.tide+ex.v+'temp-vox.jpg'):
        os.remove(ex.tide+ex.v+'temp-vox.jpg')
    root = tkinter.Tk()
    def doDat():
        root.destroy()
        try:
            temp.roota.destroy()
        except:
            pass
        exit()
    root.protocol('WM_DELETE_WINDOW', doDat)
    w = 270
    h = 257
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    root.configure(background=ex.forestgreen)
    if indo == None:
        indo=ex.fold
    root.title(indo)
    def sorter():
        file = browse_button()
        if os.path.isdir(file):
            root.destroy()
            try:
                temp.roota.destroy()
            except:
                pass
            egg="Completed!"
            egg=masterLoop(file,halo.nedra)
            mainCat(egg)
        else:
            root.title('Select a Path...')
            ms.config(text='Select a Path!')
            return
    background_image=tkinter.PhotoImage(data = image.imageA)
    a = tkinter.Button(root,image=background_image,text ="",command=sorter, anchor='c',bg=ex.forestgreen,fg=ex.white,font=('Helvetica', 16, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    a.pack()
    a.place(bordermode=OUTSIDE, height=180, width=270,relx=0.5, rely=0.0, anchor=N)
    red = tkinter.Text(root,font=('Helvetica', 14),bg=ex.green4,fg='black',insertbackground='gold')
    red.pack()
    red.place(bordermode=OUTSIDE, height=25, width=270,relx=0.5, rely=0.695, anchor=N)
    red.insert("1.0", "")
    def credula():
        df=red.get("1.0", END).replace('\n','').replace('\t','')
        if df.replace(' ','').replace('\n','').replace('\t','')=='':
            sorter()
        else:
            df=df.replace('\n','').replace('\t','').replace('\\',ex.v).replace('/',ex.v)
            if os.path.isdir(df):
                root.destroy()
                try:
                    temp.roota.destroy()
                except:
                    pass
                egg="Completed!"
                egg=masterLoop(df,halo.nedra)
                mainCat(egg)
            else:
                root.title('Invalid Path!')
                ms.config(text='Invalid Path!')
                return
    ab = tkinter.Button(root,text ="Sort",command=credula, anchor='c',bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 14, 'bold'),activebackground=ex.activebackground,activeforeground='lime')
    ab.pack()
    ab.place(bordermode=OUTSIDE, height=27, width=135,relx=0.25, rely=1.0, anchor=S)
    def kala():
        root.destroy()
        exit()
    ac = tkinter.Button(root,text ="Exit",command=kala, anchor='c',bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 14, 'bold'),activebackground=ex.activebackground,activeforeground='lime')
    ac.pack()
    ac.place(bordermode=OUTSIDE, height=27, width=135,relx=0.75, rely=1.0, anchor=S)
    ms = Label(root, text="Display Prompts?",bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 10, 'bold'))
    ms.place(bordermode=OUTSIDE, height=27, width=267,relx=0.5, rely=0.9, anchor=S)
    def gray():
        if str(chkValue.get()) == 'True':
            halo.nedra=True
        else:
            halo.nedra=False
        print('Nedra',halo.nedra)
    def nono():
        gray()
    chkValue = tkinter.BooleanVar()
    chkValue.set(True)
    chkExample = tkinter.Checkbutton(root, var=chkValue,bg=ex.activebackground,activebackground=ex.activebackground,fg='black',activeforeground='lime',command=nono)
    chkExample.place(bordermode=OUTSIDE, height=27, width=20,relx=0.75, rely=0.9, anchor=S)
    def settings():
        temp.roota = tkinter.Tk()
        roota=temp.roota
        w = 270
        h = 257
        ws = roota.winfo_screenwidth()
        hs = roota.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        roota.geometry('%dx%d+%d+%d' % (w, h, x, y))
        roota.resizable(0, 0)
        roota.configure(background=ex.forestgreen)
        roota.title('Settings')
        choices = ['480 X 480 - Sandisk Clip Sport','300 X 300 Good Quality','600 X 600 iTunes','1,000 X 1,000 Better Quality','1,600 X 1,600 High Quality']
        tkvar = StringVar(roota)
        def setter(o):
            print(tkvar.get())
            if tkvar.get()==choices[0]:
                origami.size=480, 480
                print(origami.size)
            elif tkvar.get()==choices[1]:
                origami.size=300, 300
                print(origami.size)
            elif tkvar.get()==choices[2]:
                origami.size=600, 600
                print(origami.size)
            elif tkvar.get()==choices[3]:
                origami.size=1000, 1000
                print(origami.size)
            elif tkvar.get()==choices[4]:
                origami.size=1600, 1600
                print(origami.size)
            else:
                print('erra')
        popupMenu = OptionMenu(roota, tkvar, *choices,command=setter)
        popupMenu.config(highlightbackground=ex.activebackground,bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 12, 'bold'),activebackground=ex.activebackground,activeforeground='lime')
        popupMenu["menu"].config(bg="GREEN",font=('Helvetica', 13, 'bold'),fg=ex.activeforeground)
        popupMenu.place(bordermode=OUTSIDE, height=27, width=270,relx=0.5, rely=0.10, anchor=N)
        tkvar.set(choices[0])
        msa = Label(roota, text="Set Embedded Album Art Size",bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 12, 'bold'))
        msa.place(bordermode=OUTSIDE, height=27, width=270,relx=0.5, rely=0.0, anchor=N)
        choices2 = ['Dont Change','Acapella', 'Acid', 'Acid Jazz', 'Acid Punk', 'Acoustic', 'Alternative', 'Alternative Rock', 'Ambient', 'Anime', 'Avantgarde', 'Ballad', 'Bass', 'Beat', 'Bebob', 'Big Band', 'Black Metal', 'Bluegrass', 'Blues', 'Booty Bass', 'BritPop', 'Cabaret', 'Celtic', 'Chamber Music', 'Chanson', 'Chorus', 'Christian Gangsta Rap', 'Christian Rap', 'Christian Rock', 'Classic Rock', 'Classical', 'Club', 'Comedy', 'Contemporary Christian', 'Country', 'Crossover', 'Cult', 'Dance', 'Dance Hall', 'Darkwave', 'Death Metal', 'Disco', 'Dream', 'Drum & Bass', 'Drum Solo', 'Duet', 'Easy Listening', 'Egypt', 'Electronic', 'Ethnic', 'Euro-House', 'Euro-Techno', 'Eurodance', 'Fast Fusion', 'Folk', 'Folk-Rock', 'Folklore', 'Freestyle', 'Funk', 'Fusion', 'Game', 'Gangsta', 'Goa', 'Gospel', 'Gothic', 'Gothic Rock', 'Grunge', 'Hard Rock', 'Hardcore', 'Heavy Metal', 'Hip-Hop', 'House', 'House', 'Humour', 'Indie', 'Industrial', 'Instrumental', 'Instrumental Pop', 'Instrumental Rock', 'JPop', 'Jazz', 'Jazz+Funk', 'Jungle', 'Latin', 'Lo-Fi', 'Meditative', 'Merengue', 'Metal', 'Musical', 'National Folk', 'Native US', 'Negerpunk', 'New Age', 'New Wave', 'Noise', 'Oldies', 'Opera', 'Other', 'Polka', 'Polsk Punk', 'Pop', 'Pop-Folk', 'Pop/Funk', 'Porn Groove', 'Power Ballad', 'Pranks', 'Primus', 'Progressive Rock', 'Psychadelic', 'Psychedelic Rock', 'Punk', 'Punk Rock', 'R&B', 'Rap', 'Rave', 'Reggae', 'Retro', 'Revival', 'Rhythmic Soul', 'Rock', 'Rock & Roll', 'Salsa', 'Samba', 'Satire', 'Showtunes', 'Ska', 'Slow Jam', 'Slow Rock', 'Sonata', 'Soul', 'Sound Clip', 'Soundtrack', 'Southern Rock', 'Space', 'Speech', 'Swing', 'Symphonic Rock', 'Symphony', 'Synthpop', 'Tango', 'Techno', 'Techno-Industrial', 'Terror', 'Thrash Metal', 'Top 40', 'Trailer', 'Trance', 'Tribal', 'Trip-Hop', 'Unknown', 'Vocal', 'Vocal']
        tkvar2 = StringVar(roota)
        def setter2(o):
            print(tkvar2.get())
            if tkvar2.get()==choices2[0]:
                origami.setGen=False
                origami.genre=None
            else:
                origami.setGen=True
                origami.genre=str(tkvar2.get())
        popupMenu2 = OptionMenu(roota, tkvar2, *choices2,command=setter2)
        popupMenu2.config(highlightbackground=ex.activebackground,bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 12, 'bold'),activebackground=ex.activebackground,activeforeground='lime')
        popupMenu2["menu"].config(bg="GREEN",font=('Helvetica', 13, 'bold'),fg=ex.activeforeground)
        popupMenu2.place(bordermode=OUTSIDE, height=27, width=270,relx=0.5, rely=0.30, anchor=N)
        tkvar2.set(choices2[0])
        msa2 = Label(roota, text="Change Genre To?",bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 12, 'bold'))
        msa2.place(bordermode=OUTSIDE, height=27, width=270,relx=0.5, rely=0.2, anchor=N)
        def quitt():
            roota.destroy()
        acv = tkinter.Button(roota,text ="Done",command=quitt, anchor='c',bg=ex.activebackground,fg=ex.activeforeground,font=('Helvetica', 14, 'bold'),activebackground=ex.activebackground,activeforeground='lime')
        acv.pack()
        acv.place(bordermode=OUTSIDE, height=27, width=270,relx=0.5, rely=1.0, anchor=S)
        roota.mainloop()
    background_image2=tkinter.PhotoImage(data = image.imageC)
    app = tkinter.Button(root,image=background_image2,text ="",command=settings, anchor='c',bg=ex.forestgreen,fg=ex.white,font=('Helvetica', 16, 'bold'),activebackground=ex.activebackground,activeforeground=ex.activeforeground)
    app.pack()
    app.place(bordermode=OUTSIDE, height=20, width=20,relx=0.96, rely=0.885, anchor=S)
    root.mainloop()
mainCat('CrayTag 1.0')
