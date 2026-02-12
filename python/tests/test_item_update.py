# -*- coding: utf-8 -*-
import unittest

from src.gilded_rose import update_item
from gilded_rose import Item

class GildedRoseTest(unittest.TestCase):
    def test_update_normal_item_before_sell_date(self):
        item = Item(name='normal item', sell_in=1, quality=10)
        update_item(item)

        self.assertEqual(item.quality, 9)
        self.assertEqual(item.sell_in, 0)
    
    def test_update_normal_item_after_sell_date(self):
        item = Item(name='normal item', sell_in=0, quality=10)
        update_item(item)

        self.assertEqual(item.quality, 8)
        self.assertEqual(item.sell_in, -1)
        
if __name__ == '__main__':
    unittest.main()
