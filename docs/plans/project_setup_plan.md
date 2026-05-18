A Detailed Plan for Project Setup
Before writing any business logic, we need to establish a disciplined development environment. This initial step is not just about creating folders; it's about setting up a framework that ensures code quality, consistency, and reliability from day one, preventing technical debt from accumulating as we build features.

Objective: To initialize the frontend and backend projects within a monorepo structure, configure version control, and set up a fully automated quality pipeline for linting, formatting, and testing.

Success Criteria:

A monorepo with separate apps/web (frontend) and apps/api (backend) directories is functional.

Running pnpm install at the project root successfully installs all dependencies.

A developer can run a single command (e.g., pnpm run check) to lint, format-check, and test the entire codebase.

A pre-commit hook automatically runs the quality checks before any code is committed.

Part 1: Initialize the Monorepo Structure
A monorepo keeps our frontend and backend in a single repository, which simplifies dependency management and code sharing.

Create the Project Root and Initialize:

Create a new directory for your project (e.g., mocker-suite) and navigate into it.

Initialize the root package.json with pnpm init. Set "private": true to prevent accidental publication of the root workspace.

Configure pnpm Workspaces:

Create a pnpm-workspace.yaml file in the project root. This tells pnpm where to find the packages in our monorepo.

Add the following configuration to define the locations of our applications:

yaml
packages:
  - "apps/*"
Scaffold Application Directories:

Create the apps/ directory.

Inside apps/, create two subdirectories: web and api.

Navigate into both apps/web and apps/api and initialize each with its own package.json using pnpm init. Name them appropriately (e.g., @mocker-suite/web and @mocker-suite/api).

Part 2: Frontend and Backend Initialization
We'll set up the two projects with their core frameworks. For a B2B SaaS, a robust frontend framework like Next.js and a strongly-typed backend are crucial.

Initialize the Frontend (apps/web):

Choose a battle-tested starter. Next.js with TypeScript is the industry standard for SaaS applications due to its performance and features.

Action: Use the official Next.js creation command inside the apps/web directory: npx create-next-app@latest . --typescript --tailwind --eslint --app --src-dir --import-alias "@/*".

This command will automatically configure TypeScript, Tailwind CSS for styling, and ESLint for code quality.

Initialize the Backend (apps/api):

For maximum flexibility with our free resources, a standard Express.js server with TypeScript provides a solid foundation without imposing too many opinions.

Action: Inside apps/api, install the core dependencies manually:

bash
pnpm add express cors dotenv
pnpm add -D typescript @types/express @types/node ts-node nodemon
Create a basic tsconfig.json file and a src/index.ts file that starts a simple Express server on a port like 3001. This confirms the backend can run independently.

Part 3: Configure the Unified Quality Toolchain
Consistent code is critical for maintainability. We will implement an automated quality pipeline that all developers and CI/CD systems will use.

Install and Configure Linting and Formatting:

To maximize speed and simplicity, we'll use Biome, a modern all-in-one tool that replaces ESLint and Prettier.

Action at the Root:

Install Biome: pnpm add -D -w @biomejs/biome.

Create a biome.json configuration file at the root. This file will contain the formatting and linting rules for the entire monorepo.

Tip: Start with Biome's recommended settings by running pnpm biome init and then customize the biome.json as needed.

Create Unified NPM Scripts:

The root package.json is the control panel for our monorepo. Add the following scripts to orchestrate operations across all applications:

json
"scripts": {
  "dev:web": "pnpm --filter @mocker-suite/web dev",
  "dev:api": "pnpm --filter @mocker-suite/api dev",
  "lint": "pnpm -r lint",
  "format": "biome format --write .",
  "format:check": "biome format .",
  "check": "biome check .",
  "test": "pnpm -r test"
}
Update the scripts in apps/web/package.json and apps/api/package.json to include "lint": "biome lint ." and "test": "vitest run".

Install and Configure a Unified Testing Framework (Vitest):

Vitest is a blazing-fast, Vite-native unit testing framework that works perfectly in our environment.

Action at the Root: Install Vitest as a dev dependency for the whole workspace: pnpm add -D -w vitest.

Create a vitest.config.ts file in both apps/web and apps/api to configure their test environments. A sample test file (e.g., index.test.ts) should be added to verify the setup.

Part 4: Automate Checks with Git Hooks and CI
The final step is to make this quality pipeline automatic, preventing bad code from being committed or merged.

Set Up a Pre-Commit Hook with Husky:

Husky allows us to run scripts in response to Git events.

Action at the Root:

Install and initialize Husky: pnpm add -D -w husky && npx husky init.

This creates a .husky/ directory. Edit the .husky/pre-commit file to run our unified checks on files that are about to be committed:

bash
pnpm run format:check
pnpm run lint
pnpm run test
Draft the Baseline CI Workflow (GitHub Actions):

We will create a workflow that runs the exact same quality checks on every push and pull request, ensuring our rules are enforced remotely.

Action: Create the file .github/workflows/quality.yml with the following content:

yaml
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
This completes the initial setup. We now have a monorepo with initialized frontend and backend projects, a powerful automated quality pipeline, and a CI/CD configuration that will validate every change. This solid foundation allows us to focus entirely on building Mocker Suite's features, like integrating mock APIs and webhook testing tools, with complete confidence.
