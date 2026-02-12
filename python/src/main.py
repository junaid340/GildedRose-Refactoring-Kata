import sys

from .gilded_rose import *
from .db import *

# Refactored from texttest_fixture.py to a new file to separate concerns and make it easier to manage items in the future
def main():
    print("OMGHAI!")
    items = get_items()

    days = 2
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("") 
        GildedRose(items).update_quality()

if __name__ == "__main__":
    main()
