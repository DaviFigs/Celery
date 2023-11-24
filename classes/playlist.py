class PLaylist:
    name = 'New playlist'
    gender = 'None'
    songs = []

    def __init__(self, name, gender) -> None:
        self.name = name
        self.gender = gender

    def get_all_songs(self):
        songs = self.songs
        return {f'{self.name} songs': self.songs}
    