from world import *
from const import *
from items import items
from events import *

bob=Player('Bob', 'dwarf', 25, 100, 75, 20)

town_square = WorldRoom(
    "Town Square",
    "A wide open space with a statue in the centre and a sign post in front of it.\n" \
    "It seems eerily quiet.",
    "A wide open space",
    # [NORTH, EAST, WEST],
    {NORTH: BLACK_FOREST, EAST: GENERAL_STORE, WEST: TAVERN},
    ["town signpost", "statue"]
)

black_forest = WorldRoom(
    "Black Forest",
    "The infamous Black Forest, a single winding path goes as far as you can see.",
    "A wooded area",
    {EAST: "dungeon", WEST: "castle"},
    ["apple", "mushroom"]
)

general_store = WorldRoom(
    "General Store",
    "A small, cramped store. The shopkeeper stands behind a wooden counter.",
    "A small building with a sign hanging above the door",
    {WEST: TOWN_SQUARE},
    event = GeneralStoreEvent("lets go shopping", player=bob, items=['potion'])
    
)

tavern = WorldRoom(
    "The Duck's Arms Tavern",
    "A cosy tavern that has seen better days.",
    "A small building with a sign hanging above the door",
    {EAST: TOWN_SQUARE}

)

rooms = {
    TOWN_SQUARE: town_square,
    BLACK_FOREST: black_forest,
    GENERAL_STORE: general_store,
    TAVERN: tavern
}

