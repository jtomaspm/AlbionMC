import { Component, JSX, createSignal } from 'solid-js';
import NavBar from './components/navbar';
import Footer from './components/footer';
import { AuthProvider } from './components/authProvider';
import { Screen } from './components/screen';
import Welcome from './screens/welcome';
import { AllItems } from './screens/items/all';
import { CreateItems } from './screens/items/create';
import { AllCrafting } from './screens/crafting/all';
import { CreateCrafting } from './screens/crafting/create';
import { AllPrices } from './screens/prices/all';
import { CreatePrices } from './screens/prices/create';
import { AllSources } from './screens/sources/all';
import { CreateSources } from './screens/sources/create';
import Profile from './screens/profile';
import Settings from './screens/settings';
import Error from './screens/error';

const App: Component = () => {
  const [selectedScreen, setSelectedScreen] = createSignal<string>('welcome');

  const handleScreenChange = (screenName: string) => {
    setSelectedScreen(screenName);
  };

  const screens: { [key: string]: JSX.Element } = {
    'welcome': <Welcome />,
    'profile': <Profile />,
    'settings': <Settings />,
    'items/all': <AllItems />,
    'items/create': <CreateItems />,
    'crafting/all': <AllCrafting />,
    'crafting/create': <CreateCrafting />,
    'prices/all': <AllPrices />,
    'prices/create': <CreatePrices />,
    'sources/all': <AllSources />,
    'sources/create': <CreateSources />,
  };

  return (
    <>
      <AuthProvider>
        <NavBar onSelectScreen={handleScreenChange} />
        <Screen>
          {
            screens[selectedScreen()] ??
            <Error />
          }
        </Screen>
        <Footer />
      </AuthProvider>
    </>
  );
}

export default App;