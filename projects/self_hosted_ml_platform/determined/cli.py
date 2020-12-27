import os
import docker

DETERMINED_VERSION = '0.13.10'
DETERMINED_MASTER_NODE_IMAGE = 'determinedai/determined-master:{version}'.format(version=DETERMINED_VERSION)
DETERMINED_CONFIG_PATH = '/etc/determined/master.yaml'

client = docker.from_env()


def run_master_node():
    print('Run master node')
    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(script_dir, 'config.yaml')
    vol_args = dict()
    config_vol_arg = dict()
    config_vol_arg['bind'] = DETERMINED_CONFIG_PATH
    vol_args[config_path] = config_vol_arg
    client.containers.run(DETERMINED_MASTER_NODE_IMAGE, detach=True, volumes=vol_args)

if __name__ == '__main__':
    run_master_node()