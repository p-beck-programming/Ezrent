/** @type {import('tailwindcss').Config} */
module.exports = {
    // Specify files to scan for classes
    content: [
      "./templates/**/*.{html,htm}",
      "./static/src/**/*.{js,jsx,ts,tsx}",
      "./static/src/**/*.css",
    ],
    
    // Dark mode configuration
    darkMode: 'class', // or 'media' for OS-level dark mode preference
    
    theme: {
      extend: {
        // Custom colors
        colors: {
          primary: {
            50:  '#f0f9ff',
            100: '#e0f2fe',
            200: '#bae6fd',
            300: '#7dd3fc',
            400: '#38bdf8',
            500: '#0ea5e9',
            600: '#0284c7',
            700: '#0369a1',
            800: '#075985',
            900: '#0c4a6e',
            950: '#082f49',
          },
          secondary: {
            50:  '#f8fafc',
            100: '#f1f5f9',
            200: '#e2e8f0',
            300: '#cbd5e1',
            400: '#94a3b8',
            500: '#64748b',
            600: '#475569',
            700: '#334155',
            800: '#1e293b',
            900: '#0f172a',
            950: '#020617',
          },
        },
        
        // Custom spacing
        spacing: {
          '128': '32rem',
          '144': '36rem',
        },
        
        // Custom font families
        fontFamily: {
          sans: ['Inter', 'ui-sans-serif', 'system-ui', '-apple-system', 'sans-serif'],
          serif: ['Merriweather', 'ui-serif', 'Georgia', 'serif'],
          mono: ['Fira Code', 'ui-monospace', 'monospace'],
        },
        
        // Custom breakpoints
        screens: {
          'xs': '475px',
          'sm': '640px',
          'md': '768px',
          'lg': '1024px',
          'xl': '1280px',
          '2xl': '1536px',
        },
        
        // Custom animations
        animation: {
          'fade-in': 'fadeIn 0.5s ease-in',
          'slide-in': 'slideIn 0.5s ease-in',
        },
        
        // Custom keyframes
        keyframes: {
          fadeIn: {
            '0%': { opacity: '0' },
            '100%': { opacity: '1' },
          },
          slideIn: {
            '0%': { transform: 'translateY(-10px)', opacity: '0' },
            '100%': { transform: 'translateY(0)', opacity: '1' },
          },
        },
        
        // Custom border radius
        borderRadius: {
          '4xl': '2rem',
          '5xl': '2.5rem',
        },
        
        // Custom box shadows
        boxShadow: {
          'inner-lg': 'inset 0 2px 4px 0 rgb(0 0 0 / 0.15)',
          'custom': '0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)',
        },
      },
    },
    
    // Plugins
    plugins: [
      require('@tailwindcss/forms'),     // Add if using forms
      require('@tailwindcss/typography'), // Add if using prose classes
      require('@tailwindcss/aspect-ratio'), // Add if using aspect-ratio utilities
    ],
    
    // Prefix to avoid conflicts
    prefix: '',
    
    // Important configuration
    important: false,
    
    // Separator configuration
    separator: ':',
    
    // Future configuration
    future: {
      hoverOnlyWhenSupported: true,
      respectDefaultRingColorOpacity: true,
    },
    
    // Experimental features
    experimental: {
      optimizeUniversalDefaults: true,
    },
  }