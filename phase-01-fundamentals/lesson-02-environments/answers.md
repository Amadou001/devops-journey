# Lesson 2: Environment Configuration and Deployment

## Assignment: Understanding Environments and Configuration

### 1. Difference Between Staging and Production

**Staging Environment:**
- A testing environment that closely resembles production.
- Used to test new features, updates, and bug fixes before release.
- Helps identify problems without affecting real users.

**Production Environment:**
- The live environment where the application is accessible to actual users.
- Handles real traffic and real user data.
- Must remain stable, secure, and reliable.

**Why can't we just test in production?**

Testing directly in production is risky because bugs, configuration errors, or incomplete features could cause downtime, data loss, security vulnerabilities, or a poor user experience.

The purpose of staging is to identify and fix these problems before they reach real users.

### 2. Understanding `ModuleNotFoundError`

**Scenario:**

A teammate's code works on their laptop but crashes on the server with:

```python
ModuleNotFoundError: No module named 'requests'
```

**What most likely happened?**

The `requests` library is installed on the teammate's laptop but is missing from the server's Python environment.

The application depends on a package that was not properly installed or included in the deployment process.

**Which technique prevents this?**

Use a Python virtual environment and a `requirements.txt` file to manage and document project dependencies.

On the development machine:

```bash
# Create a virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install requests

# Save dependencies
pip freeze > requirements.txt
```

On the server:

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install all project dependencies
pip install -r requirements.txt
```

This ensures that the server installs the dependencies required by the application.

### 3. Why Should Database Passwords Not Be Stored Directly in Python Code?

Putting database passwords directly in Python code is called **hardcoding credentials**, and it creates security risks.

**Reason 1: Security and Exposure**

If the code is pushed to GitHub or shared with other developers, the database password could become visible to unauthorized people. They could use it to access, modify, or delete sensitive database information.

**Reason 2: Difficult Configuration Management**

Different environments (development, staging, and production) may require different database credentials.

Hardcoding passwords makes it difficult to change credentials without modifying the source code.

**Better approach: Environment Variables**

Store sensitive configuration outside the source code.

Example:

```python
import os

DB_PASSWORD = os.environ.get("DB_PASSWORD")
```

Set the environment variable:

```bash
export DB_PASSWORD="your_secure_password"
```

This keeps credentials separate from application code.

### 4. Difference Between Inline Environment Variables and `export`

Both commands set environment variables, but their scope and duration are different.

**Option 1: Inline Environment Variable**

```bash
APP_ENV=production python3 app.py
```

- Sets `APP_ENV` only for that command and the process it starts.
- The variable is available to `app.py`.
- It does not remain set in your current terminal after the command finishes.

**Option 2: Using `export`**

```bash
export APP_ENV=production
```

- Sets the environment variable in the current shell.
- Makes it available to subsequently launched processes and their child processes.
- Remains available in that shell until it is changed, unset, or the shell terminates.

**Comparison:**

| Feature | Inline assignment | `export` |
|---|---|---|
| Syntax | `APP_ENV=production python3 app.py` | `export APP_ENV=production` |
| Scope | One command and its child processes | Current shell and subsequently launched child processes |
| Persists after command? | No | Yes, within the shell |
| Available to Python? | Yes | Yes |

### 5. Experiment: Case Sensitivity in Environment Variables

**Command:**

```bash
APP_ENV=Production python3 app.py
```

**Question: What happens to debug mode, and why?**

If the application checks the environment using an exact comparison such as:

```python
import os

APP_ENV = os.environ.get("APP_ENV", "development")

DEBUG = APP_ENV == "development"
```

The application reports:

```text
Debug mode: False
```

**Why?**

Environment variable values are case-sensitive when compared as strings in Python.

Therefore:

```python
"Production" == "production"
```

Returns:

```python
False
```

The capital `P` makes the value different from the expected lowercase string.

**What does this teach us?**

Configuration values must match the expected format and spelling exactly when using strict string comparisons.

To make configuration handling more flexible, you can normalize the value:

```python
APP_ENV = os.environ.get("APP_ENV", "development").lower()
```

Now both `Production` and `production` are interpreted as `production`.

---

## Key Takeaways

| Concept | What to Remember |
|---|---|
| Staging | Test changes before releasing them. |
| Production | Live environment used by real users. |
| Virtual Environments | Isolate Python dependencies. |
| `requirements.txt` | Documents project dependencies. |
| Environment Variables | Keep configuration and secrets outside source code. |
| Inline Assignment | Sets a variable for one command. |
| `export` | Makes a variable available to processes launched from the current shell. |
| Case Sensitivity | Configuration values must match expected strings. |

**Lesson 2 Objective:** Understand how to manage application environments, dependencies, and configuration safely before deploying applications to production.