from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from smac.env.starcraft2.maps import smac_maps

# 自行注册的地图参数
from smac.env.starcraft2.maps import user_maps


def get_map_params(map_name):
    # map_param_registry = smac_maps.get_smac_map_registry()
    map_param_registry = user_maps.get_smac_map_registry()
    return map_param_registry[map_name]
