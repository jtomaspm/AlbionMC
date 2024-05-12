import { createSignal, Component } from 'solid-js';
import Welcome from "./components/welcome";
import NavBar from './components/navbar';
import Footer from './components/footer';
import { AuthProvider } from './components/authProvider';

const App: Component = () => {
  const [scrollPosition, setScrollPosition] = createSignal(0);

  window.addEventListener("scroll", () => {
    setScrollPosition(window.scrollY);
  });

  return (
    <>
      <AuthProvider>
        <NavBar />
        <Footer />
      </AuthProvider>
    </>
  );
}

export default App;