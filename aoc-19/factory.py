from puzzle import Blueprint
from resources import Resources


def make_robot_ore(
    blueprint: Blueprint, resources: Resources
) -> Resources | None:

    if blueprint.max_spend_ore <= resources.robots_ore:
        # no need more ore-collecting robots
        return None

    cost = blueprint.cost_robot_ore
    time = resources.time_cost(cost)

    return (
        None
        if time is None
        else resources.produce(time + 1).make_robot("ore", cost)
    )


def make_robot_clay(
    blueprint: Blueprint, resources: Resources
) -> Resources | None:

    if blueprint.max_spend_clay <= resources.robots_clay:
        # no need more clay-collecting robots
        return None

    cost = blueprint.cost_robot_clay
    time = resources.time_cost(cost)

    return (
        None
        if time is None
        else resources.produce(time + 1).make_robot("clay", cost)
    )


def make_robot_obsidian(
    blueprint: Blueprint, resources: Resources
) -> Resources | None:

    if blueprint.max_spend_obsidian <= resources.robots_obsidian:
        # no need more obsidian-collecting robots
        return None

    cost = blueprint.cost_robot_obsidian
    time = resources.time_cost(cost)

    return (
        None
        if time is None
        else resources.produce(time + 1).make_robot("obsidian", cost)
    )


def make_robot_geode(
    blueprint: Blueprint, resources: Resources
) -> Resources | None:

    cost = blueprint.cost_robot_geode
    time = resources.time_cost(cost)

    return (
        None
        if time is None
        else resources.produce(time + 1).make_robot("geode", cost)
    )


def make_robots(blueprint: Blueprint, resources: Resources) -> list[Resources]:

    new_robots = [
        x
        for x in (
            make_robot_geode(blueprint, resources),
            make_robot_obsidian(blueprint, resources),
            make_robot_clay(blueprint, resources),
            make_robot_ore(blueprint, resources),
        )
        if x is not None
    ]

    return new_robots
