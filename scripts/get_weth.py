from brownie import interface

def get_weth(account):
    print("getting WETH ...")
    # ABI and Address
    weth = interface.IWeth("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
    tx = weth.deposit({"from": account, "value": 0.1 * 1e18})
    tx.wait(1)
    print("Get 0.1 WETH")