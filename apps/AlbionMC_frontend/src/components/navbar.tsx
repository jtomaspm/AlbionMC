import { Component } from "solid-js";
import { UserWidget } from "./userWidget";
import { useAuth } from "./authProvider";

const NavLinks: Component<NavBarProps> = function (props) {

    const handleScreenChange = (screenName: string) => {
        props.onSelectScreen(screenName);
    };

    return (
        <>
            <li>
                <details>
                    <summary>Items</summary>
                    <ul class="p-2">
                        <li><a onClick={() => handleScreenChange("items/all")}>All</a></li>
                        <li><a onClick={() => handleScreenChange("items/create")}>Create</a></li>
                    </ul>
                </details>
            </li>
            <li>
                <details>
                    <summary>Crafting</summary>
                    <ul class="p-2">
                        <li><a onClick={() => handleScreenChange("crafting/all")}>All</a></li>
                        <li><a onClick={() => handleScreenChange("crafting/create")}>Create</a></li>
                    </ul>
                </details>
            </li>
            <li>
                <details>
                    <summary>Prices</summary>
                    <ul class="p-2">
                        <li><a onClick={() => handleScreenChange("prices/all")}>All</a></li>
                        <li><a onClick={() => handleScreenChange("prices/create")}>Create</a></li>
                    </ul>
                </details>
            </li>
            <li>
                <details>
                    <summary>Sources</summary>
                    <ul class="p-2">
                        <li><a onClick={() => handleScreenChange("sources/all")}>All</a></li>
                        <li><a onClick={() => handleScreenChange("sources/create")}>Create</a></li>
                    </ul>
                </details>
            </li>
        </>
    )
}

interface NavBarProps {
    onSelectScreen: (screenName: string) => void;
    setTheme: (theme: string) => void;
    themes: string[];
    theme: () => string;
}

const NavBar: Component<NavBarProps> = function (props) {
    const { user, login, logout, loading } = useAuth();

    const handleScreenChange = (screenName: string) => {
        props.onSelectScreen(screenName);
    };

    return (
        <div class="navbar bg-base-100 fixed top-0 w-full z-10">
            <div class="navbar-start">
                <div class="dropdown">
                    <div tabIndex={0} role="button" class="btn btn-ghost lg:hidden">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h8m-8 6h16" /></svg>
                    </div>
                    {
                        user() != null ?
                            <ul tabIndex={0} class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
                                <NavLinks onSelectScreen={props.onSelectScreen} setTheme={props.setTheme} themes={props.themes} theme={props.theme}/>
                            </ul> : <></>
                    }
                </div>
            <div class="dropdown">
                <a tabIndex={0} class="btn btn-ghost text-xl">
                    AlbionMC
                    <svg width="12px" height="12px" class="h-2 w-2 fill-current opacity-60 inline-block" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2048 2048"><path d="M1799 349l242 241-1017 1017L7 590l242-241 775 775 775-775z"></path></svg>
                </a>
                <ul onChange={e => {props.setTheme((e.target as HTMLInputElement).value)}} tabIndex={0} class="dropdown-content z-[1] p-2 shadow-2xl bg-base-300 rounded-box w-52">
                    {
                        props.themes.map(item =>
                            <li><input type="radio" name="theme-dropdown" class="theme-controller btn btn-sm btn-block btn-ghost justify-start" aria-label={item} value={item} /></li>
                        )
                    }
                </ul>
            </div>
            </div>
            <div class="navbar-center hidden lg:flex">
                {
                    user() != null ?
                        <ul class="menu menu-horizontal px-1">
                            <NavLinks onSelectScreen={props.onSelectScreen} setTheme={props.setTheme} themes={props.themes} theme={props.theme}/>
                        </ul> : <></>
                }
            </div>
            <div class="navbar-end">
                <UserWidget onSelectScreen={props.onSelectScreen} setTheme={props.setTheme} themes={props.themes} theme={props.theme}/>
            </div>
        </div>
    )
}

export default NavBar;