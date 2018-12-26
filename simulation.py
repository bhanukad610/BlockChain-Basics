from blockChain import *
myBlockChain = BlockChain()
myBlockChain.addNewBlock("my data")
myBlockChain.addNewBlock("hello")
myBlockChain.addNewBlock("blockchain")
myBlockChain.printBlockChain()

myBlockChain.mineChain()
myBlockChain.printBlockChain()

myBlockChain.changeData(1,"hello world")
myBlockChain.printBlockChain()

myBlockChain.mineChain()
myBlockChain.printBlockChain()