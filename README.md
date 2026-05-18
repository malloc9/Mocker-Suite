# Mocker Suite

A unified mocking platform that simulates an entire backend ecosystem, providing features for mock API building, dynamic responses, geolocation simulation, webhook testing, scenario orchestration, and team collaboration.

## Overview

Mocker Suite is designed to be a comprehensive mocking solution that integrates various mocking services into a cohesive platform. It aims to solve the challenge of modern frontend development where applications increasingly rely on complex backend interactions during development and testing.

## Key Features

- **Mock API Building**: Create and manage mock API endpoints with customizable responses
- **Dynamic Responses**: Generate responses based on request parameters, headers, or body content
- **Geolocation Simulation**: Simulate requests from different geographic locations
- **Webhook Testing**: Test webhook integrations with configurable endpoints and payloads
- **Scenario Orchestration**: Define and execute complex testing scenarios
- **Team Collaboration**: Share mock configurations and scenarios with team members

## Architecture

Mocker Suite follows a monorepo structure with separate applications:

- **Backend API** (`apps/api`): Core mocking service built with Node.js/TypeScript
- **Frontend Web** (`apps/web`): User interface built with Next.js/React

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- pnpm (package manager)
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/malloc9/Mocker-Suite.git
   cd Mocker-Suite
   ```

2. Install dependencies:
   ```bash
   pnpm install
   ```

### Development

To start the development servers:

```bash
# Start both frontend and backend
pnpm dev

# Or start individually
pnpm dev:api   # Backend API
pnpm dev:web   # Frontend web app
```

The backend API will be available at `http://localhost:3001`
The frontend web app will be available at `http://localhost:3000`

### Environment Variables

Create a `.env` file in the root directory based on the example below:

```env
# Backend API
PORT=3001
NODE_ENV=development

# Frontend
NEXT_PUBLIC_API_URL=http://localhost:3001
```

## Project Structure

```
Mocker-Suite/
├── apps/
│   ├── api/          # Backend API service
│   └── web/          # Frontend web application
├── issue*.md         # GitHub issue tracking files
├── PLAN.md           # Implementation plan
├── PROJECT.md        # Project vision and feature set
├── project_setup_plan.md  # Detailed setup instructions
├── package.json      # Root package.json (workspace configuration)
└── pnpm-lock.yaml    # Lock file for dependency management
```

## Technology Stack

- **Backend**: Node.js, TypeScript, Express/Vitest (testing)
- **Frontend**: Next.js, React, TypeScript, Tailwind CSS
- **Package Manager**: pnpm
- **Code Quality**: Biome (linting/formatting), Husky (git hooks)
- **Testing**: Vitest

## Development Guidelines

### Code Style

- Follow TypeScript strict mode
- Use functional components with hooks for React
- Maintain consistent naming conventions
- Write tests for new features

### Git Workflow

- Create feature branches from `main`
- Use descriptive commit messages
- Pull requests require review before merging
- Keep branches up to date with `main`

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or support, please open an issue in the GitHub repository.