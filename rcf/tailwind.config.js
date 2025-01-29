const defaultTheme = require("tailwindcss/defaultTheme");
module.exports = {
  content: [
    "./templates/**/*.html", // Scanne les templates pour les classes
    "./static_src/js/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        "rcf-blue": {
          50: "#f1f6ff",
          100: "#e5edff",
          200: "#cedeff",
          300: "#a7c1ff",
          400: "#7698ff",
          500: "#3f64ff",
          600: "#1838ff",
          700: "#0729fa",
          800: "#0522d2",
          900: "#061dac",
          950: "#001575",
        },
        "rcf-orange": {
          50: "#fffbea",
          100: "#fff3c5",
          200: "#ffe687",
          300: "#ffd348",
          400: "#ffbe1e",
          500: "#fc9c04",
          600: "#e07400",
          700: "#b94f04",
          800: "#963d0a",
          900: "#7b320c",
          950: "#471801",
        },
        "rcf-grey": "#E7ECEF",
        "rcf-black": "#0A0903",
      },
      fontFamily: {
        sans: ["Tahoma", "Arial", "sans-serif"], // Remplace la police sans-serif
        cursive: ["Brush Script MT"],
        mono: ["Courier New", "monospace"],
      },
    },
  },
  plugins: [require("daisyui")],
};
