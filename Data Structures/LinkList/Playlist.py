import random
from doubly_linkedlist import DoublyLinkedList, Song


class Playlist:

    def __init__(self, name='My Playlist'):
        self.name = name
        self.songs = DoublyLinkedList()  # one list for storing songs
        self.current_song = None
        self.is_playing = False
        self.loop_mode = False
        self.recently_played = DoublyLinkedList()  # another for storing played songs, for keeping track of played songs
        self.max_history = 10

    def add_song(self, title, artist, duration):  # to add song into the playlist
        song = Song(title, artist, duration)
        self.songs.insert_at_end(song)

        if self.songs.size == 1:
            self.current_song = self.songs.head

        print(f'{song} Added')

    def next_song(self):  # to select next song
        if not self.current_song:
            print('No song is currently selected!')
            return
        if self.current_song.next:
            self.current_song = self.current_song.next
            print(f"next song: {self.current_song.song}")
        elif self.loop_mode:
            self.current_song = self.songs.head
            print('Looping back to start.....')
            print(f"next song: {self.current_song.song}")
        else:
            print('end of the playlist reached!')
            return

    def remove_song(self, title):  # to remove song from the playlist
        if self.current_song and self.current_song.song.title == title:
            self.next_song()

        if self.songs.delete_by_title(title):
            print(f'Removed {title}!')
            return True
        else:
            print(f'song {title} not found!')
            return False

    def show_playlist(self):
        if self.songs.is_empty():
            print('Playlist is empty!')
            return
        print(f"\n{'-' * 60}")
        print(f"Playlist: {self.name}, {self.songs.size} songs")
        print(f"{'-' * 60}")

        current = self.songs.head
        pos = 1
        while current:
            marker = "▶️ " if current == self.current_song else "   "
            print(f"{marker}{pos}. {current.song}")
            current = current.next
            pos += 1

        print(f"{'-' * 60}")

    def add_to_history(self, song):  # function to add played song into recently played list
        self.recently_played.insert_at_beginnings(song)

        if self.recently_played.size > self.max_history:
            if self.recently_played.tail:
                self.recently_played.tail = self.recently_played.tail.prev
                if self.recently_played.tail:
                    self.recently_played.tail.next = None
                self.recently_played.size -= 1

    def show_history(self):
        if self.recently_played.is_empty():
            print('Play songs to show here!')
            return
        print(f"\n{'-' * 60}")
        print(f"Recently played: Last {min(self.max_history, self.recently_played.size)}")
        print(f"{'-' * 60}")

        current = self.recently_played.head
        pos = 1
        while current:
            print(f"{pos}. {current.song} played {current.song.play_count} times")
            current = current.next
            pos += 1

        print(f"{'-' * 60}")

    def play(self):  # to play a song from the playlist
        if self.songs.is_empty():
            print('Playlist is empty!')
            return

        if not self.current_song:
            self.current_song = self.songs.head

        self.is_playing = True
        self.add_to_history(self.current_song.song)
        self.current_song.song.play_count += 1

        print(f"Now playing: {self.current_song.song}")

    def pause(self):
        if not self.current_song:
            self.current_song = self.songs.head
        if self.is_playing:
            self.is_playing = False
            print("Playback paused")
        else:
            print("Already paused!")

    def previous_song(self):  # to select previous song of selected song from the playlist
        if not self.current_song:
            print(f"No song is currently playing!")
            return

        if self.current_song.prev:
            self.current_song = self.current_song.prev
        elif self.loop_mode:
            self.current_song = self.songs.tail
            print("Looping to end.....")
        else:
            print("Already at the beginning!")
            return

        print(f"Previous: {self.current_song.song}")

    def jump_to(self, pos):  # to select and play specific positioned song in the list
        node = self.songs.get_at_pos(pos - 1)
        if node:
            self.current_song = node
            print(f"current song: {node.song}")

    def playing_song(self):  # function to show current playing song
        if self.current_song:
            status = "playing" if self.is_playing else "paused"
            print(f"{status}: {self.current_song.song}")
            return

        else:
            print("No song is selected!")

    def shuffle(self):  # function to shuffle the playlist
        if self.songs.size < 2:
            print("Need minimum 2 songs to shuffle!")
            return

        songs_list = self.songs.to_list()
        random.shuffle(songs_list)

        self.songs = DoublyLinkedList()  # creating new list
        for song in songs_list:
            self.songs.insert_at_end(song)

        self.current_song = self.songs.head
        print(f"Playlist shuffled!")

    def toggle_loop(self):  # function to on or off loop mode
        self.loop_mode = not self.loop_mode
        status = "on" if self.loop_mode else "off"
        print(f"toggle mode: {status}")

    def reverse_playlist(self):  # function to reverse the playlist
        if self.songs.size < 2:
            print("Need minimum 2 songs to reverse!")
            return

        self.songs.head = self.songs.reverse()
        self.current_song = self.songs.head
        print("playlist is reversed!")

    def search_song(self, title):
        node, pos = self.songs.search(title)
        if node:
            print(f"found {node.song} at {pos}")
            return True
        else:
            print(f"'{title}' named song not found in playlist!")
            return False

    def sort(self, val='title'):
        if self.songs.is_empty():
            print("playlist is empty!")
            return

        song_list = self.songs.to_list()
        if val.lower() == 'title':
            sorted_song_list = sorted(song_list, key=lambda song: song.title.lower().strip())
            print("playlist is now sorted by title!")

        elif val.lower() == "artist":
            sorted_song_list = sorted(song_list, key=lambda song: song.artist.lower().strip())
            print("playlist is now sorted by artist!")

        elif val.lower() == "duration":
            sorted_song_list = sorted(song_list, key=lambda song: song.duration)
            print("playlist is now sorted by duration!")

        else:
            print(f"Invalid sort option Use 'title', 'artist', or 'duration'")
            return

        self.songs = DoublyLinkedList()
        for song in sorted_song_list:
            self.songs.insert_at_end(song)
        self.current_song = self.songs.head

    def stats(self):  # function to display statistics of the playlist (metadata of playlist)
        if self.songs.is_empty():
            print("playlist is empty!")
            return

        total_duration = sum(song.duration for song in self.songs.to_list())
        total_plays = sum(song.play_count for song in self.songs.to_list())

        hours = total_duration // 3600
        mins = (total_duration % 3600) // 60
        secs = total_duration % 60

        print(f"\n{'-' * 60}")
        print(f" Playlist Statistics: {self.name}")
        print(f"{'-' * 60}")
        print(f"  Total Songs: {self.songs.size}")
        print(f"  Total Duration: {hours}h {mins}m {secs}s")
        print(f"  Total Plays: {total_plays}")
        print(f"  Loop Mode: {'ON' if self.loop_mode else 'OFF'}")
        print(f"{'-' * 60}")


if __name__ == "__main__":
    print("\n🎵 Music Playlist Manager\n")

    # Create playlist
    playlist = Playlist("My Awesome Mix")

    # Add songs
    print("--- Adding Songs ---")
    playlist.add_song("Sway", "Michael Buble", 354)
    playlist.add_song("Just the two of us", "Bill Withers, Grover Washington, Jr.", 482)
    playlist.add_song("I Think They Call This Love", "Matthew lfield", 391)
    playlist.add_song("Toms Diner", "Suzanne Vega", 183)
    playlist.add_song("Scary Gary", "Kito Shoma", 431)

    # Display playlist
    playlist.show_playlist()

    # Navigation test
    print("\n--- Navigation Test ---")
    playlist.playing_song()
    playlist.play()
    playlist.playing_song()
    playlist.pause()
    playlist.playing_song()
    # playlist.stats()
    playlist.next_song()
    playlist.play()
    playlist.next_song()
    playlist.play()
    playlist.previous_song()
    playlist.play()
    # playlist.playing_song()

    # Jump test
    # print("\n--- Jump Test ---")
    # playlist.jump_to(5)
    # playlist.play()
    # playlist.playing_song()
    #
    # Loop mode test
    # print("\n--- Loop Mode Test ---")
    # playlist.toggle_loop()
    # playlist.next_song()
    # playlist.next_song()
    # playlist.next_song()
    # playlist.next_song()
    # playlist.next_song()
    # print(playlist.songs.head.song)
    #
    # Shuffle test
    # print("\n--- Shuffle Test ---")
    # playlist.shuffle()
    # playlist.show_playlist()
    #
    # Reverse test
    # print("\n--- Reverse Test ---")
    # playlist.reverse_playlist()
    # print(playlist.songs.head.song)
    # playlist.show_playlist()
    #
    # History test
    print("\n--- Play History ---")
    playlist.show_history()
    #
    # Search test
    # print("\n--- Search Test ---")
    # playlist.search_song("Sway")
    # playlist.search_song("Unknown Song")
    #
    # Remove test
    print("\n--- Remove Test ---")
    playlist.remove_song("Scary gary")
    playlist.show_playlist()
    #
    # Statistics
    playlist.sort('artist')
    playlist.show_playlist()
    playlist.stats()