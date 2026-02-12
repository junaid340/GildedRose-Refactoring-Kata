# -*- coding: utf-8 -*-
import unittest

from src.gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    # test for normal items before sell date
    def test_update_normal_item_before_sell_date(self):
        item = Item(name='normal item', sell_in=1, quality=10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_item(item)

        self.assertEqual(item.quality, 9)
        self.assertEqual(item.sell_in, 0)
    
    # test for normal items after sell date
    def test_update_normal_item_after_sell_date(self):
        item = Item(name='normal item', sell_in=0, quality=10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_item(item)

        self.assertEqual(item.quality, 8)
        self.assertEqual(item.sell_in, -1)
    
    # test for conjured items before sell date
    def test_update_conjured_items_before_sell_date(self):
        item = Item(name='Conjured item', sell_in=1, quality=10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_item(item)

        self.assertEqual(item.quality, 8)
        self.assertEqual(item.sell_in, 0)
    
    # test for conjured items after sell date
    def test_update_conjured_items_after_sell_date(self):
        item = Item(name='Conjured item', sell_in=0, quality=10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_item(item)

        self.assertEqual(item.quality, 6)
        self.assertEqual(item.sell_in, -1)
    
    # test for conjured items quality never negative
    def test_update_conjured_items_quality_never_negative(self):
        item = Item(name='Conjured item', sell_in=0, quality=0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_item(item)

        self.assertEqual(0, item.quality)
        self.assertEqual(-1, item.sell_in)
        
if __name__ == '__main__':
    unittest.main()
