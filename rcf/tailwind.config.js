const defaultTheme = require("tailwindcss/defaultTheme");
module.exports = {
  content: [
    "./rcf/**/*.{html,js,jsx,ts,tsx}",
    "./src/**/*.{html,js}",
    "../rcf/templates/**/*.html",
    "../rcf/**/templates/**/*.html",
    "./rcf/templates/**/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
};
