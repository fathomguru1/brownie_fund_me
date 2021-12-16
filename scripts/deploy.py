from brownie import FundMe,network,config,MockV3Aggregator
from scripts.help_scripts import get_account,LOCAL_BLOCKCHAIN_ENVIRONMENTS

def deploy_fund_me():
    account = get_account()
    # fund_me = FundMe.deploy({"from": account})

    #代码发布,etherscan上可以查看
    # fund_me = FundMe.deploy({"from": account},publish_source=True)
    #pass the price feed address to our constract
    #if we are on a persistent network like rinkeby, use the associated address 0x8A753747A1Fa494EC906cE90E9f37563A8AF630e
    #otherwise, deploy  mocks

    # if network.show_active() != "development":
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        print(f"the active network is {network.show_active()}")
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"] 
    else:
        print(f"the active network is {network.show_active()}")
        print("Deploying Mocks...")
        mock_aggregator = MockV3Aggregator.deploy(18,20000000000000000000,{"from": account})
        price_feed_address = mock_aggregator.address
        print("Deployed Mocks...")

    # fund_me = FundMe.deploy(price_feed_address,{"from": account},publish_source=True)
    # fund_me = FundMe.deploy(price_feed_address,{"from": account},publish_source=config["networks"][network.show_active()].get("verify"))
    fund_me = FundMe.deploy(price_feed_address,{"from": account})


    # print(f"Contract deployed to {fund_me.address}")

def main():
    deploy_fund_me()