import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
// Relative base + HashRouter: works at https://sdpursley.github.io/ESL-Curriculum/ with no server routing.
export default defineConfig({ base: './', plugins: [react(), tailwindcss()], build: { assetsInlineLimit: 0 } })
