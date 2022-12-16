from brownie import accounts, config, interface, network
from web3 import Web3
from scripts.get_weth import get_weth

def main():
    print('main started ...')
    account = accounts[0]
    print(account)
    erc20_address = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2" # Token Wrapped Ether
    get_weth(account)
    lending_pool = get_lending_pool()
    amount = Web3.toWei(0.1, "ether")
    approve_erc20(amount, lending_pool.address, erc20_address, account)

def get_lending_pool():
    lending_pool_address_provider_address = '0xB53C1a33016B2DC2fF3653530bfF1848a515c8c5'
    lending_pool_address_provider = interface.ILendingPoolAddressProvider(
        lending_pool_address_provider_address
    )
    lending_pool_address = lending_pool_address_provider.getLendingPool()
    lending_pool = interface.LendingPool(lending_pool_address)
    return lending_pool

def approve_erc20(amount, lending_pool_address, erc20_address, account):
    print("Approving ERC20...")
    erc20 = interface.IERC20(erc20_address)
    tx = erc20.approve(lending_pool_address, amount, {"from": account})
    tx.wait(1)
    print("Approved!")
