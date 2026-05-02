# E-voting-system-using-blockchain-and-python

A secure and tamper-proof e-voting system built using blockchain technology to ensure transparency and trust in voting.

## Problem

Traditional voting systems can have issues like:
- Vote tampering
- Lack of transparency
- Double voting
- Dependence on third parties

## Solution

This project uses a custom blockchain to:
- Store votes securely
- Prevent data tampering
- Eliminate double voting
- Ensure transparency without third-party verification

## Features

- SHA-256 based hashing
- Custom blockchain implementation
- Proof-of-Work consensus
- Encrypted voting system
- Unique user tokens

## Tech Stack

- Python
- Blockchain concepts
- Cryptography

## How it Works

1. User gets a unique token
2. Vote is encrypted
3. Vote is added as a block
4. Block is validated using mining
5. Data becomes immutable

## Results

- 100% vote immutability
- No double voting
- Fully transparent system
- No third-party dependency

## How to Run

### Web UI (Recommended for Codespace/Cloud)

```bash
python3 run_web.py
```

Then open your browser to `http://localhost:5000` to access the voting interface.

### Desktop GUI (Local machine with display)

```bash
python3 run_gui.py
```

### Server (Command-line socket mode)

```bash
python3 run_server.py
```

## Installation

```bash
pip install -r requirements.txt
```

Then use the new interface to enter a voter ID, select a candidate, cast your vote, and inspect the blockchain.
