const defaultTheme = require("tailwindcss/defaultTheme");
module.exports = {
  content: [
    "./templates/**/*.html", // Scanne les templates pour les classes
    "./static_src/js/**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
};
