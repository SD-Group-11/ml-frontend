module.exports = {
  preset: '@vue/cli-plugin-unit-jest',
  transform: {
    '^.+\\.vue$': 'vue-jest'
  },
  transformIgnorePatterns: ["/node_modules/(?!ag-grid-vue)"],
  collectCoverage:true
}
