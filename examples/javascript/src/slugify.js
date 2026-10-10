/** Lowercase text and join whitespace-separated words with hyphens. */
export function slugify(text) {
  return text.trim().toLowerCase().split(/\s+/u).join('-');
}
