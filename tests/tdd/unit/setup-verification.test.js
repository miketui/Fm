// TDD Setup Verification Test
// Constitutional Article III: Test-First Imperative

describe('TDD Setup Verification', () => {
  test('Jest configuration is working', () => {
    expect(true).toBe(true);
  });

  test('Global utilities are available', () => {
    expect(typeof global.readXHTMLFile).toBe('function');
    expect(typeof global.readCSSFile).toBe('function');
    expect(typeof global.fontExists).toBe('function');
  });

  test('Constitutional constants are defined', () => {
    expect(global.CONSTITUTIONAL_ARTICLES).toBeDefined();
    expect(global.TDD_PHASES).toBeDefined();
    expect(global.FRONTMATTER_FILES).toHaveLength(7);
    expect(global.CHAPTER_FILES).toHaveLength(16);
    expect(global.REQUIRED_FONTS).toHaveLength(6);
  });

  test('TDD methodology constants are available', () => {
    expect(global.TDD_PHASES.RED).toBe('Write failing tests');
    expect(global.TDD_PHASES.GREEN).toBe('Implement minimum code to pass');
    expect(global.TDD_PHASES.REFACTOR).toBe('Optimize while maintaining tests');
  });
});