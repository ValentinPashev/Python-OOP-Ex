from typing import List
from project import Album
from project import Song


class Band:
    def __init__(self, name: str) -> None:
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)

        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name:str) -> str:
        try:
            album_to_remove = next(filter(lambda a: a.name == album_name, self.albums))
        except StopIteration:
            return f"Album {self.name} is not found."

        if album_to_remove.publish:
            return "Album has been published. It cannot be removed."

        self.albums.remove(album_to_remove)

        return f"Album {album_name} has been removed."

    def details(self) -> str:
        albums_details = "\n".join(a.details() for a in self.albums)
        return f"Band {self.name}\n" \
               f"{albums_details}"


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())