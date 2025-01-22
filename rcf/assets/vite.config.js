import { defineConfig } from "vite";

export default defineConfig({
  server: {
    host: "localhost",
    port: 5173,
    strictPort: true,
    open: false,
    watch: {
      usePolling: true,
      disableGlobbing: false,
    },
    proxy: {
      "/static": "http://localhost:8000", // Proxy les requêtes vers Django si nécessaire
      "/@vite": "http://localhost:5173", // Assure-toi que les fichiers HMR sont correctement proxyfiés
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
