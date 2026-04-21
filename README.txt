# 🧠🔗 ConceptAPI – AI-Powered Blockchain Web App

**ConceptAPI** was the name of an inter-school competition held during the academic session **2023–2024**, where this project was developed.
The project secured **🥈 Second Place overall**, showcasing an innovative integration of **blockchain technology with AI-generated data**.

---

## 🚀 Project Overview

This project is a **Flask-based web application** that combines:

* A **basic blockchain system**
* A **simulated multi-node network**
* An **AI text generation model (T5-small)**

Users can input text, which is processed by an AI model and then stored as a block across multiple blockchain nodes.

---

## ✨ Key Features

* 🔗 Custom blockchain implementation
* 🤖 AI-generated block data using a transformer model
* 🌐 Interactive web interface using Flask
* 🧩 Simulated distributed blockchain (3 nodes)
* 📦 JSON-based block representation
* ⚡ Real-time block updates

---

## 🏗️ Project Structure

```
.
├── app.py                # Main backend application
├── templates/
│   └── index.html       # Frontend UI
├── README.md            # Project documentation
```

---

## ⚙️ Technologies Used

* **Python**
* **Flask** – Backend web framework
* **PyTorch** – Machine learning framework
* **Hugging Face Transformers** – AI text generation
* **Hashlib** – SHA-256 hashing
* **JSON** – Data handling

---

## 🧱 Blockchain Implementation

### Block Class

Each block contains:

* `index` – Position in the chain
* `previous_hash` – Hash of the previous block
* `timestamp` – Time of creation
* `data` – AI-generated content
* `nonce` – For future mining logic
* `hash` – SHA-256 hash of the block

---

### Blockchain Class

* Initializes with an **origin (genesis) block**
* Maintains a chain of blocks
* Handles adding new blocks
* Ensures linkage via hashes

---

## 🌐 Multi-Node Simulation

The system simulates **three independent blockchain nodes**:

```python
node1 = Blockchain()
node2 = Blockchain()
node3 = Blockchain()
```

Each node receives identical blocks, mimicking a distributed system (simplified).

---

## 🤖 AI Integration

The application uses a **pre-trained T5-small transformer model** to generate text:

```
generate_response(prompt)
```

### Workflow:

1. User inputs text
2. AI generates a response
3. Response is stored as block data
4. Block is added to all nodes

---

## 🖥️ Web Application

### Routes:

* `/` → Displays all blockchain nodes and their blocks
* `/add_block` → Accepts user input and adds a new block

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

``` 
git clone https://github.com/your-username/conceptapi.git
cd conceptapi
```

### 2. Install Dependencies

``` 
pip install flask torch transformers
```

### 3. Run the Application

``` 
python app.py
```

---

## 🌐 Usage

1. Open your browser and go to:

   http://127.0.0.1:5000/
   

2. Enter a prompt in the input field

3. Submit to generate AI-based block data

4. View updated blockchain across all nodes

---

## ⚠️ Limitations

* No real consensus mechanism (Proof of Work / Stake not implemented)
* No chain validation or tamper detection
* Nodes are simulated locally (not distributed)
* Uses a small AI model (limited response quality)

---

## 🔮 Future Improvements

* 🔐 Add blockchain validation system
* ⛏️ Implement mining (Proof of Work)
* 🌍 Create real distributed nodes
* 🧠 Upgrade to a more powerful AI model
* 💾 Add database persistence
* 🎨 Improve frontend UI/UX

---

## 🏆 Achievement

🥈 **Second Place – ConceptAPI (2023–2024)**
An inter-school competition recognizing innovation in technology and problem-solving.

---

## 🤝 Contributing

Contributions are welcome!

* Fork the repository
* Create a new branch
* Submit a pull request

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

