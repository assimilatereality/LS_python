import json
from sections_bkup import SectionsFactory

class DashBoardModule:

    def __init__(self, name, bounds=None):

        if bounds is None:
            self.bounds = {'top': 1, 'left': 1, 'width': 32, 'height': 38}
        self._tiles = []
        self._name = name
        self.bounds['top']  = 3

    def set_name(self,x):
        self._name = x

    def get_name(self):
        return self._name

    def get_bounds(self):
        return self.bounds['top']

    def add_section_headers(self):
        self._tiles.append(
            SectionsFactory(
                self._name).tiles
        )


    def build(self):
        return {
            'tiles': self._tiles
        }

dashbd_name = 'Service Dashboard_#_1'
ary = ['5 min.', '2 hrs.', '24 hrs', 'Today', '7 days', '30 days']

if __name__ == "__main__":
    dashboard_module = DashBoardModule(dashbd_name)
    print(dashboard_module.get_name())
    dashboard_module.add_section_headers()
    for i in ary:
        dashboard_module.set_name(i)
        print(dashboard_module.get_name())
        print(dashboard_module.get_bounds())
        dashboard_module.add_section_headers()

    with open('main.json', 'w') as outfile:
        json.dump(dashboard_module.build(), outfile, sort_keys=False, indent=2
                      )
