import hashlib
import json
import time
from flask import Flask, render_template, request
class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def to_dict(self):
        return {
            'index': self.index,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'data': self.data,
            'nonce': self.nonce,
            'hash': self.hash
        }

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.index = len(self.chain)
        new_block.previous_hash = self.get_latest_block().hash
        new_block.timestamp = int(time.time())
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    #For security purposes there must be an is_valid function.

    def to_dict(self):
        return [block.to_dict() for block in self.chain]

# Simulation
node1 = Blockchain()
node2 = Blockchain()
node3 = Blockchain()

data_to_add = "New data generated"

new_block = Block(0, "0", 0, data_to_add)
node1.add_block(new_block)
node2.add_block(new_block)
node3.add_block(new_block)

print("Block added to all nodes.")


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', node1=node1.chain, node2=node2.chain, node3=node3.chain)

@app.route('/add_block', methods=['POST'])
def add_block():
    data_to_add = request.form['data']
    new_block = Block(0, "0", 0, data_to_add)
    
    node1.add_block(new_block)
    node2.add_block(new_block)
    node3.add_block(new_block)

    return index()

if __name__ == '__main__':
    app.run(debug=False)