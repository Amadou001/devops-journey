# Lesson 3: CI/CD and Automated Pipelines

## Assignment 3

### 1. Difference Between Continuous Integration, Continuous Delivery, and Continuous Deployment

These three concepts describe different levels of automation in the software delivery process.

**Continuous Integration (CI)**

Developers frequently integrate their code changes into a shared repository. Each change triggers automated processes such as building the application and running tests to detect problems early.

**Continuous Delivery (CD)**

After successful integration and testing, the application is automatically prepared for release and can be deployed to production at any time. However, a human must approve the production deployment.

**Continuous Deployment (CD)**

Every code change that successfully passes the automated pipeline is automatically deployed to production without requiring human approval.

**Comparison:**

| Practice | What Happens? | Human Approval? |
|---|---|---|
| Continuous Integration | Code is integrated, built, and tested automatically. | No production approval involved. |
| Continuous Delivery | Code is automatically prepared for production. | Yes, before production deployment. |
| Continuous Deployment | Code is automatically deployed to production after passing tests. | No. |

**Key distinction:** Continuous Delivery includes a manual approval step before production deployment, whereas Continuous Deployment does not.

### 2. Experiment: What Happens When We Remove `set -e`?

**What is `set -e`?**

In a Bash script, `set -e` tells the shell to exit when a command fails (returns a non-zero exit status), subject to certain shell-context exceptions.

**Experiment:**

1. Open `pipeline.sh`.
2. Remove the `set -e` line.
3. Intentionally break a test.
4. Run the pipeline again.

**What happens?**

Without `set -e`, the script may continue executing even after a command fails. For example, tests can fail, but the pipeline may still proceed to package the application and generate an artifact.

Depending on the remaining commands, the script could even finish with a successful exit status despite the failed test.

**Why is this dangerous in a real company?**

- Broken code could be packaged and deployed.
- Failed tests might go unnoticed.
- Production could become unstable.
- Users could experience application failures.

**Conclusion:**

`set -e` helps prevent a pipeline from continuing after unexpected command failures. However, it should be combined with explicit error handling and proper exit-status checks.

**Important:** Restore `set -e` after completing the experiment.

### 3. Why Name Artifacts Using the Commit Hash?

An artifact is a packaged version of an application that is ready to be deployed.

Using a Git commit hash in the artifact name makes it possible to identify exactly which version of the source code produced that artifact.

Example:

```text
app-a82f91c.tar.gz
```

Instead of:

```text
app-latest.tar.gz
```

**Why is this important?**

- **Traceability:** We can identify the exact source-code version associated with an artifact.
- **Rollback:** We can redeploy a previously working version if a new deployment fails.
- **Debugging:** We can investigate which code changes introduced a problem.
- **Version control:** Different builds can be stored and identified without overwriting one another.

**Example:**

```text
app-a82f91c.tar.gz  → Previous stable version
app-b73d21e.tar.gz  → New version with a bug
```

If the new version causes problems, we can roll back to `app-a82f91c.tar.gz`.

### 4. Explain "Build Once, Deploy Many"

"Build once, deploy many" means creating an application artifact once and promoting that exact same artifact through different environments.

For example:

```text
       Source Code
            |
            v
       Build Artifact
            |
            v
       Automated Tests
            |
            v
       Development
            |
            v
        Staging
            |
            v
       Production
```

The same artifact is used in development, staging, and production.

**What could go wrong if we rebuilt the artifact separately for production?**

- Dependencies or package versions might change.
- Different build configurations could produce different results.
- The production artifact might behave differently from the tested staging artifact.
- A new bug could be introduced during the production build.

**Conclusion:**

Building once ensures consistency across environments and reduces the risk of deploying something different from what was tested.

Environment-specific settings, such as database credentials and API URLs, should be injected at deployment time rather than changing the artifact itself.

### 5. Experiment: Uncommitted Changes and Git Commit Hashes

**Scenario:**

You modify `app.py` without committing the changes, then execute your pipeline.

The artifact is named using your last Git commit hash, but it contains your latest uncommitted modifications.

**Why is this a problem?**

The artifact's name suggests that it represents a specific Git commit, but its actual contents include changes that are not part of that commit.

This creates a mismatch between the artifact identity and its source code.

**Potential problems:**

- Difficult debugging because the artifact cannot be reproduced from the commit.
- Incorrect rollback because the artifact does not represent the expected version.
- Loss of traceability.
- Inconsistent deployments.

**How do real CI systems avoid this?**

Real CI systems such as GitHub Actions generally obtain source code from a Git repository at a specific commit or ref when a workflow is triggered.

For example:

```yaml
name: CI Pipeline

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Get commit hash
        run: echo "COMMIT_HASH=$(git rev-parse HEAD)" >> $GITHUB_ENV

      - name: Build application
        run: |
          mkdir -p artifacts
          tar -czf artifacts/app-${COMMIT_HASH}.tar.gz app.py
```

**Why does this solve the problem?**

- GitHub Actions checks out the committed repository version.
- Uncommitted local changes are not included.
- The pipeline builds from a specific commit.
- The artifact can be traced back to its source commit.

**Conclusion:**

A reliable CI pipeline should build from a clean, committed source-code version rather than arbitrary local modifications.

---

## Key Takeaways

| Concept | What to Remember |
|---|---|
| Continuous Integration | Automatically integrate and test code changes. |
| Continuous Delivery | Keep software ready for production with human approval before release. |
| Continuous Deployment | Automatically deploy every change that passes the pipeline. |
| `set -e` | Helps stop Bash scripts when commands fail. |
| Commit Hash | Identifies the exact source-code version. |
| Build Once, Deploy Many | Promote the same artifact through multiple environments. |
| GitHub Actions | Builds and tests code from a checked-out repository version. |
| Artifact Traceability | Ensures deployed software can be linked to its source code. |

**Lesson 3 Objective:** Understand how CI/CD pipelines automate software integration, testing, packaging, and deployment while maintaining reliability, consistency, and traceability.