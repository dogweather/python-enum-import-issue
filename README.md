A minimal reproducible demo that Enums aren't always singletons.
This can silently cause subtle bugs because `is` and `==` don't
work as expected.

