**Objective:** Configure a unified quality toolchain for the monorepo using Biome for linting and formatting, and Vitest for testing.

**Tasks:**
- [ ] Install Biome as a dev dependency for the whole workspace: `pnpm add -D -w @biomejs/biome`
- [ ] Create a `biome.json` configuration file at the root (start with recommended settings via `pnpm biome init` and customize as needed)
- [ ] Update the root `package.json` to include the following scripts:
    ```json
    "scripts": {
      "dev:web": "pnpm --filter @mocker-suite/web dev",
      "dev:api": "pnpm --filter @mocker-suite/api dev",
      "lint": "pnpm -r lint",
      "format": "biome format --write .",
      "format:check": "biome format .",
      "check": "biome check .",
      "test": "pnpm -r test"
    }
    ```
- [ ] Update the scripts in `apps/web/package.json` and `apps/api/package.json` to include:
    - `"lint": "biome lint ."`
    - `"test": "vitest run"`
- [ ] Install Vitest as a dev dependency for the whole workspace: `pnpm add -D -w vitest`
- [ ] Create a `vitest.config.ts` file in both `apps/web` and `apps/api` to configure their test environments
- [ ] Add a sample test file (e.g., `index.test.ts`) in each app to verify the test setup

**Success Criteria:**
- Running `pnpm run format:check`, `pnpm run lint`, and `pnpm run test` from the root executes the respective checks across all workspaces.
- The formatting and linting rules are consistent across the monorepo.
- Unit tests can be written and run with Vitest in both frontend and backend applications.

**Related Files:**
- biome.json
- package.json (root)
- apps/web/package.json
- apps/api/package.json
- apps/web/vitest.config.ts
- apps/api/vitest.config.ts

**Labels:** setup, quality-tooling