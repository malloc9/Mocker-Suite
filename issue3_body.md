**Objective:** Initialize the backend application using Express.js with TypeScript.

**Tasks:**
- [ ] Navigate to `apps/api` directory
- [ ] Install core dependencies: `pnpm add express cors dotenv`
- [ ] Install development dependencies: `pnpm add -D typescript @types/express @types/node ts-node nodemon`
- [ ] Create a basic `tsconfig.json` file
- [ ] Create a `src/index.ts` file that starts a simple Express server on a port like 3001
- [ ] Add a "dev" script to `package.json` to run the server with nodemon: `"dev": "nodemon src/index.ts"`

**Success Criteria:**
- The backend application is initialized and can be run with `pnpm dev`
- The Express server starts successfully on port 3001 (or configured port)
- The project uses TypeScript and has a basic server setup.

**Note:** This assumes the monorepo structure is already set up (from issue #3) and we are working inside the `apps/api` directory.

**Related Files:**
- apps/api/package.json
- apps/api/tsconfig.json
- apps/api/src/index.ts

**Labels:** setup, backend