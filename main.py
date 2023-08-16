import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(value.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

# Create a blockchain
my_blockchain = Blockchain()
my_blockchain.add_block(Block(1, time.time(), "Data 1", my_blockchain.chain[-1].hash))
my_blockchain.add_block(Block(2, time.time(), "Data 2", my_blockchain.chain[-1].hash))

for block in my_blockchain.chain:
    print(f"Block {block.index} - Hash: {block.hash}")



from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def display_blocks():
    return render_template('blocks.html', blockchain=my_blockchain.chain)

if __name__ == '__main__':
    app.run(debug=True)
