from tkinter import *

import random

root = Tk()
root.title("Rock, Paper, Scissor Game")
width = 700
height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#99ff99")

comp_score = 0
player_score = 0

def score_window():
    window_score = Tk()
    window_score.title("Scores")
    width = 570
    height = 520
    screen_width = window_score.winfo_screenwidth()
    screen_height = window_score.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window_score.geometry("%dx%d+%d+%d" % (width, height, x, y))
    window_score.resizable(0, 0)
    window_score.config(bg="#99ff99")

def save_window():
    global e1
    window_save = Tk()
    window_save.title("Save")
    width = 370
    height = 120
    screen_width = window_save.winfo_screenwidth()
    screen_height = window_save.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window_save.geometry("%dx%d+%d+%d" % (width, height, x, y))
    window_save.resizable(0, 0)
    window_save.config(bg="#99ff99")

    lbl_player_name = Label(window_save,text="Player Name: ")
    lbl_player_name.place(x = 30, y = 50)
    lbl_player_name.config(bg="#99ff99")
    e1 = Entry(window_save)
    e1.place(x = 130, y = 50)
    enter = Button(window_save, text="Save", command=save_player_name)
    enter.place(x = 280, y = 45)

def save_player_name():
    global e1, comp_score, player_score
    player_name = e1.get()
    print(e1.get())
    print(player_score, comp_score)

    


#================================IMAGES========================================
blank_img=PhotoImage(file="images/blank.png")
player_rock=PhotoImage(file="images/player_rock.png")
sm_player_rock=player_rock.subsample(3, 3)
player_paper=PhotoImage(file="images/player_paper.png")
sm_player_paper=player_paper.subsample(3, 3)
player_scissor=PhotoImage(file="images/player_scissor.png")
sm_player_scissor= player_scissor.subsample(3, 3)
com_rock=PhotoImage(file="images/com_rock.png")
com_paper=PhotoImage(file="images/com_paper.png")
com_scissor=PhotoImage(file="images/com_scissor.png")



#===============================METHODS========================================
def Rock():
    player_choice = 1
    player_img.configure(image=player_rock)
    MatchProcess(player_choice)
 
def Paper():
    player_choice = 2
    player_img.configure(image=player_paper)
    MatchProcess(player_choice)
    
def Scissor():
    player_choice = 3
    player_img.configure(image=player_scissor)
    MatchProcess(player_choice)

def MatchProcess(player_choice):
    global comp_score, player_score
    com_choice = random.randint(1,3)
    if com_choice == 1:
        comp_img.configure(image=com_rock)

    elif com_choice == 2:
        comp_img.configure(image=com_paper)
        
    elif com_choice == 3:
        comp_img.configure(image=com_scissor)
    
    if com_choice == player_choice:
        lbl_status.config(text="Game Tie")

    elif abs(com_choice - player_choice) == 1:
        if com_choice > player_choice:
            lbl_status.config(text="Computer Wins")
            comp_score += 1
            lbl_comp_score.config(text=comp_score)
        else:
            lbl_status.config(text="Player Wins")
            player_score += 1
            lbl_player_score.config(text=player_score)

    else:
        if com_choice < player_choice:
            lbl_status.config(text="Computer Wins")
            comp_score += 1
            lbl_comp_score.config(text=comp_score)
        else:
            lbl_status.config(text="Player Wins")
            player_score += 1
            lbl_player_score.config(text=player_score)
    

def ExitApp():
    root.destroy()
    exit()

#===============================LABEL WIDGET=========================================
player_img = Label(root,image=blank_img)
comp_img = Label(root,image=blank_img)
lbl_player = Label(root,text="PLAYER")
lbl_player.grid(row=1, column=1)
lbl_player.config(bg="#99ff99")
lbl_computer = Label(root,text="COMPUTER")
lbl_computer.grid(row=1, column=3)
lbl_computer.config(bg="#99ff99")
lbl_status=Label(root, text="", font=('arial', 8))
lbl_status.config(bg="#99ff99")
lbl_status.grid(row=3, column=2)
lbl_player_score=Label(root, text="0")
lbl_player_score.config(bg="#99ff99")
lbl_player_score.grid(row=3, column=1)
lbl_comp_score=Label(root, text="0")
lbl_comp_score.config(bg="#99ff99")
lbl_comp_score.grid(row=3, column=3)
player_img.grid(row=2,column=1, padx=30, pady=20)
comp_img.grid(row=2,column=3, pady=20)
lbl_player_name = Label(root,text="Made by Manjunath, Amit & Pratham")
lbl_player_name.grid(row=5, column=2)



#===============================BUTTON WIDGET===================================
rock = Button(root, image=sm_player_rock, command=Rock)
paper = Button(root, image=sm_player_paper, command=Paper)
scissor = Button(root, image=sm_player_scissor, command=Scissor)
score = Button(root, text="Score", command=score_window)
save = Button(root, text="Save", command=save_window)
rock.grid(row=4,column=1, pady=30)
paper.grid(row=4,column=2, pady=30)
scissor.grid(row=4,column=3, pady=30)
score.grid(row=5, column=1)
save.grid(row=5, column=3)


#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
