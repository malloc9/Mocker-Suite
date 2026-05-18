**Objective:** Create a GitHub Actions workflow for continuous integration that runs quality checks on every push and pull request.

**Tasks:**
- [ ] Create the directory `.github/workflows/` if it doesn't exist
- [ ] Create a file `.github/workflows/quality.yml` with the following content:
  ```yaml
  name: Quality Checks
  on: [push, pull_request]
  jobs:
    quality:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - uses: pnpm/action-setup@v2
        - uses: actions/setup-node@v4
          with:
            node-version: 20
            cache: 'pnpm'
        - run: pnpm install
        - run: pnpm run format:check
        - run: pnpm run lint
        - run: pnpm run test
  ```
- [ ] Verify the workflow triggers correctly on pushes and pull requests

**Success Criteria:**
- The GitHub Actions workflow runs automatically on every push and pull request
- The workflow executes the same quality checks as the local pre-commit hook (format check, lint, test)
- The workflow passes when code quality is maintained and fails when checks don't pass

**Related Files:**
- .github/workflows/quality.yml
- package.json (scripts: format:check, lint, test)

**Labels:** setup, ci-cd