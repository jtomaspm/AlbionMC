import { useAuth } from "./authProvider";


const LoginButton = function () {
    const { user, login, logout } = useAuth();

    function loginGithub(e: MouseEvent) {
        login()
    }

    return (
        <>
            <a onClick={(e) => loginGithub(e)} class="btn">Github Login</a>
        </>
    )

}

const UserComponent = function () {
    const { user, login, logout } = useAuth();
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
                    <li><a>Logout</a></li>
                </ul>
            </div>
        </>
    )
}

export const UserWidget = function () {
    const { user, login, logout } = useAuth();
    return (
        <>
            {user() ? <UserComponent /> : <LoginButton />}
        </>
    )
}