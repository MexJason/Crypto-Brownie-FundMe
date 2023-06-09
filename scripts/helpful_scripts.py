from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVS:
        return accounts[0]
    else:
        # requires us to add wallets and from_key to brownie-config.yaml
        return accounts.add(config["wallets"]["from_key"])
    
def deploy_mocks():
    print(f'Active is {network.show_active()}')
    print('Deploying mocks...')

    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, STARTING_PRICE, {'from': get_account()}
        ) 
    print('Mocks deployed!')