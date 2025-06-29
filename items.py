from world import WorldItem, Weapon, Potion
from const import *

town_signpost = WorldItem(
    "A wooden signpost with three directions; " \
    "North: Black Forest, " \
    "East: General Store, " \
    "West: Duke's Arms Tavern",
    "A signpost with three directions",
    takeable = False,
    takeable_desc = "You cannot take the sign, it is bolted to the ground",
    edible = False,
    edible_desc = "You are not a wood worm"
)

statue = WorldItem(
    "A large stone statue of an Elf holding a bow in a majestic pose. " \
    "The plaque reads; ", #TODO add flavour text
    "A statue of a figure holding a bow",
    False,
    "You are not that strong",
    False,
    "You cannot eat stone"
)

red_potion = Potion(
    "A small glass bottle filled with an iridescant red liquid",
    "red potion",
    RED
)
dagger = Weapon(
    "A small blade with a leather wrapped hilt.",
    "dagger",
    damage = 5
)
fist = Weapon(
    "Your fist",
    "fist",
    damage = 1
)


items = {
    "town signpost": town_signpost,
    "statue": statue,
    "red potion": red_potion,
    "dagger": dagger,
    "fist": fist
}

