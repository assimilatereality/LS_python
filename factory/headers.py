import json
# from ___ import ___

def _generate_tile_name(tile):
    tile_type = tile
    return tile_type
  #  return f'tile-{tile_type}'

class TileFactory:
    def __init__(self, tile, period=''):
        self.name = _generate_tile_name(tile)
        self.tile = tile
        self.period = period
        self.tiles = self._build()

    def _build(self):
        return {
            'tiles': [
                {
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
            ]
        }

if __name__ == "__main__":
    tile_period = [
        {
            'Service Dashboard_#_1': '',
            '5 min.': ''
        }
    ]

    for i in tile_period:
        for tile, period in i.items():
            tile_row = TileFactory(tile, period)
            print(tile_row)

            with open(f'{_generate_tile_name(tile)}.json', 'w') as outfile:
                json.dump(tile_row.tiles, outfile, sort_keys=False, indent=2)