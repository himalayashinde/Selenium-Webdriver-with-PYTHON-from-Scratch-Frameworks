# 🚀 Selenium WebDriver with Python from Scratch + Frameworks

Welcome! This repository is a hands-on, beginner-to-advanced journey into Python automation with Selenium WebDriver. It’s designed to help you master Python basics, build robust test frameworks, and adopt industry best practices for scalable, maintainable test automation.

---

## 🎯 What You'll Learn

- Python programming essentials (variables, data types, functions, OOP)
- Selenium WebDriver automation from the ground up
- Test framework architecture using PyTest
- Page Object Model (POM) for maintainable tests
- Data-driven and cross-browser testing
- Reporting, logging, and CI/CD integration

---

## 🗂️ Project Structure

```
.
├── README.md
├── PythonBasics/         # Python fundamentals & demos
│   ├── FirstDemo.py
│   ├── DataType.py
│   ├── FunctionsDemo.py
│   ├── OopsDemo.py
│   ├── readWriteTXTFile.py
│   └── ...
├── PythonSelenium/       # Selenium scripts & framework (to be added)
├── pytestDemo/           # PyTest demos & reports
│   ├── test_demo1.py
│   ├── test_fixtureDemo.py
│   ├── report.html
│   └── ...
├── .idea/                # IDE configs
└── __pycache__/          # Python cache files
```

---

## ⚡ Getting Started

### Prerequisites

- Python 3.8+ (recommended: 3.13)
- pip (Python package manager)
- Chrome/Firefox browser
- IDE (VSCode, PyCharm, etc.)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/himalayashinde/Selenium-Webdriver-with-PYTHON-from-Scratch-Frameworks.git
   ```
2. **Navigate to the project directory**
   ```bash
   cd Selenium-Webdriver-with-PYTHON-from-Scratch-Frameworks
   ```
3. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```
4. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. **Install dependencies**
   ```bash
   pip install selenium pytest webdriver-manager
   ```

---

## 🏃‍♂️ Quickstart

- **Run Python basics demo:**
  ```bash
  python PythonBasics/FirstDemo.py
  ```
- **Run data types demo:**
  ```bash
  python PythonBasics/DataType.py
  ```
- **Run PyTest demo:**
  ```bash
  pytest pytestDemo/ --html=pytestDemo/report.html
  ```

---

## 🧑‍💻 Learning Path

- **Phase 1:** Python Fundamentals (`PythonBasics/`)
- **Phase 2:** Selenium WebDriver Basics (`PythonSelenium/`)
- **Phase 3:** Framework Development (PyTest, POM, config)
- **Phase 4:** Advanced Topics (parallel, CI/CD, Docker)

---

## 🛠️ Features (Planned & In Progress)

- [x] Python basics & OOP demos
- [x] PyTest demo suite with HTML reporting
- [ ] Selenium WebDriver scripts
- [ ] Page Object Model implementation
- [ ] Data-driven & cross-browser testing
- [ ] CI/CD pipeline examples

---

## 📋 Example requirements.txt

```
selenium>=4.15.0
pytest>=7.4.0
webdriver-manager>=4.0.0
pytest-html>=4.0.0
allure-pytest>=2.13.0
```

---

## 🖥️ Example: Basic Selenium Script

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://example.com")
element = driver.find_element(By.ID, "element-id")
element.click()
driver.quit()
```

---

## 🧪 Testing & Reporting

- Run all tests:
  ```bash
  pytest pytestDemo/ --html=pytestDemo/report.html
  ```
- View HTML report: open `pytestDemo/report.html` in your browser.

---

## 💡 Best Practices

- Use Page Object Model for maintainable code
- Prefer explicit waits over sleeps
- Keep test data separate from test logic
- Follow PEP 8 coding standards
- Write clear, descriptive test names

---

## 📚 Resources

- [Selenium Python Docs](https://selenium-python.readthedocs.io/)
- [PyTest Docs](https://docs.pytest.org/)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)

---

## 👨‍💻 Author

**Himalaya Shinde**  
GitHub: [@himalayashinde](https://github.com/himalayashinde)

---

**Happy Testing! 🚀**

*This framework is for educational purposes and can be extended for production use with proper security and performance considerations.*
