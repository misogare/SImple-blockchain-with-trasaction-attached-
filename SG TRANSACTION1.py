import json
import datetime
import hashlib
#the chain module first block 
block = {
    'index':1,
    'timestamp': str(datetime.datetime.now()),
    'previous_hash':"0"*64
}
print("Single Block:")
print(block)
#list
chain = []

chain.append(block)
#using the previous block
previous_block = chain[0]
# 9 blocks ignore the first one it has 0000*64 hash 
#check valid chain and adding new blocks to chain 
for index in range(2,11):
    encoded_block = json.dumps(previous_block,sort_keys=True).encode()
    hash = hashlib.sha256(encoded_block).hexdigest()
    new_block = {
        'index':index,
        'timestamp' : str(datetime.datetime.now()),
        'previous_hash' : hash
    }
    chain.append(new_block)
    previous_block = new_block

print("the blocks of the chain :")
#each block 
for block in chain:
    print(block)
#put it in blockchainSG json
f = open('blockchainSG.json','w')
json.dump(chain,f,sort_keys=True)
f.close()
#read the block chain from blockchainSG
chain = []
f = open ("blockchainSG.json", "r")
chain = json.load(f)
f.close()


#add the transaction to block chain same as above but now you see the details of transaction
idrow = 0
bruh =int(input("enter the transaction list number "))
for i in range(0,bruh):
    print("pls enter the electericity amount u wanna move ",end ="")
    electericity = int(input())
    print("\033[Fkw")
    spropertyaddress = input("enter the address value ")
    rpropertyaddress = input("reciver address")
    name = input("enter the senders name")
    rname = input("enter the reciever name")
    amountmoney = int(input('enter the amount for buying that'))


    inputs = []
    outputs = []
#list of inputs
    input1 = {'sender' : name , 'amount':electericity,'sender property address':spropertyaddress }
    input2 ={'sender':rname, 'amount':amountmoney, 'reciever property address':rpropertyaddress}
    output1 = {'reciever':name, 'amount':amountmoney, 'sender property address':spropertyaddress}
    output2={'reciever':rname,'amount':electericity,'property address':rpropertyaddress }
#making a dictionary list 
    inputs.append(input1)
    inputs.append(input2)
    outputs.append(output1)
    outputs.append(output2)
    idrow += 1
    transaction = {
        "id" : idrow ,
        'inputs':inputs,
        'outputs':outputs
    }
    #length of chain 
    block_index = len(chain)
    previous_block = chain[block_index - 1]
    #applying the same basic as the above chain module above 
    encoded_block =json.dumps(previous_block,sort_keys=True).encode()
    hash = hashlib.sha256(encoded_block).hexdigest()
    new_block = {
        'index': block_index + 1,
        'timestamp': str(datetime.datetime.now()),
        'previous_hash': hash,
        'transaction':transaction
    }
    chain.append(new_block)
    print('print the new block')
    print(new_block)

    print('transaction')
    for i in transaction["inputs"]:
        print(i)
    for o in transaction['outputs']:
        print(o)
    f1 = open("blockchainSG.json",'w')
    json.dump(chain,f1,sort_keys=True)
    f1.close()

    f2 = open("blockchainSG.json",'r')
    chain1 = json.load(f2)
    for block in chain1:
        print(block)
