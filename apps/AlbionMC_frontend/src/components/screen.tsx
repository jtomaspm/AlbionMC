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
    <div class="min-h-screen pt-56" style={{ "background-image": `url(${Wallpaper})`, "background-size": "cover", "background-position": "center" }}>
      <div class="min-h-screen flex flex-col items-center">
      {
        user() == null ? <Login /> :
          props.children
      }
      </div>
    </div>
  );
}