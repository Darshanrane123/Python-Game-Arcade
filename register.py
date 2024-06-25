import customtkinter
from subprocess import call
from rateus import *
import os
from tkinter import filedialog
from login import *
from createAccount import *
from shooter_game import *
import cv2
from PIL import Image,ImageTk
import datetime
import random

class Game:


    # constructor
    def __init__(self , root1, username_lg="" ):

        # -----------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------
        self.root = root1
        self.root.geometry ( "1535x780+-7+0" )
        self.root.title ( 'Exsto Gaming Platform' )
        self.root.configure(bg = '#212122')

        userName = username_lg
        which_game = [0,1,2,3]
        self.frame = customtkinter.CTkFrame ( master = self.root , width = 1535 , height = 110 , fg_color = 'white' )
        self.frame.place ( x = -7 , y = 0 )
        self.frame.pack ( pady = 5 , padx = 10 )

        self.frame1 = customtkinter.CTkFrame ( master = self.root , width = 1535 , height = 670,fg_color = '#212122')
        self.frame1.place ( x = -7 , y = 110 )
        self.frame1.pack ( pady = 5 , padx = 10 )
        self.entry1 = Label ( self.frame, text= f"{userName}",width = 12 , bg = "white" , border = 0 )
        # self.entry1.insert(0,f"{userName}")
        self.entry1.place ( x = 1408 , y = 84 )
        # -----------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------

        self.label = customtkinter.CTkLabel (master=self.frame, text='Exsto Gaming', font=('Comic Sans MS', 37, 'bold'), text_color='black')
        self.label.place(x=120, y=20)
        self.i2 = PhotoImage ( file = 'images/back1.png' )
        self.i3 = PhotoImage ( file = 'images/rating3.6.png' )
        self.i4 = PhotoImage ( file = 'images/rating 4.3.png' )
        self.i5 = PhotoImage ( file = 'images/rating 4.5.png' )
        self.i6 = PhotoImage ( file = 'images/rating 4.8.png' )
        self.img = PhotoImage(file="images/logo1.png")
        Label(self.frame, image=self.img, bg='white').place(x=10, y=3)
        self.img1 = PhotoImage(file="images/search.png")
        self.img2 = PhotoImage(file="images/profile.png")
        self.img3 = PhotoImage(file="images/mario.png")
        self.img31 = PhotoImage(file="images/mario2.png")
        self.img4 = PhotoImage(file="images/play.png")
        self.img5 = PhotoImage(file="images/bgimg1.png")
        self.img51 = PhotoImage(file="images/bgimg2.png")
        self.img6 = PhotoImage(file="images/profile1.png")
        self.img7 = PhotoImage(file="images/6bg.png")
        self.img8 = PhotoImage(file="images/rate us.png")
        self.img9 = PhotoImage ( file = "images/FALPPYBIRD LOGO.png" )
        self.img10 = PhotoImage ( file = "images/FALPPYBIRD LOGO1.png" )
        self.img11 = PhotoImage ( file = "images/medal1.png" )
        self.img12 = PhotoImage ( file = "images/starfill1.png" )
        self.img13 = PhotoImage ( file = "images/space invader.png" )
        self.img14 = PhotoImage ( file = "images/space invader1.png" )
        self.imgM1 = PhotoImage ( file = "images/M1.png" )

        # -----------------------------------------------------------------------------------------------

        def mario():
            marioGame = which_game[0]
            for self.f in self.frame1.winfo_children ( ):
                self.f.destroy ( )

            def play():
                import testing

                if userName == "":
                    messagebox.showerror("Invalid", "You have to first login the  account !")

                else:
                    self.root.destroy ( )
                    self.root2 = Tk ( )
                    self.obj = testing.Mario( self.root2 ,userName, marioGame)



            self.b4 = Label ( self.frame1 , image = self.img3 , bg = 'white' , border = 3 )
            self.b4.place ( x = 70 , y = 70 )
            self.b6 = Button ( self.frame1 , image = self.img4 , bg = 'white' , border = 0 , command = play ,
                               cursor = 'hand2' )
            self.b6.place ( x = 300 , y = 500 )
            self.l2 = Label ( self.frame1 , text = " Mario Vs Dragon " , bg = '#212122' , fg = 'white' , border = 0 ,
                              font = ('Comic Sans MS' , 20 , 'bold') )
            self.l2.place ( x = 995 , y = 115 )
            self.l2 = Label ( self.frame1 , text = "Mario made his debut in the classic 1981 arcade \n"
                                                   "game Donkey Kong. In this game, we will protect ourself\n"
                                                   "from Dragon's fireball. If we collide With fireball or Cactus\n"
                                                   "then game ends. In this game we have to complete 3 levels\n"
                                                   "1st level is easy , in 2nd level more cactus wall is added\n"
                                                   "And 3rd level also the same one more cactus wall add .\n  "
                                                   "Game looks easy to play but 3rd level is very tough.\n"
                                                   "So who one can played all three levels then he is the winner!!\n " ,
                              bg = '#212122' , fg = 'white' ,
                              border = 0 ,
                              font = ('Century' , 15 , 'bold') )
            self.button3 = Button ( self.frame1 , image = self.i2 , bg = '#212122' , border = -10 , command = home )
            self.button3.place ( x = 0 , y = 0 )
            Label ( self.frame1 , text = 'Back' , bg = '#212122' , fg = 'white' ,
                    font = ('Future' , 12 , 'bold') ).place ( x = 3 , y = 60 )

            def rate_us():
                if userName != "":
                    import rateus
                    self.root.destroy ( )
                    self.root1 = Tk ( )
                    self.obj = rateus.Rateus ( self.root1 , userName , marioGame )
                else:
                    messagebox.showwarning ( "Invalid" , "Please First Login the account !" )

            def how_to_play():
                call ( ['python' , 'how to play mario vs dragon game.py'] )

            self.l2.place ( x = 800 , y = 200 )
            self.l2 = Button ( self.frame1 , text = "How to Play ?" , bg = '#212122' , fg = 'Slate Blue1' ,
                               border = 0 ,
                               font = ('Arial Rounded MT Bold' , 15 , 'bold') , cursor = 'hand2', command = how_to_play )
            self.l2.place ( x = 880 , y = 440 )
            Frame ( self.frame1 , width = 120 , height = 3 , bg = 'Slate Blue1' ,
                    highlightbackground = 'blue' ).place ( x = 890 ,
                                                           y = 470 )
            self.l2 = Button ( self.frame1 , text = "Rate us" , bg = '#212122' , fg = 'Slate Blue1' , border = 0 ,
                               font = ('Arial Rounded MT Bold' , 15 , 'bold') , cursor = 'hand2' ,
                               command = rate_us )
            self.l2.place ( x = 1250 , y = 440 )
            Frame ( self.frame1 , width = 90 , height = 3 , bg = 'Slate Blue1' ,
                    highlightbackground = 'blue' ).place (
                x = 1255 , y = 470 )
            Label ( self.frame1 , image = self.img8 , width = 50 , bg = '#212122' ,
                    highlightbackground = 'blue' ).place (
                x = 1350 , y = 410 )

        # -----------------------------------------------------------------------------------------------



        def shooter():
            shooter1 = which_game[1]
            for self.f in self.frame1.winfo_children ( ):
                self.f.destroy ( )

            def play():
                import shooter_game
                if userName == "":
                    messagebox.showerror ( "Invalid" , "You have to first login the  account !" )

                # calling strore window and calling Store class in main.py
                else:
                    self.root.destroy ( )
                    self.root2 = Tk ( )
                    self.obj = shooter_game.Shooter( self.root2 , username_lg, shooter1 )

            self.b4 = Label ( self.frame1 , image = self.img5 , bg = 'white' , border = 3 )
            self.b4.place ( x = 70 , y = 70 )
            self.b6 = Button ( self.frame1 , image = self.img4 , bg = 'white' , border = 0 , command = play ,
                               cursor = 'hand2' )
            self.b6.place ( x = 300 , y = 500 )
            self.b6.focus_set ( )
            self.l2 = Label ( self.frame1 , text = " Shooter Game" , bg = '#212122' , fg = 'white' , border = 0 ,
                              font = ('Comic Sans MS' , 20 , 'bold') )
            self.l2.place ( x = 1020 , y = 110 )
            self.l2 = Label ( self.frame1 , text = "Get ready for non-stop action in our shooter game! \n"
                                                   "Pick your favorite weapons and team up with friends to \n"
                                                   "take down enemies in exciting battles. Whether you like \n"
                                                   "sniping from a distance or getting up close with a shotgun,\n "
                                                   "there's something for everyone. Play with friends or go solo in \n"
                                                   "thrilling missions filled with excitement and challenges. \n"
                                                   "Easy to play, hard to master – our shooter game is sure to keep \n"
                                                   "you entertained for hours!" , bg = '#212122' , fg = 'white' ,
                              border = 0 ,
                              font = ('Century' , 15 , 'bold') )
            self.button3 = Button ( self.frame1 , image = self.i2 , bg = '#212122' , border = -10 , command = home )
            self.button3.place ( x = 0 , y = 0 )
            Label ( self.frame1 , text = 'Back' , bg = '#212122' , fg = 'white' ,
                    font = ('Future' , 12 , 'bold') ).place ( x = 3 , y = 60 )

            def rate_us():
                if userName != "":
                    import rateus
                    self.root.destroy ( )
                    self.root1 = Tk ( )
                    self.obj = rateus.Rateus ( self.root1 , userName , shooter1 )
                else:
                    messagebox.showwarning ( "Invalid" , "Please First Login the account !" )

            def how_to_play():
                call ( ['python' , 'how to play shooter game.py'] )

            self.l2.place ( x = 800 , y = 200 )
            self.l2 = Button ( self.frame1 , text = "How to Play ?" , bg = '#212122' , fg = 'Slate Blue1' , border = 0 ,
                               font = ('Arial Rounded MT Bold' , 15 , 'bold') , cursor = 'hand2' , command = how_to_play)
            self.l2.place ( x = 880 , y = 440 )
            Frame ( self.frame1 , width = 120 , height = 3 , bg = 'Slate Blue1' , highlightbackground = 'blue' ).place (
                x = 890 ,
                y = 470 )
            self.l2 = Button ( self.frame1 , text = "Rate us" , bg = '#212122' , fg = 'Slate Blue1' , border = 0 ,
                               font = ('Arial Rounded MT Bold' , 15 , 'bold') , cursor = 'hand2' , command = rate_us )
            self.l2.place ( x = 1250 , y = 440 )
            Frame ( self.frame1 , width = 90 , height = 3 , bg = 'Slate Blue1' , highlightbackground = 'blue' ).place (
                x = 1255 , y = 470 )
            Label ( self.frame1 , image = self.img8 , width = 50 , bg = '#212122' ,
                    highlightbackground = 'blue' ).place (
                x = 1350 , y = 410 )

        # -----------------------------------------------------------------------------------------------

        def flappy():
            flappy1 = which_game[2]

            for self.f in self.frame1.winfo_children ( ):
                self.f.destroy ( )

            def play():
                import game
                if userName == "":
                    messagebox.showerror ( "Invalid" , "You have to first login the  account !" )

                # calling strore window and calling Store class in main.py
                else:
                    # self.root.destroy ( )

                    self.obj = game.Game(username_lg, flappy1)


            self.b4 = Label ( self.frame1 , image = self.img10 , bg = 'white' , border = 3 )
            self.b4.place ( x = 70 , y = 70 )
            self.b6 = Button ( self.frame1 , image = self.img4 , bg = 'white' , border = 0 , command = play ,
                               cursor = 'hand2' )
            self.b6.place ( x = 300 , y = 500 )
            self.b6.focus_set ( )
            self.l2 = Label ( self.frame1 , text = " Flappy Bird " , bg = '#212122' , fg = 'white' , border = 0 ,
                              font = ('Comic Sans MS' , 20 , 'bold') )
            self.l2.place ( x = 995 , y = 110 )
            self.l2 = Label ( self.frame1 , text = "Flappy Bird is an arcade-style game where the \n"
                                                   "player takes control of a bird named Faby. \n"
                                                   "Faby persistently moves to the right, and your\n"
                                                   "task is to navigate it through pairs of pipes.\n"
                                                   " These pipes have equally sized gaps placed at \n"
                                                   "random heights. The bird automatically descends, \n"
                                                   "and you can make it ascend by tapping the touchscreen.\n"
                                                   " The objective is to fly as far as possible without \n"
                                                   "colliding with the pipes" ,
                              bg = '#212122' , fg = "white" , border = 0 , font = ('Century' , 15 , 'bold') )
            self.button3 = Button ( self.frame1 , image = self.i2 , bg = '#212122' , border = -10 , command = home )
            self.button3.place ( x = 0 , y = 0 )
            Label ( self.frame1 , text = 'Back' , bg = '#212122' , fg = 'white' ,
                    font = ('Future' , 12 , 'bold') ).place ( x = 3 , y = 60 )

            def rate_us():
                if userName != "":
                    import rateus
                    self.root.destroy ( )
                    self.root1 = Tk ( )
                    self.obj = rateus.Rateus ( self.root1 , userName , flappy1 )
                else:
                    messagebox.showwarning ( "Invalid" , "Please First Login the account !" )

            def how_to_play():
                call ( ['python' , 'how to play flappy bird.py'] )

            self.l2.place ( x = 800 , y = 200 )
            self.l2 = Button ( self.frame1 , text = "How to Play ?" , bg = '#212122' , fg = 'Slate Blue1' ,
                               border = 0 ,
                               font = ('Arial Rounded MT Bold' , 15 , 'bold') , cursor = 'hand2', command = how_to_play )
            self.l2.place ( x = 880 , y = 440 )
            Frame ( self.frame1 , width = 120 , height = 3 , bg = 'Slate Blue1' ,
                    highlightbackground = 'blue' ).place ( x = 890 ,
                                                           y = 470 )
            self.l2 = Button ( self.frame1 , text = "Rate us" , bg = '#212122' , fg = 'Slate Blue1' , border = 0 ,
                               font = ('Arial Rounded MT Bold' , 15 , 'bold') , cursor = 'hand2' ,
                               command = rate_us )
            self.l2.place ( x = 1250 , y = 440 )
            Frame ( self.frame1 , width = 90 , height = 3 , bg = 'Slate Blue1' ,
                    highlightbackground = 'blue' ).place (
                x = 1255 , y = 470 )
            Label ( self.frame1 , image = self.img8 , width = 50 , bg = '#212122' ,
                    highlightbackground = 'blue' ).place (
                x = 1350 , y = 410 )

        def spaceInavder():
            space = which_game[3]

            for self.f in self.frame1.winfo_children ( ):
                self.f.destroy ( )

            def play():
                import main
                if userName == "":
                    messagebox.showerror ( "Invalid" , "You have to first login the  account !" )

                # calling strore window and calling Store class in main.py
                else:
                    self.root.destroy ( )
                    self.root2 = Tk ( )

                    self.obj = main.Space(self.root2,username_lg,space)


            self.b4 = Label ( self.frame1 , image = self.img14 , bg = 'white' , border = 3 )
            self.b4.place ( x = 70 , y = 70 )
            self.b6 = Button ( self.frame1 , image = self.img4 , bg = 'white' , border = 0 , command = play ,
                               cursor = 'hand2' )
            self.b6.place ( x = 300 , y = 500 )
            self.b6.focus_set ( )
            self.l2 = Label ( self.frame1 , text = " Space Invader " , bg = '#212122' , fg = 'white' , border = 0 ,
                              font = ('Comic Sans MS' , 20 , 'bold') )
            self.l2.place ( x = 1025 , y = 115 )
            self.l2 = Label ( self.frame1 , text = "Space Invaders is a classic arcade game that was \n"
                                                   "first released in 1978. It was designed by Tomohiro \n"
                                                   "Nishikado and originally sold and manufactured by Taito in Japan.\n"
                                                   "The game was later licensed by Midway for release in North America.\n"
                                                   "The objective of Space Invaders is to control a laser cannon \n"
                                                   "that moves horizontally across the bottom of the screen and fire \n"
                                                   "at descending aliens. The aim is to shoot all of the aliens\n"
                                                   "before they reach the bottom of the screen. The aliens move \n"
                                                   "back and forth and every time they complete a row, they move \n"
                                                   "down one level. The game gets progressively faster and more \n"
                                                   "challenging as the aliens get closer to the bottom of the screen.\n" ,
                              bg = '#212122' , fg = "white" , border = 0 , font = ('Century' , 15 , 'bold') )
            self.button3 = Button ( self.frame1 , image = self.i2 , bg = '#212122' , border = -10 , command = home )
            self.button3.place ( x = 0 , y = 0 )
            Label ( self.frame1 , text = 'Back' , bg = '#212122' , fg = 'white' ,
                    font = ('Future' , 12 , 'bold') ).place ( x = 3 , y = 60 )

            def rate_us():
                if userName != "":
                    import rateus
                    self.root.destroy ( )
                    self.root1 = Tk ( )
                    self.obj = rateus.Rateus ( self.root1 , userName , space )
                else:
                    messagebox.showwarning ( "Invalid" , "Please First Login the account !" )

            def how_to_play():
                call ( ['python' , 'how to play space invader.py'] )

            self.l2.place ( x = 800 , y = 200 )
            self.l2 = Button ( self.frame1 , text = "How to Play ?" , bg = '#212122' , fg = 'Slate Blue1' ,
                               border = 0 ,
                               font = ('Arial Rounded MT Bold' , 15 , 'bold') , cursor = 'hand2' ,
                               command = how_to_play )
            self.l2.place ( x = 880 , y = 480 )
            Frame ( self.frame1 , width = 120 , height = 3 , bg = 'Slate Blue1' ,
                    highlightbackground = 'blue' ).place ( x = 890 ,
                                                           y = 510 )
            self.l2 = Button ( self.frame1 , text = "Rate us" , bg = '#212122' , fg = 'Slate Blue1' , border = 0 ,
                               font = ('Arial Rounded MT Bold' , 15 , 'bold') , cursor = 'hand2' ,
                               command = rate_us )
            self.l2.place ( x = 1250 , y = 480 )
            Frame ( self.frame1 , width = 90 , height = 3 , bg = 'Slate Blue1' ,
                    highlightbackground = 'blue' ).place (
                x = 1255 , y = 510 )
            Label ( self.frame1 , image = self.img8 , width = 50 , bg = '#212122' ,
                    highlightbackground = 'blue' ).place (
                x = 1350 , y = 450 )

        # -----------------------------------------------------------------------------------------------
        self.ima2 = cv2.imread ( "C:/Users/sujal/PycharmProjects/new_Python_Project/images/mario1.png" )
        self.imgr2 = cv2.resize ( self.ima2 , (310 , 173) )
        self.img_rgb2 = cv2.cvtColor ( self.imgr2 , cv2.COLOR_BGR2RGB )
        self.img_tk1 = ImageTk.PhotoImage ( Image.fromarray ( self.img_rgb2 ) )
        self.la1 = (Button(self.frame1, image = self.img_tk1, bg ='#212122', border = 4, cursor = "hand2", command = mario))
        self.la1.place(x=10, y=70)
        self.le1 = Label(self.frame1, image = self.i3,bg ='#212122', border = 0)
        self.le1.place(x=5 , y=320)

        # -----------------------------------------------------------------------------------------------
        self.ima3 = cv2.imread ( "C:/Users/sujal/PycharmProjects/new_Python_Project/images/bgimg.png" )
        self.imgr3 = cv2.resize ( self.ima3 , (310 , 173) )
        self.img_rgb3 = cv2.cvtColor ( self.imgr3 , cv2.COLOR_BGR2RGB )
        self.img_tk2 = ImageTk.PhotoImage ( Image.fromarray ( self.img_rgb3 ) )
        self.la2 = (Button(self.frame1, image = self.img_tk2, bg ='#212122', border = 4, cursor = "hand2", command = shooter))
        self.la2.place(x=340, y=70)
        self.le2 = Label ( self.frame1 , image = self.i5 , bg = '#212122' , border = 0 )
        self.le2.place ( x = 340 , y = 320 )

        # -----------------------------------------------------------------------------------------------
        self.ima4 = cv2.imread ( "C:/Users/sujal/PycharmProjects/new_Python_Project/images/FALPPYBIRD LOGO1.png" )
        self.imgr4 = cv2.resize ( self.ima4 , (310 , 173) )
        self.img_rgb4 = cv2.cvtColor ( self.imgr4 , cv2.COLOR_BGR2RGB )
        self.img_tk3 = ImageTk.PhotoImage ( Image.fromarray ( self.img_rgb4 ) )
        self.la3 = Button(self.frame1, image = self.img_tk3, bg ='#212122', border = 4, cursor = "hand2", command = flappy)
        self.la3.place(x=670, y=70)
        self.le3 = Label ( self.frame1 , image = self.i4 , bg = '#212122' , border = 0 )
        self.le3.place ( x = 670 , y = 320 )

        # -----------------------------------------------------------------------------------------------
        self.la4 = Button(self.frame1, image = self.img13, bg ='#212122', border = 4,  cursor = "hand2", command = spaceInavder)
        self.la4.place(x=1000, y=70)
        self.le4 = Label(self.frame1, image = self.i6,bg ='#212122', border = 0)
        self.le4.place(x=1000 , y=320)

        Frame ( self.frame1 , width = 1 , height = 640 , bg = 'white' ).place ( x = 1330 , y = 10 )
        self.le5 = Label ( self.frame1 , text = "Recently Played", bg = '#212122' ,fg = "white", border = 0 , font = ("Comic Sans MS",13))
        self.le5.place ( x = 1370 , y = 40 )
        Frame ( self.frame1 , width = 130 , height = 2 , bg = 'white' ).place ( x = 1370 , y = 65 )

        # self.Played_Game = None

        if userName != "":

            self.conn1 = mysql.connector.connect ( host = 'localhost' , password = 'Suj@y935974' , user = 'root' ,
                                                   database = 'game' )
            self.Cursor_obj1 = self.conn1.cursor ( )
            self.Cursor_obj1.execute (
                f" select Recently_played, played_time from create_account where username= '{username_lg}'" , () )
            self.file = self.Cursor_obj1.fetchone ( )
            print(self.file)
            if self.file[1] is not None and self.file[0] is not None:
                self.Played_Game = self.file[0]
                self.Played_time = self.file[1]
            else:
                self.Played_Game = self.file[0]
                self.Played_time = 0

            # self.root.configure(self.Played_Game, text=f"{self.file[0]}")
            # self.root.configure(self.Played_time, text=f"{self.file[1]}")
            self.conn1.close ( )


            # if self.Played_time is None or self.Played_Game is None :
            #     pass

            if self.Played_Game == 0:
                self.ima = cv2.imread("C:/Users/sujal/PycharmProjects/new_Python_Project/images/mario1.png" )
                self.imgr1 = cv2.resize ( self.ima , (160 , 90) )
                self.img_rgb1 = cv2.cvtColor ( self.imgr1 , cv2.COLOR_BGR2RGB )
                self.img_tk = ImageTk.PhotoImage ( Image.fromarray ( self.img_rgb1 ) )
                self.L1 = Label(self.frame1, image = self.img_tk,bg='#212122', border=2 )
                self.L1.place(x=1355,y=90)
                self.L2 = Label ( self.frame1 ,text = f"Played Time :  {round(self.Played_time / 60,2)} MIN", bg = '#212122',fg="White" , border = 0, font =("Century", 9, "bold"))
                self.L2.place ( x = 1350 , y = 200 )

            elif self.Played_Game == 1:
                self.ima = cv2.imread ( "C:/Users/sujal/PycharmProjects/new_Python_Project/images/bgimg2.png" )
                self.imgr1 = cv2.resize ( self.ima , (160 , 90) )
                self.img_rgb1 = cv2.cvtColor ( self.imgr1 , cv2.COLOR_BGR2RGB )
                self.img_tk = ImageTk.PhotoImage ( Image.fromarray ( self.img_rgb1 ) )
                self.L1 = Label ( self.frame1 , image = self.img_tk , bg = '#212122' , border = 2 )
                self.L1.place ( x = 1355 , y = 90 )
                self.L2 = Label ( self.frame1 , text = f"Played Time :  {round ( self.Played_time / 60 , 2 )} MIN" ,
                                  bg = '#212122' , fg = "White" , border = 0 , font = ("Century" , 9 , "bold") )
                self.L2.place ( x = 1350 , y = 200 )

            elif self.Played_Game == 2:
                self.pt = self.Played_time / 60
                self.ima = cv2.imread("C:/Users/sujal/PycharmProjects/new_Python_Project/images/FALPPYBIRD LOGO1.png" )
                self.imgr1 = cv2.resize ( self.ima , (160 , 90) )
                self.img_rgb1 = cv2.cvtColor ( self.imgr1 , cv2.COLOR_BGR2RGB )
                self.img_tk = ImageTk.PhotoImage ( Image.fromarray ( self.img_rgb1 ) )
                self.L1 = Label(self.frame1, image = self.img_tk,bg='#212122', border=2 )
                self.L1.place(x=1355,y=90)
                self.L2 = Label ( self.frame1 , text = f"Played Time :  {round ( self.Played_time / 60 , 2 )} MIN" ,
                                  bg = '#212122' , fg = "White" , border = 0 , font = ("Century" , 9 , "bold") )
                self.L2.place ( x = 1350 , y = 200 )

            elif self.Played_Game == 3:
                self.ima = cv2.imread("C:/Users/sujal/PycharmProjects/new_Python_Project/images/space invader1.png" )
                self.imgr1 = cv2.resize ( self.ima , (160 , 90) )
                self.img_rgb1 = cv2.cvtColor ( self.imgr1 , cv2.COLOR_BGR2RGB )
                self.img_tk = ImageTk.PhotoImage ( Image.fromarray ( self.img_rgb1 ) )
                self.L1 = Label(self.frame1, image = self.img_tk,bg='#212122', border=2 )
                self.L1.place(x=1355,y=90)
                self.L2 = Label ( self.frame1 , text = f"Played Time :  {round ( self.Played_time / 60 , 2 )} MIN" ,
                                  bg = '#212122' , fg = "White" , border = 0 , font = ("Century" , 9 , "bold") )
                self.L2.place ( x = 1350 , y = 200 )





        # -----------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------
        def on_enter(e):
            self.entry.delete(0, 'end')

        def on_leave(e):
            name = self.entry.get()
            if name == '':
                self.entry.insert(0, 'Ex. Mario vs Dragon')

        # -----------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------

        self.entry = customtkinter.CTkEntry(master = self.frame, width=400, height = 40)
        self.entry.place(x=550, y=35)
        self.entry.insert(0, 'Ex. Mario vs Dragon')
        self.entry.bind('<FocusIn>', on_enter)
        self.entry.bind('<FocusOut>', on_leave)

        # -----------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------


        def check_Which_You_want_to_play():

            if self.entry.get() == "":
                pass

            elif self.entry.get() in str.lower('Mario Vs Dragon') or self.entry.get() in str.upper('Mario Vs Dragon') or self.entry.get() in 'Mario Dragon':
                for self.f in self.frame1.winfo_children ( ):
                    self.f.destroy ( )
                marioGame = which_game[0]
                def play():
                    import testing

                    if userName == "":
                        messagebox.showerror ( "Invalid" , "You have to first login the  account !" )


                    else:
                        self.root.destroy ( )
                        self.root2 = Tk ( )
                        self.obj = testing.Mario ( self.root2 , userName ,marioGame)
                self.b4 = Label ( self.frame1 , image = self.img3 , bg = 'white' , border = 3 )
                self.b4.place (x = 70 , y = 70 )
                self.b6 = Button ( self.frame1 , image = self.img4 , bg = 'white' , border = 0 , command = play, cursor = 'hand2' )
                self.b6.place ( x = 300 , y = 500 )
                self.button3 = Button ( self.frame1 , image = self.i2 , bg = '#212122' , border = -10 , command = home )
                self.button3.place ( x = 0 , y = 0 )
                Label ( self.frame1 , text = 'Back' , bg = '#212122' , fg = 'white' ,
                        font = ('Future' , 12 , 'bold') ).place ( x = 3 , y = 60 )
                self.l2 = Label ( self.frame1 , text = " Mario Vs Dragon " , bg = '#212122' , fg = 'white' , border = 0 ,
                                  font = ('Comic Sans MS' , 20 , 'bold') )
                self.l2.place ( x = 995 , y = 115 )
                self.l2 = Label ( self.frame1 , text = "Mario made his debut in the classic 1981 arcade \n"
                                                       "game Donkey Kong. In this game, we will protect ourself\n"
                                                       "from Dragon's fireball. If we collide With fireball or Cactus\n"
                                                       "then game ends. In this game we have to complete 3 levels\n"
                                                       "1st level is easy , in 2nd level more cactus wall is added\n"
                                                       "And 3rd level also the same one more cactus wall add .\n  "
                                                       "Game looks easy to play but 3rd level is very tough.\n"
                                                       "So who one can played all three levels then he is the winner!!\n " , bg = '#212122' , fg = 'white' ,
                                  border = 0 ,
                                  font = ('Century' , 15 , 'bold') )


                def rate_us():
                    if userName != "":
                        import rateus
                        self.root.destroy ( )
                        self.root1 = Tk ( )
                        self.obj = rateus.Rateus ( self.root1 , userName , marioGame )
                    else:
                        messagebox.showwarning ( "Invalid" , "Please First Login the account !" )

                def how_to_play():
                    call ( ['python' , 'how to play mario vs dragon game.py'] )

                self.l2.place ( x = 800 , y = 200 )
                self.l2 = Button ( self.frame1 , text = "How to Play ?" , bg = '#212122' , fg = 'Slate Blue1' ,
                                   border = 0 ,
                                   font = ('Arial Rounded MT Bold' , 15 , 'bold') , cursor = 'hand2', command = how_to_play )
                self.l2.place ( x = 880 , y = 440 )
                Frame ( self.frame1 , width = 120 , height = 3 , bg = 'Slate Blue1' ,
                        highlightbackground = 'blue' ).place ( x = 890 ,
                                                               y = 470 )
                self.l2 = Button ( self.frame1 , text = "Rate us" , bg = '#212122' , fg = 'Slate Blue1' , border = 0 ,
                                   font = ('Arial Rounded MT Bold' , 15 , 'bold') , cursor = 'hand2' ,
                                   command = rate_us )
                self.l2.place ( x = 1250 , y = 440 )
                Frame ( self.frame1 , width = 90 , height = 3 , bg = 'Slate Blue1' ,
                        highlightbackground = 'blue' ).place (
                    x = 1255 , y = 470 )
                Label ( self.frame1 , image = self.img8 , width = 50 , bg = '#212122' ,
                        highlightbackground = 'blue' ).place (
                    x = 1350 , y = 410 )

            # -----------------------------------------------------------------------------------------------
            elif self.entry.get() in 'shooter game' or self.entry.get() in str.lower('shooter game') or self.entry.get() in str.upper('shooter game') :
                for self.f in self.frame1.winfo_children ( ):
                    self.f.destroy ( )
                shooter = which_game[1]
                def play():
                    import shooter_game
                    if userName == "":
                        messagebox.showerror ( "Invalid" , "You have to first login the  account !" )
                    else:
                        self.root.destroy ( )
                        self.root2 = Tk ( )
                        self.obj = shooter_game.Shooter ( self.root2 , username_lg , shooter)

                self.b4 = Label ( self.frame1 , image =self.img5 , bg = 'white' , border = 3)
                self.b4.place (x = 70 , y = 70 )
                self.b6 = Button ( self.frame1 , image = self.img4 , bg = 'white' , border = 0 , command = play, cursor = 'hand2' )
                self.b6.place ( x = 300 , y = 500 )
                self.b6.focus_set()
                self.l2 = Label (self.frame1 , text =" Shooter Game" , bg = '#212122' , fg = 'white' , border = 0 ,
                             font = ('Comic Sans MS' , 20 , 'bold') )
                self.l2.place ( x = 1020 , y = 110 )
                self.l2 = Label ( self.frame1 , text = "Get ready for non-stop action in our shooter game! \n"
                                             "Pick your favorite weapons and team up with friends to \n"
                                             "take down enemies in exciting battles. Whether you like \n"
                                             "sniping from a distance or getting up close with a shotgun,\n "
                                             "there's something for everyone. Play with friends or go solo in \n"
                                             "thrilling missions filled with excitement and challenges. \n"
                                             "Easy to play, hard to master – our shooter game is sure to keep \n"
                                             "you entertained for hours!", bg = '#212122' , fg = 'white' , border = 0 ,
                             font = ('Century' , 15 , 'bold') )

                self.button3 = Button ( self.frame1 , image = self.i2 , bg = '#212122' , border = -10 , command = home )
                self.button3.place ( x = 0 , y = 0 )
                Label ( self.frame1 , text = 'Back' , bg = '#212122' , fg = 'white' ,
                        font = ('Future' , 12 , 'bold') ).place ( x = 3 , y = 60 )

                def rate_us():
                    if userName != "":
                        import rateus
                        self.root.destroy ( )
                        self.root1 = Tk ( )
                        self.obj = rateus.Rateus ( self.root1 , userName , shooter )
                    else:
                        messagebox.showwarning ( "Invalid" , "Please First Login the account !" )

                def how_to_play():
                    call(['python', 'how to play shooter game.py'])


                self.l2.place ( x = 800 , y = 200 )
                self.l2 = Button( self.frame1 , text = "How to Play ?" , bg = '#212122' , fg = 'Slate Blue1' , border = 0 ,
                             font = ('Arial Rounded MT Bold' , 15 , 'bold'), cursor = 'hand2', command = how_to_play)
                self.l2.place ( x = 880 , y = 440 )
                Frame ( self.frame1 , width = 120 , height = 3 , bg = 'Slate Blue1' , highlightbackground = 'blue' ).place ( x = 890 ,
                                                                                                                y = 470 )
                self.l2 = Button ( self.frame1 , text = "Rate us" , bg = '#212122' , fg = 'Slate Blue1' , border = 0 ,
                              font = ('Arial Rounded MT Bold' , 15 , 'bold') , cursor = 'hand2', command = rate_us )
                self.l2.place ( x = 1250 , y = 440 )
                Frame ( self.frame1 , width = 90 , height = 3 , bg = 'Slate Blue1' , highlightbackground = 'blue' ).place (
                    x = 1255 ,y = 470 )
                Label ( self.frame1 , image=self.img8,width = 50  , bg = '#212122' , highlightbackground = 'blue' ).place (
                    x = 1350 ,y = 410 )


            # -----------------------------------------------------------------------------------------------

            elif self.entry.get ( ) in 'flappy bird' or self.entry.get ( ) in str.lower ('flappy bird' ) or self.entry.get ( ) in str.upper ( 'flappy bird' ):
                for self.f in self.frame1.winfo_children ( ):
                    self.f.destroy ( )
                flappy = which_game[2]
                def play():
                    import shooter_game
                    if userName == "":
                        messagebox.showerror ( "Invalid" , "You have to first login the  account !" )
                    else:
                        self.root.destroy ( )
                        self.root2 = Tk ( )
                        self.obj = shooter_game.Shooter ( self.root2 , username_lg, flappy )

                self.b4 = Label ( self.frame1 , image = self.img10 , bg = 'white' , border = 3 )
                self.b4.place ( x =70 , y = 70 )
                self.b6 = Button ( self.frame1 , image = self.img4 , bg = 'white' , border = 0 , command = play ,
                                   cursor = 'hand2' )
                self.b6.place ( x = 300 , y = 500 )
                self.b6.focus_set ( )
                self.l2 = Label ( self.frame1 , text = " Flappy Bird " , bg = '#212122' , fg = 'white' , border = 0 ,
                                  font = ('Comic Sans MS' , 20 , 'bold') )
                self.l2.place ( x = 995 , y = 110 )
                self.l2 = Label ( self.frame1 , text = "Flappy Bird is an arcade-style game where the \n"
                                                       "player takes control of a bird named Faby. \n"
                                                       "Faby persistently moves to the right, and your\n"
                                                       "task is to navigate it through pairs of pipes.\n"
                                                       " These pipes have equally sized gaps placed at \n"
                                                       "random heights. The bird automatically descends, \n"
                                                       "and you can make it ascend by tapping the touchscreen.\n"
                                                       " The objective is to fly as far as possible without \n"
                                                       "colliding with the pipes" ,
                                  bg = '#212122' ,fg= "white",border = 0 ,font = ('Century' , 15 , 'bold') )

                self.button3 = Button ( self.frame1 , image = self.i2 , bg = '#212122' , border = -10 , command = home )
                self.button3.place ( x = 0 , y = 0 )
                Label ( self.frame1 , text = 'Back' , bg = '#212122' , fg = 'white' ,
                        font = ('Future' , 12 , 'bold') ).place ( x = 3 , y = 60 )

                def rate_us():
                    if userName != "":
                        import rateus
                        self.root.destroy ( )
                        self.root1 = Tk ( )
                        self.obj = rateus.Rateus ( self.root1 , userName , flappy )
                    else:
                        messagebox.showwarning ( "Invalid" , "Please First Login the account !" )


                def how_to_play():
                    call ( ['python' , 'how to play flappy bird.py'] )

                self.l2.place ( x = 800 , y = 200 )
                self.l2 = Button ( self.frame1 , text = "How to Play ?" , bg = '#212122' , fg = 'Slate Blue1' ,
                                   border = 0 ,
                                   font = ('Arial Rounded MT Bold' , 15 , 'bold') , cursor = 'hand2' ,command = how_to_play )
                self.l2.place ( x = 880 , y = 440 )
                Frame ( self.frame1 , width = 120 , height = 3 , bg = 'Slate Blue1' ,
                        highlightbackground = 'blue' ).place ( x = 890 ,
                                                               y = 470 )
                self.l2 = Button ( self.frame1 , text = "Rate us" , bg = '#212122' , fg = 'Slate Blue1' , border = 0 ,
                                   font = ('Arial Rounded MT Bold' , 15 , 'bold') , cursor = 'hand2' ,
                                   command = rate_us )
                self.l2.place ( x = 1250 , y = 440 )
                Frame ( self.frame1 , width = 90 , height = 3 , bg = 'Slate Blue1' ,
                        highlightbackground = 'blue' ).place (
                    x = 1255 , y = 470 )
                Label ( self.frame1 , image = self.img8 , width = 50 , bg = '#212122' ,
                        highlightbackground = 'blue' ).place (
                    x = 1350 , y = 410 )
            elif self.entry.get ( ) in 'space invader' or self.entry.get ( ) in str.lower ('space invader' ) or self.entry.get ( ) in str.upper ( 'space invader' ):
                for self.f in self.frame1.winfo_children ( ):
                    self.f.destroy ( )
                space = which_game[3]



                def play():
                    import main
                    if userName == "":
                        messagebox.showerror ( "Invalid" , "You have to first login the  account !" )

                    # calling strore window and calling Store class in main.py
                    else:
                        self.root.destroy ( )
                        self.root2 = Tk ( )

                        self.obj = main.Space ( self.root2 , username_lg ,space)

                self.b4 = Label ( self.frame1 , image = self.img14 , bg = 'white' , border = 3 )
                self.b4.place ( x = 70 , y = 70 )
                self.b6 = Button ( self.frame1 , image = self.img4 , bg = 'white' , border = 0 , command = play ,
                                   cursor = 'hand2' )
                self.b6.place ( x = 300 , y = 500 )
                self.b6.focus_set ( )
                self.l2 = Label ( self.frame1 , text = " Space Invader " , bg = '#212122' , fg = 'white' , border = 0 ,
                                  font = ('Comic Sans MS' , 20 , 'bold') )
                self.l2.place ( x = 1025 , y = 115 )
                self.l2 = Label ( self.frame1 , text = "Space Invaders is a classic arcade game that was \n"
                                                       "first released in 1978. It was designed by Tomohiro \n"
                                                       "Nishikado and originally sold and manufactured by Taito in Japan.\n"
                                                       "The game was later licensed by Midway for release in North America.\n"
                                                       "The objective of Space Invaders is to control a laser cannon \n"
                                                       "that moves horizontally across the bottom of the screen and fire \n"
                                                       "at descending aliens. The aim is to shoot all of the aliens\n"
                                                       "before they reach the bottom of the screen. The aliens move \n"
                                                       "back and forth and every time they complete a row, they move \n"
                                                       "down one level. The game gets progressively faster and more \n"
                                                       "challenging as the aliens get closer to the bottom of the screen.\n" ,
                                  bg = '#212122' , fg = "white" , border = 0 , font = ('Century' , 15 , 'bold') )
                self.button3 = Button ( self.frame1 , image = self.i2 , bg = '#212122' , border = -10 , command = home )
                self.button3.place ( x = 0 , y = 0 )
                Label ( self.frame1 , text = 'Back' , bg = '#212122' , fg = 'white' ,
                        font = ('Future' , 12 , 'bold') ).place ( x = 3 , y = 60 )

                def rate_us():
                    if userName != "":
                        import rateus
                        self.root.destroy ( )
                        self.root1 = Tk ( )
                        self.obj = rateus.Rateus ( self.root1 , userName , space )
                    else:
                        messagebox.showwarning("Invalid", "Please First Login the account !")

                def how_to_play():
                    call ( ['python' , 'how to play space invader.py'] )

                self.l2.place ( x = 800 , y = 200 )
                self.l2 = Button ( self.frame1 , text = "How to Play ?" , bg = '#212122' , fg = 'Slate Blue1' ,
                                   border = 0 ,
                                   font = ('Arial Rounded MT Bold' , 15 , 'bold') , cursor = 'hand2' ,
                                   command = how_to_play )
                self.l2.place ( x = 880 , y = 480 )
                Frame ( self.frame1 , width = 120 , height = 3 , bg = 'Slate Blue1' ,
                        highlightbackground = 'blue' ).place ( x = 890 ,
                                                               y = 510 )
                self.l2 = Button ( self.frame1 , text = "Rate us" , bg = '#212122' , fg = 'Slate Blue1' , border = 0 ,
                                   font = ('Arial Rounded MT Bold' , 15 , 'bold') , cursor = 'hand2' ,
                                   command = rate_us )
                self.l2.place ( x = 1250 , y = 480 )
                Frame ( self.frame1 , width = 90 , height = 3 , bg = 'Slate Blue1' ,
                        highlightbackground = 'blue' ).place (
                    x = 1255 , y = 510 )
                Label ( self.frame1 , image = self.img8 , width = 50 , bg = '#212122' ,
                        highlightbackground = 'blue' ).place (
                    x = 1350 , y = 450 )


        def home():
                        for self.f in self.frame1.winfo_children():
                            self.f.destroy()
                        # -----------------------------------------------------------------------------------------------
                        self.ima2 = cv2.imread ( "C:/Users/sujal/PycharmProjects/new_Python_Project/images/mario1.png" )
                        self.imgr2 = cv2.resize ( self.ima2 , (310 , 173) )
                        self.img_rgb2 = cv2.cvtColor ( self.imgr2 , cv2.COLOR_BGR2RGB )
                        self.img_tk1 = ImageTk.PhotoImage ( Image.fromarray ( self.img_rgb2 ) )
                        self.la1 = (Button ( self.frame1 , image = self.img_tk1 , bg = '#212122' , border = 4 ,
                                             cursor = "hand2" , command = mario ))
                        self.la1.place ( x = 10 , y = 70 )
                        self.le1 = Label ( self.frame1 , image = self.i3 , bg = '#212122' , border = 0 )
                        self.le1.place ( x = 5 , y = 320 )

                        # -----------------------------------------------------------------------------------------------
                        self.ima3 = cv2.imread ( "C:/Users/sujal/PycharmProjects/new_Python_Project/images/bgimg.png" )
                        self.imgr3 = cv2.resize ( self.ima3 , (310 , 173) )
                        self.img_rgb3 = cv2.cvtColor ( self.imgr3 , cv2.COLOR_BGR2RGB )
                        self.img_tk2 = ImageTk.PhotoImage ( Image.fromarray ( self.img_rgb3 ) )
                        self.la2 = (Button ( self.frame1 , image = self.img_tk2 , bg = '#212122' , border = 4 ,
                                             cursor = "hand2" , command = shooter ))
                        self.la2.place ( x = 340 , y = 70 )
                        self.le2 = Label ( self.frame1 , image = self.i5 , bg = '#212122' , border = 0 )
                        self.le2.place ( x = 340 , y = 320 )

                        # -----------------------------------------------------------------------------------------------
                        self.ima4 = cv2.imread (
                            "C:/Users/sujal/PycharmProjects/new_Python_Project/images/FALPPYBIRD LOGO1.png" )
                        self.imgr4 = cv2.resize ( self.ima4 , (310 , 173) )
                        self.img_rgb4 = cv2.cvtColor ( self.imgr4 , cv2.COLOR_BGR2RGB )
                        self.img_tk3 = ImageTk.PhotoImage ( Image.fromarray ( self.img_rgb4 ) )
                        self.la3 = Button ( self.frame1 , image = self.img_tk3 , bg = '#212122' , border = 4 ,
                                            cursor = "hand2" , command = flappy )
                        self.la3.place ( x = 670 , y = 70 )
                        self.le3 = Label ( self.frame1 , image = self.i4 , bg = '#212122' , border = 0 )
                        self.le3.place ( x = 670 , y = 320 )

                        # -----------------------------------------------------------------------------------------------
                        self.la4 = Button ( self.frame1 , image = self.img13 , bg = '#212122' , border = 4 ,
                                            cursor = "hand2" , command = spaceInavder )
                        self.la4.place ( x = 1000 , y = 70 )
                        self.le4 = Label ( self.frame1 , image = self.i6 , bg = '#212122' , border = 0 )
                        self.le4.place ( x = 1000 , y = 320 )

                        Frame ( self.frame1 , width = 1 , height = 640 , bg = 'white' ).place ( x = 1330 , y = 10 )
                        self.le5 = Label ( self.frame1 , text = "Recently Played" , bg = '#212122' , fg = "white" ,
                                           border = 0 , font = ("Comic Sans MS" , 13) )
                        self.le5.place ( x = 1370 , y = 40 )
                        Frame ( self.frame1 , width = 130 , height = 2 , bg = 'white' ).place ( x = 1370 , y = 65 )

                        self.conn1 = mysql.connector.connect ( host = 'localhost' , password = 'Suj@y935974' ,
                                                               user = 'root' ,
                                                               database = 'game' )
                        self.Cursor_obj1 = self.conn1.cursor ( )
                        self.Cursor_obj1.execute (
                            f" select Recently_played, played_time from create_account where username= '{username_lg}'" ,
                            () )
                        self.file = self.Cursor_obj1.fetchone ( )
                        self.Played_Game = self.file[0]
                        self.Played_time = self.file[1]
                        self.conn1.close ( )
                        if self.Played_Game == 0:
                            self.ima = cv2.imread (
                                "C:/Users/sujal/PycharmProjects/new_Python_Project/images/mario1.png" )
                            self.imgr1 = cv2.resize ( self.ima , (160 , 90) )
                            self.img_rgb1 = cv2.cvtColor ( self.imgr1 , cv2.COLOR_BGR2RGB )
                            self.img_tk = ImageTk.PhotoImage ( Image.fromarray ( self.img_rgb1 ) )
                            self.L1 = Label ( self.frame1 , image = self.img_tk , bg = '#212122' , border = 2 )
                            self.L1.place ( x = 1355 , y = 90 )
                            self.L2 = Label ( self.frame1 ,
                                              text = f"Played Time :  {round ( self.Played_time / 60 , 2 )} MIN" ,
                                              bg = '#212122' , fg = "White" , border = 0 ,
                                              font = ("Century" , 9 , "bold") )
                            self.L2.place ( x = 1350 , y = 200 )

                        elif self.Played_Game == 1:
                            self.ima = cv2.imread (
                                "C:/Users/sujal/PycharmProjects/new_Python_Project/images/bgimg.png" )
                            self.imgr1 = cv2.resize ( self.ima , (160 , 90) )
                            self.img_rgb1 = cv2.cvtColor ( self.imgr1 , cv2.COLOR_BGR2RGB )
                            self.img_tk = ImageTk.PhotoImage ( Image.fromarray ( self.img_rgb1 ) )
                            self.L1 = Label ( self.frame1 , image = self.img_tk , bg = '#212122' , border = 2 )
                            self.L1.place ( x = 1355 , y = 90 )
                            self.L2 = Label ( self.frame1 ,
                                              text = f"Played Time :  {round ( self.Played_time / 60 , 2 )} MIN" ,
                                              bg = '#212122' , fg = "White" , border = 0 ,
                                              font = ("Century" , 9 , "bold") )
                            self.L2.place ( x = 1350 , y = 200 )

                        elif self.Played_Game == 2:
                            self.ima = cv2.imread (
                                "C:/Users/sujal/PycharmProjects/new_Python_Project/images/FALPPYBIRD LOGO1.png" )
                            self.imgr1 = cv2.resize ( self.ima , (160 , 90) )
                            self.img_rgb1 = cv2.cvtColor ( self.imgr1 , cv2.COLOR_BGR2RGB )
                            self.img_tk = ImageTk.PhotoImage ( Image.fromarray ( self.img_rgb1 ) )
                            self.L1 = Label ( self.frame1 , image = self.img_tk , bg = '#212122' , border = 2 )
                            self.L1.place ( x = 1355 , y = 90 )
                            self.L2 = Label ( self.frame1 ,
                                              text = f"Played Time :  {round ( self.Played_time / 60 , 2 )} MIN" ,
                                              bg = '#212122' , fg = "White" , border = 0 ,
                                              font = ("Century" , 9 , "bold") )
                            self.L2.place ( x = 1350 , y = 200 )

                        elif self.Played_Game == 3:
                            self.ima = cv2.imread (
                                "C:/Users/sujal/PycharmProjects/new_Python_Project/images/space invader1.png" )
                            self.imgr1 = cv2.resize ( self.ima , (160 , 90) )
                            self.img_rgb1 = cv2.cvtColor ( self.imgr1 , cv2.COLOR_BGR2RGB )
                            self.img_tk = ImageTk.PhotoImage ( Image.fromarray ( self.img_rgb1 ) )
                            self.L1 = Label ( self.frame1 , image = self.img_tk , bg = '#212122' , border = 2 )
                            self.L1.place ( x = 1355 , y = 90 )
                            self.L2 = Label ( self.frame1 ,
                                              text = f"Played Time :  {round ( self.Played_time / 60 , 2 )} MIN" ,
                                              bg = '#212122' , fg = "White" , border = 0 ,
                                              font = ("Century" , 9 , "bold") )
                            self.L2.place ( x = 1350 , y = 200 )

        # -----------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------

        # -----------------------------------------------------------------------------------------------
        def login():
            import login
            self.root.destroy ( )
            # calling strore window and calling Store class in main.py
            self.root1 = Tk ( )

            self.obj = login.LogInPage ( self.root1 , username_lg = f"{username_lg}" )

        # -----------------------------------------------------------------------------------------------
        def newAccount():
            import createAccount
            self.root.destroy ( )
            self.root1 = Tk ( )
            self.obj = createAccount.SignInPage ( self.root1 , username_lg = f"{username_lg}" )

        # -----------------------------------------------------------------------------------------------
        def profile():
            for self.f in self.frame1.winfo_children():
                self.f.destroy()
            if userName == "":

                self.button3 = Button ( self.frame1 , image = self.i2 , bg = '#212122' , border = -10 , command = home )
                self.button3.place ( x = 30 , y = 20 )
                Label ( self.frame1 , text = 'Back' , bg = '#212122' , fg = 'white' ,
                        font = ('Future' , 12 , 'bold') ).place ( x = 35 , y = 75 )
                self.l1 = Label ( self.frame1, text = 'Profile' , bg = '#212122' , fg = 'white' , border = 0 ,
                                  font = ('Futura' , 20 , 'bold') )
                self.l1.place ( x = 720 , y = 30 )
                self.b6 = Label ( self.frame1 , image = self.img6 , bg = '#212122' , fg = 'white' , border = 0 )
                self.b6.place ( x = 660 , y = 80 )
                self.entry2 = Label ( self.frame1 , text = "No User Is Signed" , width = 15 , fg = 'white' ,
                                      bg = "#212122" , border = 0 , font = ('Century' , 16 , 'bold') )
                self.entry2.place ( x = 650 , y = 300 )

            else:
        # -----------------------------------------------------------------------------------------------

                self.button3 = Button (  self.frame1, image = self.i2 , bg = '#212122' , border = -10 , command = home )
                self.button3.place ( x = 30 , y = 20 )
                Label (self.frame1, text = 'Back' , bg = '#212122' ,fg= 'white' ,font = ('Future' , 12 , 'bold') ).place ( x = 35 , y = 75 )
                self.l1 = Label ( self.frame1 ,text = 'Profile', bg = '#212122' , fg='white', border = 0, font=('Futura',20,'bold'))
                self.l1.place ( x = 325 , y = 30 )
                self.b6 = Label ( self.frame1 , image = self.img6 ,bg= '#212122',fg= 'white', border = 0 )
                self.b6.place ( x = 270 , y = 80 )
                self.entry2 = Label ( self.frame1 , text = f"{username_lg}" , width = 10 ,fg='white', bg = "#212122" , border = 0, font = ('Century', 16, 'bold') )
                self.entry2.place ( x = 295 , y = 300 )


                Frame ( self.frame1 , width = 1 , height = 550 , bg = 'white' ).place ( x = 700 , y = 40 )


                conn = mysql.connector.connect ( host = 'localhost' , password = 'Suj@y935974' , user = 'root',database = 'game' )
                Cursor_obj = conn.cursor ( )

                Cursor_obj.execute (
                    f"select userid,email,mobile_no,descrip,score_mario,score_shooter,score_flappy,score_space, rating_mario,rating_shooter,rating_flappy,rating_space from create_account where username='{userName}'" ,() )
                # global username
                username = Cursor_obj.fetchone ( )
                print(username)

                if username is None:
                    for i in range(0,12):
                        self.frame1.configure(username[i], text="None")

                self.entry2 = Label ( self.frame1 , text = f"{username[1]}" , width = 22 , fg = 'white' , bg = "#212122" ,border = 0 , font = ('Century' , 16 , 'bold') )
                self.entry2.place ( x = 220 , y = 340 )

                self.Lal1 = Label ( self.frame1 , text = f"UserId :"  , fg = 'white' , bg = "#212122" ,
                                      border = 0 , font = ('Century' , 16 , 'bold') )
                self.Lal1.place ( x = 798 , y = 80 )
                self.La2 = Label ( self.frame1 , text = f"Email :"  ,
                                      fg = 'white' , bg = "#212122" ,
                                      border = 0 , font = ('Century' , 16 , 'bold') )
                self.La2.place ( x = 800 , y = 127 )

                self.entry2 = Label ( self.frame1 , text = f"{username[0]}" , fg = 'white' ,
                                      bg = "#212122" ,
                                      border = 0 , font = ('Century' , 16 , 'bold') )
                self.entry2.place ( x = 898 , y = 80 )
                self.entry2 = Label ( self.frame1 , text = f"{username[1]}" ,
                                      fg = 'white' , bg = "#212122" ,
                                      border = 0 , font = ('Century' , 16 , 'bold') )
                self.entry2.place ( x = 890 , y = 127 )

                self.entry2 = Label ( self.frame1 , text = f"Mobile No. :" ,fg = 'white' , bg = "#212122" ,border = 0 , font = ('Century' , 16 , 'bold') )
                self.entry2.place ( x = 800 , y = 170 )

                self.La3 = Label ( self.frame1 , text = f"{username[2]}" , fg = 'white' ,
                                      bg = "#212122" , border = 0 , font = ('Century' , 16 , 'bold') )
                self.La3.place ( x = 945 , y = 170 )

                self.entry2 = Label ( self.frame1 , text = f"Game - " , width = 10 , fg = 'white' ,bg = "#212122" , border = 0 , font = ('Century' , 22 , 'bold') )
                self.entry2.place ( x = 765 , y = 280 )
                self.entry2 = Label ( self.frame1 , text = f"Mario Vs Dragon - " , width = 15 , fg = 'white' , bg = "#212122" ,
                                      border = 0 , font = ('Century' , 16 , 'bold') )
                self.entry2.place ( x = 760 , y = 370 )
                self.entry2 = Label ( self.frame1 , text = f"Shooter Game - " , width = 15 , fg = 'white' , bg = "#212122" ,
                                      border = 0 , font = ('Century' , 16 , 'bold') )
                self.entry2.place ( x = 778 , y = 410 )
                self.entry2 = Label ( self.frame1 , text = f"Flappy Bird - " , width = 15 , fg = 'white' , bg = "#212122" ,
                                      border = 0 , font = ('Century' , 16 , 'bold') )
                self.entry2.place ( x = 788 , y = 450 )
                self.entry2 = Label ( self.frame1 , text = f"Space Invader - " , width = 15 , fg = 'white' , bg = "#212122" ,
                                      border = 0 , font = ('Century' , 16 , 'bold') )
                self.entry2.place ( x = 779 , y = 490 )

                self.entry2 = Label ( self.frame1 ,image =self.img11 , fg = 'white' ,
                                      bg = "#212122" , border = 0 , font = ('Century' , 16 , 'bold') )
                self.entry2.place ( x = 1055 , y = 250 )
                self.entry2 = Label ( self.frame1 , image = self.img12 , fg = 'white' ,
                                      bg = "#212122" , border = 0 , font = ('Century' , 16 , 'bold') )
                self.entry2.place ( x = 1220 , y = 270 )
                self.entry2 = Label ( self.frame1 , image = self.img12 , fg = 'white' ,
                                      bg = "#212122" , border = 0 , font = ('Century' , 16 , 'bold') )
                self.entry2.place ( x = 1280 , y = 270 )
                self.entry2 = Label ( self.frame1 , image = self.img12 , fg = 'white' ,
                                      bg = "#212122" , border = 0 , font = ('Century' , 16 , 'bold') )
                self.entry2.place ( x = 1340 , y = 270 )

                self.size = [370,410,450,490]
                self.game = [4,5,6,7]
                self.rating = [8,9,10,11]

                for i in range(4):
                    self.entry2 = Label ( self.frame1 , text = f"{username[self.game[i]]}" , width = 18 ,
                                          fg = 'white' , bg = "#212122" , border = 0 , font = ('Century' , 16 , 'bold') )
                    self.entry2.place ( x = 985, y = self.size[i] )

                    self.entry2 = Label ( self.frame1 , text = f"{username[self.rating[i]]}" , width = 10 ,
                                          fg = 'white' , bg = "#212122" , border = 0 , font = ('Century' , 16 , 'bold') )
                    self.entry2.place ( x = 1230 , y = self.size[i] )


                conn.close ( )
                self.entry2 = Label ( self.frame1 , text = "Suggestion / \n   Comments: " , width = 15 ,
                                          fg = 'white' , bg = "#212122" , border = 0 , font = ('Century' , 16 , 'bold') )
                self.entry2.place ( x = 15 ,y=400 )
                self.entry3 = customtkinter.CTkTextbox(master=self.frame1, width=450,height = 120,bg_color="grey52", border_width= 2,font = ('Century' , 11 , 'bold'))
                self.entry3.place(x=210, y=400)
                self.entry3.insert(END,f'{username[3]}')

                def update_descrip():
                    print ( self.entry3.get ( '1.0' , END ) )
                    try:
                        con1 = mysql.connector.connect ( host = 'localhost' , password = 'Suj@y935974' , user = 'root' ,
                                                             database = 'game' )
                        Cursor_obj6 = con1.cursor ( )
                        Cursor_obj6.execute(f" update create_account set descrip = '{self.entry3.get('1.0' , END )}' where username= '{userName}'",())
                        messagebox.showinfo("Success","Your Response is submitted !\n Thank You !!")
                        con1.commit ( )
                        con1.close ( )
                    except:
                        messagebox.showerror ( "Invalid" , "Your Response is not Submitted !" )

                self.b1 = customtkinter.CTkButton ( self.frame1 , width = 34 , text = 'Submit' , text_color = "black",fg_color = "burlywood", bg_color = '#212122' ,border_spacing = 10 , font = ('Futura' , 20 ,
                                                                                  'bold') , command = update_descrip )
                self.b1.place(x=380, y=550)

                def upload():
                        self.image_path = filedialog.askopenfilename ( initialdir = os.getcwd ( ) ,
                                                            title = "Select image file" ,
                                                            filetypes = (("JPG File" , "*.jpg") ,
                                                                         ("PNG File" , "*.png"),
                                                                         ) )

                        if userName != "" and self.image_path != "":
                            connec = mysql.connector.connect ( host = 'localhost' , password = 'Suj@y935974' , user = 'root' ,
                                                                   database = 'game' )
                            Cursor_obj4 = connec.cursor ( )
                            Cursor_obj4.execute (
                                    f" update create_account set profile_photo = '{self.image_path}' where username= '{username_lg}'" , () )
                            messagebox.showinfo ( "Success" , "Profile photo is updated!\n Thank You !!" )

                            connec.commit ( )
                            connec.close ( )


                            self.ima = cv2.imread ( self.image_path )
                            self.image = cv2.resize (self.ima , (190 , 190) )
                            # Convert the image to RGB format
                            self.image_rgb = cv2.cvtColor (self. image , cv2.COLOR_BGR2RGB )
                            # Convert the image to a format that can be displayed by Tkinter
                            self.image_tk = ImageTk.PhotoImage ( Image.fromarray (self.image_rgb ) )
                            # Update the image on the button
                            self.b6.config(image=self.image_tk)
                            self.b6 = self.image_tk


                self.b6 = Button ( self.frame1 , image = self.img6 , bg = '#212122' , fg = 'white' , border = 0, command = upload )
                self.b6.place ( x = 270 , y = 80 )

            if userName != "":
                self.conn1 = mysql.connector.connect ( host = 'localhost' , password = 'Suj@y935974' , user = 'root' ,database = 'game' )
                self.Cursor_obj1 = self.conn1.cursor ( )
                self.Cursor_obj1.execute (
                f" select profile_photo from create_account where username= '{username_lg}'" , () )
                self.filename2 = self.Cursor_obj1.fetchone()
                if self.filename2[0] is not None:

                    self.fn13 = self.filename2[0]

                    self.ima = cv2.imread ( self.fn13)
                    self.image = cv2.resize ( self.ima , (190 , 190) )
                    self.image1 = cv2.resize(self.ima, (75, 75))
                    # Convert the image to RGB format
                    self.image_rgb = cv2.cvtColor ( self.image , cv2.COLOR_BGR2RGB )
                    # Convert the image to a format that can be displayed by Tkinter
                    self.image_tk = ImageTk.PhotoImage ( Image.fromarray ( self.image_rgb ) )

                    self.image_rgb1 = cv2.cvtColor ( self.image1 , cv2.COLOR_BGR2RGB )
                    # Convert the image to a format that can be displayed by Tkinter
                    self.image_tk1 = ImageTk.PhotoImage ( Image.fromarray ( self.image_rgb1 ) )

                    # Update the image on the button
                    self.b6.config ( image = self.image_tk )
                    self.b6 = self.image_tk
                    self.b3 = Button ( self.frame , image = self.image_tk1, bg = 'white' , border = 0 , command = profile )
                    self.b3.place ( x = 1410 , y = 2 )

                self.conn1.close ( )



        # -----------------------------------------------------------------------------------------------

        self.b1 = customtkinter.CTkButton(self.frame, width=36, text='Login', bg_color='white',border_spacing=10, font=('Futura',20,
                                                                                            'bold'), command=login)
        self.b1.place(x=1100, y=34)
        self.b2 = customtkinter.CTkButton(self.frame, width=36, text='New Account', bg_color='white',border_spacing=10, font=('Futura',20,
                                                                                             'bold'), command=newAccount)
        self.b2.place(x=1220, y=34)

        self.b3 = Button(self.frame, image = self.img2, bg = 'white',border = 0, command=profile)
        self.b3.place(x=1410, y=2)

        self.b5 =Button(self.frame,image =self.img1,  width=35, height = 35, border = 0, fg='white',bg='white', command = check_Which_You_want_to_play, cursor = 'hand2')
        self.b5.place(x=975, y=37)
        if userName != "":
            self.fn13 = None
            self.conn1 = mysql.connector.connect ( host = 'localhost' , password = 'Suj@y935974' , user = 'root' ,
                                                   database = 'game' )
            self.Cursor_obj1 = self.conn1.cursor ( )
            self.Cursor_obj1.execute (
                f" select profile_photo from create_account where username= '{username_lg}'" , () )
            self.filename2 = self.Cursor_obj1.fetchone ( )
            if self.filename2[0] is not None:
                self.fn13 = self.filename2[0]

                self.ima = cv2.imread ( self.fn13 )
                self.image1 = cv2.resize ( self.ima , (75 , 75) )

                self.image_rgb1 = cv2.cvtColor ( self.image1 , cv2.COLOR_BGR2RGB )
                # Convert the image to a format that can be displayed by Tkinter
                self.image_tk1 = ImageTk.PhotoImage ( Image.fromarray ( self.image_rgb1 ) )

                self.b3.config ( image = self.image_tk1 )
                self.b3 = self.image_tk1
            self.conn1.close ( )
     # -----------------------------------------------------------------------------------------------
     # -----------------------------------------------------------------------------------------------
if __name__=='__main__':
    root1 = Tk ( )
    for f in root1.winfo_children ( ):
        f.destroy ( )
    obj = Game( root1, username_lg="sujay9420")
    root1.mainloop ( )
     # -----------------------------------------------------------------------------------------------
     # -----------------------------------------------------------------------------------------------




