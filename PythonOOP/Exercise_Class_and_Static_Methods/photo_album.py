from math import ceil


class PhotoAlbum:
    SYMBOLS = "-"
    DASHES_COUNT = 11

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for page in range(self.pages):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                slot = len(self.photos[page])
                return f"{label} photo added successfully on page {page + 1} slot {slot}"

        return f"No more free slots"

    def display(self):

        result = [
            self.DASHES_COUNT * self.SYMBOLS
        ]

        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append(self.DASHES_COUNT * self.SYMBOLS)

        return "\n".join(result)

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
