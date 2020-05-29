class ver:
    sion="2.1" # Version number of program. # ver.sion
"""
##############################
    CrayTag.
##############################
    Coded by: Dalton Overlin
##########################################################
    Last Code Revision Date: May. 26th, 2020
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
import os, sys, threading
def ravage():
    try:
        os._exit(0)
    except:
        print('Kraken Error!')
        sys.exit("Kraken Error!")
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
            ravage()
    else:
        print('Exiting, Goodbye:)')
        ravage()
sys.setrecursionlimit(100000)
try:
    import random
except:
    installer('random')
    import random
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
class dirTree:
    A=os.getcwd()
    B=os.getcwd()
def browse_button():
    coo = filedialog.askdirectory(initialdir = dirTree.B)
    if os.path.isdir(coo):
        dirTree.B=str(coo)
    return coo
def browseFile():
    return filedialog.askopenfilename(initialdir = dirTree.A,title = "Select Image File",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
class ram:
    NotifyMissingArtist=True # DONE
    NotifyMissingCover=True # DONE
    NotifyMissingAlbumName=True # DONE
    RenumberFilenames=True # DONE
    ResizeAlbumCoverSize=480,480 # DONE
    ChangeAllGenres=False # DONE
    GenreToChangeTo="Pop" # DONE
    LiveFeedback="Initializing." # The GUI will pull live data from here.
    files=0 # Number of mp3s tagged.
    rt=None # The root holder for settings.
    CoversToSearchFor=None # Filenames of covers to search for.
    FilesToDelete=None # List of files to delete.
    coffee=None # DONE
    DontResiveJPG=False # DONE
    WillEmbedArt=True # DONE
    KeepBackup=True # DONE
    DeleteEmbedded=True # DONE
    KillThread=False # DONE
class maxx:
    div=' ' # This can be anything like ' ', ' - ', etc.  maxx.div
def reno(Input):
    if type(Input)!=list:
        print('Input must be list!')
        return None
    else:
        if Input==[]:
            print('Cant send empty list for sorting!')
    if ram.RenumberFilenames==False:
        return Input
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
class ex:
    tide = os.getcwd()
class img:
    A="""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"""
    B="""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"""
    C="""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"""
    D="""iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAMAAAD04JH5AAAC+lBMVEUAAADB//7U//5m//ti//xf//12//ts//tm//xl//vs//9o//ve//5l//xm//uH//sy//Bj//xD/+9f//1n//tl//tj//xl//xl//z0//9l//tm//tn//su/+/8//////9k//xl//xm//v////x//9d//z////9///7///+//////////9l//r3//////9l//tl//pm//z///9j//xl//v5///////9//////////9l//tl//tm//z9///5//////////////9l//v///9g//1l//tl//v////////8///////+///+///////+//9m//tv//z8//////9Z//r+//9m//xm//v+///8///7///////3///////9//9k//z9///+//9l//uX//5j//xm//tl//tl//v0//81/+9k//z+//9o//1m//yS//75//9i//xh//xh//z+//+w//8y/++l//+h///v///i//6F//6P//6X//13//vh///d///s//9///yc//5k//yG//zX///L///p//90//x5//u1//y6///u///l//7L//29//20///S//6k//zB///c//+Q//yt//y5//+6//2o//yU//y9//3r///T///J//9Z//qy//3R//7e//74//9h//r4//+p//3H//01//Dv//7e//0u//7X//vn//7r//5o//Ga//+U//Xj///t//40//6W//W5//hw//7B//hg//CF//7w//+N//6M//VS/+/A//+s///I//84/+6g//+8//+x//9J/++O//XY//9X/+/F///Q//p4//7///+Q//VZ//4w//5Q//7T//99//NN//75///K//mZ//Z2//L0//90//5e//6B//ND//59//5l//Gd//WJ//5y//KJ//TN//+u//en//aF//Sk//46//61//94//Jm//5V//43/+6B//xq//5j//6V//9s//Gp//9t//5G//6B//5L/+9A//49/+4p/+5G/+95//NZ//CJ31dwAAAAqXRSTlMAAwVUkqwOFWFQBwoKdjII8o7+sAZMi11wDTchI/Yc+XJqEb0Ps7IpEdebpxwV0VsYe8uYLiKsL/SVVz1tNBjEaYIq3KlBJ+qhJXFRQ+NaRpRHVr53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"""
try:
    if os.path.isfile(ex.tide+'/'+'temp-vox.jpg'):
        os.remove(ex.tide+'/'+'temp-vox.jpg')
except:
    print('Erra Prince7')
class taffy:
    dataToReturn=None
def handler(available,issue): # This will handle missing album art and additional info.
    ram.LiveFeedback='Waiting for User to Enter Missing data.'
    taffy.dataToReturn=None
    roota = tkinter.Tk()
    background_image2=tkinter.PhotoImage(data = img.D)
    roota.iconphoto(False, background_image2)
    w = 600
    h = 400
    ws = roota.winfo_screenwidth()
    hs = roota.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    roota.geometry('%dx%d+%d+%d' % (w, h, x, y))
    roota.resizable(0, 0)
    roota.configure(bg='#000099')
    roota.title('Missing Album '+issue[0].upper()+issue[1:]+'.')
    donna=400
    class zat:
        canva=None
        canC='#000099' # zat.canC
    def quitt():
            roota.destroy()
    acv = tkinter.Button(roota,text ="Done",bg='#000099',fg='#00ffff',activebackground='#00ffff',activeforeground='#000099',command=quitt, anchor='c',font=('Helvetica', 14, 'bold'))
    acv.pack()
    acv.place(bordermode=OUTSIDE, height=50, width=300,relx=0.5, rely=1.0, anchor=SW)
    if issue=='cover':
        msa = Label(roota, text="Missing Album Art",font=('Helvetica', 13, 'bold'),bg='#000099',fg='#00ffff',activebackground='#00ffff',activeforeground='#000099',anchor='center')
        msa.place(bordermode=OUTSIDE, height=27, width=300,relx=0.0, rely=0.0, anchor=NW)
        msa3 = Label(roota, text="Album Information",bg='#000099',fg='#00ffff',activebackground='#00ffff',activeforeground='#000099',font=('Helvetica', 13, 'bold'),anchor='center')
        msa3.place(bordermode=OUTSIDE, height=27, width=300,relx=1.0, rely=0.0, anchor=NE)
        zat.canva=tkinter.Canvas(roota, relief=SUNKEN, height=300, width=300,bg=zat.canC,highlightthickness=1, highlightbackground="cyan")
        zat.canva.pack()
        zat.canva.place(bordermode=OUTSIDE,height=300,width=300,relx=0,rely=0.056,anchor=NW)
        msa4 = Label(roota, relief=SUNKEN,text="Please Select Album Art in JPG Format.",bg='#000099',fg='#00ffff',activebackground='#00ffff',activeforeground='#000099',font=('Helvetica', 9, 'bold'),anchor='w')
        msa4.place(bordermode=OUTSIDE, height=26, width=300,relx=0.0, rely=0.84, anchor=W)
        def upd():
            fbi=str(browseFile())
            roota.lift()
            if os.path.isfile(fbi)==False:
                msa4.config(text='Must Choose JPG/JPEG Image.')
                return
            if fbi.lower().endswith('.jpg') or fbi.lower().endswith('.jpeg'):
                pass
            else:
                msa4.config(text='Must Choose JPG/JPEG Image..')
                return
            taffy.dataToReturn=str(fbi)
            roota.destroy()
            return
            '''
            try:
                zat.canva.destroy()
                image2 = Image.open(fbi)
                size = 300, 300
                image2.thumbnail(size,Image.ANTIALIAS)
                photo2 = ImageTk.PhotoImage(image2)
                zat.canva=tkinter.Canvas(roota,  height=300, width=300,bg=zat.canC,highlightthickness=1, highlightbackground="cyan")
                zat.canva.pack()
                zat.canva.place(bordermode=OUTSIDE,height=300,width=300,relx=0,rely=0.06,anchor=NW)
                labelh = Label(zat.canva,bg='#000099',fg='#00ffff',activebackground='#00ffff',activeforeground='#000099',image=photo2)
                labelh.image = photo2
                labelh.place(bordermode=OUTSIDE,relx=0,rely=0,width=302,height=302)
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
                acv.config(text='Must Choose JPG/JPEG Image...')
                zat.canva=tkinter.Canvas(roota,  height=300, width=300,bg=zat.canC,highlightthickness=1, highlightbackground="cyan")
                zat.canva.pack()
                zat.canva.place(bordermode=OUTSIDE,height=300,width=300,relx=0,rely=0.06,anchor=NW)
            '''
        a = tkinter.Button(roota,text ="Open Cover Selector",bg='#000099',fg='#00ffff',activebackground='#00ffff',activeforeground='#000099',command=upd, anchor='c',font=('Helvetica', 14, 'bold'))
        a.pack()
        a.place(bordermode=OUTSIDE, height=50, width=300,relx=0.0, rely=1.0, anchor=SW)
        donna=400
        red = tkinter.Text(roota,bg='#000099',fg='#00ffff',font=('Helvetica', 12,'bold'))
        red.pack()
        red.place(bordermode=OUTSIDE, height=325, width=300,relx=1, rely=0.060, anchor=NE)
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
                    taft+='__________________Filenames Below\n'
                    fix=False
                else:
                    taft+=t+'\n'
        red.insert("1.0", taft)
        red.config(state=DISABLED)
    else:
        val='Missing Album '
        if issue=='name':
            val+='Name'
        else:
            val+='Artist'
        msa = Label(roota, text=val,font=('Helvetica', 13, 'bold'),bg='#000099',fg='#00ffff',activebackground='#00ffff',activeforeground='#000099',anchor='center')
        msa.place(bordermode=OUTSIDE, height=27, width=300,relx=0.0, rely=0.0, anchor=NW)
        msa3 = Label(roota, text="Album Information",bg='#000099',fg='#00ffff',activebackground='#00ffff',activeforeground='#000099',font=('Helvetica', 13, 'bold'),anchor='center')
        msa3.place(bordermode=OUTSIDE, height=27, width=300,relx=1.0, rely=0.0, anchor=NE)
        def leaveBlank():
            taffy.dataToReturn=None
            roota.destroy()
            return
        a = tkinter.Button(roota,text ="Leave Blank",command=leaveBlank, anchor='c',font=('Helvetica', 14, 'bold'),bg='#000099',fg='#00ffff',activebackground='#00ffff',activeforeground='#000099')
        a.pack()
        a.place(bordermode=OUTSIDE, height=50, width=300,relx=0.0, rely=1.0, anchor=SW)
        donna=400
        red = tkinter.Text(roota,bg='#000099',fg='#00ffff',font=('Helvetica', 12,'bold'))
        red.pack()
        red.place(bordermode=OUTSIDE, height=325, width=300,relx=1, rely=0.060, anchor=NE)
        fix=True
        taft=''
        for t in available:
            if fix:
                if issue=='name':
                    taft+='Artist: '
                else:
                    taft+='Album: '
                taft+=t+'\n'+'__________________Filenames Below\n'
                fix=False
            else:
                taft+=t+'\n'
        red.insert("1.0", taft)
        red.config(state=DISABLED)
        class jig:
            fig=True
            a=True
        red2 = tkinter.Text(roota,wrap=WORD,font=('Helvetica', 12),bg='#b3b3ff',fg='black')
        red2.pack()
        red2.place(bordermode=OUTSIDE, height=230, width=300,relx=0, rely=0.062, anchor=NW)
        dell='Type '
        if issue=='name':
            dell+='Album Name Here'
        else:
            dell+='Artist Name Here'
        red2.insert('1.0',dell)
        def clara():
            red2.delete('1.0',END)
            jig.fig=False
        if issue=='name':
            jig.a=True # 'Artist Name Here'
        else:
            jig.a=False # 'Album Name Here'
        def randoM():
            clara()
            temp=''
            if jig.a: # Gen Album Name
                A=['Analyse', 'Approach', 'Area', 'Assess', 'Assume', 'Authority', 'Available', 'Benefit', 'Concept', 'Consist', 'Constitute', 'Context', 'Contract', 'Create', 'Data', 'Define', 'Derive', 'Distribute', 'Economy', 'Environment', 'Establish', 'Estimate', 'Evident', 'Export', 'Factor', 'Finance', 'Formula', 'Function', 'Identify', 'Income', 'Indicate', 'Individual', 'Interpret', 'Involve', 'Issue', 'Labour', 'Legal', 'Legislate', 'Major', 'Method', 'Occur', 'Percent', 'Period', 'Policy', 'Principle', 'Proceed', 'Process', 'Require', 'Research', 'Respond', 'Role', 'Section', 'Sector', 'Significant', 'Similar', 'Source', 'Specific', 'Structure', 'Theory', 'Vary', 'Achieve', 'Acquire', 'Administrate', 'Affect', 'Appropriate', 'Aspect', 'Assist', 'Category', 'Chapter', 'Commission', 'Community', 'Complex', 'Compute', 'Conclude', 'Conduct', 'Consequent', 'Construct', 'Consume', 'Credit', 'Culture', 'Design', 'Distinct', 'Element', 'Equate', 'Evaluate', 'Feature', 'Final', 'Focus', 'Impact', 'Injure', 'Institute', 'Invest', 'Item', 'Journal', 'Maintain', 'Normal', 'Obtain', 'Participate', 'Perceive', 'Positive', 'Potential', 'Previous', 'Primary', 'Purchase', 'Range', 'Region', 'Regulate', 'Relevant', 'Reside', 'Resource', 'Restrict', 'Secure', 'Seek', 'Select', 'Site', 'Strategy', 'Survey', 'Text', 'Tradition', 'Transfer', 'Alternative', 'Circumstance', 'Comment', 'Compensate', 'Component', 'Consent', 'Considerable', 'Constant', 'Constrain', 'Contribute', 'Convene', 'Coordinate', 'Core', 'Corporate', 'Correspond', 'Criteria', 'Deduce', 'Demonstrate', 'Document', 'Dominate', 'Emphasis', 'Ensure', 'Exclude', 'Framework', 'Fund', 'Illustrate', 'Immigrate', 'Imply', 'Initial', 'Instance', 'Interact', 'Justify', 'Layer', 'Link', 'Locate', 'Maximise', 'Minor', 'Negate', 'Outcome', 'Partner', 'Philosophy', 'Physical', 'Proportion', 'Publish', 'React', 'Register', 'Rely', 'Remove', 'Scheme', 'Sequence', 'Sex', 'Shift', 'Specify', 'Sufficient', 'Task', 'Technical', 'Technique', 'Technology', 'Valid', 'Volume', 'Access', 'Adequate', 'Annual', 'Apparent', 'Approximate', 'Attitude', 'Attribute', 'Civil', 'Code', 'Commit', 'Communicate', 'Concentrate', 'Confer', 'Contrast', 'Cycle', 'Debate', 'Despite', 'Dimension', 'Domestic', 'Emerge', 'Error', 'Ethnic', 'Goal', 'Grant', 'Hence', 'Hypothesis', 'Implement', 'Implicate', 'Impose', 'Integrate', 'Internal', 'Investigate', 'Job', 'Label', 'Mechanism', 'Obvious', 'Occupy', 'Option', 'Output', 'Overall', 'Parallel', 'Parameter', 'Phase', 'Predict', 'Principal', 'Prior', 'Professional', 'Project', 'Promote', 'Regime', 'Resolve', 'Retain', 'Series', 'Statistic', 'Status', 'Stress', 'Subsequent', 'Sum', 'Summary', 'Undertake', 'Academy', 'Adjust', 'Alter', 'Amend', 'Aware', 'Capacity', 'Challenge', 'Clause', 'Compound', 'Conflict', 'Consult', 'Contact', 'Decline', 'Discrete', 'Draft', 'Enable', 'Energy', 'Enforce', 'Entity', 'Equivalent', 'Evolve', 'Expand', 'Expose', 'External', 'Facilitate', 'Fundamental', 'Generate', 'Generation', 'Image', 'Liberal', 'Licence', 'Logic', 'Margin', 'Medical', 'Mental', 'Modify', 'Monitor', 'Network', 'Notion', 'Objective', 'Orient', 'Perspective', 'Precise', 'Prime', 'Psychology', 'Pursue', 'Ratio', 'Reject', 'Revenue', 'Stable', 'Style', 'Substitute', 'Sustain', 'Symbol', 'Target', 'Transit', 'Trend', 'Version', 'Welfare', 'Whereas', 'Abstract', 'Accurate', 'Acknowledge', 'Aggregate', 'Allocate', 'Assign', 'Attach', 'Author', 'Bond', 'Brief', 'Capable', 'Cite', 'Cooperate', 'Discriminate', 'Display', 'Diverse', 'Domain', 'Edit', 'Enhance', 'Estate', 'Exceed', 'Expert', 'Explicit', 'Federal', 'Fee', 'Flexible', 'Furthermore', 'Gender', 'Ignorant', 'Incentive', 'Incidence', 'Incorporate', 'Index', 'Inhibit', 'Initiate', 'Input', 'Instruct', 'Intelligent', 'Interval', 'Lecture', 'Migrate', 'Minimum', 'Ministry', 'Motive', 'Neutral', 'Nevertheless', 'Overseas', 'Precede', 'Presume', 'Rational', 'Recover', 'Reveal', 'Scope', 'Subsidy', 'Tape', 'Trace', 'Transform', 'Transport', 'Underlie', 'Utilise', 'Adapt', 'Adult', 'Advocate', 'Aid', 'Channel', 'Chemical', 'Classic', 'Comprehensive', 'Comprise', 'Confirm', 'Contrary', 'Convert', 'Couple', 'Decade', 'Definite', 'Deny', 'Differentiate', 'Dispose', 'Dynamic', 'Eliminate', 'Empirical', 'Equip', 'Extract', 'File', 'Finite', 'Foundation', 'Globe', 'Grade', 'Guarantee', 'Hierarchy', 'Identical', 'Ideology', 'Infer', 'Innovate', 'Insert', 'Intervene', 'Isolate', 'Media', 'Mode', 'Paradigm', 'Phenomenon', 'Priority', 'Prohibit', 'Publication', 'Quote', 'Release', 'Reverse', 'Simulate', 'Sole', 'Somewhat', 'Submit', 'Successor', 'Survive', 'Thesis', 'Topic', 'Transmit', 'Ultimate', 'Unique', 'Visible', 'Voluntary', 'Abandon', 'Accompany', 'Accumulate', 'Ambiguous', 'Append', 'Appreciate', 'Arbitrary', 'Automate', 'Bias', 'Chart', 'Clarify', 'Commodity', 'Complement', 'Conform', 'Contemporary', 'Contradict', 'Crucial', 'Currency', 'Denote', 'Detect', 'Deviate', 'Displace', 'Drama', 'Eventual', 'Exhibit', 'Exploit', 'Fluctuate', 'Guideline', 'Highlight', 'Implicit', 'Induce', 'Inevitable', 'Infrastructure', 'Inspect', 'Intense', 'Manipulate', 'Minimise', 'Nuclear', 'Offset', 'Paragraph', 'Plus', 'Practitioner', 'Predominant', 'Prospect', 'Radical', 'Random', 'Reinforce', 'Restore', 'Revise', 'Schedule', 'Tense', 'Terminate', 'Theme', 'Thereby', 'Uniform', 'Vehicle', 'Via', 'Virtual', 'Visual', 'Widespread', 'Accommodate', 'Analogy', 'Anticipate', 'Assure', 'Attain', 'Behalf', 'Bulk', 'Cease', 'Coherent', 'Coincide', 'Commence', 'Compatible', 'Concurrent', 'Confine', 'Controversy', 'Converse', 'Device', 'Devote', 'Diminish', 'Distort', 'Duration', 'Erode', 'Ethic', 'Format', 'Found', 'Inherent', 'Insight', 'Integral', 'Intermediate', 'Manual', 'Mature', 'Mediate', 'Medium', 'Military', 'Minimal', 'Mutual', 'Norm', 'Overlap', 'Passive', 'Portion', 'Preliminary', 'Protocol', 'Qualitative', 'Refine', 'Relax', 'Restrain', 'Revolution', 'Rigid', 'Route', 'Scenario', 'Sphere', 'Subordinate', 'Supplement', 'Suspend', 'Team', 'Temporary', 'Trigger', 'Unify', 'Violate', 'Vision', 'Adjacent', 'Albeit', 'Assemble', 'Collapse', 'Colleague', 'Compile', 'Conceive', 'Convince', 'Depress', 'Encounter', 'Enormous', 'Forthcoming', 'Incline', 'Integrity', 'Intrinsic', 'Invoke', 'Levy', 'Likewise', 'Nonetheless', 'Notwithstanding', 'Odd', 'Ongoing', 'Panel', 'Persist', 'Pose', 'Reluctance', 'So-called', 'Straightforward', 'Undergo', 'Whereby']
                B=['for', 'and', 'nor', 'but', 'or', 'yet', 'so']
                C=['Agastopia', 'Argle-bargle', 'Bibble', 'Billingsgate', 'Blatherskite', 'Bobsy-die', 'Borborygmus', 'Bumfuzzle', 'Cabotage', 'Cacophony', 'Cattywampus', 'Collywobbles', 'Conjubilant', 'Curmudgeon', 'Doodle Sack', 'Discombobulate', 'Deipnophobia', 'Dipthong', 'Donkey Engine', 'Dragoman', 'Erf', 'Erinaceous', 'Finifugal', 'Fipple', 'Firman', 'Flummox', 'Frankenfood', 'Fudgel', 'Funambulist', 'Futz', 'Gabelle', 'Gardyloo', 'Gibberish', 'Gobbledygook', 'Groke', 'Grommet', 'Gubbins', 'Halfpace', 'Hullaballoo', 'Ill-willie', 'Impignorate', 'Jentacular', 'Kakorrhaphiophobia', 'Kerfuffle', 'Lackadaisical', 'Lamprophony', 'Lollygag', 'Macrosmatic', 'Meldrop', 'Nudiustertian', 'Obelus', 'Octothorpe', 'Oxter', 'Pauciloquent', 'Poppycock', 'Quire', 'Quomodocunquizing', 'Ragamuffin', 'Ratoon', 'Salopettes', 'Smicker', 'Snickersnee', 'Sprunt', 'Taradiddle', 'Tittynope', 'Ulotrichous', 'Valetudinarian', 'Whiffler', 'Whippersnapper', 'Widdershins', 'Woebegone', 'Winklepicker', 'Xertz', 'Yarborough', 'Zoanthropy']
                cd=random.choice([1,2])
                for t in range(cd):
                    temp+=random.choice(A)+' '
                    temp+=random.choice(B)+' '
                    temp+=random.choice(C)+' '
                temp=temp.strip()
            else: # For missing album.
                A=['Michael', 'Christopher', 'Jessica', 'Matthew', 'Ashley', 'Jennifer', 'Joshua', 'Amanda', 'Daniel', 'David', 'James', 'Robert', 'John', 'Joseph', 'Andrew', 'Ryan', 'Brandon', 'Jason', 'Justin', 'Sarah', 'William', 'Jonathan', 'Stephanie', 'Brian', 'Nicole', 'Nicholas', 'Anthony', 'Heather', 'Eric', 'Elizabeth', 'Adam', 'Megan', 'Melissa', 'Kevin', 'Steven', 'Thomas', 'Timothy', 'Christina', 'Kyle', 'Rachel', 'Laura', 'Lauren', 'Amber', 'Brittany', 'Danielle', 'Richard', 'Kimberly', 'Jeffrey', 'Amy', 'Crystal', 'Michelle', 'Tiffany', 'Jeremy', 'Benjamin', 'Mark', 'Emily', 'Aaron', 'Charles', 'Rebecca', 'Jacob', 'Stephen', 'Patrick', 'Sean', 'Erin', 'Zachary', 'Jamie', 'Kelly', 'Samantha', 'Nathan', 'Sara', 'Dustin', 'Paul', 'Angela', 'Tyler', 'Scott', 'Katherine', 'Andrea', 'Gregory', 'Erica', 'Mary', 'Travis', 'Lisa', 'Kenneth', 'Bryan', 'Lindsey', 'Kristen', 'Jose', 'Alexander', 'Jesse', 'Katie', 'Lindsay', 'Shannon', 'Vanessa', 'Courtney', 'Christine', 'Alicia', 'Cody', 'Allison', 'Bradley', 'Samuel', 'Shawn', 'April', 'Derek', 'Kathryn', 'Kristin', 'Chad', 'Jenna', 'Tara', 'Maria', 'Krystal', 'Jared', 'Anna', 'Edward', 'Julie', 'Peter', 'Holly', 'Marcus', 'Kristina', 'Natalie', 'Jordan', 'Victoria', 'Jacqueline', 'Corey', 'Keith', 'Monica', 'Juan', 'Donald', 'Cassandra', 'Meghan', 'Joel', 'Shane', 'Phillip', 'Patricia', 'Brett', 'Ronald', 'Catherine', 'George', 'Antonio', 'Cynthia', 'Stacy', 'Kathleen', 'Raymond', 'Carlos', 'Brandi', 'Douglas', 'Nathaniel', 'Ian', 'Craig', 'Brandy', 'Alex', 'Valerie', 'Veronica', 'Cory', 'Whitney', 'Gary', 'Derrick', 'Philip', 'Luis', 'Diana', 'Chelsea', 'Leslie', 'Caitlin', 'Leah', 'Natasha', 'Erika', 'Casey', 'Latoya', 'Erik', 'Dana', 'Victor', 'Brent', 'Dominique', 'Frank', 'Brittney', 'Evan', 'Gabriel', 'Julia', 'Candice', 'Karen', 'Melanie', 'Adrian', 'Stacey', 'Margaret', 'Sheena', 'Wesley', 'Vincent', 'Alexandra', 'Katrina', 'Bethany', 'Nichole', 'Larry', 'Jeffery', 'Curtis', 'Carrie', 'Todd', 'Blake', 'Christian', 'Randy', 'Dennis', 'Alison', 'Trevor', 'Seth', 'Kara', 'Joanna', 'Rachael', 'Luke', 'Felicia', 'Brooke', 'Austin', 'Candace', 'Jasmine', 'Jesus', 'Alan', 'Susan', 'Sandra', 'Tracy', 'Kayla', 'Nancy', 'Tina', 'Krystle', 'Russell', 'Jeremiah', 'Carl', 'Miguel', 'Tony', 'Alexis', 'Gina', 'Jillian', 'Pamela', 'Mitchell', 'Hannah', 'Renee', 'Denise', 'Molly', 'Jerry', 'Misty', 'Mario', 'Johnathan', 'Jaclyn', 'Brenda', 'Terry', 'Lacey', 'Shaun', 'Devin', 'Heidi', 'Troy', 'Lucas', 'Desiree', 'Jorge', 'Andre', 'Morgan', 'Drew', 'Sabrina', 'Miranda', 'Alyssa', 'Alisha', 'Teresa', 'Johnny', 'Meagan', 'Allen', 'Krista', 'Marc', 'Tabitha', 'Lance', 'Ricardo', 'Martin', 'Chase', 'Theresa', 'Melinda', 'Monique', 'Tanya', 'Linda', 'Kristopher', 'Bobby', 'Caleb', 'Ashlee', 'Kelli', 'Henry', 'Garrett', 'Mallory', 'Jill', 'Jonathon', 'Kristy', 'Anne', 'Francisco', 'Danny', 'Robin', 'Lee', 'Tamara', 'Manuel', 'Meredith', 'Colleen', 'Lawrence', 'Christy', 'Ricky', 'Randall', 'Marissa', 'Ross', 'Mathew', 'Jimmy', 'Abigail', 'Kendra', 'Carolyn', 'Billy', 'Deanna', 'Jenny', 'Jon', 'Albert', 'Taylor', 'Lori', 'Rebekah', 'Cameron', 'Ebony', 'Wendy', 'Angel', 'Micheal', 'Kristi', 'Caroline', 'Colin', 'Dawn', 'Kari', 'Clayton', 'Arthur', 'Roger', 'Roberto', 'Priscilla', 'Darren', 'Kelsey', 'Clinton', 'Walter', 'Louis', 'Barbara', 'Isaac', 'Cassie', 'Grant', 'Cristina', 'Tonya', 'Rodney', 'Bridget', 'Joe', 'Cindy', 'Oscar', 'Willie', 'Maurice', 'Jaime', 'Angelica', 'Sharon', 'Julian', 'Jack', 'Jay', 'Calvin', 'Marie', 'Hector', 'Kate', 'Adrienne', 'Tasha', 'Michele', 'Ana', 'Stefanie', 'Cara', 'Alejandro', 'Ruben', 'Gerald', 'Audrey', 'Kristine', 'Ann', 'Shana', 'Javier', 'Katelyn', 'Brianna', 'Bruce', 'Deborah', 'Claudia', 'Carla', 'Wayne', 'Roy', 'Virginia', 'Haley', 'Brendan', 'Janelle', 'Jacquelyn', 'Beth', 'Edwin', 'Dylan', 'Dominic', 'Latasha', 'Darrell', 'Geoffrey', 'Savannah', 'Reginald', 'Carly', 'Fernando', 'Ashleigh', 'Aimee', 'Regina', 'Mandy', 'Sergio', 'Rafael', 'Pedro', 'Janet', 'Kaitlin', 'Frederick', 'Cheryl', 'Autumn', 'Tyrone', 'Martha', 'Omar', 'Lydia', 'Jerome', 'Theodore', 'Abby', 'Neil', 'Shawna', 'Sierra', 'Nina', 'Tammy', 'Nikki', 'Terrance', 'Donna', 'Claire', 'Cole', 'Trisha', 'Bonnie', 'Diane', 'Summer', 'Carmen', 'Mayra', 'Jermaine', 'Eddie', 'Micah', 'Marvin', 'Levi', 'Emmanuel', 'Brad', 'Taryn', 'Toni', 'Jessie', 'Evelyn', 'Darryl', 'Ronnie', 'Joy', 'Adriana', 'Ruth', 'Mindy', 'Spencer', 'Noah', 'Raul', 'Suzanne', 'Sophia', 'Dale', 'Jodi', 'Christie', 'Raquel', 'Naomi', 'Kellie', 'Ernest', 'Jake', 'Grace', 'Tristan', 'Shanna', 'Hilary', 'Eduardo', 'Ivan', 'Hillary', 'Yolanda', 'Alberto', 'Andres', 'Olivia', 'Armando', 'Paula', 'Amelia', 'Sheila', 'Rosa', 'Robyn', 'Kurt', 'Dane', 'Glenn', 'Nicolas', 'Gloria', 'Eugene', 'Logan', 'Steve', 'Ramon', 'Bryce', 'Tommy', 'Preston', 'Keri', 'Devon', 'Alana', 'Marisa', 'Melody', 'Rose', 'Barry', 'Marco', 'Karl', 'Daisy', 'Leonard', 'Randi', 'Maggie', 'Charlotte', 'Emma', 'Terrence', 'Justine', 'Britney', 'Lacy', 'Jeanette', 'Francis', 'Tyson', 'Elise', 'Sylvia', 'Rachelle', 'Stanley', 'Debra', 'Brady', 'Charity', 'Hope', 'Melvin', 'Johanna', 'Karla', 'Jarrod', 'Charlene', 'Gabrielle', 'Cesar', 'Clifford', 'Byron', 'Terrell', 'Sonia', 'Julio', 'Stacie', 'Shelby', 'Shelly', 'Edgar', 'Roxanne', 'Dwayne', 'Kaitlyn', 'Kasey', 'Jocelyn', 'Alexandria', 'Harold', 'Esther', 'Kerri', 'Ellen', 'Abraham', 'Cedric', 'Carol', 'Katharine', 'Shauna', 'Frances', 'Antoine', 'Tabatha', 'Annie', 'Erick', 'Alissa', 'Sherry', 'Chelsey', 'Franklin', 'Branden', 'Helen', 'Traci', 'Lorenzo', 'Dean', 'Sonya', 'Briana', 'Angelina', 'Trista', 'Bianca', 'Leticia', 'Tia', 'Kristie', 'Stuart', 'Laurie', 'Harry', 'Leigh', 'Elisabeth', 'Alfredo', 'Aubrey', 'Ray', 'Arturo', 'Joey', 'Kelley', 'Max', 'Andy', 'Latisha', 'Johnathon', 'India', 'Eva', 'Ralph', 'Yvonne', 'Warren', 'Kirsten', 'Miriam', 'Kelvin', 'Lorena', 'Staci', 'Anita', 'Rene', 'Cortney', 'Orlando', 'Carissa', 'Jade', 'Camille', 'Leon', 'Paige', 'Marcos', 'Elena', 'Brianne', 'Dorothy', 'Marshall', 'Daryl', 'Colby', 'Terri', 'Gabriela', 'Brock', 'Gerardo', 'Jane', 'Nelson', 'Tamika', 'Alvin', 'Chasity', 'Trent', 'Jana', 'Enrique', 'Tracey', 'Antoinette', 'Jami', 'Earl', 'Gilbert', 'Damien', 'Janice', 'Christa', 'Tessa', 'Kirk', 'Yvette', 'Elijah', 'Howard', 'Elisa', 'Desmond', 'Clarence', 'Alfred', 'Darnell', 'Breanna', 'Kerry', 'Nickolas', 'Maureen', 'Karina', 'Roderick', 'Rochelle', 'Rhonda', 'Keisha', 'Irene', 'Ethan', 'Alice', 'Allyson', 'Hayley', 'Trenton', 'Beau', 'Elaine', 'Demetrius', 'Cecilia', 'Annette', 'Brandie', 'Katy', 'Tricia', 'Bernard', 'Wade', 'Chance', 'Bryant', 'Zachery', 'Clifton', 'Julianne', 'Angelo', 'Elyse', 'Lyndsey', 'Clarissa', 'Meaghan', 'Tanisha', 'Ernesto', 'Isaiah', 'Xavier', 'Clint', 'Jamal', 'Kathy', 'Salvador', 'Jena', 'Marisol', 'Darius', 'Guadalupe', 'Chris', 'Patrice', 'Jenifer', 'Lynn', 'Landon', 'Brenton', 'Sandy', 'Jasmin', 'Ariel', 'Sasha', 'Juanita', 'Israel', 'Ericka', 'Quentin', 'Jayme', 'Damon', 'Heath', 'Kira', 'Ruby', 'Rita', 'Tiara', 'Jackie', 'Jennie', 'Collin', 'Lakeisha', 'Kenny', 'Norman', 'Leanne', 'Hollie', 'Destiny', 'Shelley', 'Amie', 'Callie', 'Hunter', 'Duane', 'Sally', 'Serena', 'Lesley', 'Connie', 'Dallas', 'Simon', 'Neal', 'Laurel', 'Eileen', 'Lewis', 'Bobbie', 'Faith', 'Brittani', 'Shayla', 'Eli', 'Judith', 'Terence', 'Ciara', 'Charlie', 'Alyson', 'Vernon', 'Alma', 'Quinton', 'Nora', 'Lillian', 'Leroy', 'Joyce', 'Chrystal', 'Marquita', 'Lamar', 'Ashlie', 'Kent', 'Emanuel', 'Joanne', 'Gavin', 'Yesenia', 'Perry', 'Marilyn', 'Graham', 'Constance', 'Lena', 'Allan', 'Juliana', 'Jayson', 'Shari', 'Nadia', 'Tanner', 'Isabel', 'Becky', 'Rudy', 'Blair', 'Christen', 'Rosemary', 'Marlon', 'Glen', 'Genevieve', 'Damian', 'Michaela', 'Shayna', 'Marquis', 'Fredrick', 'Celeste', 'Bret', 'Betty', 'Kurtis', 'Rickey', 'Dwight', 'Rory', 'Mia', 'Josiah', 'Norma', 'Bridgette', 'Shirley', 'Sherri', 'Noelle', 'Chantel', 'Alisa', 'Zachariah', 'Jody', 'Christin', 'Julius', 'Gordon', 'Latonya', 'Lara', 'Lucy', 'Jarrett', 'Elisha', 'Deandre', 'Audra', 'Beverly', 'Felix', 'Alejandra', 'Nolan', 'Tiffani', 'Lonnie', 'Don', 'Darlene', 'Rodolfo', 'Terra', 'Sheri', 'Iris', 'Maxwell']
                cd=random.choice([2,3])
                for t in range(cd):
                    temp+=random.choice(A)+' '
                temp=temp.strip()
            red2.insert('1.0',temp)
        ax = tkinter.Button(roota,text ="Generate Random",command=randoM, anchor='c',font=('Helvetica', 14, 'bold'),bg='#000099',fg='#00ffff',activebackground='#00ffff',activeforeground='#000099')
        ax.pack()
        ax.place(bordermode=OUTSIDE, height=50, width=300,relx=0.0, rely=0.875, anchor=SW)
        ax2 = tkinter.Button(roota,text ="Clear Text Box",command=clara, anchor='c',font=('Helvetica', 14, 'bold'),bg='#000099',fg='#00ffff',activebackground='#00ffff',activeforeground='#000099')
        ax2.pack()
        ax2.place(bordermode=OUTSIDE, height=50, width=300,relx=0.0, rely=0.75, anchor=SW)
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
                    return
                aloe.vera=False
            else:
                taffy.dataToReturn=yum.replace('\n','').replace('\t','').strip()
                roota.destroy()
        acv.config(command=quitt2)
    roota.mainloop()
def masterLoop(path):
    ram.files=0
    def crawler(path): # This will be called recursively to handle sub folders.
        if ram.KillThread:
            ravage()
            return
        if os.path.isdir(path)==False:
            return
        files=os.listdir(path)
        if files==[]:
            return
        glu=False
        if ram.FilesToDelete != None:
            for t in files:
                if t.lower() in ram.FilesToDelete:
                    try:
                        os.remove(path+'/'+t)
                        glu=True
                    except:
                        print('Deletion of ',path+'/'+t,' Failed!')
        if glu:
            files=os.listdir(path)
            if files==[]:
                return
        dirTree.A=path
        files.sort()
        trx=True
        mp3s=[]
        covers=[]
        for t in files:
            if ram.KillThread:
                ravage()
                return
            try:
                if t.lower().endswith('.mp3'):
                    trx=False
                    mp3s.append(t)
                else:
                    if t.lower().endswith('.jpg') or t.lower().endswith('.jpeg'):
                        covers.append(t)
            except:
                pass
            if os.path.isdir(path+'/'+t):
                try:
                    crawler(path+'/'+t) # This specifies recursive sub folder calls.
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
            if ram.CoversToSearchFor!=None:
                for t in covers:
                    if t.lower() in ram.CoversToSearchFor:
                        cover=path+'/'+t
                        try:
                            os.rename(path+'/'+t,path+'/'+'cover.jpg')
                            if os.path.isfile(path+'/'+'cover.jpg'):
                                cover=path+'/cover.jpg'
                            else:
                                cover=path+'/'+t
                        except:
                            cover=path+'/'+t
                        cam=False
                        break
            if cam:
                for t in covers:
                    if t.lower().startswith('cover'):
                        cover=path+'/'+t
                        cam=False
                        break
            if cam:
                for t in covers:
                    if t.lower().startswith('folder'):
                        try:
                            os.rename(path+'/'+t,path+'/'+'cover.jpg')
                            if os.path.isfile(path+'/'+'cover.jpg'):
                                cover=path+'/cover.jpg'
                            else:
                                cover=path+'/'+t
                        except:
                            cover=path+'/'+t
                        cam=False
                        break
            if cam:
                for t in covers:
                    if t.lower().startswith('art'):
                        try:
                            os.rename(path+'/'+t,path+'/'+'cover.jpg')
                            if os.path.isfile(path+'/'+'cover.jpg'):
                                cover=path+'/cover.jpg'
                            else:
                                cover=path+'/'+t
                        except:
                            cover=path+'/'+t
                        cam=False
                        break
            if cam:
                for t in covers:
                    if t.lower().startswith('album'):
                        try:
                            os.rename(path+'/'+t,path+'/'+'cover.jpg')
                            if os.path.isfile(path+'/'+'cover.jpg'):
                                cover=path+'/cover.jpg'
                            else:
                                cover=path+'/'+t
                        except:
                            cover=path+'/'+t
                        cam=False
                        break
            if cam:
                for t in covers:
                    if t.lower().startswith('front'):
                        try:
                            os.rename(path+'/'+t,path+'/'+'cover.jpg')
                            if os.path.isfile(path+'/'+'cover.jpg'):
                                cover=path+'/cover.jpg'
                            else:
                                cover=path+'/'+t
                        except:
                            cover=path+'/'+t
                        cam=False
                        break
            if cam:
                for t in covers:
                    if t.lower().startswith('back'):
                        try:
                            os.rename(path+'/'+t,path+'/'+'cover.jpg')
                            if os.path.isfile(path+'/'+'cover.jpg'):
                                cover=path+'/cover.jpg'
                            else:
                                cover=path+'/'+t
                        except:
                            cover=path+'/'+t
                        cam=False
                        break
            if cover==None:
                cover=path+'/'+covers[0]
        albums=[]
        data=[] # Meaning Filenames.
        artists=[]
        for t in mp3s:
            if ram.KillThread:
                ravage()
                return
            aus=eyed3.load(path+'/'+t)
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
        if len(albums)==[]:
            return
        if len(albums)!=1:
            thebes=True
        else:
            thebes=False
        c=0
        newFnames=[]
        for t in data:
            if ram.KillThread:
                ravage()
                return
            egypt=t
            egypt.sort()
            if egypt==[]:
                print('Error: Nimue')
                ram.LiveFeedback='Error: Nimue'
                return
            faith=reno(egypt)
            cv=0
            for b in egypt:
                os.rename(path+'/'+b,path+'/'+faith[cv])
                if os.path.isfile(path+'/'+faith[cv]) == False:
                    print('Issue H2O',path+'/'+faith[cv])
                    ram.LiveFeedback=str('Issue H2O',path+'/'+faith[cv])
                    return
                cv+=1
            newFnames.append(faith)
        c=0
        if ram.NotifyMissingAlbumName:
            for t in albums:
                if t=='None' or t==None:
                    handler([artists[c][0],'\n'.join(data[c])],'name')
                    gdi=taffy.dataToReturn
                    if gdi==None or gdi=='' or gdi=='None':
                        pass
                    else:
                        albums[c]=str(gdi)
                c+=1
        c=0
        if ram.NotifyMissingArtist:
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
        for t in newFnames:
            if ram.KillThread:
                ravage()
                return
            found=None # Will hold album cover path
            addCover=True # This will determine if cover was found or not.
            if thebes: # This means more than one album, so individual covers must be extracted.
                for v in t:
                    try:
                        tag = TinyTag.get(path+'/'+v,image=True)
                        photor=tag.get_image()
                        if photor == '' or photor == None or len(photor) < 10:
                            found=None
                        else:
                            found=photor
                            break
                    except:
                        found=None
                if found==None and ram.NotifyMissingCover: # This should call the missing data setter if checked.
                    dirTree.A=str(path)
                    handler([albums[c],artists[c][0],'\n'.join(t)],'cover')
                    found=taffy.dataToReturn
                else:
                    try:
                        if ram.KeepBackup:
                            grey=open(path+'/'+'cover.jpg','wb')
                            grey.write(found)
                            grey.close()
                            found=path+'/'+'cover.jpg'
                        else:
                            found=None
                    except:
                        found=None
                if os.path.isfile(str(found)):
                    try:
                        if ram.KeepBackup:
                            im = Image.open(found)
                            im.save(path+'/'+'cover.jpg','JPEG')
                            addCover=True
                        else:
                            found=None
                            addCover=False
                    except:
                        addCover=False
                else:
                    addCover=False
            else: # This is for singular albums.
                if cover==None or os.path.isfile(cover)==False:
                    for v in t:
                        try:
                            tag = TinyTag.get(path+'/'+v,image=True)
                            photor=tag.get_image()
                            if photor == '' or photor == None or len(photor) < 10:
                                found=None
                            else:
                                found=photor
                                break
                        except:
                            found=None
                    if found==None and ram.NotifyMissingCover: # This should call the missing data setter if checked.
                        handler([albums[c],artists[c][0],'\n'.join(t)],'cover')
                        found=taffy.dataToReturn
                    else:
                        try:
                            if ram.KeepBackup:
                                grey=open(path+'/'+'cover.jpg','wb')
                                grey.write(found)
                                grey.close()
                                found=path+'/'+'cover.jpg'
                            else:
                                pass
                        except:
                            found=None
                    if os.path.isfile(str(found)):
                        try:
                            if ram.KeepBackup:
                                im = Image.open(found)
                                im.save(path+'/'+'cover.jpg','JPEG')
                                addCover=True
                            else:
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
            inhibit=None
            debt=True
            if found != None and os.path.isfile(found):
                if ram.DontResiveJPG:
                    try:
                        if ram.KeepBackup:
                            im = Image.open(found)
                            size = ram.ResizeAlbumCoverSize
                            im.thumbnail(size, Image.ANTIALIAS)
                            im.save(found,'JPEG')
                        else:
                            pass
                    except:
                        print('Turbin Error')
                        ram.LiveFeedback='Turbin Error'
                        found=None
            class coo:
                imagedata=None
            for F in t: # F == filename.
                if ram.KillThread:
                    ravage()
                    return
                try:
                    aus=eyed3.load(path+'/'+F)
                    if ram.DeleteEmbedded:
                        try:
                            for t in [y.description for y in aus.tag.images]:
                                aus.tag.images.remove(t)
                        except:
                            print('Cola Error')
                            ram.LiveFeedback='Cola Error'
                    if addCover and ram.WillEmbedArt: # For cover.
                        try:
                            if debt:
                                debt=False
                                try:
                                    if os.path.isfile(ex.tide+'/'+'temp-vox.jpg'):
                                        os.remove(ex.tide+'/'+'temp-vox.jpg')
                                except:
                                    print('Erra Prince')
                                    ram.LiveFeedback='Erra Prince'
                                inhibit=str(albums[c])
                                im = Image.open(found)
                                size = ram.ResizeAlbumCoverSize
                                im.thumbnail(size, Image.ANTIALIAS)
                                im.save(ex.tide+'/'+'temp-vox.jpg','JPEG')
                                coo.imagedata = open(ex.tide+'/'+'temp-vox.jpg',"rb").read()
                            if inhibit == str(albums[c]):
                                for t in [y.description for y in aus.tag.images]:
                                    aus.tag.images.remove(t)
                                aus.tag.images.set(3,coo.imagedata,"image/jpeg")
                            else:
                                try:
                                    if os.path.isfile(ex.tide+'/'+'temp-vox.jpg'):
                                        os.remove(ex.tide+'/'+'temp-vox.jpg')
                                except:
                                    print('Erra Prince2')
                                    ram.LiveFeedback='Erra Prince2'
                                inhibit=str(albums[c])
                                im = Image.open(found)
                                size = ram.ResizeAlbumCoverSize
                                im.thumbnail(size, Image.ANTIALIAS)
                                im.save(ex.tide+'/'+'temp-vox.jpg','JPEG')
                                coo.imagedata = open(ex.tide+'/'+'temp-vox.jpg',"rb").read()
                                for t in [y.description for y in aus.tag.images]:
                                    aus.tag.images.remove(t)
                                aus.tag.images.set(3,coo.imagedata,"image/jpeg")
                        except:
                            print('Erra: JING')
                            ram.LiveFeedback='Erra: JING'
                    aus.tag.album=str(albums[c])
                    ram.LiveFeedback='Processing Album: '+str(albums[c])
                    if ram.KillThread:
                        ravage()
                        return
                    try:
                        if artists[c][0]=='None' or artists[c][0]==None or artists[c][0]=='':
                            aus.tag.comments.set(str(albums[c]))
                        else:
                            aus.tag.comments.set(str(artists[c][0]))
                    except:
                        print('Erra Mohigo')
                        ram.LiveFeedback='Erra Mohigo'
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
                            ram.LiveFeedback='Erra Kiosk'
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
                            ram.LiveFeedback='Erra vinmo'
                    if ram.ChangeAllGenres:
                        try:
                            aus.tag.genre=str(ram.GenreToChangeTo)
                            aus.tag.non_std_genre=str(ram.GenreToChangeTo)
                        except:
                            print('Erra halo')
                            ram.LiveFeedback='Erra halo'
                    aus.tag.track_num = trackC
                    trackC+=1
                    aus.tag.save()
                    ram.files+=1
                except:
                    print('Erra Shim')
                    ram.LiveFeedback='Erra Shim'
            c+=1 # This must go to end of this for loop.
    try:
        crawler(path) # This always at end of masterLoop(). Above return statement.
    except:
        ram.LiveFeedback='Done! Due to an Error or Bad Folder Path.'
        try:
            if os.path.isfile(ex.tide+'/'+'temp-vox.jpg'):
                os.remove(ex.tide+'/'+'temp-vox.jpg')
        except:
            print('Erra Prince5')
        return
    ram.LiveFeedback='Done! Processed '+str(ram.files)+' mp3s.'
    try:
        if os.path.isfile(ex.tide+'/'+'temp-vox.jpg'):
            os.remove(ex.tide+'/'+'temp-vox.jpg')
    except:
        print('Erra Prince')
    return
class vera:
    a=None
def callMaster():
    masterLoop(vera.a)
class dome:
    x=None # dome.x
def multiplex():
    #cm = threading.Thread(target=print_square, args=(10,))
    root=tkinter.Tk()
    background_image2=tkinter.PhotoImage(data = img.D)
    root.iconphoto(False, background_image2)
    class hepa:
        a=True
    def van():
        rootx=tkinter.Tk()
        background_image3=tkinter.PhotoImage(data = img.D)
        rootx.iconphoto(False, background_image3)
        def fum():
            hepa.a=True
            rootx.destroy()
        rootx.protocol('WM_DELETE_WINDOW', fum)
        rootx.title('Alert!')
        w = 150
        h = 100
        ws = rootx.winfo_screenwidth()
        hs = rootx.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        rootx.geometry('%dx%d+%d+%d' % (w, h, x, y))
        rootx.resizable(0, 0)
        rootx.configure(background='#0066ff')
        def knox():
            rootx.destroy()
            ram.KillThread=True
            time.sleep(1)
            root.destroy()
            hepa.a=True
            mainCat('Ended Processing Early Per User Request!')
        cy = tkinter.Button(rootx,text ="Yes",command=knox,anchor='c',font=('Helvetica', 12, 'bold'),relief=RAISED,activebackground='#0000ff',activeforeground='black',fg='#00ffff',bg='#000099',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2)
        cy.pack()
        cy.place(bordermode=OUTSIDE, height=25, width=75,relx=0.5, rely=1.0, anchor=SE)
        def cruella():
            rootx.destroy()
            hepa.a=True
        cy2 = tkinter.Button(rootx,text ="No",command=cruella,anchor='c',font=('Helvetica', 12, 'bold'),relief=RAISED,activebackground='#0000ff',activeforeground='black',fg='#00ffff',bg='#000099',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2)
        cy2.pack()
        cy2.place(bordermode=OUTSIDE, height=25, width=75,relx=1, rely=1.0, anchor=SE)

        at4 = Label(rootx,wraplength=150, fg='black',bg='#0066ff',text='Stop Running Processes?',justify=LEFT,font=('Helvetica', 14, 'bold'))
        at4.place(bordermode=OUTSIDE,height=75, width=600,relx=0.5, rely=0.0, anchor=N)
        rootx.mainloop()
    def zayu():
        if hepa.a:
            hepa.a=False
            van()
    root.protocol('WM_DELETE_WINDOW', van)
    def upS():
        if ram.LiveFeedback.startswith('Done!'):
            try:
                rootx.destroy()
            except:
                pass
            root.destroy()
            dome.x.join()
            mainCat(ram.LiveFeedback)
            return
        d.config(text=ram.LiveFeedback)
        root.after(3000,upS)
    def mecca():
        ram.LiveFeedback='Initializing!'
        dome.x = threading.Thread(target=callMaster)
        dome.x.start()
        upS()
    root.title('Processing Files.')
    w = 600
    h = 100
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    root.configure(background='#000099')
    backg=tkinter.PhotoImage(data = img.C)
    at = Label(root, bg='#2d00b3',image=backg)
    at.place(bordermode=OUTSIDE,height=70, width=600,relx=0, rely=0.0, anchor=NW)
    d = Label(root, text='Initializing.',anchor='w',relief=SUNKEN,fg='black',bg='cyan',highlightbackground="#000066", highlightcolor="#0000ff", highlightthickness=4,font=('Helvetica', 13,'bold'))
    d.place(bordermode=OUTSIDE, height=30, width=600,relx=0.5, rely=1, anchor=S)
    root.after(100,mecca)
    root.mainloop()
def colaC(temp):
    vera.a=temp
    multiplex()
class nim:
    indo=None # nim.indo
    rt=None # nim.rt
def settings():
    ram.coffee=True
    ram.rt=Toplevel(nim.rt)
    def vine():
        ram.rt.destroy()
        ram.coffee=None
        nim.indo.config(text='Settings closed; no settings saved.')
    ram.rt.protocol('WM_DELETE_WINDOW', vine)
    ram.rt.title('Settings')
    w = 600
    h = 400
    ws = ram.rt.winfo_screenwidth()
    hs = ram.rt.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    ram.rt.geometry('%dx%d+%d+%d' % (w, h, x, y))
    ram.rt.resizable(0, 0)
    ram.rt.configure(background='#0066ff')
    bw = tkinter.Text(ram.rt,relief=SUNKEN,fg='black',bg='#b3b3ff',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12),insertbackground='#000066')
    bw.pack()
    bw.place(bordermode=OUTSIDE, height=100, width=600,relx=0, rely=0.20, anchor=NW)
    class nuw:
        nu=True
    class nuw2:
        nu=True

    if ram.CoversToSearchFor==None or ram.CoversToSearchFor=='' or ram.CoversToSearchFor==[]:
        bw.insert("1.0", "Cover.jpg\nFolder.jpeg\nArt.jpg")
    else:
        bw.insert("1.0",'\n'.join(ram.CoversToSearchFor))
        nuw.nu=False
    def mp2(cdf):
        if nuw.nu:
            nuw.nu=False
            bw.delete('1.0',END)
    bw.bind('<Button-1>',mp2)
    bw.bind('<Button-2>',mp2)
    bw.bind('<Button-3>',mp2)
    bw2 = tkinter.Text(ram.rt,relief=SUNKEN,fg='black',bg='#b3b3ff',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12),insertbackground='#000066')
    bw2.pack()
    bw2.place(bordermode=OUTSIDE, height=100, width=600,relx=0, rely=0.65, anchor=NW)
    if ram.FilesToDelete==None or ram.FilesToDelete=='' or ram.FilesToDelete==[]:
        bw2.insert("1.0", "Example.txt\nJunk.jpg\nUnused File.dat\nGarbage.file")
    else:
        bw2.insert("1.0",'\n'.join(ram.FilesToDelete))
        nuw2.nu=False
    def mp22(cdf):
        if nuw2.nu:
            nuw2.nu=False
            bw2.delete('1.0',END)
    bw2.bind('<Button-1>',mp22)
    bw2.bind('<Button-2>',mp22)
    bw2.bind('<Button-3>',mp22)
    a23 = Label(ram.rt, fg='cyan',bg='#290066',text='Album Cover Names.',wraplength=130,font=('Helvetica', 14, 'bold'),justify=LEFT)
    a23.place(bordermode=OUTSIDE,height=80, width=130,relx=0.0, rely=0.0, anchor=NW)
    a232 = Label(ram.rt, fg='cyan',bg='#290066',wraplength=470,text='Enter the name or names of the JPEG image files for the program to look for. If your album cover is named cover.jpg the program will look for that filename in the directory its scanning. The program scans each folder seperately, it will look for a different cover in each folder containing mp3 files. Place each image name on a seperate line as shown below.',font=('Helvetica', 10, 'bold'),justify=LEFT)
    a232.place(bordermode=OUTSIDE,height=80, width=470,relx=1.0, rely=0.0, anchor=NE)
    a24 = Label(ram.rt, fg='cyan',bg='#290066',wraplength=130,justify=LEFT,text='Delete These Files.',font=('Helvetica', 14, 'bold'))
    a24.place(bordermode=OUTSIDE,height=80, width=130,relx=0.0, rely=0.45, anchor=NW)
    a242 = Label(ram.rt, fg='cyan',bg='#290066',wraplength=470,justify=LEFT,text='You can specify files for the program to delete while it is scanning your files. For example, maybe you have unused files in each folder and want to batch delete them. Enter each filename you want deleted as demonstrated below on each seperate line. By default the program doesnt delete anything unles you specify it to do so. No worries.',font=('Helvetica', 10, 'bold'))
    a242.place(bordermode=OUTSIDE,height=80, width=470,relx=1.0, rely=0.45, anchor=NE)
    def saveS():
        if nuw.nu and nuw2.nu:
            ram.rt.destroy()
            ram.CoversToSearchFor=None
            ram.FilesToDelete=None
            nim.indo.config(text='Settings closed; no settings saved.')
            ram.coffee=None
            return
        if nuw.nu == False and bw.get('1.0',END).replace('\n','').replace('\t','').strip() != '':
            A=bw.get('1.0',END).strip().replace('\t','') # Album covers to search for.
            if '\n' in A:
                A=A.split('\n')
                temp=[]
                for t in A:
                    if t.strip()!='' and '.jp' in t.strip().lower():
                        if t.strip().lower().endswith('.jpg') or t.strip().lower().endswith('.jpeg'):
                            temp.append(str(t.strip().lower()))
                if temp!=[]:
                    A=temp
                else:
                    A=None
            else:
                if A.strip()!='' and '.jp' in A.strip().lower():
                    if A.strip().lower().endswith('.jpg') or A.strip().lower().endswith('.jpeg'):
                        A=[A.lower()]
                    else:
                        A=None
                else:
                    A=None
            if A!=None:
                ram.CoversToSearchFor=A
            else:
                ram.CoversToSearchFor=None
        else:
            ram.CoversToSearchFor=None
        if nuw2.nu == False and bw2.get('1.0',END).replace('\n','').replace('\t','').strip() != '':
            A=bw2.get('1.0',END).strip() # Files to delete.
            if '\n' in A:
                A=A.split('\n')
                temp=[]
                for t in A:
                    if t.strip()!='':
                        temp.append(str(t.strip().lower()))
                if temp!=[]:
                    A=temp
                else:
                    temp=None
                    A=None
            else:
                A=[A.lower()]
            if A!=None:
                ram.FilesToDelete=A
            else:
                ram.FilesToDelete=None
        else:
            ram.FilesToDelete=None
        ram.rt.destroy()
        nim.indo.config(text='Settings Saved.')
        ram.coffee=None
        return
    e4 = tkinter.Button(ram.rt,command=saveS,text ="Save Settings",anchor='c',font=('Helvetica', 14, 'bold'),relief=RAISED,activebackground='#0000ff',activeforeground='black',fg='#00ffff',bg='#000099',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2)
    e4.pack()
    e4.place(bordermode=OUTSIDE, height=39.5, width=600,relx=1.0, rely=1.0, anchor=SE)
    background_image7=tkinter.PhotoImage(data = img.D)
    ram.rt.iconphoto(False, background_image7)
    ram.rt.mainloop()
def star():
    ram.NotifyMissingArtist=True
    ram.NotifyMissingCover=True
    ram.NotifyMissingAlbumName=True
    ram.RenumberFilenames=True
    ram.ResizeAlbumCoverSize=480,480
    ram.ChangeAllGenres=False
    ram.GenreToChangeTo="Pop"
    ram.files=0
    ram.rt=None
    ram.coffee=None
    ram.DontResiveJPG=False
    ram.WillEmbedArt=True
    ram.KeepBackup=True
    ram.DeleteEmbedded=True
def mainCat(indo):
    star()
    nim.rt=tkinter.Tk()
    root=nim.rt
    root.withdraw()
    root.config(background="#2d00b3")
    def vin():
        root.destroy()
        try:
            ram.rt.destroy()
        except:
            pass
        ravage()
    root.protocol('WM_DELETE_WINDOW', vin)
    root.title('CrayTag '+ver.sion)
    w = 600
    h = 400
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    root.configure(background='#2d00b3')
    can=tkinter.Canvas(root)
    back=tkinter.PhotoImage(data = img.A)
    a = Label(root, bg='#2d00b3',image=back)
    a.place(bordermode=OUTSIDE,height=200, width=400,relx=0, rely=0.0, anchor=NW)
    back2=tkinter.PhotoImage(data = img.B)
    a2 = Label(root, bg='#2d00b3',image=back2)
    a2.place(bordermode=OUTSIDE,height=70, width=108,relx=0.483, rely=0.565, anchor=NW)
    def Pompeii(rtds):
        if ram.coffee==None:
            nim.indo=d
            settings()
        else:
            return
    a2.bind('<Button-1>',Pompeii)
    a2.bind('<Button-2>',Pompeii)
    a2.bind('<Button-3>',Pompeii)
    b = tkinter.Text(root,relief=SUNKEN,fg='black',bg='#b3b3ff',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12),insertbackground='#000066')
    b.pack()
    b.place(bordermode=OUTSIDE, height=25, width=300,relx=0, rely=0.5, anchor=NW)
    b.insert("1.0", "Type or Select Path of Folder to Process.")
    class nu:
        nu=True
    def mp(cdf):
        if nu.nu:
            nu.nu=False
            b.delete('1.0',END)
            d.config(text='Type or Select Path to Folder with Files to Process.')
    b.bind('<Button-1>',mp)
    b.bind('<Button-2>',mp)
    b.bind('<Button-3>',mp)
    def browser():
        temp=browse_button()
        if str(temp)=='':
            d.config(text='Must Select a Valid Path!')
        else:
            if os.path.isdir(temp):
                nu.nu=False
                d.config(text='Path Selected.')
                b.delete('1.0',END)
                b.insert('1.0',str(temp))
    c = tkinter.Button(root,text ="Browse",command=browser,anchor='c',font=('Helvetica', 12, 'bold'),relief=RAISED,activebackground='#0000ff',activeforeground='black',fg='#00ffff',bg='#000099',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2)
    c.pack()
    c.place(bordermode=OUTSIDE, height=25, width=100,relx=0.5, rely=0.5, anchor=NW)
    d = Label(root, text=indo,anchor='w',relief=SUNKEN,fg='#00ffff',bg='#000099',highlightbackground="#000066", highlightcolor="#0000ff", highlightthickness=4,font=('Helvetica', 11))
    d.place(bordermode=OUTSIDE, height=33, width=397,relx=0, rely=1, anchor=SW)
    class dui:
        b=0
        c=['Invalid','Incorrect','Wrong']
        d=True
    def smo():
        temp=b.get('1.0',END)
        temp=temp.replace('\n','').replace('\t','')
        temp=temp.strip()
        if temp=='' or temp=="Type or Select Path of Folder to Process.":
            d.config(text='Must Specify Path! Try using Browse Button!')
            return
        if os.path.isdir(temp)==False:
            if dui.d==True:
                dui.d=False
                d.config(text='Path is '+random.choice(dui.c))
                dui.b=random.randint(0,5)
            elif dui.b==1:
                d.config(text='Path is Still '+random.choice(dui.c))
                dui.b=random.randint(0,5)
            elif dui.b==2:
                d.config(text='Path is Still '+random.choice(dui.c)+'!')
                dui.b=random.randint(0,5)
            elif dui.b==3:
                d.config(text='Darling, the Path is Still '+random.choice(dui.c)+'?')
                dui.b=random.randint(0,5)
            elif dui.b==4:
                d.config(text=random.choice(['Darling!','Hmm?','Sorry!','Ugh!','Bleh!','Yuck!','Nope!','Nah!','Honey!','Shockingly!'])+' the Path is Still '+random.choice(dui.c)+'.')
                dui.b=random.randint(0,5)
            else:
                d.config(text=random.choice(['Darling','Sorry','Ugh','Bleh','Yuck','Nope','Nah','Honey','Shockingly'])+' the Path is Still '+random.choice(dui.c)+'.')
                dui.b=random.randint(0,5)
            return
        dui.d=True
        try:
            ram.rt.destroy()
        except:
            pass
        try:
            root.destroy()
        except:
            print('V2 error')
        ram.rt=None
        ram.KillThread=False
        colaC(temp)
    e = tkinter.Button(root,command=smo,text ="Start",anchor='c',font=('Helvetica', 14, 'bold'),relief=RAISED,activebackground='#0000ff',activeforeground='black',fg='#00ffff',bg='#000099',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2)
    e.pack()
    e.place(bordermode=OUTSIDE, height=80, width=204,relx=1.0, rely=1.0, anchor=SE)
    f = Label(root, text='Notify to Add Missing Album Artist',relief=SUNKEN,anchor='w',fg='#b3b3ff',bg='#000099',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    f.place(bordermode=OUTSIDE, height=25, width=250,relx=0, rely=0.562, anchor=NW)
    g = Label(root, text='Notify to Add Missing Album Cover',relief=SUNKEN,anchor='w',fg='#b3b3ff',bg='#000099',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    g.place(bordermode=OUTSIDE, height=25, width=250,relx=0, rely=0.622, anchor=NW)
    h = Label(root, text='Notify to Add Missing Album Name',relief=SUNKEN,anchor='w',fg='#b3b3ff',bg='#000099',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    h.place(bordermode=OUTSIDE, height=25, width=250,relx=0, rely=0.682, anchor=NW)
    i = Label(root, text='Resize Album Cover to:',relief=SUNKEN,anchor='w',fg='#b3b3ff',bg='#000099',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    i.place(bordermode=OUTSIDE, height=25, width=170,relx=0, rely=0.742, anchor=NW)
    choices = ['25x25','50x50','75x75','100x100','125x125','150x150','160x160','175x175','200x200','250x250','300x300','350x350','400x400','480x480','500x500','600x600','700x700','800x800','900x900','1000x1000']
    tkvar = StringVar(root)
    def setter(kilo):
        temp=tkvar.get().split('x')
        ram.ResizeAlbumCoverSize=(int(temp[0]),int(temp[1]))
        d.config(text='Changed Cover Size to: '+' x '.join(temp))
    popupMenu = OptionMenu(root, tkvar, *choices,command=setter)
    popupMenu.config(relief=SUNKEN,fg='black',bg='#b3b3ff',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    popupMenu["menu"].config(bg='#b3b3ff',font=('Helvetica', 13, 'bold'),fg='black')
    popupMenu.place(bordermode=OUTSIDE, height=25, width=110,relx=0.28, rely=0.742, anchor=NW)
    tkvar.set(choices[13])
    j = Label(root, text='or Custom:',relief=SUNKEN,anchor='w',fg='#b3b3ff',bg='#000099',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    j.place(bordermode=OUTSIDE, height=25, width=90,relx=0.458, rely=0.742, anchor=NW)
    def mull():
        p.config(text=str(k.get()))
    k = Spinbox(root, command=mull,from_=0, to=10000,relief=SUNKEN,fg='black',bg='#b3b3ff',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    k.place(bordermode=OUTSIDE, height=25, width=60,relx=0.605, rely=0.742, anchor=NW)
    def mulla(jhg):
        mull()
    k.bind('<KeyRelease>',mulla)
    m = Label(root, text='x',relief=SUNKEN,anchor='w',fg='#b3b3ff',bg='#000099',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    m.place(bordermode=OUTSIDE, height=25, width=17,relx=0.705, rely=0.742, anchor=NW)
    def setC():
        temp=k.get()
        try:
            temp=int(temp)
        except:
            d.config(text='Alert: Must Enter only Numbers For Cover Size!')
            return
        if temp<=0:
            d.config(text='Alert: Cover Size Must be Greater than 0.')
            return
        else:
            ram.ResizeAlbumCoverSize=temp,temp
            d.config(text='Saved Custom Cover Size: '+str(temp)+' x '+str(temp))
    o = tkinter.Button(root,text ="Save Custom",command=setC,anchor='c',font=('Helvetica', 11, 'bold'),relief=RAISED,activebackground='#0000ff',activeforeground='black',fg='#00ffff',bg='#000099',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2)
    o.pack()
    o.place(bordermode=OUTSIDE, height=25, width=103,relx=1, rely=0.742, anchor=NE)
    p = Label(root, text='0',relief=SUNKEN,anchor='w',fg='black',bg='#b3b3ff',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    p.place(bordermode=OUTSIDE, height=25, width=59,relx=0.732, rely=0.742, anchor=NW)
    def gray():
        if str(chkValue.get()) == 'True':
            ram.NotifyMissingArtist=True
            d.config(text='Enabled Notify Missing Artist.')
        else:
            ram.NotifyMissingArtist=False
            d.config(text='Disabled Notify Missing Artist.')
    chkValue = tkinter.BooleanVar()
    chkValue.set(True)
    q = tkinter.Checkbutton(root, var=chkValue,command=gray,relief=SUNKEN,fg='#000099',bg='#b3b3ff',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,activebackground='#b3b3ff',activeforeground='blue',font=('Helvetica', 12))
    q.place(bordermode=OUTSIDE, height=25, width=40,relx=0.415, rely=0.562, anchor=NW)
    def gray2():
        if str(chkValue2.get()) == 'True':
            ram.NotifyMissingCover=True
            d.config(text='Enabled Notify Missing Cover.')
        else:
            ram.NotifyMissingCover=False
            d.config(text='Disabled Notify Missing Cover.')
    chkValue2 = tkinter.BooleanVar()
    chkValue2.set(True)
    q2 = tkinter.Checkbutton(root, var=chkValue2,command=gray2,relief=SUNKEN,fg='#000099',bg='#b3b3ff',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,activebackground='#b3b3ff',activeforeground='blue',font=('Helvetica', 12))
    q2.place(bordermode=OUTSIDE, height=25, width=40,relx=0.415, rely=0.622, anchor=NW)
    def gray3():
        if str(chkValue3.get()) == 'True':
            ram.NotifyMissingAlbumName=True
            d.config(text='Enabled Notify Missing Album Name.')
        else:
            ram.NotifyMissingAlbumName=False
            d.config(text='Disabled Notify Missing Album Name.')
    chkValue3 = tkinter.BooleanVar()
    chkValue3.set(True)
    q3 = tkinter.Checkbutton(root, var=chkValue3,command=gray3,relief=SUNKEN,fg='#000099',bg='#b3b3ff',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,activebackground='#b3b3ff',activeforeground='blue',font=('Helvetica', 12))
    q3.place(bordermode=OUTSIDE, height=25, width=40,relx=0.415, rely=0.682, anchor=NW)
    r = Label(root, text='Renumber mp3 Filenames:',relief=SUNKEN,anchor='w',fg='#b3b3ff',bg='#000099',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    r.place(bordermode=OUTSIDE, height=25, width=195,relx=0, rely=0.802, anchor=NW)
    def gray4():
        if str(chkValue4.get()) == 'True':
            ram.RenumberFilenames=True
            d.config(text='Enabled Filename Renumbering.')
        else:
            ram.RenumberFilenames=False
            d.config(text='Disabled Filename Renumbering.')
    chkValue4 = tkinter.BooleanVar()
    chkValue4.set(True)
    q4 = tkinter.Checkbutton(root, var=chkValue4,command=gray4,relief=SUNKEN,fg='#000099',bg='#b3b3ff',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,activebackground='#b3b3ff',activeforeground='blue',font=('Helvetica', 12))
    q4.place(bordermode=OUTSIDE, height=25, width=40,relx=0.325, rely=0.802, anchor=NW)
    choices2 = ['01 - Example.mp3','01-Example.mp3','01- Example.mp3','01 Example.mp3','01Example.mp3','01. Example.mp3','01.Example.mp3','01_Example.mp3','01_ Example.mp3','01:Example.mp3','01 : Example.mp3','01)- Example.mp3','01 ~ Example.mp3','01~ Example.mp3','01~Example.mp3']
    tkvar2 = StringVar(root)
    def setter2(kilo):
        if tkvar2.get()==choices2[0]:
            maxx.div=' - '
        elif tkvar2.get()==choices2[1]:
            maxx.div='-'
        elif tkvar2.get()==choices2[2]:
            maxx.div='- '
        elif tkvar2.get()==choices2[3]:
            maxx.div=' '
        elif tkvar2.get()==choices2[4]:
            maxx.div=''
        elif tkvar2.get()==choices2[5]:
            maxx.div='. '
        elif tkvar2.get()==choices2[6]:
            maxx.div='.'
        elif tkvar2.get()==choices2[7]:
            maxx.div='_'
        elif tkvar2.get()==choices2[8]:
            maxx.div='_ '
        elif tkvar2.get()==choices2[9]:
            maxx.div=':'
        elif tkvar2.get()==choices2[10]:
            maxx.div=' : '
        elif tkvar2.get()==choices2[11]:
            maxx.div=')- '
        elif tkvar2.get()==choices2[12]:
            maxx.div=' ~ '
        elif tkvar2.get()==choices2[13]:
            maxx.div='~ '
        elif tkvar2.get()==choices2[14]:
            maxx.div='~'
        else:
            print('Codfish Error')
        d.config(text='Set Renumber Style to:   '+str(tkvar2.get()))
    popupMenu2 = OptionMenu(root, tkvar2, *choices2,command=setter2)
    popupMenu2.config(relief=SUNKEN,fg='black',bg='#b3b3ff',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    popupMenu2["menu"].config(bg='#b3b3ff',font=('Helvetica', 13, 'bold'),fg='black')
    popupMenu2.place(bordermode=OUTSIDE, height=25, width=161,relx=0.392, rely=0.802, anchor=NW)
    tkvar2.set(choices2[3])
    s = Label(root, text='Change all Genres to:',relief=SUNKEN,anchor='w',fg='#b3b3ff',bg='#000099',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    s.place(bordermode=OUTSIDE, height=25, width=160,relx=0, rely=0.862, anchor=NW)
    choices3 = ['Dont Change','Acapella', 'Acid', 'Acid Jazz', 'Acid Punk', 'Acoustic', 'Alternative', 'Alternative Rock', 'Ambient','ASMR', 'Anime', 'Avantgarde', 'Ballad', 'Bass', 'Beat', 'Bebob', 'Big Band', 'Black Metal', 'Bluegrass', 'Blues', 'Booty Bass', 'BritPop', 'Cabaret', 'Celtic', 'Chamber Music', 'Chanson', 'Chorus', 'Christian Gangsta Rap', 'Christian Rap', 'Christian Rock', 'Classic Rock', 'Classical', 'Club', 'Comedy', 'Contemporary Christian', 'Country', 'Crossover', 'Cult', 'Dance', 'Dance Hall', 'Darkwave', 'Death Metal', 'Disco', 'Dream', 'Drum & Bass', 'Drum Solo', 'Duet', 'Easy Listening', 'Egypt', 'Electronic', 'Ethnic', 'Euro-House', 'Euro-Techno', 'Eurodance', 'Fast Fusion', 'Folk', 'Folk-Rock', 'Folklore', 'Freestyle', 'Funk', 'Fusion', 'Game', 'Gangsta', 'Goa', 'Gospel', 'Gothic', 'Gothic Rock', 'Grunge', 'Hard Rock', 'Hardcore', 'Heavy Metal', 'Hip-Hop', 'House', 'House', 'Humour', 'Indie', 'Industrial', 'Instrumental', 'Instrumental Pop', 'Instrumental Rock', 'JPop', 'Jazz', 'Jazz+Funk', 'Jungle', 'Latin', 'Lo-Fi', 'Meditative', 'Merengue', 'Metal', 'Musical', 'National Folk', 'Native US', 'Negerpunk', 'New Age', 'New Wave', 'Noise', 'Oldies', 'Opera', 'Other', 'Polka', 'Polsk Punk', 'Pop', 'Pop-Folk', 'Pop-Funk', 'Porn Groove', 'Power Ballad', 'Pranks', 'Primus', 'Progressive Rock', 'Psychadelic', 'Psychedelic Rock', 'Punk', 'Punk Rock', 'R&B', 'Rap', 'Rave', 'Reggae', 'Retro', 'Revival', 'Rhythmic Soul', 'Rock','Russian','Rpop','RusPop', 'Rock & Roll', 'Salsa', 'Samba', 'Satire', 'Showtunes', 'Ska', 'Slow Jam', 'Slow Rock', 'Sonata', 'Soul', 'Sound Clip', 'Soundtrack', 'Southern Rock', 'Space', 'Speech', 'Swing', 'Symphonic Rock', 'Symphony', 'Synthpop', 'Tango', 'Techno', 'Techno-Industrial', 'Terror', 'Thrash Metal', 'Top 40', 'Trailer', 'Trance', 'Tribal', 'Trip-Hop', 'Unknown', 'Vocal', 'Vocal']
    tkvar3 = StringVar(root)
    def setter3(kilo):
        if tkvar3.get()==choices3[0]:
            ram.ChangeAllGenres=False
            d.config(text='Disabled Changing Genre.')
        else:
            ram.GenreToChangeTo=str(tkvar3.get())
            ram.ChangeAllGenres=True
            d.config(text='Will Change Genres to: '+ram.GenreToChangeTo)
    popupMenu3 = OptionMenu(root, tkvar3, *choices3,command=setter3)
    popupMenu3.config(relief=SUNKEN,fg='black',bg='#b3b3ff',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    popupMenu3["menu"].config(bg='#b3b3ff',font=('Helvetica', 13, 'bold'),fg='black')
    popupMenu3.place(bordermode=OUTSIDE, height=25, width=240,relx=0.26, rely=0.862, anchor=NW)
    tkvar3.set(choices3[0])
    scroll = Scrollbar(root)
    scroll.place(relx=1, rely=0, anchor=NE,height=200, width=15)
    vexx = Text(root, wrap=WORD, yscrollcommand=scroll.set)
    dearWorld="""\n\n\n\n\n\n\n\n\n\n\nInstructions Below.\n
----------------------

Welcome to CrayTag """+ver.sion+"""

By: Dalton Overlin.

----------------------

These instructions will help you better understand CrayTag and how to use it.

----------------------

----------------------
Type or Select Path of Folder to Process (or "Browse" button)
----------------------

The text box allows you to manually type the path of the folder to be processed (meaning the folder holding mp3s for processing). The "Browse" button opens a GUI window to select the folder for processing. That way you don't have to manually type out the path.

----------------------
Notify to Add Missing Album Artist (Checkbox)
----------------------

When this option is checked, while the program is processing your mp3 files if it finds an album with no defined artist name it will pop-up asking you to add the missing artist name. If you uncheck the box it will not notify you to add the missing data.

----------------------
Notify to Add Missing Album Cover (Checkbox)
----------------------

When this option is checked, while the program is processing your mp3 files if it finds an album with no defined album cover it will pop-up asking you to add the missing album cover. If you uncheck the box it will not notify you to add the missing cover.

----------------------
Notify to Add Missing Album Name (Checkbox)
----------------------

When this option is checked, while the program is processing your mp3 files if it finds an album with no defined album name it will pop-up asking you to add the missing album name. If you uncheck the box it will not notify you to add the missing album name.

----------------------
Resize Album Cover to: (dropdown menu)
----------------------

It allows you to select the size for the album art to be resized to. This will be the size that either embedded or standalone album covers will be resized too. For this operation, you don't need to click the "Save Custom" button as changing the dropdown value immediately sets the value.

----------------------
or Custom: & "Save Custom" button (for custom album art size)
----------------------

This option allows you to set a custom album cover size by either typing a numeric value or by using the toggle option to increase or decrease the value. Once you've set the custom size you must click the "Save Custom" button for the custom album cover size to be set.

----------------------
Renumber mp3 Filenames: (checkbox)
----------------------

When this box is checked it will carry out the file renumbering process. If the box is not checked it will not renumber the files.

----------------------
Renumbering Example Style (Dropdown Menu)
----------------------

This dropdown menu will give you options for different renumbering styles to choose from.

----------------------
Change all Genres to: (dropdown menu)
----------------------

If you leave this option at "Don't Change" then the program will not change the genre of all files being processed. But if you do change the option, then all files that are processed by the program will be changed to the new genre.

----------------------
Delete Embedded (dropdown menu)
----------------------

By default this option is set to No, when set to No it will not remove embedded album art. If you set this option to Yes then all embedded album art in your mp3 files will be removed. This is a way of stripping all embedded album art.

----------------------
Resize JPG File (dropdown menu)
----------------------

By default this option is set to No, when set to No it will not resize external album art (external meaning album art stored as separate image files). If you set this option to Yes then all external album art will be resized.

----------------------
Embed Cover (dropdown menu)
----------------------

By default, this option is set to Yes when setting to Yes it will embed album art into mp3 files. If you set this option to No then-new album art will not be embedded into the mp3 files. This option does not strip embedded album covers, it just prevents the setting of new embedded album covers if set to No.

----------------------
Keep Backup (dropdown menu)
----------------------

By default, this option is set to Yes. This option controls whether or not a backup of an embedded album cover will be made before resizing. This is done by extracting embedded album art and storing it as an external image file. Yes means a backup will be made. No means a backup will not be made.

----------------------
Start (button)
----------------------

This button is notably larger than the rest and is located at the bottom right area of the main GUI window. Once you've defined a directory to process and optionally additional settings you simply click the "Start" button and it will start processing the files.

----------------------
Settings (button with fish image)
----------------------

This button opens up a new window that will give you additional options. There is an option to specify custom names for album covers to look for. While the second option in the settings menu will let you define files to be deleted during the scanning process. This means if you define a filename like "folder.jpg" to be deleted the program will delete that file if it comes across it during the scan process of the directory you define.

----------------------
Processing Window
----------------------

This window will display while the program is processing your files. It will display live feedback of the current albums it is processing. If you want to cancel the processing of files just click the X button at the top right of the window. Once you do it will pop-up asking you if you want to cancel the running processes.

----------------------
Feedback Area
----------------------

There is a small text area at the bottom left of the main program window. This text area will give you feedback whenever you change a setting. After processing file this text area will also hold data about how many files were processed.
"""
    vexx.insert("1.0", dearWorld)
    vexx.config(state=DISABLED,bg='#000099',fg='#00ffff')
    vexx.place(bordermode=OUTSIDE, height=202, width=186,relx=0.975, rely=0, anchor=NE)
    scroll.config(command=vexx.yview)
    h4 = Label(root, text='Delete Embedded',relief=SUNKEN,anchor='w',fg='#b3b3ff',bg='#000099',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    h4.place(bordermode=OUTSIDE, height=25, width=142,relx=0.665, rely=0.5018, anchor=NW)
    f5 = Label(root, text='Resive JPG File',relief=SUNKEN,anchor='w',fg='#b3b3ff',bg='#000099',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    f5.place(bordermode=OUTSIDE, height=25, width=142,relx=0.665, rely=0.562, anchor=NW)
    g5 = Label(root, text='Embed Cover',relief=SUNKEN,anchor='w',fg='#b3b3ff',bg='#000099',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    g5.place(bordermode=OUTSIDE, height=25, width=142,relx=0.665, rely=0.622, anchor=NW)
    h5 = Label(root, text='Keep Backup',relief=SUNKEN,anchor='w',fg='#b3b3ff',bg='#000099',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    h5.place(bordermode=OUTSIDE, height=25, width=142,relx=0.665, rely=0.682, anchor=NW)
    choices5 = ['No dont resize JPG files.','Yes resize JPG files.']
    tkvar5 = StringVar(root)
    def setter5(kilo):
        if tkvar5.get()==choices5[0] or tkvar5.get()=='No':
            d.config(text='Wont resize JPG files used as cover.')
            ram.DontResiveJPG=False
        else:
            d.config(text='Will resize JPG files used as cover.')
            ram.DontResiveJPG=True
    popupMenu5 = OptionMenu(root, tkvar5, *choices5,command=setter5)
    popupMenu5.config(relief=SUNKEN,fg='black',bg='#b3b3ff',anchor='w',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    popupMenu5["menu"].config(bg='#b3b3ff',font=('Helvetica', 13, 'bold'),fg='black')
    popupMenu5.place(bordermode=OUTSIDE, height=25, width=62,relx=0.90, rely=0.562, anchor=NW)
    tkvar5.set('No')
    choices6 = ['No dont embed album cover in mp3s.','Yes embed album cover in mp3s.']
    tkvar6 = StringVar(root)
    def setter6(kilo):
        if tkvar6.get()==choices6[1] or tkvar6.get()=='Yes':
            d.config(text='Will embed cover in mp3s.')
            ram.WillEmbedArt=True
        else:
            d.config(text='Wont embed cover in mp3s.')
            ram.WillEmbedArt=False
    popupMenu6 = OptionMenu(root, tkvar6, *choices6,command=setter6)
    popupMenu6.config(relief=SUNKEN,fg='black',bg='#b3b3ff',anchor='w',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    popupMenu6["menu"].config(bg='#b3b3ff',font=('Helvetica', 13, 'bold'),fg='black')
    popupMenu6.place(bordermode=OUTSIDE, height=25, width=62,relx=0.90, rely=0.622, anchor=NW)
    tkvar6.set('Yes')
    choices7 = ['No dont keep backup, meaning dont store a JPG before resizing.','Yes keep backup, meaning dont delete JPG file.']
    tkvar7 = StringVar(root)
    def setter7(kilo):
        if tkvar7.get()==choices7[1] or tkvar7.get()=='Yes':
            d.config(text='Will keep backup by storing JPG before resizing embedded art.')
            ram.KeepBackup=True
        else:
            d.config(text='Wont keep backup by storing JPG before resizing embedded art.')
            ram.KeepBackup=False
    popupMenu7 = OptionMenu(root, tkvar7, *choices7,command=setter7)
    popupMenu7.config(relief=SUNKEN,fg='black',bg='#b3b3ff',anchor='w',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    popupMenu7["menu"].config(bg='#b3b3ff',font=('Helvetica', 13, 'bold'),fg='black')
    popupMenu7.place(bordermode=OUTSIDE, height=25, width=62,relx=0.90, rely=0.682, anchor=NW)
    tkvar7.set('Yes')
    choices8 = ['No dont remove embedded album art.','Yes remove embedded album art.']
    tkvar8 = StringVar(root)
    def setter8(kilo):
        if tkvar8.get()==choices8[0] or tkvar8.get()=='No':
            d.config(text='Wont remove embedded album art.')
            ram.DeleteEmbedded=False
            ram.WillEmbedArt=True
        else:
            d.config(text='Will remove embedded album art.')
            ram.DeleteEmbedded=True
            ram.WillEmbedArt=False
    popupMenu8 = OptionMenu(root, tkvar8, *choices8,command=setter8)
    popupMenu8.config(relief=SUNKEN,fg='black',bg='#b3b3ff',anchor='w',highlightbackground="#000066", highlightcolor="#000066", highlightthickness=2,font=('Helvetica', 12))
    popupMenu8["menu"].config(bg='#b3b3ff',font=('Helvetica', 13, 'bold'),fg='black')
    popupMenu8.place(bordermode=OUTSIDE, height=25, width=62,relx=0.90, rely=0.5018, anchor=NW)
    tkvar8.set('No')
    background_image7=tkinter.PhotoImage(data = img.D)
    root.iconphoto(False, background_image7)
    root.deiconify()
    root.mainloop()
mainCat('Notification Area: CrayTag '+ver.sion)
