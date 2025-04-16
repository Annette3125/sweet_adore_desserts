'use strict';

function setTheme(mode) {
    if (mode !== "light" && mode !== "dark" && mode !== "auto") {
        console.error(`Got invalid theme mode: ${mode}. Resetting to auto.`);
        mode = "auto";
    }
    document.documentElement.dataset.theme = mode;
    localStorage.setItem("theme", mode);
}

function cycleTheme() {
    const currentTheme = localStorage.getItem("theme") || "auto";
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

    let mode;  // Būtinai deklaruojame čia

    if (prefersDark) {
        // Auto (dark) -> Light -> Dark
        if (currentTheme === "auto") {
            mode = "light";
        } else if (currentTheme === "light") {
            mode = "dark";
        } else {
            mode = "auto";
        }
    } else {
        // Auto (light) -> Dark -> Light
        if (currentTheme === "auto") {
            mode = "dark";
        } else if (currentTheme === "dark") {
            mode = "light";
        } else {
            mode = "auto";
        }
    }

    setTheme(mode);  // Tik vienas kvietimas, kai mode jau priskirtas
}

function initTheme() {
    const currentTheme = localStorage.getItem("theme");
    if (currentTheme) {
        setTheme(currentTheme);
    } else {
        setTheme("auto");
    }
}

window.addEventListener('load', () => {
    initTheme();
    const buttons = document.getElementsByClassName("theme-toggle");
    Array.from(buttons).forEach(btn => btn.addEventListener("click", cycleTheme));
});
