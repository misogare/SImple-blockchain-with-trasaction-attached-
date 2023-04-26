# Python Blockchain with Transaction Project

*** This Python project implements a simple blockchain that allows users to attach transactions to blocks. 
The blockchain consists of a series of blocks, with each block containing a hash of the previous block and a transaction. 
The initial version of the project contains 10 pre-made hashes of blocks in the chain.
***

## Usage
To run the project, you need to have Python installed on your system. Clone the project repository and navigate to the root directory in your terminal or command prompt. Then, run the following command:

Copy code
```
python SG transaction1.py
```
      This will start the blockchain and display the pre-made 10 hashes of blocks in the chain. The program will then ask the user to input valid transaction data. Once the user enters the transaction data, the program creates a new block with the transaction attached and adds it to the blockchain.

      The program will keep running, allowing the user to add new transactions and blocks to the chain. Each block in the chain will have a unique hash and a transaction attached to it.

## Dependencies
    The project uses the built-in hashlib module to calculate the hash values of blocks. No additional external libraries are required.

## Contributing
    If you want to contribute to the project, feel free to fork the repository and make changes. You can then submit a pull request to have your changes reviewed and merged into the main branch.
