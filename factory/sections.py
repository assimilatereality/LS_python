class SectionsFactory:
    def __init__(self, tile):
        self.name = tile
        self.tile = tile
        self.tiles = self._build()

    def _build(self):
        sections = {
            'name': self.name,
            'tileType': 'HEADER',
            'configured': 'true',
            'bounds': {
                'top': 0,
                'left': 0,
                'width': 418,
                'height': 38
            },
            'tileFilter': {}
        }

tile_sections = [
    'Service Dashboard_#_1',
    '5 min.'
]


for i in tile_sections:
    section_header = SectionsFactory(i)

    print(section_header)
