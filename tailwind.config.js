/** Tailwind config for the static build.
 * Rebuild CSS with: npx -y tailwindcss@3.4.17 -c tailwind.config.js -o assets/tailwind.css --minify
 */
module.exports = {
  content: ["./**/*.html"],
  // 'hidden' is toggled from JS at runtime, so it may not appear in markup
  safelist: ["hidden"],
  theme: { extend: {} },
  plugins: [],
};
