import { Component, createSignal } from 'solid-js';
import NavBar from './components/navbar';
import Footer from './components/footer';
import { AuthProvider } from './components/authProvider';
import { Screen } from './components/screen';
import { screens } from './config/screens'
import { themes } from './config/themes'

const App: Component = () => {
  const [selectedScreen, setSelectedScreen] = createSignal<string>('profile');
  const [theme, setTheme] = createSignal<string>('dim');

  const handleScreenChange = (screenName: string) => {
    setSelectedScreen(screenName);
  };

  return (
    <div data-theme={theme()}>
      <AuthProvider>
        <NavBar onSelectScreen={handleScreenChange} setTheme={setTheme} themes={themes} theme={theme} />
        <Screen>
          {
            screens[selectedScreen()] ??
            screens["error"]
          }
        </Screen>
        <Footer />
      </AuthProvider>
    </div>
  );
}

export default App;