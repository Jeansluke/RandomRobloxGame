import requests
import random
import tkinter as tk

#hey jeans here im gonna add hashtags to give you info about what the stuff does

def get_random_roblox_game():
    url = 'https://games.roblox.com/v1/games/list?sortOrder=Random' #This gets the random roblox games
    games_list = []

    try:
        for _ in range(5):  # This does 5 trys to get games and if it did not get that in 5 trys it will send a error code 
            response = requests.get(url)
            if response.status_code == 200:
                games = response.json()['games']
                games_list.extend(games)
            else:
                print(f"Failed to fetch data. Status code: {response.status_code}") #here is where the error goes when it did 5 trys it should pop up in the console
    except requests.RequestException as e:
        print(f"Request error: {e}")

    return games_list

def show_random_game_info():
    games = get_random_roblox_game() #this gets a random roblox game from the list
    random_game = random.choice(games) if games else None 

    if random_game:
        window = tk.Toplevel(root)
        window.title("Random Roblox Game Info") #this opens that gui when you click get random roblox game

        game_name_label = tk.Label(window, text=f"Name: {random_game.get('name', 'N/A')}") #this adds the name of the game to the gui
        game_name_label.pack()

        place_id = random_game.get('placeId') #this does the placeid in the gui
        if place_id:
            game_link_label = tk.Label(window, text=f"Play Game", fg="blue", cursor="hand2") 
            game_link_label.pack()
            game_link_label.bind("<Button-1>", lambda e: open_game_link(place_id)) #this sends that the player has clicked the play button to send to the other command

        price = random_game.get('price')
        if price:
            price_label = tk.Label(window, text=f"Price: {price}") #this gives the price of the game
            price_label.pack()

        creator_info_label = tk.Label(window, text=f"Creator: {random_game.get('creatorName', 'N/A')} ({random_game.get('creatorType', 'N/A')})") #and this get the creator/group of the game
        creator_info_label.pack()

    else:
        print("Failed to fetch a random Roblox game.") #and this prints error in the console if something went wrong

def open_game_link(place_id):
    import webbrowser
    url = f"https://www.roblox.com/games/{place_id}" 
    webbrowser.open_new_tab(url) #and this gets that you clicked the play button via "game_link_label.bind("<Button-1>", lambda e: open_game_link(place_id))" and opens in your webrowser

root = tk.Tk()
root.title("Random Roblox Game")
root.geometry("250x50")

button = tk.Button(root, text="Get Random Roblox Game", command=show_random_game_info)
button.pack()

root.mainloop()

#thats basicly how the code works do with what you want with the code and if anything happens its not my fault and i will not be fixing bugs for you its now out of my control. -jeansluke