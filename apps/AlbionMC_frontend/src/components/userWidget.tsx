import { Component } from "solid-js";
import { useAuth } from "./authProvider";


const LoginButton = function () {
    const { user, login, logout, loading } = useAuth();

    function loginGithub(e: MouseEvent) {
        if (!user()) login();
    }

    return (
        <>
            <a onClick={(e) => loginGithub(e)} class="btn btn-primary btn-sm" style={{ position: 'relative' }}>
                {loading() || user() != null ? (
                    <div
                        style={{
                            position: 'absolute',
                            top: '50%',
                            left: '50%',
                            transform: 'translate(-50%, -50%)',
                            width: '20px',
                            height: '20px',
                            border: '2px solid #ffffff',
                            "border-top-color": 'transparent',
                            "border-radius": '50%',
                            animation: 'spin 1s linear infinite',
                        }}
                    ></div>
                ) : "Github Login"}
            </a>
        </>
    );
};

const UserComponent: Component<UserProps> = function (props) {
    const { user, login, logout, loading } = useAuth();
    const handleScreenChange = (screenName: string) => {
        props.onSelectScreen(screenName);
    };

    return (
        <>
            <div class="dropdown dropdown-end">
                <div tabIndex={0} role="button" class="btn btn-ghost btn-circle avatar">
                    <div class="w-10 rounded-full">
                        <img alt="Tailwind CSS Navbar component" src={user()?.data.avatar_url} />
                    </div>
                </div>
                <ul tabIndex={0} class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
                    <li>
                        <a onClick={() => handleScreenChange("profile")} class="justify-between">
                            Profile
                            <span class="badge">New</span>
                        </a>
                    </li>
                    <li><a onClick={() => handleScreenChange("settings")}>Settings</a></li>
                    <li><a onClick={logout}>Logout</a></li>
                </ul>
            </div>
        </>
    )
}

interface UserProps {
    onSelectScreen: (screenName: string) => void;
}

interface WidgetProps {
    onSelectScreen: (screenName: string) => void;
    setTheme: (theme: string) => void;
    themes: string[];
    theme: () => string;
}

export const UserWidget: Component<WidgetProps> = function (props) {
    const { user, login, logout, loading } = useAuth();

    const handleScreenChange = (screenName: string) => {
        props.onSelectScreen(screenName);
    };

    return (
        <>
            {user() ? <UserComponent onSelectScreen={handleScreenChange} /> : <LoginButton />}
        </>
    )
}