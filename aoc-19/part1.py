import os
from pathlib import Path

from cache import Cache
from factory import make_robots
from puzzle import Blueprint, max_time, read
from resources import Resources, Robots, Time, Value


def calc_value(r: Resources) -> Value:
    return r.value


def calc_timevalue(r: Resources) -> tuple[Time, Value]:
    return (r.time, r.value)


def calc_timerobots(r: Resources) -> tuple[Time, Value]:
    return (r.time, r.robots)


def key_storerobots(r: Resources) -> tuple[Value, Robots]:
    return (r.store, r.robots)


def working(blueprint: Blueprint, resources: Resources) -> Resources:

    global cache

    if resources.time <= 0:
        return resources

    # print(resources)

    key = resources.key()
    if (res := cache[key]) is not None:
        return res

    # max_valuable = max(
    #     (working(blueprint, r) for r in make_robots(blueprint, resources)),
    #     key=calc_value,
    #     default=resources,
    # )

    # cache[key] = max_valuable

    robots = make_robots(blueprint, resources)
    max_valuable = max(
        (working(blueprint, r) for r in robots),
        key=calc_value,
        default=resources,
    )

    cache[key] = max_valuable

    return max_valuable

    expand = [resources]

    finally_resources = []
    seen = set()  # type: ignore
    max_valuable = resources
    while len(expand) > 0:

        robots = make_robots(blueprint, max_valuable)

        expand.sort(key=calc_timevalue)
        max_valuable = expand.pop()
        if (max_valuable.store, max_valuable.robots) in seen:
            continue
        seen.add((max_valuable.store, max_valuable.robots))

        robots = make_robots(blueprint, max_valuable)
        if not robots:
            finally_resources.append(max_valuable)
        else:
            news = {(r.store, r.robots) for r in robots} - seen
            expand.extend(r for r in robots if (r.store, r.robots) in news)
            seen |= news

            print(f"Expand {len(expand)}, Seen {len(seen)} {max_valuable}")

    max_valuable = max(finally_resources, key=calc_value)

    while True:
        robots = make_robots(blueprint, max_valuable)
        if not robots:
            break
        max_valuable = max(robots, key=calc_value)

    # expand.sort(key=lambda r: (r.time, r.value))
    # max_valuable = max(expand, key=lambda r: (r.time, r.value))

    # if max_valuable.robots_geode > 0:
    #     finally_resources.append(max_valuable)
    #     break

    # robots = make_robots(blueprint, max_valuable)
    # if not robots:
    #     break

    # expand = robots

    # max_valuable = max(finally_resources, key=calc_value)

    # print(f"Rem.Time: {max_valuable.time}", cache.cache_info)
    print(max_valuable, "Value:", max_valuable.value)
    # input("Press...")

    # while True:

    #     robot = make_robot_geode(blueprint, max_valuable)

    #     print(max_valuable, "Value:", max_valuable.value)
    #     print(robot, "Value:", max_valuable.value)
    #     # input("Press...")

    #     if robot is None:
    #         break

    #     max_valuable = robot

    # print(f"Rem.Time: {max_valuable.time}", cache.cache_info)
    # print(max_valuable, "Value:", max_valuable.value)
    # print(key, cache[key])
    # max_valuable.show()
    # input("Waiting...")
    # if len(max_valuable.trace) != time_max - remain + 1:
    #     print(remain, key, len(max_valuable.trace))
    #     max_valuable.show()
    #     raise IndexError

    return max_valuable


if __name__ == "__main__":

    os.chdir(Path(__file__).parent)

    TRAINING = False
    blueprints = read("data-training.txt" if TRAINING else "data.txt")

    quality_level = 0

    cache: Cache[Resources] = Cache()

    for (n_blueprint, blueprint) in blueprints.items():

        # if n_blueprint != 1:
        #     continue

        cache.clear()

        # resources = {Resources()}
        # alt_resources = set()
        max_valuable = working(blueprint, Resources(max_time))
        geodes, _, _, _ = max_valuable.value

        # # reduce
        # robots = {r.robots for r in alt_resources}
        # value_partial = partial(value, time_max - t)
        # resources = {
        #     max(
        #         (r for r in alt_resources if r.robots == robot),
        #         key=value_partial,
        #     )
        #     for robot in robots
        # }

        # print(len(resources))

        # for r in sorted(resources, key=value_partial):
        #     print(f"{t:2}", value_partial(r), r)
        # input("Press key...")

        # max_geodes = max(r.geode for r in resources)

        print(f"Max Valuable: {geodes}")
        # max_valuable.show()
        print(f"Blueprint {n_blueprint} can open {geodes} geodes")

        quality_level += n_blueprint * geodes

    print("Quality Level:", quality_level)
