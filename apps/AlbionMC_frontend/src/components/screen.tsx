import { Component, JSX } from "solid-js";

interface ScreenProps {
  children?: JSX.Element;
}


export const Screen: Component<ScreenProps> = props => {
  return (
    <div class="min-h-screen flex flex-col justify-center items-center">
      {props.children}
    </div>
  );
}