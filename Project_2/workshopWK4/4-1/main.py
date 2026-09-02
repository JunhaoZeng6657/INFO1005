from resource_pool import ResourcePool
from summoning_ritual import SummonRitual

resources = ResourcePool(
    100,
    100,
    100,
    100,
    100
)

print(resources)

ritual_1 = SummonRitual(
    "Raise Skeleton",
    "Skeleton Warrior",
    30,
    10,
    20,
    7,
    25,
    0,
    0
    )

ritual_2 = SummonRitual(
    "Raise Zombie",
    "Zombie Brute",
    50,
    15,
    30,
    10,
    0,
    20,
    0
)

print(ritual_1)
print(ritual_2)

selected_ritual = ritual_1
print("Selected:")
print(selected_ritual)

if selected_ritual.can_perform(resources):
    print("The ritual can be performed.")
else:
    print("The ritual cannot be performed.")

undead_1 = selected_ritual.perform_ritual(
    resources,
    "undead_001"
    )

print(resources)

if undead_1 is not None:
    print(undead_1)

if undead_1 is not None:
    undead_1.level_up()
    print(undead_1)

if undead_1 is not None:
    undead_1.level_up()
    print(undead_1)