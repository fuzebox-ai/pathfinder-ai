# Pathfinder AI

> To provide clear, actionable insights for businesses to navigate complex market landscapes.

## Prerequisites

- [Node.js](https://nodejs.org/) 18 or higher
- [npm](https://www.npmjs.com/) (comes with Node.js) or [bun](https://bun.sh/)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/fuzebox-ai/pathfinder-ai.git
cd pathfinder-ai
```

### 2. Install dependencies

```bash
npm install
# or
bun install
```

### 3. Start the development server

```bash
npm run dev
# or
bun run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

## Available Scripts

| Command | Description |
|---|---|
| `npm run dev` | Start development server with HMR |
| `npm run build` | Build for production (output to `dist/`) |
| `npm run preview` | Preview the production build locally |
| `npm run lint` | Run ESLint |

## Tech Stack

- [React 18](https://react.dev/) — UI library
- [TypeScript](https://www.typescriptlang.org/) — type safety
- [Vite](https://vitejs.dev/) — build tool and dev server
- [ESLint](https://eslint.org/) — code quality

## Project Structure

```
pathfinder-ai/
├── public/          # Static assets
├── src/
│   ├── App.tsx      # Root component
│   ├── App.css      # App-level styles
│   ├── index.css    # Global styles
│   └── main.tsx     # Entry point
├── index.html       # HTML template
├── package.json
├── tsconfig.json
└── vite.config.ts
```

## Contributing

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Commit your changes: `git commit -m 'feat: add your feature'`
3. Push to the branch: `git push origin feature/your-feature`
4. Open a Pull Request targeting `main`

## License

© 2026 FuzeBox. All rights reserved.
