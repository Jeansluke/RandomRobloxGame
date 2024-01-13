import requests
import random
import tkinter as tk

def get_random_roblox_game():
    url = 'https://games.roblox.com/v1/games/list?sortOrder=Random'
    games_list = []

    try:
        for _ in range(5):  # Making 5 requests to get more games
            response = requests.get(url)
            if response.status_code == 200:
                games = response.json()['games']
                games_list.extend(games)
            else:
                print(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request error: {e}")

    return games_list

def show_random_game_info():
    games = get_random_roblox_game()
    random_game = random.choice(games) if games else None

    if random_game:
        window = tk.Toplevel(root)
        window.title("Random Roblox Game Info")

        game_name_label = tk.Label(window, text=f"Name: {random_game.get('name', 'N/A')}")
        game_name_label.pack()

        place_id = random_game.get('placeId')
        if place_id:
            game_link_label = tk.Label(window, text=f"Play Game", fg="blue", cursor="hand2")
            game_link_label.pack()
            game_link_label.bind("<Button-1>", lambda e: open_game_link(place_id))

        price = random_game.get('price')
        if price:
            price_label = tk.Label(window, text=f"Price: {price}")
            price_label.pack()

        creator_info_label = tk.Label(window, text=f"Creator: {random_game.get('creatorName', 'N/A')} ({random_game.get('creatorType', 'N/A')})")
        creator_info_label.pack()

    else:
        print("Failed to fetch a random Roblox game.")

def open_game_link(place_id):
    import webbrowser
    url = f"https://www.roblox.com/games/{place_id}"
    webbrowser.open_new_tab(url)

root = tk.Tk()
root.title("Random Roblox Game")
root.geometry("250x50")

button = tk.Button(root, text="Get Random Roblox Game", command=show_random_game_info)
button.pack()

root.mainloop()
