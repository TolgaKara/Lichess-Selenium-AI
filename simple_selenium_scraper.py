from selenium import webdriver
from time import sleep
import os
import pyperclip
import re
import pandas as pd

# Connect to chrome Webdriver
driver = webdriver.Chrome('chromedriver.exe')

# Size and other metrics
#driver.fullscreen_window()

# Call the URL
driver.get('http://www.lichess.org')

"""
 Get us a decent Move to get adventage of the Opponent Player
"""
def best_move_suggestor():
    pass

"""
Move
    Player_Move
    Oponent_Move
Turn
Player_Color
Opponent_Color
"""
def sel_crawler_data():
    player_color = input('Black (B) or White (w)')
    opponent_color = None
    moves_dataset = None
    moves_list = None

    move = []
    

    if str(player_color).lower() == 'w' or str(player_color).lower() == 'white':
        player_color = "White"
        opponent_color = "Black"
        print("Opponent_Color: ", opponent_color)
        moves_dataset = pd.read_csv('white_move.csv')
        moves_dataset.columns = ['index','moves']
        moves_list = moves_dataset['moves'].tolist()
    elif str(player_color).lower() == 'b' or str(player_color).lower() == 'black':
        player_color = "Black"
        opponent_color = "White"
        print("Opponent_Color: ", opponent_color)
        moves_dataset = pd.read_csv('black_move.csv')
        moves_dataset.columns = ['index','moves']
        moves_list = moves_dataset['moves'].tolist()
    else:
        print("The input you have given is wrong, Please try again")
        sel_crawler_data()
    sleep(3)
    while True:
        sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("game is running")
        all_data = driver.find_element_by_css_selector('div.moves')
        all_data_str = all_data.text
        
        turn = [int(s) for s in all_data_str.split() if s.isdigit()]

        move = [str(i) for i in all_data_str.split() if i not in str(turn)]

        moves_done_list = ' '.join(move)
            
        best_sequences = [str_.split() for str_ in moves_list]
        moves_sequence = moves_done_list.split()
        count = len(moves_sequence)
        suggestions = []

        for best_sequence in best_sequences:
            if moves_sequence == best_sequence[:count]:
                if len(best_sequence) > count:
                    suggestions.append(best_sequence[count])

        print('Turn: ', turn)
        print('Move: ', move)
        print("Move_done:"+ moves_done_list)
        for suggestion in suggestions:
            print('Suggestion: ',suggestion)
        

        


def create_match():
    # as
    driver.find_element_by_css_selector('a.fat.config_friend').click()
    sleep(3)
    driver.find_element_by_css_selector('button.button.random').click()

    # Get the Current URL and save it into the clipboard
    current_url = driver.current_url
    pyperclip.copy(current_url)

    # Ask the User if the Game has started
    game_ready = input('Has the Game started? ')

    if game_ready != "":
        sel_crawler_data()



def requested_match():

    sended_url = input('URL: ')
    driver.get(sended_url)

    sleep(5)

    sel_crawler_data()

    
    

def ai_match():
    driver.find_element_by_css_selector('a.fat.config_ai').click()
    sleep(3)
    driver.find_element_by_css_selector('button.button.random').click()
    
    sleep(5)
    sel_crawler_data()

"""
Its an menu which follow is certain direction in the option of selecting a Match
Structure:
    ----- Lichess Menu -----
    ------------------------
    (1) Create Match and wait until its start
    (2) Getting a Invitation Link
    (3) Play against Computer (AI)
    (0) Quit Programm

return menu_number

"""
def menu():
    # Menu Output
    print('''
    --- Lichess Menu ---
    ------------------------
    (1) Create Match and wait until its start
    (2) Getting a Invitation Link
    (3) Play against Computer (AI)
    (0) Quit Programm''')

    # User input what Lichess Action should be run
    menu_number = input('\nSelection: ')

    if menu_number is '1':
        print("""
        (1) Create Match and wait until its start [is running]
        """)
        create_match()
    elif menu_number is '2':
        print("""
        (2) Getting a Invitation Link [is running]
        """)
        requested_match()
    elif menu_number is '3':
        print("""
        (3) Play against Computer (AI) [is running]
        """)
        ai_match()
    elif menu_number is '0':
        print("""
        (0) Quit Programm
        """)
        exit()
    else:
        print("""
        It seems like the input you are given is wrong.
        Please try it again!
        """)
        menu()
        



if __name__ == "__main__":
    menu()

    sleep(5)
    driver.close()

