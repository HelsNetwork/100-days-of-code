import subprocess 
import os 
import re
from collections import namedtuple 
import configparser


def linux_psswds(verbose=1):
    network_path = "/etc/NetworkManager/system-connections/"
    fields = ["ssid", "auth-alg", "key-mgmt", "psk"]
    Profile = namedtuple("Profile", [f.replace("-", "_")for f in fields])
    profiles = []
    for file in os.listdir(network_path):
        data = { k.replace("-", "_"): None for k in fields}
        config = configparser.ConfigParser()
        config.read(os.path.join(network_path, file))
        for _, section in config.items():
            for k, v in section.items():
                if k in fields:
                    data[k.replace("-", "_")] = v 
        profile = Profile(**data)
        if verbose >= 1:
            linux_profile(profile)
        profiles.append(profile)
    return profiles
