from Playlist import Playlist
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    print("\n" + "-" * 70)
    print("🎵 MUSIC PLAYLIST MANAGER".center(70))
    print("-" * 70)
    print("  1.  Add Song")
    print("  2.  Remove Song")
    print("  3.  Display Playlist")
    print("  4.  Play/Resume")
    print("  5.  Pause")
    print("  6.  Next Song")
    print("  7.  Previous Song")
    print("  8.  Jump to Song")
    print("  9.  Current Song")
    print(" 10.  Shuffle Playlist")
    print(" 11.  Reverse Playlist")
    print(" 12.  Sort Playlist")
    print(" 13.  Toggle Loop Mode")
    print(" 14.  Search Song")
    print(" 15.  Show History")
    print(" 16.  Show Statistics")
    print(" 17.  Load Sample Playlist")
    print("  0.  Exit")
    print("-" * 70)


def load_sample_playlist(playlist):
    sample_songs = [
        ("Sway", "Michael Buble", 742),
        ("Just the two of us", "Bill Withers, Grover Washington, Jr.", 489),
        ("I Think They Call This Love", "Matthew lfield", 554),
        ("Hotel California", "Eagles", 391),
        ("Toms Diner", "Suzanne Vega", 286),
        ("Stairway to Heaven", "Led Zeppelin", 482),
        ("Scary Gary", "Kito Shoma", 916),
        ("Smells Like Teen Spirit", "Nirvana", 301),
        ("Billie Jean", "Michael Jackson", 294),
        ("Sweet Child O' Mine", "Guns N' Roses", 356),
    ]
    print("\nLoading sample playlist....")
    for title, artist, duration in sample_songs:
        playlist.add_song(title, artist, duration)
    print(f"\nLoaded {len(sample_songs)} sample songs!")


def get_int_input(prompt, min_val=None, max_val=None):
    # to get integer input
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Please enter a value >= {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Please enter a value <= {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number!")


def interactive_menu():
    # main interactive CLI loop
    print("\n🎵 Welcome to Music Playlist Manager!")
    name = input("\nEnter playlist name (press Enter for 'My Playlist'): ").strip()
    playlist = Playlist(name if name else "My Playlist")

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\n--- Add New Song ---")
            title = input("song title: ").strip()
            if not title:
                print("title cant be empty!")
                continue
            artist = input("Artist name: ").strip()
            if not artist:
                print("Artist cannot be empty!")
                continue
            duration = get_int_input("Duration (in seconds): ", min_val=1)
            playlist.add_song(title,artist,duration)

        elif choice == "2":
            if playlist.songs.is_empty():
                print("Playlist is empty!")
            else:
                title = input("\nEnter song title to remove: ").strip()
                playlist.remove_song(title)

        elif choice == "3":
            playlist.show_playlist()

        elif choice == "4":
            playlist.play()

        elif choice == "5":
            playlist.pause()

        elif choice == "6":
            playlist.next_song()

        elif choice == "7":
            playlist.previous_song()

        elif choice == "8":
            if playlist.songs.is_empty():
                print("Playlist is empty!")
            else:
                pos = get_int_input(f"\nEnter position (1-{playlist.songs.size}): ",
                                    1, playlist.songs.size)
                playlist.jump_to(pos)

        elif choice == "9":
            playlist.playing_song()

        elif choice == "10":
            playlist.shuffle()

        elif choice == "11":
            playlist.reverse_playlist()

        elif choice == "12":
            key = input("\nEnter sort by(title, artist, duration): ")
            playlist.sort(key)

        elif choice == "13":
            playlist.toggle_loop()

        elif choice == "14":
            title = input("\n Enter song title to search: ")
            playlist.search_song(title)

        elif choice == "15":
            playlist.show_history()

        elif choice == "16":
            playlist.stats()

        elif choice == "17":
            if playlist.songs.size > 0:
                confirm = input("\nThis will add songs to your current playlist. Continue? (y/n): ")
                if confirm.lower() != 'y':
                    continue
            load_sample_playlist(playlist)

        elif choice == "0":
            print("\n Thank you for using Music Playlist Manager!")
            print("🎵 Keep the music alive!")
            break

        else:
            print("❌ Invalid choice! Please enter a number from the menu.")

        input("\nPress Enter to continue.....")


if __name__ == "__main__":
    interactive_menu()
