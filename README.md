# 🧪 Provineer Regression Tests

This project contains UI regression tests for the Provineer web platform, using:

- **Python**
- **Pytest**
- **Selenium**
- **Allure** for reporting
- **Docker + Docker Compose** for isolated and reproducible test runs

---

## 🚀 Quick Start

### ✅ Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- (Optional) [Allure CLI](https://docs.qameta.io/allure/#_installing_a_commandline) — required to generate the HTML report

---

### 🔧 Setup & Run

1. **Clone the repository**

```bash
git clone https://github.com/Alex-spec/Provineer_ui_regression_tests.git
cd Provineer_ui_regression_tests
```

2. **Run tests via Docker Compose**

```bash
docker-compose up --build --abort-on-container-exit
```

- This will build the test container
- Launch a Selenium Chrome browser inside Docker
- Run all Pytest tests in the `tests/` folder
- Store Allure results in `./allure-results/`

3. **Generate and open Allure Report**

```bash
allure generate ./allure-results -o ./allure-report --clean
allure open ./allure-report
```

📌 This opens a full-featured test dashboard in your default browser.

---

## 📁 Project Structure

```
provineer-regression-tests/
├── tests/                  # Test files (test_*.py)
├── conftest.py            # Pytest fixtures and WebDriver setup
├── requirements.txt       # Python dependencies
├── Dockerfile.tests       # Docker image to run tests
├── docker-compose.yml     # Test infrastructure definition
├── allure-results/        # Raw test results (created after run)
├── allure-report/         # Final HTML report (after generation)
```

---

## 🧪 Example Output

```bash
tests/test_provineer.py::test_proofs_and_certificates PASSED 
tests/test_provineer.py::test_shared_feature PASSED   
...
============================== 3 passed in 32.50s ==============================
```

Then open: `allure-report/index.html`

---

## 🛠 Troubleshooting

- ❗ If the Allure report is empty:
  - Check that test files start with `test_` and contain test functions like `def test_something():`
  - Make sure `allure-pytest` is listed in `requirements.txt`
  - Run the `allure generate ...` command manually

---

## 💡 Tips

- You can extend this setup to support:
  - Parallel test runs with `pytest-xdist`
  - Headless or visible browsers
  - CI/CD pipelines (e.g., GitHub Actions or GitLab CI)




