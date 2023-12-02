import heapq
import re
from copy import copy
from dataclasses import dataclass
from functools import cache


@dataclass
class State:
    minute: int
    ore_bots: int
    clay_bots: int
    obs_bots: int
    geo_bots: int
    ore: int
    clay: int
    obs: int
    geo: int

    # True if we want to explore this state first
    def __lt__(self: "State", other: "State"):
        return not (
            self.minute < other.minute
            or self.geo_bots > other.geo_bots
            or self.geo > other.geo
            or self.obs_bots > other.obs_bots
            or self.obs > other.obs
            or self.clay_bots > other.clay_bots
            or self.clay > other.clay
            or self.ore_bots > other.ore_bots
            or self.ore > other.ore
        )

    def __hash__(self):
        return tuple(value for value in self.__dict__.values()).__hash__()

    def advance(self):
        self.minute += 1
        self.ore += self.ore_bots
        self.clay += self.clay_bots
        self.obs += self.obs_bots
        self.geo += self.geo_bots

    def buy_ore_bot(self, ore_req):
        if self.ore >= ore_req:
            dupe = copy(self)
            dupe.ore_bots += 1
            dupe.ore -= ore_req
            return dupe

    def buy_clay_bot(self, ore_req):
        if self.ore >= ore_req:
            dupe = copy(self)
            dupe.clay_bots += 1
            dupe.ore -= ore_req
            return dupe

    def buy_obs_bot(self, ore_req, clay_req):
        if self.ore >= ore_req and self.clay >= clay_req:
            dupe = copy(self)
            dupe.obs_bots += 1
            dupe.ore -= ore_req
            dupe.clay -= clay_req
            return dupe

    def buy_geo_bot(self, ore_req, obs_req):
        if self.ore >= ore_req and self.obs >= obs_req:
            dupe = copy(self)
            dupe.geo_bots += 1
            dupe.ore -= ore_req
            dupe.obs -= obs_req
            return dupe


@cache
def get_full_count(o_o, c_o, b_o, b_c, g_o, g_b):
    to_visit = [State(0, 1, 0, 0, 0, 0, 0, 0, 0)]
    visited_states = set()
    max_geodes = 0
    ore_cap = max(o_o, c_o, b_o, g_o) * 3
    clay_cap = b_c * 3
    obs_cap = g_b * 3

    while to_visit:
        curr_state = heapq.heappop(to_visit)
        visited_states.add(curr_state)
        curr_state.advance()
        print(curr_state.minute, max_geodes)
        if curr_state.minute == 24:
            max_geodes = max(max_geodes, curr_state.geo)
        elif curr_state.geo + (2 * curr_state.geo_bots + 1) * (24 - curr_state.minute) < max_geodes:
            continue
        elif ore_adv := curr_state.buy_geo_bot(g_o, g_b):
            heapq.heappush(to_visit, ore_adv) if ore_adv not in visited_states else None
        else:
            to_add = []
            if obs_adv := curr_state.buy_obs_bot(b_o, b_c):
                to_add.append(obs_adv)
            if clay_adv := curr_state.buy_clay_bot(c_o):
                to_add.append(clay_adv)
            if obs_adv := curr_state.buy_ore_bot(o_o):
                to_add.append(obs_adv)
            curr_state.ore = min(curr_state.ore, ore_cap)
            curr_state.clay = min(curr_state.clay, clay_cap)
            curr_state.obs = min(curr_state.obs, obs_cap)
            to_add.append(curr_state)
            for adder in to_add:
                if adder not in visited_states:
                    heapq.heappush(to_visit, adder)
    return max_geodes


def get_geode_count(filename: str):
    blueprints = []
    with open(filename) as file:
        while next_line := file.readline().strip():
            o_o, c_o, b_o, b_c, g_o, g_b = [int(resource.split(" ")[0]) for resource in re.findall(r"\d ore|\d clay|\d obsidian", next_line)]
            blueprints.append(get_full_count(o_o, c_o, b_o, b_c, g_o, g_b))
    print(blueprints)


if __name__ == "__main__":
    get_geode_count("input0.txt")
    # get_geode_count("input1.txt")
