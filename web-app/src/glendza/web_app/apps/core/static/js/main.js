/* -------------- Constants -------------- */

const SHRUGGIE = "¯\\_(ツ)_/¯";

const THEMING_ATTRIBUTE_NAME = "data-theme";

const THEMES = {
  light: "light",
  dark: "dark",
};

const THEME_ICONS = {
  [THEMES.light]: "🌞",
  [THEMES.dark]: "🌚",
};

const CSS_VARIABLES = {
  headerBgOpacity: "--header-bg-opacity",
};

const LOCAL_STORAGE_PREFIX = "glendza";

const LOCAL_STORAGE_KEYS = {
  theme: `${LOCAL_STORAGE_PREFIX}:theme`,
  scrollPosition: `${LOCAL_STORAGE_PREFIX}:scrollPosition`,
};

// Example of a scroll position at which the header should be fully opaque
const HEADER_FULL_OPACITY_SCROLL_POSITION = 300;

const ELEMENT_IDS = {
  themeToggleButton: "theme-toggle-button",
};

/* -------------- Theme utils -------------- */

function getTheme() {
  // First check if the user has already declared a preference:.
  const configuredTheme = localStorage.getItem(LOCAL_STORAGE_KEYS.theme);
  if (configuredTheme && Object.values(THEMES).includes(configuredTheme)) {
    return configuredTheme;
  }

  // If not, check if the user has a system preference:
  const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");
  return prefersDarkScheme.matches ? THEMES.dark : THEMES.light;
}

function setTheme(theme) {
  document.documentElement.setAttribute(THEMING_ATTRIBUTE_NAME, theme);
}

function setThemeButtonAttributes(themeToggleButton, theme) {
  const inverseTheme = theme === THEMES.light ? THEMES.dark : THEMES.light;
  const label = `Switch to ${inverseTheme} mode`;
  themeToggleButton.title = label;
  themeToggleButton.ariaLabel = label;
  themeToggleButton.textContent = THEME_ICONS[theme];
}

function toggleTheme(themeToggleButton) {
  const currentTheme = document.documentElement.getAttribute(
    THEMING_ATTRIBUTE_NAME
  );
  const newTheme = currentTheme === THEMES.light ? THEMES.dark : THEMES.light;
  document.documentElement.setAttribute(THEMING_ATTRIBUTE_NAME, newTheme);
  localStorage.setItem(LOCAL_STORAGE_KEYS.theme, newTheme);
  setThemeButtonAttributes(themeToggleButton, newTheme);
}

function setUpTheming() {
  // First, set up the theme from the user's preference:
  const themeSetting = getTheme();
  setTheme(themeSetting);

  // Then, set up the toggle button:
  const themeToggleButton = document.getElementById(
    ELEMENT_IDS.themeToggleButton
  );

  if (!themeToggleButton) {
    console.warn(
      `No theme toggle button found with id "${ELEMENT_IDS.themeToggleButton}"`
    );
    return;
  }

  themeToggleButton.addEventListener("click", function () {
    toggleTheme(themeToggleButton);
  });
  setThemeButtonAttributes(themeToggleButton, themeSetting);
}

/* -------------- Header opacity -------------- */

function setHeaderBgOpacity() {
  const opacityValue = window.scrollY / HEADER_FULL_OPACITY_SCROLL_POSITION;
  document.documentElement.style.setProperty(
    CSS_VARIABLES.headerBgOpacity,
    opacityValue
  );
}

/* -------------- Scroll position -------------- */

function saveScrollPosition() {
  localStorage.setItem(LOCAL_STORAGE_KEYS.scrollPosition, window.scrollY);
}

function restoreScrollPosition() {
  const scrollPosition = localStorage.getItem(
    LOCAL_STORAGE_KEYS.scrollPosition
  );

  if (scrollPosition) {
    window.scrollTo(0, scrollPosition);
    localStorage.removeItem(LOCAL_STORAGE_KEYS.scrollPosition);
  }
}

/* -------------- Event handlers -------------- */

function onDOMContentLoaded() {
  setUpTheming();
  setHeaderBgOpacity();

  console.log(
    `%c${SHRUGGIE}`,
    "font-size: 30px; color: red; font-weight: bold;"
  );
}

function onWindowLoad() {
  restoreScrollPosition();
}

function onBeforeUnload() {
  saveScrollPosition();
}

function onScroll() {
  setHeaderBgOpacity();
}

/* -------------- Event listeners -------------- */

window.addEventListener("load", onWindowLoad);
document.addEventListener("DOMContentLoaded", onDOMContentLoaded);
window.addEventListener("scroll", onScroll);
window.addEventListener("beforeunload", onBeforeUnload);
