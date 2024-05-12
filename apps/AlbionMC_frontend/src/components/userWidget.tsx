import { useAuth } from "./authProvider";


const LoginButton = function () {
    const { user, login, logout, loading } = useAuth();

    function loginGithub(e: MouseEvent) {
        if(!user()) login();
    }

    return (
        <>
            <a onClick={(e) => loginGithub(e)} class="btn" style={{ position: 'relative' }}>
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

const UserComponent = function () {
    const { user, login, logout, loading } = useAuth();
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
                        <a class="justify-between">
                            Profile
                            <span class="badge">New</span>
                        </a>
                    </li>
                    <li><a>Settings</a></li>
                    <li><a onClick={logout}>Logout</a></li>
                </ul>
            </div>
        </>
    )
}

export const UserWidget = function () {
    const { user, login, logout, loading } = useAuth();
    return (
        <>
            {user() ? <UserComponent /> : <LoginButton />}
        </>
    )
}