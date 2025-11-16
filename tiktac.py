import tkinter

def set_tile(row, column):
    global cur_player
    
    if (game_over):
        return
    
    if board[row][column]["text"] !="":
        return
    board[row][column]["text"] = cur_player
    if cur_player == player:
        cur_player=player1
    else:
        cur_player=player
    label["text"]=cur_player+"'s turn"
    
            
    check_winner()
def check_winner():
    global turns,game_over
    turns+=1
    
    for row in range(3):
        if(board[row][0]["text"]==board[row][1]["text"]==board[row][2]["text"]
           and board[row][0]["text"]!=""):
            label.config(text=board[row][0]["text"]+" is the winner!",foreground=color_red)
            for column in range(3):
                board[row][column].config(foreground=color_red,background=color_black)
            game_over=True
            return 
         
    for column in range(3):
     if(board[0][column]["text"]==board[1][column]["text"]==board[2][column]["text"]
       and board[0][column]["text"]!=""):
        label.config(text=board[0][column]["text"]+" is the winner!",foreground=color_red)
        for row in range(3):
            board[row][column].config(foreground=color_red,background=color_black)
        game_over=True
        return
    if(board[0][0]["text"]==board[1][1]["text"]==board[2][2]["text"]
       and board[0][0]["text"]!=""):
        label.config(text=board[0][0]["text"]+" is the winner!",foreground=color_red)
        for i in range(3):
            board[i][i].config(foreground=color_red,background=color_black)
        game_over=True
        return
    if(board[0][2]["text"]==board[1][1]["text"]==board[2][0]["text"]
       and board [0][2]["text"]!=""):
        board[0][2].config(foregrounnd-color_red,background=color_black)
        board[1][1].config(foreground=color_red,background=color_black)
        board[2][0].config(foreground=color_red,background=color_black)
        
        game_over=True
        return
    if turns==9:
        game_over=True
        label.config(text="It's a tie!",foreground=color_red)
        return
  
    
        

        
    

def new_game():
    global turns,game_over
    
    turns=0
    game_over=False
    
    label["text"]=cur_player+"'s turn"
    
    for row in range(3):
        for column in range(3):
           
            board[row][column].config(text="",foreground="black",background=color_black) 

player = "X"
player1 = "O"

cur_player = player
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


color_red = "#e75480"
color_black="#3A3535"
color_gray = "#d3d3d3"

turns=0
game_over=False

window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
frame.pack()

label = tkinter.Label(
    frame,
    text="Player X's turn",
    font=("italic", 30),
    background=color_gray,
    foreground="black",
    anchor="center",
    width=15
)
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(
            frame,
            text="",
            font=("italic", 60),
            background=color_black,
            foreground="blue",
            width=4,
            height=1,
            command=lambda row=row, column=column: set_tile(row, column)
        )
        board[row][column].grid(row=row + 1, column=column)

button = tkinter.Button(
    frame,
    text="Restart",
    font=("italic", 20),
    background=color_gray,
    foreground="black",
    command=new_game
)
button.grid(row=4, column=0, columnspan=3, sticky="we")

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()
