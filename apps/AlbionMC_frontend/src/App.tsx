import { createSignal, Component } from 'solid-js';
import Welcome from "./components/welcome";

const App: Component = () => {
  const [scrollPosition, setScrollPosition] = createSignal(0);

  window.addEventListener("scroll", () => {
    setScrollPosition(window.scrollY);
  });

  return (
    <div class="bg-gray-600 font-family-karla flex">
      <aside class="relative bg-sidebar h-screen w-64 hidden sm:block shadow-xl">
        <div class="p-6">
          <p class="text-black text-3xl font-semibold">AlbionMC</p>
        </div>
        <nav class="text-white text-base font-semibold pt-3">
          {/* Your navigation links */}
            <a href="index.html" class="flex items-center active-nav-link text-white py-4 pl-6 nav-item">
                <i class="fas fa-tachometer-alt mr-3"></i>
                Welcome
            </a>
            <a href="blank.html" class="flex items-center text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item">
                <i class="fas fa-sticky-note mr-3"></i>
                Items
            </a>
            <a href="tables.html" class="flex items-center text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item">
                <i class="fas fa-table mr-3"></i>
                Crafting Slots
            </a>
            <a href="forms.html" class="flex items-center text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item">
                <i class="fas fa-align-left mr-3"></i>
                Item Prices
            </a>
            <a href="tabs.html" class="flex items-center text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item">
                <i class="fas fa-tablet-alt mr-3"></i>
                Data Sources
            </a>
            <a href="calendar.html" class="flex items-center text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item">
                <i class="fas fa-calendar mr-3"></i>
                Settings
            </a>
        </nav>
        <a class="absolute w-full upgrade-btn bottom-0 active-nav-link text-white flex items-center justify-center py-4">
          <i class="fas fa-arrow-circle-up mr-3"></i>
            User Info
        </a>
      </aside>

      <div class="w-full flex flex-col h-screen overflow-y-hidden">
        {/* Your header JSX */}
        <main class="w-full flex-grow p-6">
          {/* Your main content JSX */}
        </main>
        <footer class="w-full bg-gray-600 text-white text-right p-4 sm:block shadow-xl">
          Follow on <a target="_blank" href="https://github.com/jtomaspm/AlbionMC" class="underline">Github</a>.
        </footer>
      </div>
    </div>
  );
}

export default App;