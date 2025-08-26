/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Palette crypto/fintech
        crypto: {
          primary: '#6366f1',
          secondary: '#8b5cf6',
          accent: '#06b6d4',
          success: '#10b981',
          warning: '#f59e0b',
          danger: '#ef4444',
          dark: '#0f172a',
          darker: '#020617'
        },
        // Gradients personnalisés
        gradient: {
          'blue-purple': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
          'purple-pink': 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
          'cyan-blue': 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
          'purple-cyan': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
        }
      },
      fontFamily: {
        'crypto': ['Inter', 'system-ui', 'sans-serif'],
        'mono': ['JetBrains Mono', 'Fira Code', 'monospace']
      },
      animation: {
        'gradient': 'gradient 8s linear infinite',
        'float': 'float 6s ease-in-out infinite',
        'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'bounce-slow': 'bounce 3s infinite'
      },
      keyframes: {
        gradient: {
          '0%, 100%': {
            'background-size': '200% 200%',
            'background-position': 'left center'
          },
          '50%': {
            'background-size': '200% 200%',
            'background-position': 'right center'
          }
        },
        float: {
          '0%, 100%': {
            transform: 'translateY(0px)'
          },
          '50%': {
            transform: 'translateY(-20px)'
          }
        }
      },
      backdropBlur: {
        xs: '2px',
      },
      boxShadow: {
        'crypto': '0 0 20px rgba(99, 102, 241, 0.3)',
        'crypto-lg': '0 0 40px rgba(99, 102, 241, 0.4)',
        'glow': '0 0 20px rgba(139, 92, 246, 0.5)'
      }
    },
  },
  plugins: [],
}