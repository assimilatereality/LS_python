class SectionsFactory:
    def __init__(self, tile, period=''):
        self.name = tile
        self.tile = tile
        self.period = period
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
        return sections
