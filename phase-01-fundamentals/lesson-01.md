# Lesson 1: What DevOps Is

## Assignment 1: Understanding DevOps

### 1. What is DevOps?

DevOps is not a collection of tools you install. It's a culture, a set of practices, and an approach to software development and IT operations.

It promotes collaboration between Development (Dev) and Operations (Ops) teams to deliver software faster, more reliably, and more efficiently.

### 2. Why Are Frequent, Small Deployments Safer?

Deploying small changes frequently is safer because there are fewer modifications to investigate if something goes wrong, making bugs easier to identify, troubleshoot, and fix.

Smaller deployments also:
- Reduce the risk of major system failures.
- Make rollbacks easier.
- Provide faster feedback.
- Make software delivery more predictable and reliable.

### 3. Why Can Developers and Operations Teams Have Conflicting Goals?

Developers want to release new features quickly, while Operations wants to minimize changes to avoid system failures and downtime.

DevOps resolves this conflict by promoting:
- Collaboration.
- Shared responsibility.
- Automation through CI/CD.
- Continuous monitoring.

Both teams work toward the same goal: delivering software quickly, reliably, and safely.

### 4. How Do We Measure DevOps Performance?

DevOps performance can be evaluated using four key metrics.

**Speed (How fast do we deliver?)**

| Metric | Description |
|---|---|
| Deployment Frequency | How often code is released to production. |
| Lead Time for Changes | How long it takes for a code change to reach production after being committed. |

**Stability (How reliable is delivery?)**

| Metric | Description |
|---|---|
| Change Failure Rate | The percentage of deployments that cause problems in production. |
| Time to Restore Service | How long it takes to recover when something breaks. |

### 5. Deploying a Flask Application to a New Ubuntu Server

**Scenario:** A Flask application uses PostgreSQL and runs locally on a developer's laptop. What manual steps are required to make it accessible over the internet?

**Step 1: Server Preparation**
- Provision a new Ubuntu server.
- Connect to the server through SSH.
- Update system packages.
- Install Python, PostgreSQL, Git, and required dependencies.
- Clone the Flask application repository.

**Step 2: Application Configuration**
- Configure PostgreSQL.
- Create a database and database user.
- Configure database permissions.
- Set environment variables and application secrets.
- Install Python dependencies.
- Configure Flask with a production WSGI server such as Gunicorn.
- Test the application.

**Step 3: Deployment and Networking**
- Configure Nginx as a reverse proxy.
- Configure a domain name and DNS records.
- Enable HTTPS using an SSL/TLS certificate.
- Configure firewall rules.
- Create a systemd service to manage the application.
- Start the application and verify that it is accessible over the internet.

---

## Quick Check: Git & SSH

### 1. SSH Keys: Private vs. Public

SSH uses a pair of cryptographic keys to authenticate users securely.

**Private Key: `~/.ssh/id_ed25519`**

- This is your secret SSH key.
- It proves your identity when connecting to remote servers or services such as GitHub.
- It must remain secure on your computer.
- Never share it, upload it to GitHub, or send it to anyone.
- Anyone who obtains it could potentially impersonate you.

**Public Key: `~/.ssh/id_ed25519.pub`**

- This is your public SSH key.
- It is mathematically linked to your private key.
- You can safely share it with services such as GitHub, GitLab, or remote Linux servers.
- It allows those services to recognize and authenticate your SSH connection.

**Remember:**
- Private key = NEVER SHARE.
- Public key = SAFE TO SHARE.

### 2. What Is `.gitkeep`?

`.gitkeep` is a naming convention used to make Git track an otherwise empty directory.

Git tracks files rather than empty directories. By placing a `.gitkeep` file inside an empty directory, Git can preserve that directory in the repository.

Example:

```text
my-project/
├── src/
├── logs/
│   └── .gitkeep
└── uploads/
    └── .gitkeep
```

**Note:** `.gitkeep` is not an official Git command or feature. It is simply a convention used by developers.

### 3. Difference Between `git add` and `git commit`

**`git add` — Stage Your Changes**

When you modify a file, Git detects the modification but doesn't automatically include it in your next commit.

You use `git add` to select which changes you want to include.

```bash
git add app.py
```

To stage all changes:

```bash
git add .
```

**`git commit` — Save Your Changes**

Once you've staged your changes, you use `git commit` to create a snapshot in your Git history.

```bash
git commit -m "Add user authentication"
```

**Git Workflow:**

```text
Working Directory
       |
       | git add
       v
  Staging Area
       |
       | git commit
       v
 Local Repository
       |
       | git push
       v
 Remote Repository (GitHub)
```

**Important Git Commands**

| Command | Purpose |
|---|---|
| `git status` | Check modified and staged files. |
| `git add .` | Stage all changes. |
| `git add app.py` | Stage a specific file. |
| `git commit -m "message"` | Create a commit. |
| `git log` | View commit history. |
| `git push` | Upload commits to a remote repository. |
| `git pull` | Retrieve and integrate remote changes. |