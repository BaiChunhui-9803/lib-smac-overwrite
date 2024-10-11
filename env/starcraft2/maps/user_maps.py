from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from pysc2.maps import lib


class USERMap(lib.Map):
    directory = "PyMARL_Maps"
    # download = "https://github.com/oxwhirl/smac#smac-maps"
    players = 2
    step_mul = 10
    game_steps_per_episode = 0


map_param_registry = {
    "MarineMicro_MvsM_4": {
        "n_agents": 4,
        "n_enemies": 4,
        "limit": 60,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
    "MarineMicro_MvsM_4_2": {
        "n_agents": 4,
        "n_enemies": 4,
        "limit": 60,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
}


def get_smac_map_registry():
    return map_param_registry


for name in map_param_registry.keys():
    globals()[name] = type(name, (USERMap,), dict(filename=name))
