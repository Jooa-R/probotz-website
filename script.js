const header = document.querySelector(".site-header");
const navToggle = document.querySelector(".nav-toggle");

if (header && navToggle) {
  header.classList.add("nav-enhanced");
  const label = navToggle.querySelector(".sr-only");
  const setOpen = (isOpen) => {
    header.classList.toggle("nav-open", isOpen);
    navToggle.setAttribute("aria-expanded", String(isOpen));
    label.textContent = isOpen ? "Close navigation" : "Open navigation";
  };
  navToggle.addEventListener("click", () => {
    setOpen(!header.classList.contains("nav-open"));
  });

  header.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      setOpen(false);
    });
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && header.classList.contains("nav-open")) {
      setOpen(false);
      navToggle.focus();
    }
  });
  document.addEventListener("click", (event) => {
    if (!header.contains(event.target)) setOpen(false);
  });
  window.matchMedia("(max-width: 1040px)").addEventListener("change", () => setOpen(false));
}
