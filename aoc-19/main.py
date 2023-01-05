import os
from collections.abc import Hashable
from pathlib import Path

from cache import Cache
from config import DATAFILE, MAX_TIME
from factory import make_robots
from puzzle import Blueprint, Geode, read  # noqa
from resources import Resources, Value  # noqa


# for use as a key at dictionaries
def reskey(blueprint: Blueprint, resources: Resources) -> Hashable:
    store = tuple(
        min(x, y)
        for x, y in zip(
            (
                blueprint.max_spend_ore * resources.time,
                blueprint.max_spend_clay * resources.time,
                blueprint.max_spend_obsidian * resources.time,
                resources.geode,
            ),
            resources.store,
        )
    )
    return (resources.time, resources.robots, store)


def calc_value(r: Resources) -> Value:
    return r.value


# def calc_value(r: Resources) -> Geode:
#     return r.value[0]


def working(blueprint: Blueprint, resources: Resources) -> Resources:

    global cache

    if resources.time <= 0:
        return resources

    key = reskey(blueprint, resources)
    if (res := cache[key]) is not None:
        return res

    robots = make_robots(blueprint, resources)
    max_valuable = max(
        (working(blueprint, r) for r in robots),
        key=calc_value,
        default=resources,
    )

    cache[key] = max_valuable

    return max_valuable


if __name__ == "__main__":

    from config import PART

    os.chdir(Path(__file__).parent)

    blueprints = read(DATAFILE)

    if PART == 2:
        blueprints = {k: bp for k, bp in blueprints.items() if k in (1, 2, 3)}

    quality_level = 0
    restul_part2 = 1

    cache: Cache[Resources] = Cache()

    for (n_blueprint, blueprint) in blueprints.items():

        cache.clear()

        initial_resource = Resources(MAX_TIME)
        initial_resource.active_trace()
        max_valuable = working(blueprint, initial_resource)
        geodes, _, _, _ = max_valuable.value

        print(f"Max Valuable: {max_valuable}")
        print(cache.cache_info)
        max_valuable.show()

        print(f"Blueprint {n_blueprint} can open {geodes} geodes")

        if PART == 1:
            quality_level += n_blueprint * geodes
        else:
            restul_part2 *= geodes

    if PART == 1:
        print("Quality Level:", quality_level)
    else:
        print("Result:", restul_part2)
