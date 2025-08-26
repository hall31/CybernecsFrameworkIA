/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  output: 'standalone',
  env: {
    NEXT_PUBLIC_WS_LOGS_URL: process.env.NEXT_PUBLIC_WS_LOGS_URL || 'ws://localhost:8000/ws/logs',
    NEXT_PUBLIC_API_BASE_URL: process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000',
  },
}

module.exports = nextConfig