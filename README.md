A minimal reproducible demo that Enums aren't always singletons.
This facts silently causes subtle bugs because `is` and `==` don't
work as expected.

Tested with Python 3.12.1

To run the demo:

```bash
python src/dog_house/main.py
```

Output:

```
The enums are not singletons: Dog.PHOEBE/4307352272 vs. Dog.PHOEBE/4307841440
phoebe_1 == phoebe_2: False
phoebe_1 is phoebe_2: False
```
