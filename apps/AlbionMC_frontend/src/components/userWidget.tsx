import { createEffect, createSignal } from "solid-js";
import { useAuth } from "./authProvider";


const LoginButton = function () {
    const [loading, setLoading] = createSignal(false);

    const { user, login, logout } = useAuth();

    function loginGithub(e: MouseEvent) {
        console.log("Logging in")
        console.log(import.meta.env.GITHUB_CLIENT_ID)
        console.log(import.meta.env.GITHUB_CLIENT_SECRET)
        setLoading(true);
        // Redirect user to GitHub OAuth page
        window.location.href = 'https://github.com/login/oauth/authorize' +
            `?client_id=` + import.meta.env.VITE_GITHUB_CLIENT_ID;

    }

    // Callback function to handle redirection after GitHub authentication
    function handleGithubCode() {
        const urlParams = new URLSearchParams(window.location.search);
        const code = urlParams.get('code');
        console.log(code)
        if (code) {
            // If the URL contains an authorization code, exchange it for an access token
            // Send a POST request to your server to perform this exchange
            fetch('api/api/users/github/code?code='+code, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            })
                .then(response => response.json())
                .then(data => {
                    // Once you have the access token, you can store it in local storage or a cookie
                    // Redirect the user to the desired page
                    setLoading(false);
                    console.log(data)
                })
                .catch(error => {
                    console.error('Error:', error);
                    setLoading(false);
                });
        }
    }


    createEffect(() => {
        handleGithubCode()
    });


    return (
        <>
            <div class="navbar-end">
                <a onClick={(e) => loginGithub(e)} class="btn">Github Login</a>
            </div>
        </>
    )

}

export const UserWidget = function () {
    return (
        <>
            <LoginButton />
        </>
    )
}