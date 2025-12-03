module.exports = {
    content: [
        "./templates/**/*.html",          // base.html, home.html
        "./core/templates/**/*.html",     // app core
        "./theme/templates/**/*.html",    // app theme
        "./**/templates/**/*.html",       // qualquer outro app
    ],
    theme: {
        extend: {},
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
