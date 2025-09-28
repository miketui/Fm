module.exports = {
  testEnvironment: 'jsdom',
  testMatch: ['**/tests/tdd/**/*.test.js'],
  setupFilesAfterEnv: ['<rootDir>/tests/tdd/setup.js'],
  collectCoverageFrom: [
    'scripts/validators/**/*.js',
    'scripts/tdd/**/*.js',
    '!**/*.test.js',
    '!**/node_modules/**'
  ],
  coverageThreshold: {
    global: {
      branches: 100,
      functions: 100,
      lines: 100,
      statements: 100
    }
  },
  coverageReporters: ['text', 'json', 'html'],
  verbose: true,
  testTimeout: 30000,
  maxWorkers: 4
};