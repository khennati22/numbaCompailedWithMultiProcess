
from time import time
from thread import *
from web3 import Web3,IPCProvider,WebsocketProvider
web3 = Web3(IPCProvider("/.bor/data/bor.ipc"))
# web3 = Web3(WebsocketProvider("wss://polygon-mainnet.g.alchemy.com/v2/xrOg1yXcp3g0THMf3u8vVe2T9CdeZjhf"))
contractABI = '[{"inputs":[],"name":"ApeSwapFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"BoltrFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"BullFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"CafeFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"CatFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"creator","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"address[]","name":"bases","type":"address[]"}],"name":"dataForomLists","outputs":[{"internalType":"bytes[]","name":"a","type":"bytes[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DEXFFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DfynFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DinoswapFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"EddaFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"ElkFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"fromVar","type":"address"},{"internalType":"address","name":"toVar","type":"address"}],"name":"getPairDataWithoutBase","outputs":[{"internalType":"address","name":"pair","type":"address"},{"internalType":"uint256","name":"fee","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"bases","type":"address[]"}],"name":"getPairsForallBases","outputs":[{"internalType":"bytes[]","name":"a","type":"bytes[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"GravisFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"GreenhouseFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"array","type":"bytes[]"},{"internalType":"uint256","name":"length","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"includes","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"isContract","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"JavaFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"JetswapFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"KwikswapFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"LoveSwapFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MEVFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MintyswapFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"fromVar","type":"address"},{"internalType":"address","name":"toVar","type":"address"}],"name":"multiRequest","outputs":[{"internalType":"bytes[]","name":"a","type":"bytes[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"base","type":"address"},{"internalType":"address","name":"token","type":"address"}],"name":"multiRequestForallBases","outputs":[{"internalType":"bytes[]","name":"a","type":"bytes[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"base","type":"address"},{"internalType":"address","name":"token","type":"address"},{"internalType":"address","name":"secondbase","type":"address"}],"name":"multiRequestWithSecondbase","outputs":[{"internalType":"bytes[]","name":"a","type":"bytes[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pair","type":"address"}],"name":"pairCheck","outputs":[{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"token0","type":"address"},{"internalType":"address","name":"token1","type":"address"},{"internalType":"uint256","name":"reserve0","type":"uint256"},{"internalType":"uint256","name":"reserve1","type":"uint256"},{"internalType":"uint256","name":"fee","type":"uint256"},{"internalType":"address","name":"factory","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PlasmaswapFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PolydexFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PolyZapFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"ProtofiFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"QuickFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"SafeswapFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"SmartSwapFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"SushiFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Unknown1Factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Unknown2Factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Unknown3Factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Unknown4Factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Unknown5Factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Unknown6Factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Unknown7Factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Unknown8Factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Unknown9Factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"VulcanFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"WaultFinanceFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"WolfFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]'

contract = web3.eth.contract(address="0x2bEdC3Bea189eA892172f14eF3f03a0b6fC19cCd", abi=contractABI)
allBase = ["0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270","0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174","0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619","0xc2132D05D31c914a87C6611C10748AEb04B58e8F"]


def getData(token,startTime):
    databytes = contract.functions.dataForomLists(token,allBase).call()
    print((time()*1000)-startTime)
    return databytes



def get_reserves_batch_mt():
    startTime = time()*1000
    tokens = ["0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270","0xD85d1e945766Fea5Eda9103F918Bd915FbCa63E6","0xac51C4c48Dc3116487eD4BC16542e27B5694Da1b","0x3809dcDd5dDe24B37AbE64A5a339784c3323c44F","0x874e178A2f3f3F9d34db862453Cd756E7eAb0381","0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619","0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"]
    threads = []
    for i in tokens:
        t = MyThread(func=getData, args=(i,startTime))
        t.start()
        threads.append(t)
    new_pairs = []
    for t in threads:
        t.join()
        ret = t.get_result()
        new_pairs.extend(ret)
    return new_pairs


get_reserves_batch_mt()