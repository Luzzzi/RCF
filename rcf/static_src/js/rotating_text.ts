document.addEventListener("DOMContentLoaded", () => {
  // On spécifie que "items" est une NodeList d'éléments HTML
  const items: NodeListOf<HTMLElement> =
    document.querySelectorAll(".rotating-item");
  let currentIndex: number = 0;

  const rotateTexts = (): void => {
    // Nombre total d'éléments
    const totalItems: number = items.length;

    // Réinitialiser les classes pour tous les éléments
    items.forEach((item) => {
      item.classList.remove("on", "before", "after");
    });

    // Définir l'élément actuel comme "on"
    const currentItem = items[currentIndex];
    currentItem.classList.add("on");

    // Définir l'élément précédent comme "before"
    const previousIndex = (currentIndex - 1 + totalItems) % totalItems;
    const previousItem = items[previousIndex];
    previousItem.classList.add("before");

    // Définir l'élément suivant comme "after"
    const nextIndex = (currentIndex + 1) % totalItems;
    const nextItem = items[nextIndex];
    nextItem.classList.add("after");

    // Mettre à jour l'index pour le prochain cycle
    currentIndex = nextIndex;
  };

  // Lancer la rotation toutes les 2 secondes
  setInterval(rotateTexts, 2000);

  // Initialiser l'affichage
  rotateTexts();
});
