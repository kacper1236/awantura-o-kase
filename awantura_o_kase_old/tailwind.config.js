/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./panel_admin/static/*.{html,js}",
    "./panel_admin/templates/*.{html,js}",
    "./panel_admin/static/node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('./panel_admin/static/node_modules/flowbite/plugin')
  ],
}

