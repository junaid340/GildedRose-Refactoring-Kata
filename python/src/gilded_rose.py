# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    # Extracted method to update quality of items
    def update_quality(self):
        for item in self.items:
            self.update_item(item)
    
    # Extracted method to update normal items (Pre-existing logic)
    def update_normal(self, item):    
        if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            if item.quality > 0:
                if item.name != "Sulfuras, Hand of Ragnaros":
                    item.quality = item.quality - 1
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.name != "Aged Brie":
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > 0:
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
    
    # New method to update conjured items
    def update_conjured(self, item):
        # Conjured items degrade in quality twice as fast as normal items
        if item.sell_in > 0:
                item.quality = item.quality - 2
        else:
            item.quality = item.quality - 4
        
        # Ensure quality never goes negative
        if item.quality < 0: 
            item.quality = 0
        
        item.sell_in = item.sell_in - 1
    
    # New method to update items, which will call the appropriate update method based on the item name
    def update_item(self, item):
        # Check if the item is a conjured
        if item.name.startswith("Conjured"):
            self.update_conjured(item)
        else:
            self.update_normal(item)
                    
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
