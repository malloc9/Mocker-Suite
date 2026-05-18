**Objective:** Initialize the frontend application using Next.js with TypeScript, Tailwind CSS, and ESLint.

**Tasks:**
- [ ] Navigate to `apps/web` directory
- [ ] Run: `npx create-next-app@latest . --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"`
- [ ] This will configure TypeScript, Tailwind CSS, and ESLint automatically.

**Success Criteria:**
- The frontend application is initialized and can be run with `pnpm dev` (after adding the script)
- The project uses TypeScript, Tailwind CSS, and follows the app router structure with `src/` directory.

**Note:** This assumes the monorepo structure is already set up (from issue #3) and we are working inside the `apps/web` directory.

**Related Files:**
- apps/web/package.json
- apps/web/tsconfig.json
- apps/web/tailwind.config.js
- apps/web/next.config.js

**Labels:** setup, frontend