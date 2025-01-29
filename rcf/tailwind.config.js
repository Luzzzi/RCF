const defaultTheme = require("tailwindcss/defaultTheme");
module.exports = {
  content: [
    "./templates/**/*.html", // Scanne les templates pour les classes
    "./static_src/js/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        "rcf-blue": "#001575",
        "rcf-orange": "#E07400",
        "rcf-grey": "#E7ECEF",
        "rcf-black": "#0A0903",
      },
      fontFamily: {
        text: "Caveat",
      },
    },
  },
  plugins: [require("daisyui")],
};
