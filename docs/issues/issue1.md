# Initialize Monorepo Structure

## Objective
Set up a monorepo structure with separate frontend and backend applications to simplify dependency management and code sharing.

## Tasks
- [ ] Create project root directory and initialize with `pnpm init` (set `"private": true`)
- [ ] Configure pnpm Workspaces by creating `pnpm-workspace.yaml` with:
  ```yaml
  packages:
    - "apps/*"
  ```
- [ ] Scaffold application directories: create `apps/` directory with `web` and `api` subdirectories
- [ ] Initialize each application with its own `package.json` using `pnpm init` (name them `@mocker-suite/web` and `@mocker-suite/api`)

## Success Criteria
- Monorepo structure is established with separate `apps/web` and `apps/api` directories
- Running `pnpm install` at project root successfully installs all dependencies

## Related Files
- `pnpm-workspace.yaml`
- `apps/web/package.json`
- `apps/api/package.json`

## Labels
setup, infrastructure