import { defineConfig } from "vite";

export default defineConfig({
  plugins: [],
  root: "./static_src",
  base: "/static/",
  server: {
    host: "localhost",
    port: 5173,
    strictPort: true,
    open: false,
    hmr: true,
    watch: {
      usePolling: true,
      disableGlobbing: false,
    },
    resolve: {
      extensions: [
        ".js",
        ".json",
        ".scss",
        ".css",
        ".ts",
        ".woff2",
        ".woff",
        ".svg",
      ],
    },
  },
  build: {
    outDir: "../rcf/static/dist", // Dossier où Vite va générer les fichiers
    emptyOutDir: true, // Vider ce dossier à chaque build
    rollupOptions: {
      input: "./src/main.js", // Ton fichier JavaScript d'entrée
      output: {
        // Forcer tous les fichiers (JS, CSS, assets) à être générés dans `dist/`
        entryFileNames: "[name].js",
        chunkFileNames: "[name].js",
        assetFileNames: "[name][extname]",
      },
    },
  },
});
