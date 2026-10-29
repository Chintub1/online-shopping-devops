# ShopLite — Online Shopping System

A small online shopping demo for a DevOps lab. It includes product search and category filters, a session-based cart, automated tests, a Docker image, and a Jenkins pipeline that tests and builds the app from the GitHub repository.

## What the project demonstrates

- Source code stored in GitHub
- Jenkins Pipeline as Code using the `Jenkinsfile`
- Building a container image with Docker
- Searching products by name and filtering by category
- Running automated application tests in Jenkins before the app image is built
- Running the same app locally or as a container

The checkout button is intentionally a demo placeholder. The app has no database, payment processing, or real customer accounts.

## Search and categories

Use the search box to find products by name. Choose Accessories, Electronics, or Home to filter by category. Search and category filters can be used together.

## Automated tests

The tests cover the product list, case-insensitive search, category filtering, combined filters, no-result behavior, and adding an item to the cart. Run them locally with:

```bash
python -m unittest discover -s tests -v
```

Jenkins runs the same tests by building `Dockerfile.test` before it builds the application image. A failed test stops the pipeline before the application image stage.

## Run locally

You need Python 3.10 or newer.

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000.

## Run with Docker

```bash
docker build -t online-shopping:local .
docker run --rm -p 5000:5000 online-shopping:local
```

Then open http://localhost:5000.

To run the automated tests in Docker locally:

```bash
docker build -f Dockerfile.test -t online-shopping-test:local .
```

## Connect the project to GitHub

1. Sign in to GitHub and create a new **public** repository named `online-shopping-devops`. Leave the README, `.gitignore`, and license options unchecked because this folder already contains project files.
2. Open PowerShell in this project folder and run:

```bash
git init
git add .
git commit -m "Initial online shopping DevOps project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/online-shopping-devops.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. The repository page URL is `https://github.com/YOUR-USERNAME/online-shopping-devops`; add that link to your GitHub profile README or pin the repository on your profile.

## Run the Jenkins pipeline

The `Jenkinsfile` defines the pipeline. Install the Jenkins **Docker Pipeline** plugin, and make sure the Jenkins machine or agent has Git and Docker installed. The Jenkins agent account must be allowed to run Docker commands.

1. Start Jenkins and open its dashboard (commonly http://localhost:8080).
2. Choose **New Item**, enter `online-shopping-pipeline`, select **Pipeline**, then choose **OK**.
3. Under **Pipeline**, select **Pipeline script from SCM**.
4. Select **Git**, paste your GitHub repository URL, and choose the `main` branch.
5. Save and choose **Build Now**. Open the build and its **Console Output** to see the checkout and Docker image build stages.

If Jenkins is on the same machine as Docker, make sure the Jenkins service runs with Docker access. If the Docker build stage reports that `docker` is unavailable or permission is denied, install Docker on the Jenkins agent or grant that agent account Docker access.

## Lab presentation outline

1. Explain the shopping app and show the product catalog and cart.
2. Show the source code and `Jenkinsfile` in the GitHub repository.
3. In Jenkins, show the pipeline run and its successful stages.
4. Explain that Jenkins checks out the GitHub code, runs automated tests in a Docker build, and builds the application image only when the tests pass.

## Project layout

```text
online-shopping-devops/
├── app.py
├── Dockerfile
├── Dockerfile.test
├── Jenkinsfile
├── requirements.txt
├── static/style.css
├── templates/
│   ├── cart.html
│   └── index.html
└── tests/
    └── test_app.py
```

