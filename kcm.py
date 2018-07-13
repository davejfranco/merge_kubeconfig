#!/usr/bin/env python
import os
import sys
import yaml


def yaml_to_dict(yaml_file):
    """Reads yaml from file and parse to dictionary"""
    with open(yaml_file) as stream:
        try:
            d = yaml.load(stream)
        except yaml.YAMLError as err:
            print(err)
            os._exit(1)
    return d

def merge_config(configs):
    """merge all kubeconfig in dictionary format into one"""
    kubeconfig = {
        "apiVersion": "v1", 
        "clusters":[], 
        "contexts": [], 
        "current-context": "",
        "kind": "Config", 
        "preferences": {}, 
        "users": []
    }
    for config in configs:
        [kubeconfig['clusters'].append(cluster) for cluster in config['clusters']]
        [kubeconfig['contexts'].append(context) for context in config['contexts']]
        [kubeconfig['users'].append(user) for user in config['users']]
    return kubeconfig

def dict_to_yaml_file(file_dest, config):
    """write config into yaml format"""
    with open(file_dest, 'w') as outfile:
        yaml.dump(config, outfile, default_flow_style=False)


if __name__ == "__main__":
    
    configs = []
    for config in sys.argv[1:]:
        configs.append(yaml_to_dict(config))

    merged = merge_config(configs)
    try:
        dict_to_yaml_file(os.getcwd()+"/"+"mkubeconfig", merged)
    except Exception as err:
        print(err)
        os._exit(1)

    
    
        

