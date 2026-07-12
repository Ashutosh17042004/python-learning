"""Q14. Playlist Manager

Create

1 Add Song

2 Remove Song

3 Reverse Playlist

4 Sort Playlist

5 Exit"""

playlist = []
option = ["Add Song", "Remove Song", "Reverse Playlist", "Sort playlist", "Exit"]

while True:
    selected_option = input(f"Select Option {option} : ").title()
    match selected_option:
        case "Add Song":
            song_name = input("Enter song name : ").title()
            if song_name:
                playlist.append(song_name)
            else:
                print("Song name cannot be empty!!!\nPlease enter song name.")
        case "Remove Song":
            song_name = input("Enter song name : ").title()
            if song_name in playlist:
                playlist.remove(song_name)
                print(f"{song_name} song removed successfully")
            else:
                print("Song not in playist!!!\nTry again ")

        case "Reverse Playlist":
            if len(playlist) > 0:
                print(f"original playlist : {playlist}")
                playlist.reverse()
                print(f"Reversed playlist {playlist}")
            else:
                print("Sorry playlist is empty!!!")

        case "Sort playlist":
            if len(playlist) > 0:
                print(f"original playlist : {playlist}")
                playlist.sort()
                print(f"Sort playlist : {playlist}")
            else:
                print("Sorry playlist is empty!!!")
        case "Exit":
            print("Thanks for using Playlist Manager!")
            break
        case _:
            print("Invalid option!!!\nTry again")
