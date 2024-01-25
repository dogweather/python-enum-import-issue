A small demo in which Python Enums aren't singletons.
This causes subtle bugs because `is` and `==` don't
work as expected.

This demo refers to the `Dog.PHOEBE` `Enum` twice. These
references turn out to be two separate instances. The code's
imports aren't the cleanest. But imports like these are
common when tools help add them, or in projects with many
developers of different skill levels.

Tested with Python 3.12.1

To run the demo:

```bash
export PYTHONPATH=src
python src/dog_house/main.py
```

Output:

```
The enums are not singletons: Dog.PHOEBE/4307352272 vs. Dog.PHOEBE/4307841440
phoebe_1 == phoebe_2: False
phoebe_1 is phoebe_2: False
```

---

The issue seems to be when a module (here, `db.py`) is imported in different ways
such as absolute vs. relative. Python seems to consider these different modules.
[This S.O. post](https://stackoverflow.com/questions/40371360/imported-enum-class-is-not-comparing-equal-to-itself/40371452) seems to be right.

## The three files in the demo

### db.py

```python
from enum import Enum


class Dog(Enum):
    PHOEBE = 'Phoebe'
    MARU   = 'Maru'

phoebe_1 = Dog.PHOEBE
```

### logic.py

```python
from db import Dog


phoebe_2 = Dog.PHOEBE
```

### main.py

```python
from dog_house.db import phoebe_1
from logic        import phoebe_2


if id(phoebe_1) != id(phoebe_2):
    print(f'The enums are not singletons: {phoebe_1}/{id(phoebe_1)} vs. {phoebe_2}/{id(phoebe_2)}')
    print(f'phoebe_1 == phoebe_2: {phoebe_1 == phoebe_2}')
    print(f'phoebe_1 is phoebe_2: {phoebe_1 is phoebe_2}')
else:
    print('They are the same object.')
```
