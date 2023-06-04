/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html",],
  theme: {
    extend: {
      colors:{
        "custum-lite-green":"#c5efdf",
        "custom-bg":"#3d7063",
        "custom-green":"#265d58",
        "custom-dark-green":"#163129",
      },
    },
    fontFamily:{
      Ubuntu:["Ubuntu, san-serif"],
    },
  },
  plugins: [],
}

