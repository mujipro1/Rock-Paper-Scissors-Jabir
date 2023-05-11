from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random


def userprofile():
    profilewin = Toplevel()
    profilewin.title('Profile')
    profilewin.geometry('500x600+400+100')
    profilewin['background'] = '#f1f5f5'

    Label(profilewin,bg='#f1f4ed', text='Welcome  '+mainUsername.get(),
          font='none 20 bold').place(x=100, y = 10)

    #Information for the Username
    Label(profilewin, bg='#f1f4ed', text='Username').place(x=20, y=150)
    Label(profilewin, bg='#f1f4ed', text=userdiction['username']).place(x=100,y=150)

    #Information for the Phone number
    Label(profilewin, bg='#f1f4ed', text='Phone').place(x=20, y=200)
    Label(profilewin, bg='#f1f4ed', text=userdiction['phone']).place(x=100,y=200)

    mainloop()
    pass


def userlogin():
    file = open('gameregister.txt', 'r')
    data = file.readlines()

    for line in data:
        user_data = eval(line)
        if user_data['username'] == mainUsername.get() and user_data['password'] == mainPassword.get():
           global userdiction
           userdiction = user_data.copy()
           userprofile()
           return
        
    messagebox.showinfo('information', 'Incorrect Username or Password')
    file.close()


def loginmain():
    global loginwin, mainUsername, mainPassword
    
    mainUsername = StringVar()
    mainPassword = StringVar()
    
    loginwin = frames[2]
    loginwin.tkraise()
    loginwin.config(bg = '#f1f5f5')
    winframe.title('Login Section')

    login_img = PhotoImage(file='login_200.png')
    Label(loginwin, bg='#f1f4ed',image=login_img).place(x=width/2, y=150, anchor='center')
    
    #label and textbox for the username
    Label(loginwin,bg='#f1f5f5', text='Username', font='Arial 12 bold').place(x=(width/2)-100, y=270, anchor='center')
    username_entry = Entry(loginwin,fg='#4e5455',bg='#94ecf7',font='Arial 12 bold',
                           width=20,textvariable=mainUsername)
    username_entry.place(x=(width/2)+50,y=270, anchor='center')


    #Label and textbox for the password
    Label(loginwin, bg='#f1f5f5', text='Password',font='Arial 12 bold').place(x=(width/2)-100, y=300, anchor='center')
    password_entry = Entry(loginwin, fg='#4e5455',bg='#94ecf7',font='Arial 12 bold',
                           width=20, show='*',
                           textvariable=mainPassword)
    password_entry.place(x=(width/2)+50, y=300, anchor='center')

    #Button for the login
    login = Button(loginwin, bg='blue', fg='white', text='Login', width=15, height=2, font='Arial 12 bold',
           relief='groove',command=userlogin)
    login.place(x=(width/2), y=390, anchor='center')
    login.bind('<Enter>', enterBind)
    login.bind('<Leave>', leaveBind)


    #Account creation hyperlink
    registerlink = Label(loginwin, bg='#f1f4ed',
                         text="Don't Have an Account? Sign Up",
                         font=('Helveticabold', 13),
                         fg="blue", cursor="hand2")
    registerlink.place(x=(width/2), y=450, anchor='center')
    registerlink.bind("<Button-1>", lambda e:registerNewuser())
    
    username_entry.focus()
    mainloop()
    pass


def register():
    #create a file called user_registration to store the info
    #w means open the file for writing
    gamefile = open('gameregister.txt','a')

    #Get the info form the username textbox and store it in
    #extract_username
    extract_username = reg_username.get()
    extract_password = reg_password.get()
    extract_phone = reg_phone.get()

    #add the duplication info into the dictionary
    userdiction['username']=extract_username
    userdiction['password']=extract_password
    userdiction['phone']=extract_phone

    myJsonString = {}
    for key, value in userdiction.items():
        myJsonString[key] = value  

    gamefile.write(str(myJsonString))
    gamefile.write("\n")
    gamefile.close()

    messagebox.showinfo('Information',
                        'Your account has been successfully created')

    reg_username.set('')
    reg_password.set('')
    reg_phone.set('')


def registerNewuser():
    global regwin
    
    regwin = frames[3]
    regwin.tkraise()

    winframe.title('Registration')
    regwin.config(bg = '#f1f5f5')

    img = PhotoImage(file='registerIcon_200_177.png')
    Label(regwin, bg='#f1f4ed',image=img).place(x=width/2, y=150, anchor='center')

    #Label with entrybox for the user to enter name, password and phone number
    Label(regwin,bg='#f1f4ed', text='Username', font='Arial 12 bold').place(x=(width/2)-100,y=270, anchor='center')
    entry_username = Entry(regwin,fg='#4e5455',bg='#94ecf7', font='Arial 12 bold',
                           width=20,
                           textvariable = reg_username)
    entry_username.place(x=(width/2)+50, y=270, anchor='center')


    #This is for the user to enter the password
    Label(regwin,bg='#f1f4ed',text='Password', font='Arial 12 bold').place(x=(width/2)-100,y=300, anchor='center')
    entry_pwd = Entry(regwin,fg='#4e5455',bg='#94ecf7', font='Arial 12 bold',
                           width=20, show='*',
                           textvariable=reg_password)
    entry_pwd.place(x=(width/2)+50, y=300, anchor='center')

    #This is for the user to enter the phone
    Label(regwin,bg='#f1f4ed', text='Phone', font='Arial 12 bold').place(x=(width/2)-100, y=330, anchor='center')
    entry_phone = Entry(regwin,fg='#4e5455',bg='#94ecf7', font='Arial 12 bold',
                           width=20,
                           textvariable=reg_phone)
    entry_phone.place(x=(width/2)+50, y=330, anchor='center')


    #This button is to register the user's information
    regButton = Button(regwin,bg='blue', fg='white',text='Register', width=15, height=2,
           font='Arial 12 bold',command=register)
    regButton.place(x=width/2, y=390, anchor='center')
    regButton.bind('<Enter>', enterBind)
    regButton.bind('<Leave>', leaveBind)

    entry_username.focus()

    #Create a hyperlink for the Login main section
    loginLink = Label(regwin, bg='#f1f4ed',
                         text='Back to Login',
                         font=('Helveticabold', 12),
                         fg='blue', cursor='hand2')
    loginLink.place(x=(width/2), y=450, anchor='center')
    loginLink.bind('<Button-1>', lambda e: loginmain())
    mainloop()
    pass
 

def newGame():
    lblimage.destroy()
    parent = frames[1]
    parent.tkraise()

    global scores
    scores = [0, 0, 0]

    label = Label(parent, text='Rock Paper Scissors')
    label.config(font='Arial 14 bold')
    label.place(x=350, y=10)

    global scorePC, scoreUser, drawScore, gameCounter

    gameCounter = Label(parent, text='Total Turns: 0')
    gameCounter.config(font='Arial 12 bold', fg='green')
    gameCounter.place(x=70, y=10)

    scoreUser = Label(parent, text='Your Scores: '+ str(scores[0]))
    scoreUser.config(font='Arial 15 bold', fg='green')
    scoreUser.place(x=70, y=60)

    drawScore = Label(parent, text='Ties: '+str(scores[2]))
    drawScore.config(font='Arial 15 bold', fg='red')
    drawScore.place(x=400, y=60)

    scorePC = Label(parent, text='Opponent Scores: '+str(scores[1]))
    scorePC.config(font='Arial 15 bold', fg='blue')
    scorePC.place(x=600, y=60)

    label = Label(parent, text='Rock Paper Scissors')
    label.config(font='Arial 14 bold')
    label.place(x=350, y=10)

    global opponentPic, yourPic
    opponentPic = Label(parent)
    opponentPic.place(x=500,y=250)

    yourPic = Label(parent)
    yourPic.place(x=340,y=250)
    
    paperimage = Label(parent, image=img1, text='0')
    paperimage.place(x=40,y=100)

    rockimage = Label(parent, image=img2, text='1')
    rockimage.place(x=40,y=250)

    scissorimage = Label(parent, image=img3, text='2')
    scissorimage.place(x=40,y=400)

    UserButtons = [paperimage, rockimage, scissorimage]
    for i in UserButtons:
        i.bind('<Enter>', enterBind)
        i.bind('<Leave>', leaveBind)
        i.bind('<Button>', clickBind)
    pass

def enterBind(e):
    e.widget.config(cursor='hand2')

def leaveBind(e):
    e.widget.config(cursor='arrow')

def clickBind(e):
    Useridx = int(e.widget['text'])
    randomIdx = random.randint(0, 2)
    opponentPic.config(image=imgArray[randomIdx])
    yourPic.config(image=imgArray[Useridx])

    scoreSystem(Useridx, randomIdx, scores)

    scoreUser.config(text='Your Scores: '+ str(scores[0]))
    scorePC.config(text='Opponent Scores: '+ str(scores[1]))
    drawScore.config(text='Ties: '+ str(scores[2]))
    gameCounter.config(text='Total Turns: '+str(sum(scores)))
    pass

def scoreSystem(userPic, PcPic, scores):
    # 0 paper, 1 rock, 2 scissors
    # scores[user, PC, ties]
    if(userPic == PcPic):
        scores[2] += 1
    elif((userPic==0 and PcPic==1)or(userPic==1 and PcPic==2)or(userPic==2 and PcPic==0)):
        scores[0] += 1
    else: 
        scores[1] += 1
    pass

def resetGame():
    try:
        opponentPic.destroy()
        yourPic.destroy()
    except:
        pass
    newGame()
    pass

userdiction = {}
winframe = Tk()
reg_phone = StringVar()
reg_username = StringVar()
reg_password = StringVar()

winframe.title('Tic Tac Toe Game')
winframe.geometry('850x600+300+100')
winframe.resizable(False,False)

width = 850
height = 600

img = Image.open('warcraft.png')
img = img.resize((850, 600))
img = ImageTk.PhotoImage(img)

img1 = PhotoImage(file='paper100.png')
img2 = PhotoImage(file='rock100.png')
img3 = PhotoImage(file='scissors100.png')

global imgArray
imgArray = [img1, img2, img3]

frames = []
for i in range(5):
    frame = Frame(winframe, height=height, width=width)
    frame.place(x=0, y=0)
    frame.pack_propagate(False)
    frames.append(frame)

frames[0].tkraise()
lblimage = Label(frames[0], image=img)
lblimage.place(x=0,y=0)

menu = Menu(winframe)
winframe.config(menu=menu)

gameMenu = Menu(menu)
menu.add_cascade(label='Game',menu=gameMenu)
gameMenu.add_command(label='Login', command=loginmain)
gameMenu.add_command(label='New Game', command=newGame)
gameMenu.add_command(label='Reset Game', command=resetGame)

helpMenu = Menu(menu)
menu.add_cascade(label='Help',menu=helpMenu)

winframe.mainloop()