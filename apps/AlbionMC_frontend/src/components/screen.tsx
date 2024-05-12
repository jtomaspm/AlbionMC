import { Component, JSX } from "solid-js";
import { useAuth } from "./authProvider";
import Login from "../screens/login";
import Wallpaper from '../../assets/wallpaper.png'

interface ScreenProps {
  children?: JSX.Element;
}


export const Screen: Component<ScreenProps> = props => {
  const { user, login, logout, loading } = useAuth();
  return (
    <div class="min-h-screen flex flex-col justify-center items-center">
      <div class="hero min-h-screen" style={{ "background-image": `url(${Wallpaper})` }}>
        <div class="hero-overlay bg-opacity-30"></div>
        {
          user() == null ? <Login /> :
            props.children
        }
      </div>
    </div>
  );
}