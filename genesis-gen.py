import json

myauth = "be590efffcf1068a75817d2dade94a24dccf0fd8"
mysub = "57bc9febbf1aae3492b5d1a5a70f7bd80ee302d9"
ljs = "3ef78933405Df49C794Be1E8E6Bb5C2b94CA6201"

genform = {}

# config
genform["config"] = {}
genform["config"]['chainId'] = 3663
genform["config"]['homesteadBlock'] = 0
genform["config"]['eip150Block'] = 0
genform["config"]['eip155Block'] = 0
genform["config"]['eip158Block'] = 0
genform["config"]['byzantiumBlock'] = 0
genform["config"]['constantinopleBlock'] = 0
genform["config"]['petersburgBlock'] = 0

genform["difficulty"] = "1"
genform["gasLimit"] = "8000000"

genform["alloc"] = {}
genform["alloc"][myauth] = { "balance": str(1000 * 10 ** 18) }
genform["alloc"][mysub] = { "balance": str(1 * 10 ** 18) }
genform["alloc"][ljs] = { "balance": str(8 * 10 ** 18) }

# clique for PoA
genform["config"]["clique"] = {}
genform["config"]["clique"]["period"] = 5      # Minimum difference between two consecutive block’s timestamps
genform["config"]["clique"]["epoch"] = 30000   # Number of blocks after which to checkpoint and reset the pending votes

# extra data for PoA
print("If done, type x")
extradata = '0x' + '0' * 64 + myauth + psj

while True:
    newacc = input("Enter your Auth_account >>> If done, type X \n")
    if newacc == "X":
        extradata += '0' * 130
        genform["extradata"] = extradata
        print(extradata)
        break
    extradata += newacc


with open("genesis-new.json", 'w') as f:
    json.dump(genform, f)

print("saved as 'genesis-new.json'")
