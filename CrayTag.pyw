class ver:
    sion="2.2" # Version number of program. # ver.sion
"""
##############################
    CrayTag.
##############################
    Coded by: Dalton Overlin
##########################################################
    Last Code Revision Date: Jul. 11th, 2020
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
    import random, string, tkinter, shutil, time, datetime, eyed3, tinytag
    from tinytag import TinyTag
    from tkinter import *
    from tkinter import filedialog
    from tkinter import PhotoImage
    import tkinter.font as tkFont
    import tkinter as tk
    from PIL import ImageTk, Image
except:
    print("An import failed, attempting phase 2 import.")
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
def rep(hexa):
    return hexa.replace("/", "").replace("\\", "").replace(":", "").replace("*", "").replace("?", "").replace("\"", "").replace("'", "").replace("<", "").replace(">", "").replace("|", "")
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
        victor=rep(temp+t)
        holder.append(victor)
        cova+=1
    return holder
class ex:
    tide = os.getcwd()
class img:
    B="""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"""
    C="""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"""
    D="""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"""
    Q="""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"""
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
    class nim:
        ue=None
    nim.ue=tkinter.Tk()
    root=nim.ue
    background_image2=tkinter.PhotoImage(data = img.D)
    root.iconphoto(False, background_image2)
    class hepa:
        a=True
    def van():
        rootx=Toplevel(nim.ue)
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
    back=tkinter.PhotoImage(data = img.Q)
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
