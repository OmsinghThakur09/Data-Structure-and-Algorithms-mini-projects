from datetime import datetime


class Song:
    # represents song with metadata
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration  # in seconds
        self.play_count = 0
        self.added_date = datetime.now()

    def __str__(self):
        mins = self.duration // 60
        secs = self.duration % 60
        return f"{self.title} | {self.artist} | ({mins}:{secs:02d})"

    def __repr__(self):
        return f"song('{self.title}'-'{self.artist})"


class Node:
    def __init__(self, song, next=None, prev=None):
        self.song = song
        self.next = next
        self.prev = prev


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, song):
        new_node = Node(song)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def insert_at_beginnings(self, song):
        new_node = Node(song)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size +=1

    def insert_at_index(self, song, index):
        if index <= 0:
            self.insert_at_beginnings(song)
            return

        if index >= self.size:
            self.insert_at_end()
            return

        new_node = Node(song)
        current = self.head

        for _ in range(index):
            current = current.next

        new_node.next = current
        new_node.prev = current.prev
        current.prev.next = new_node
        current.prev = new_node

    def delete_by_title(self, title):
        if self.is_empty():
            return False

        current = self.head

        while current:
            if current.song.title.lower() == title.lower():

                if current == self.head:
                    self.head = current.next
                    if current.next:
                        self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.next.prev = current.prev
                    current.prev.next = current.next

                self.size -= 1
                return True

            current = current.next
        return False

    def search(self, title):
        current = self.head
        pos = 0

        while current:
            if current.song.title.lower() == title.lower():
                return current, pos

            current = current.next
            pos += 1
        return None, -1

    def get_at_pos(self, pos):
        if pos < 0 or pos >= self.size:
            return None

        current = self.head
        for _ in range(pos):
            current = current.next

        return current

    def to_list(self):
        songs = []
        current = self.head
        while current:
            songs.append(current.song)
            current = current.next

        return songs

    def reverse(self):
        if self.is_empty() or self.head == self.tail:
            return
        current = self.head
        self.head, self.tail = self.tail, self.head

        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev

        return self.head

