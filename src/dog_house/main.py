from dog_house.db import phoebe_1
from logic        import phoebe_2


id_1 = id(phoebe_1)
id_2 = id(phoebe_2)

if id_1 != id_2:
    print(f'The enums are not singletons: {id_1} != {id_2}')
else:
    print('They are the same object.')

