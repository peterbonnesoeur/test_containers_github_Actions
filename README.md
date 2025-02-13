# Test Containers Demo

This project demonstrates the use of `testcontainers-python` for integration testing with Docker containers, specifically testing a Redis connection. The project uses GitHub Actions for continuous integration with the fast `uv` package installer.

## 🚀 Features

- Uses `testcontainers-python` to spin up a Redis container for testing
- Implements a simple Redis connection test
- GitHub Actions workflow with `uv` for fast dependency installation
- Automatic container cleanup after tests

## 🛠️ Requirements

- Python 3.11+
- Docker
- `uv` (optional, for faster package installation)

## 📦 Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd <repo-name>
```

2. Install dependencies:
```bash
# Using pip
pip install -r requirements.txt

# Or using uv (faster)
uv pip install -r requirements.txt
```

## 🧪 Running Tests

Run the tests using pytest:
```bash
pytest -v
```

## 🔄 CI/CD

The project includes a GitHub Actions workflow that:
- Runs on push to main and pull requests
- Uses `uv` for fast dependency installation
- Automatically runs the test suite

## 📝 License

MIT
