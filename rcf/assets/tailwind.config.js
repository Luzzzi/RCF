module.exports = {
  content: [
    "./rcf/**/*.{html,js,jsx,ts,tsx}",
    "./src/**/*.{html,js}",
    "../rcf/templates/**/*.html",
    "../rcf/**/templates/**/*.html", // Spécifiez ici vos templates Wagtail
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
};
