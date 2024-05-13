import { Component, createEffect, createSignal } from 'solid-js';
import NavBar from './components/navbar';
import Footer from './components/footer';
import { useAuth } from './components/authProvider';
import { Screen } from './components/screen';
import { screens } from './config/screens'
import { themes } from './config/themes'
import { API_REQUEST } from './service/api';
import { UserPreferencesRequest } from './types/userPreferences';

const App: Component = () => {
  const { user, login, logout, loading } = useAuth();
  const [selectedScreen, setSelectedScreen] = createSignal<string>('profile');
  const [theme, setTheme] = createSignal<string>('dim');

  const handleScreenChange = (screenName: string) => {
    setSelectedScreen(screenName);
  };

  const handleThemeChange = (themeName: string) => {
    setTheme(themeName)
    if (!user()) return;

    API_REQUEST(
      '/user_preferences/',
      'POST',
      {},
      JSON.stringify({
        user_id: user()?.data.id,
        theme: themeName
      } as UserPreferencesRequest),
      user()?.token
    );
  };

  createEffect(() => {
    if(user()?.preferences != null && themes.includes(user()!.preferences.theme)){
      setTheme(user()!.preferences.theme)
    }
  });


  return (
    <div data-theme={theme()}>
      <NavBar onSelectScreen={handleScreenChange} setTheme={handleThemeChange} themes={themes} theme={theme} />
      <Screen>
        {
          screens[selectedScreen()] ??
          screens["error"]
        }
      </Screen>
      <Footer />
    </div>
  );
}

export default App;