import { createContext, createEffect, createSignal, useContext } from "solid-js";
import { API_URL } from "../service/api";
import { UserType } from "../types/user";

interface AuthContextType {
    user: () => UserType | null;
    login: () => void;
    logout: () => void;
}


const AuthContext = createContext<AuthContextType>();
export const useAuth = function (): AuthContextType {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error("useAuth must be used within an AuthProvider");
    }
    return context;
}


export function AuthProvider(props: any) {
    const [user, setUser] = createSignal<UserType | null>(null);

    function handleGithubCode() {
        const urlParams = new URLSearchParams(window.location.search);
        const code = urlParams.get('code');
        if (code) {
            fetch(API_URL("users/github/code?code=" + code), {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            })
                .then(response => {
                    return response.json()
                })
                .then(data => {
                    if (!data.access_token) return
                    let u = {
                        token: data.access_token,
                        data: {},
                    }
                    fetch(API_URL("users/github/info?token=" + u.token), {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json',
                        }
                    })
                        .then(info_res => info_res.json())
                        .then(info_json => {
                            u.data = info_json
                            setUser(u as UserType)
                            localStorage.setItem("user", JSON.stringify(user()))
                        })
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }
    }

    createEffect(() => {
        handleGithubCode();
        const storedUser = localStorage.getItem("user");
        if (storedUser) {
            setUser(JSON.parse(storedUser))
        }
    });

    const login = () => {
        window.location.href = API_URL("users/github/login")
    };

    const logout = () => {
        setUser(null);
        localStorage.removeItem('user');
    };

    return <AuthContext.Provider value={{ user, login, logout }}>{props.children}</AuthContext.Provider>;
}