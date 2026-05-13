# 🗳️ Secure Blockchain Voting System

A robust and tamper-proof e-voting system built using **blockchain technology** to ensure transparency, security, and integrity in the voting process. This project demonstrates real-world blockchain concepts including proof-of-work consensus, cryptographic hashing, and immutable ledger technology.

## 🎯 Problem Statement

Traditional voting systems face critical vulnerabilities:

- **Vote Tampering**: Vulnerability to unauthorized modifications
- **Lack of Transparency**: Difficult to verify vote authenticity
- **Double Voting**: No foolproof mechanism to prevent duplicate votes
- **Single Point of Failure**: Reliance on centralized authorities
- **Trust Issues**: Limited auditability and voter confidence

## 💡 Solution

This E-voting system leverages **blockchain technology** to address all these challenges:

| Challenge | Solution |
| --- | --- |
| Vote Tampering | Immutable blockchain with SHA-256 hashing |
| Double Voting | Voter ID tracking with one vote per person |
| Lack of Transparency | Public blockchain ledger (Commission View) |
| Centralization | Decentralized proof-of-work consensus |
| Trust Issues | Cryptographic verification & auditable chain |

## ✨ Core Features

### 🔐 Security Features

- **SHA-256 Cryptographic Hashing**: Industry-standard secure hashing
- **Proof-of-Work Consensus**: Mining-based block validation
- **Voter ID Hashing**: Voter anonymity with duplicate prevention
- **Immutable Ledger**: Once recorded, votes cannot be altered
- **Block Chain Validation**: Verifies chain integrity

### 🎨 User Interfaces

- **🌐 Web UI (Flask)**: Modern, responsive web interface with Bootstrap styling
  - Real-time system status dashboard
  - Beautiful voting portal
  - Interactive data visualization
  - Responsive mobile-friendly design

- **🖥️ Desktop GUI (Tkinter)**: Native desktop application for offline voting
  - Graphical candidate selection
  - Real-time blockchain verification
  - Election commission access

- **💻 CLI Server Mode**: Command-line socket-based server for headless environments

### 📊 Data Display

- **Tabular Blockchain View**: Formatted block information with timestamps and proofs
- **Election Results Table**: Organized results by constituency with vote counts
- **Commission Results Table**: Verified results view with total vote calculations
- **System Status Dashboard**: Real-time metrics (blocks, votes cast)

### 🛡️ Administrative Features

- **Election Commission View**: Secure access with login (ID: `55`)
- **Constituency-specific Results**: View results for each voting area
- **Vote Aggregation**: Automatic vote counting by candidate
- **Blockchain Verification**: Proof-of-work validation

## 📋 Constituency Structure

The system supports **3 constituencies** with **3 candidates each**:

| Constituency | Voter ID Prefix | Candidates |
| --- | --- | --- |
| A | A (e.g., A001) | Candidate A, B, C |
| B | B (e.g., B123) | Candidate X, Y, Z |
| C | C (e.g., C999) | Candidate D, E, F |

## 🛠️ Tech Stack

- **Language**: Python 3
- **Backend Framework**: Flask 2.3.3
- **GUI**: Tkinter (Desktop)
- **Cryptography**: SHA-256 (hashlib)
- **Networking**: Python Sockets
- **Data Format**: JSON
- **Testing**: Python unittest

## 🔗 How It Works

### Voting Process

1. **Voter Registration**: Voter enters unique ID (A/B/C prefix)
2. **Candidate Selection**: Choose from constituency candidates
3. **Vote Encryption**: Voter ID is hashed with SHA-256
4. **Block Creation**: Vote added to current block
5. **Mining**: Proof-of-Work algorithm validates the block
6. **Block Addition**: Validated block added to blockchain
7. **Immutability**: Vote becomes permanent in the ledger

### Blockchain Validation

```text
Genesis Block (index: 1)
    ↓
Block 2 (Vote 1) ← Proof-of-Work (0000...)
    ↓
Block 3 (Vote 2) ← Previous Hash validation
    ↓
Block N (Vote N) ← Chain integrity verified
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip package manager
- Modern web browser (for Web UI)
- Git (optional)

### Installation

1. **Clone the repository** (or download the project)

```bash
git clone https://github.com/Yogiii13/E-voting-system-using-blockchain-and-python.git
cd E-voting-system-using-blockchain-and-python
```

1. **Create a virtual environment** (recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

1. **Install dependencies**

```bash
pip install -r requirements.txt
```

## 📱 How to Run

### 🌐 Option 1: Web UI (Recommended - Cloud/Codespace)

Best for modern cloud environments, provides the most user-friendly interface.

```bash
python3 run_web.py
```

**Output:**

```text
============================================================
🔐 Secure Blockchain Voting System
============================================================

✅ Server starting on http://localhost:5000
   Open your browser and navigate to: http://localhost:5000

Press Ctrl+C to stop the server
```

**Access the application:**

- Open browser → `http://localhost:5000`
- Or use port forwarding in your development environment

**Features Available:**

- ✅ Vote Portal - Cast your vote securely
- ✅ Dashboard - View system status & block count
- ✅ View Blockchain - See all blocks in tabular format
- ✅ Election Results - View voting results by constituency (formatted table)
- ✅ Commission Login - Access official election results

---

### 🖥️ Option 2: Desktop GUI (Local Machine with Display)

Best for standalone desktop use with graphical interface.

```bash
python3 run_gui.py
```

**Features:**

- Native window interface
- Candidate selection with radio buttons
- Real-time blockchain inspection
- Commission view access
- Vote confirmation dialogs

**Requirements:**

- Display/GUI environment
- X11 server (for remote access)

---

### 💻 Option 3: CLI Server Mode (Headless/Advanced)

Best for server environments, batch processing, or integration with other systems.

```bash
python3 run_server.py
```

**Features:**

- Socket-based communication
- Headless operation
- Scriptable voting process
- Raw blockchain access

**Note:** This mode requires a separate client to interact with the server.

---

## 📖 Usage Guide

### Voting (All Interfaces)

1. **Enter Voter ID**
   - Format: Single letter (A, B, or C) followed by numbers
   - Examples: `A001`, `B123`, `C999`
   - Each voter can only vote once (duplicate prevention)

2. **Select Constituency**
   - Auto-detected from first letter of voter ID
   - Displays available candidates for that constituency

3. **Choose Candidate**
   - Radio button selection from available candidates
   - Constituency A: Candidates A, B, C
   - Constituency B: Candidates X, Y, Z
   - Constituency C: Candidates D, E, F

4. **Cast Vote**
   - Click "Cast Vote" button
   - Vote is immediately added to blockchain
   - System status updates in real-time

### 🔑 Commission Login (Authorization Required)

Access official voting results with exclusive commission credentials.

**Steps:**

1. Click **"🔑 Commission Login"** button (in Dashboard)
2. Enter Commission ID: `55`
3. Enter Constituency: `A`, `B`, or `C`
4. View aggregated results in tabular format

**What You'll See:**

- Candidate names and IDs
- Vote count per candidate
- Total votes for constituency
- Verified results from blockchain

**Example Output:**

```text
Constituency A
┌─────────────────┬──────────────────┬───────┐
│ Candidate ID    │ Candidate Name   │ Votes │
├─────────────────┼──────────────────┼───────┤
│ 1               │ Candidate A      │ 5     │
│ 2               │ Candidate B      │ 3     │
│ 3               │ Candidate C      │ 2     │
└─────────────────┴──────────────────┴───────┘
Total Votes: 10
```

### 📊 Viewing Blockchain

Click **"📊 View Blockchain"** to see the complete block chain.

**Displayed Information:**

- Block Index (block number)
- Timestamp (when block was created)
- Vote Count (how many votes in block)
- Proof (proof-of-work value)
- Previous Hash (link to previous block)

### 📈 Viewing Election Results

Click **"📈 Election Results"** to see voting statistics.

**Shows:**

- Results organized by constituency
- Candidate names with vote counts
- Total votes per constituency
- Formatted table for easy reading

---

## 📁 Project Structure

```text
E-voting-system-using-blockchain-and-python/
├── README.md                 # Project documentation
├── LICENSE                   # MIT License
├── requirements.txt          # Python dependencies
│
├── run_web.py               # Web UI entry point (Flask)
├── run_gui.py               # Desktop GUI entry point (Tkinter)
├── run_server.py            # CLI Server entry point (Sockets)
│
├── e_voting/                # Main package
│   ├── __init__.py
│   ├── app.py               # Flask application & routes
│   ├── blockchain.py        # Blockchain core implementation
│   ├── client.py            # Client implementation
│   ├── server.py            # Server socket implementation
│   ├── gui.py               # Tkinter GUI implementation
│   ├── sha.py               # SHA-256 utilities
│   │
│   ├── templates/           # Flask HTML templates
│   │   └── index.html       # Main web interface
│   │
│   └── legacy/              # Previous implementations (deprecated)
│       ├── blockchain_voting.py
│       ├── client_vote.py
│       └── server.py
│
└── tests/                   # Unit tests
    ├── test_blockchain.py   # Blockchain tests
    ├── test_server.py       # Server tests
    └── test_sha.py          # SHA-256 tests
```

## 🧪 Running Tests

Verify the system works correctly with comprehensive unit tests:

```bash
python3 -m pytest tests/          # Run all tests
python3 -m unittest tests/test_blockchain.py    # Test blockchain
python3 -m unittest tests/test_server.py        # Test server
python3 -m unittest tests/test_sha.py           # Test hashing
```

## 📊 Key Metrics

| Metric | Value |
| --- | --- |
| Vote Immutability | 100% |
| Double Voting Prevention | Yes (Voter ID tracking) |
| Transparency | Complete (Blockchain viewable) |
| Centralization | None (Decentralized consensus) |
| Cryptographic Security | SHA-256 |
| Proof-of-Work Target | 4 leading zeros |

## 🔍 API Endpoints (Web UI)

The Flask application exposes these REST endpoints:

### Voting

- `POST /api/cast-vote` - Cast a vote
  - Body: `{ "voter_id": "A001", "candidate_id": "1" }`
  - Returns: Success/Error message

### Data Retrieval

- `GET /api/blockchain` - Get complete blockchain
- `GET /api/results` - Get all election results
- `GET /api/candidates/<constituency>` - Get candidates for constituency
- `POST /api/commission-view` - Get commission verified results
  - Body: `{ "login_id": "55", "constituency": "A" }`

## 🛡️ Security Considerations

- ✅ Voter anonymity through SHA-256 hashing
- ✅ Vote immutability via blockchain
- ✅ Double voting prevention via voter ID tracking
- ✅ Proof-of-work consensus mechanism
- ✅ Chain integrity verification
- ⚠️ Commission login uses simple ID (for demo only)
- ⚠️ Not suitable for high-security production use without additional measures

## 📝 Configuration

Edit these files to customize:

**Candidates** - Modify in `e_voting/app.py`:

```python
candidates = {
    'A': {'1': 'Candidate A', '2': 'Candidate B', '3': 'Candidate C'},
    'B': {'1': 'Candidate X', '2': 'Candidate Y', '3': 'Candidate Z'},
    'C': {'1': 'Candidate D', '2': 'Candidate E', '3': 'Candidate F'},
}
```

**Commission ID** - Modify in `e_voting/blockchain.py`:

```python
def election_commission_view(self, login_id, constituency):
    if login_id != '55':  # Change this ID
        return {'error': 'Access denied. Invalid login ID.'}
```

**Server Address/Port** - Modify in `e_voting/app.py`:

```python
app.run(debug=False, host='0.0.0.0', port=5000)  # Change port here
```

## 🤝 Contributing

Contributions are welcome! Areas for enhancement:

- [ ] Add user authentication system
- [ ] Implement database backend (PostgreSQL/MongoDB)
- [ ] Create REST API clients
- [ ] Add password protection for commission view
- [ ] Implement vote audit logs
- [ ] Add support for multiple elections
- [ ] Create Docker containerization
- [ ] Add advanced cryptography (RSA/ECC)
- [ ] Implement WebSocket for real-time updates
- [ ] Create mobile app versions

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🔗 References

- [Bitcoin Whitepaper](https://bitcoin.org/bitcoin.pdf) - Blockchain fundamentals
- [Ethereum Whitepaper](https://ethereum.org/en/whitepaper/) - Smart contracts
- [SHA-256 Documentation](https://en.wikipedia.org/wiki/SHA-2) - Cryptography
- [Proof of Work](https://en.wikipedia.org/wiki/Proof_of_work) - Consensus mechanism

## 👨‍💻 Author

**Yogiii13** - Blockchain & E-voting System Developer

## 📞 Support

For issues, questions, or suggestions:

- Open a GitHub issue
- Check existing documentation
- Review test cases for usage examples

---

Built with ❤️ using Python and Blockchain Technology
