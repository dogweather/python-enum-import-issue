from dog_house.db import phoebe_1
from logic        import phoebe_2


if id(phoebe_1) != id(phoebe_2):
    print(f'The enums are not singletons: {phoebe_1}/{id(phoebe_1)} vs. {phoebe_2}/{id(phoebe_2)}')
    print(f'phoebe_1 == phoebe_2: {phoebe_1 == phoebe_2}')
    print(f'phoebe_1 is phoebe_2: {phoebe_1 is phoebe_2}')
else:
    print('They are the same object.')
