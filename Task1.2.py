
gadgets = [
    ("Explosive Batarangs", 3, True),
    ("Batarangs", 5, True),
    ("Smoke Pellets", 0, False),
    ("Tear Gas Grenades", 2, True),
    ("Night Vision Goggles", 1, True),
    ("Batclaw", 0, False),
    ("Grapple Gun", 3, True),
    ("Batsignal", 0, False),
    ("Utility Belt", 1, True),
    ("Batmobile Tires", 4, True)
]


def sort_key(gadget):
    product_name, quantity, in_stock = gadget
    return (not in_stock, -quantity, product_name)


sorted_gadgets = sorted(gadgets, key=sort_key)


for gadget in sorted_gadgets:
    print(gadget)