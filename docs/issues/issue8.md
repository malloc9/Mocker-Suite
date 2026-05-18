**Objective:** Automate quality checks before committing using Husky for Git hooks.

**Tasks:**
- [ ] Install Husky as a dev dependency for the whole workspace: `pnpm add -D -w husky`
- [ ] Initialize Husky: `npx husky init`
- [ ] This creates a `.husky/` directory. Edit the `.husky/pre-commit` file to run the following checks on staged files:
    ```bash
    pnpm run format:check
    pnpm run lint
    pnpm run test
    ```
- [ ] Make the `.husky/pre-commit` file executable if needed.

**Success Criteria:**
- Before any commit, the pre-commit hook runs formatting check, linting, and tests.
- If any of these checks fail, the commit is aborted.
- This ensures that only code passing quality checks is committed to the repository.

**Related Files:**
- .husky/pre-commit
- package.json (scripts: format:check, lint, test)

**Labels:** setup, git-hooks