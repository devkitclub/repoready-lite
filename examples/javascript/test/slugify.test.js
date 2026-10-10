import assert from 'node:assert/strict';
import test from 'node:test';
import { slugify } from '../src/slugify.js';

const cases = [
  ['RepoReady Lite', 'repoready-lite'],
  ['  Hello   World  ', 'hello-world'],
  ['Hello\tWorld\nAgain', 'hello-world-again'],
  ['', ''],
  ['   ', ''],
  ['Already-Slugged', 'already-slugged'],
];

for (const [input, expected] of cases) {
  test(`slugify ${JSON.stringify(input)}`, () => {
    assert.equal(slugify(input), expected);
  });
}
