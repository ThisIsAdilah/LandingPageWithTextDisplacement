import { defineConfig } from 'vite';
import { copyFileSync, mkdirSync } from 'fs';
import { resolve } from 'path';

export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: undefined,
      }
    }
  },
  publicDir: 'public'
});

