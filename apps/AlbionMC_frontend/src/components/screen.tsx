import { Component, JSX } from "solid-js";
import { useAuth } from "./authProvider";

interface ScreenProps {
  children?: JSX.Element;
}


export const Screen: Component<ScreenProps> = props => {
  const { user, login, logout, loading } = useAuth();
  return (
    <div class="min-h-screen flex flex-col justify-center items-center">
        {
            user() == null ? <div>Please Login!</div> : 
            props.children 
        }
    </div>
  );
}