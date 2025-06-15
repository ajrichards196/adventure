from world import WorldItem, Weapon, Potion

town_signpost = WorldItem(
    "A wooden signpost with three directions; " \
    "North: Black Forest, " \
    "East: General Store, " \
    "West: Duke's Arms Tavern",
    "A signpost with three directions",
    False,
    "You cannot take the sign, it is bolted to the ground",
    False,
    "You are not a wood worm"
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

items = {
    "town signpost": town_signpost,
    "statue": statue
}

