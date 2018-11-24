from contextlib import closing

class RefrigeratorRaider:

    def open(self):
        print('Open the Refrigerator')

    def close(self):
        print('Closing the Refrigerator')

    def TakeFood(self, food):
        print('Find {}'.format(food))
        if food == 'Sweets':
            raise RuntimeError('Diabetes Warning:')
        print('Taking {}'.format(food))

def raid(food):
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.TakeFood('Sweets')

raid('Sweets')