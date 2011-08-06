/* import() needed files here. */
describe("import()", function() {
  it("should be able to import a file.", function() {
    import('interface.js');
    expect(imported).toBeTruthy();
  });
});
