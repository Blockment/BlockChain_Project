# HomeworkChain

HomeworkChain is a blockchain-based system designed to manage homework submissions securely and efficiently. This project simulates a basic blockchain network where clients can submit, verify, and view homework transactions in a decentralized manner.

## Features

- **Client Management**: Each client has a unique identity derived from cryptographic keys.
- **Transaction Handling**: Secure creation and signing of transactions representing homework submissions.
- **Block Creation**: Accumulation of verified transactions into blocks.
- **Blockchain Integrity**: Blocks are mined to ensure integrity and are linked using cryptographic hashes.
- **Web Interface**: A simple frontend for users to upload homework files and interact with the blockchain.

## Getting Started

### Prerequisites

- Python 3
- Libraries: `pycrypto`

Install the required Python libraries using:

```bash
pip install pycrypto
```

## Running the Backend

To run the backend script, navigate to your project directory and run:

```bash
python Block.py
```

This will start the simulation of the blockchain, processing the hardcoded transactions and printing the blockchain's state.

## Running the Frontend

To view the frontend, you can serve the HTML file using Python's HTTP server module:

```bash
python -m http.server
```

Then, access the web interface by visiting [http://localhost:8000/](http://localhost:8000/) in your web browser.

## Development

### File Structure

- `Block.py`: Contains the blockchain logic and the main executable script.
- `Client.py`: Defines the `Client` class for handling client identities and keys.
- `Miners.py`: Includes the `Miner` class responsible for mining new blocks.
- `Transaction.py`: Manages the creation and signing of transactions.
- `index.html`: Frontend HTML file for the web interface.

## Maintainers

- [Sina Elahimanesh](https://github.com/SinaElahimanesh)
- [Iman Mohammadi](https://github.com/Imanm02)
