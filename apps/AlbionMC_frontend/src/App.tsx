import { Component } from 'solid-js';
import NavBar from './components/navbar';
import Footer from './components/footer';
import { AuthProvider } from './components/authProvider';
import { Screen } from './components/screen';
import Welcome from './components/welcome';

const App: Component = () => {

  return (
    <>
      <AuthProvider>
        <NavBar />
        <Screen>
          <Welcome />
        </Screen>
        <Footer />
      </AuthProvider>
    </>
  );
}

export default App;