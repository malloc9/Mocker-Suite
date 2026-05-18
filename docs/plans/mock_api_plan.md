Step 2: Detailed Plan for the Unified Mock API Builder
Objective: To design and implement the core backend and frontend features that allow users to create, store, and serve dynamic mock API endpoints from a single unified platform.

Success Criteria:

A RESTful API under /api/mocks allows for the creation, retrieval, updating, and deletion of mock endpoint configurations.

Mock configurations are persistently stored using an SQLite database.

The frontend provides a user-friendly form to create and edit mock endpoints.

A dynamic Express middleware is implemented that reads configurations from the database and serves mock responses, bypassing the need for a server restart.

Part 1: Design the Mock Configuration API
We will build a clean RESTful API to manage mock endpoint configurations. This API will be the single point of interaction for the frontend.

Define the Core Data Model (SQLite Schema):

We need a single mocks table to store all configurations.

Action: Create a new migration file (apps/api/src/db/migrations/001_create_mocks.sql).

Schema Design:

sql
CREATE TABLE IF NOT EXISTS mocks (
  id TEXT PRIMARY KEY,            -- UUID for each mock
  method TEXT NOT NULL,           -- 'GET', 'POST', 'PUT', 'PATCH', 'DELETE'
  path TEXT NOT NULL,            -- e.g., '/api/users'
  response_status INTEGER NOT NULL DEFAULT 200, -- HTTP status code
  response_body TEXT,            -- JSON string for the response body
  response_headers TEXT,         -- JSON string for key-value header pairs
  description TEXT,              -- A user-friendly name or description
  is_active INTEGER NOT NULL DEFAULT 1, -- 0 or 1 to quickly toggle the mock
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE UNIQUE INDEX idx_method_path ON mocks (method, path);
We use TEXT for id to avoid auto-incrementing integer complexities and to allow UUIDs. The response_body and response_headers are stored as JSON strings for maximum flexibility, which better-sqlite3 handles easily. A unique index on (method, path) prevents duplicate mocks for the same endpoint.

Implement the Database Layer (apps/api/src/db):

Action: Create apps/api/src/db/connection.ts.

Initialize better-sqlite3 with a file-based database (e.g., mocks.db). Enable WAL mode and foreign keys for better performance and integrity, as is best practice.

typescript
import Database from 'better-sqlite3';
import path from 'path';

const DB_PATH = path.join(__dirname, '..', '..', 'data', 'mocks.db');
const db = new Database(DB_PATH);
db.pragma('journal_mode = WAL');
db.pragma('foreign_keys = ON');
export default db;
Action: Create apps/api/src/db/mockRepository.ts. This module will contain all data access functions using the synchronous better-sqlite3 API. Functions to create: createMock, findMockById, findMocks, updateMock, deleteMock.

Build the RESTful API Routes (apps/api/src/routes/mocks.ts):

Create an Express Router to handle CRUD operations.

API Endpoints:

POST /api/mocks: Create a new mock configuration. Validates the request body, generates a UUID, and saves it via the repository.

GET /api/mocks: List all mock configurations.

GET /api/mocks/:id: Get a single mock by its ID.

PUT /api/mocks/:id: Update an existing mock configuration.

DELETE /api/mocks/:id: Delete a mock configuration.

Use a validation library (like zod) to ensure the incoming JSON matches our schema.

Part 2: Implement the Dynamic Mock-Serving Engine
This is the heart of Mocker Suite. Instead of a static mock server requiring a restart, we'll build a custom Express middleware that dynamically loads and serves mocks from the database. This approach is more powerful and directly aligns with tools like hmpo-stubber that create stub APIs using simple configurations.

Create the mockRouter Middleware (apps/api/src/middleware/mockRouter.ts):

Action: Export an Express middleware function.

Logic:

It intercepts every incoming request.
Parses the request's method and path.
Queries the mocks table in real-time using the mockRepository for a matching active configuration (is_active = 1).
If a match is found, it responds immediately with the configured response_status, response_headers, and response_body from the database.
If no match is found, it calls next() to allow the request to pass through (potentially to a backend API for proxying in future steps).
Integrate the Middleware into the Main Express App (apps/api/src/index.ts):

This middleware must be loaded before any other route handlers to ensure it catches requests first. This effectively turns our API server into a combined management API and mock-serving server.

Use an Off-the-Shelf Solution (Alternative/Complement):

For more advanced features like proxying or complex response manipulation, we can wrap a library like hmpo-stubber or dynamic-mock-express.

Action: Instead of writing all the low-level logic, we could use hmpo-stubber's ability to create dynamic stubs from JSON configurations. Our mockRouter middleware would then programmatically configure and update hmpo-stubber's runtime whenever a mock is changed via the management API. This gives us battle-tested functionality without reinventing the wheel.

Part 3: Create the Frontend Mock Builder UI
The frontend will allow users to manage their mocks without writing SQL or editing JSON files directly. We'll build a clean, form-based interface in our Next.js app.

Design the Form Component Structure (apps/web/src/components/MockForm.tsx):

Action: Create a reusable form component. We can leverage a library like react-declarative which interacts with JSON endpoints for dynamic form generation, or build it from scratch with a simpler approach.

Form Fields:

HTTP Method: A dropdown/select component with values (GET, POST, PUT, PATCH, DELETE).

Path: A text input for the endpoint path (e.g., /api/users/123).

Response Status Code: A number input or select for the HTTP status code.

Response Body: A textarea, ideally with a built-in JSON editor (like a lightweight code editor component) for syntax highlighting and validation.

Response Headers: A dynamic key-value pair editor.

Description: A text input for a user-friendly label.

Active Toggle: A switch component.

Build the Main Dashboard Page (apps/web/src/app/mocks/page.tsx):

Action: Create a new page in the Next.js app router.

Layout: A two-column layout. The left column contains a list of all saved mocks (fetched via GET /api/mocks). The right column displays the MockForm component.

Functionality:

Clicking a mock in the list populates the form for editing.

A "New Mock" button clears the form.

A "Save" button in the form sends a POST or PUT request to the management API.

A "Delete" button on a list item sends a DELETE request.

Create a Mock Tester Component:

Action: Add a panel below the form where a user can "Test" the mock endpoint.

It provides a "Send Request" button that fires a real HTTP request to the path of the mock endpoint served by our backend. The response (status, headers, body) is displayed directly in the UI, creating a tight feedback loop. This is similar to how @r35007/mock-server allows for quick prototyping.

Part 4: Integration and Verification
Unify the Development Workflow:

The frontend Next.js dev server runs on port 3000.

The backend Express server runs on port 3001.

Action: Configure the Next.js next.config.mjs to proxy API requests from /api to http://localhost:3001. This avoids CORS issues during development.

End-to-End Verification Test:

Action: Write a single, critical E2E test using Playwright or Cypress.

Test Flow: The test opens the Mocker Suite UI, creates a new mock endpoint (e.g., GET /test returning { "hello": "world" }), then directly calls http://localhost:3001/test and asserts that the response is exactly as configured. This proves the entire loop works.

This plan delivers the core "Unified Mock API Builder." We've designed a database-backed, API-driven system where users can visually manage mocks that are instantly served by a dynamic middleware. This modular foundation makes it easy to later integrate additional free services for geolocation and webhook testing.
