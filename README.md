# ShopLite — Online Shopping System

ShopLite is a Flask-based online storefront for everyday products. Browse a 12-item catalog, search by product name, filter by category, and manage a session-based shopping cart. A Jenkins pipeline runs automated tests, builds a Docker image, and deploys the updated application container.

## Features

- Responsive product catalog with 12 products across Accessories, Electronics, and Home
- Product-name search and category filters that can be combined
- Session-based cart with item removal, clear-cart, and order summary
- Automated tests for catalog, search, filters, and cart behavior
- Jenkins pipeline stages for testing, Docker image build, and deployment

The checkout control is inactive. Payment processing, customer accounts, and persistent product storage are not included.

## Technology

- Python and Flask
- Docker
- Jenkins Pipeline as Code
- GitHub

## CI/CD workflow

1. Jenkins checks out the latest code from the GitHub `main` branch.
2. Jenkins builds `Dockerfile.test`, which installs the app dependencies and runs the automated tests.
3. When tests pass, Jenkins builds the application image tagged with the build number.
4. Jenkins replaces the previous ShopLite container and deploys the new image on port `5000`.

Open [http://localhost:5000](http://localhost:5000) to view the running application. The Jenkins agent must have access to Docker, and port 5000 must be available for ShopLite.

## Run locally

Requires Python 3.10 or newer.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open [http://localhost:5000](http://localhost:5000).

## Run with Docker

```powershell
docker build -t online-shopping:local .
docker run --rm -p 5000:5000 online-shopping:local
```

## Run automated tests

Run directly with Python:

```powershell
python -m unittest discover -s tests -v
```

Or run them in Docker:

```powershell
docker build -f Dockerfile.test -t online-shopping-test:local .
```

## GitHub repository

Source code: [github.com/Chintub1/online-shopping-devops](https://github.com/Chintub1/online-shopping-devops)

## Project structure

```text
online-shopping-devops/
├── app.py
├── Dockerfile
├── Dockerfile.test
├── Jenkinsfile
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   ├── cart.html
│   └── index.html
└── tests/
    └── test_app.py
```
