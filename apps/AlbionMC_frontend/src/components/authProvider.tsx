import { createContext, createEffect, createSignal, useContext } from "solid-js";

interface AuthContextType {
  user: () => any | null;
  login: (userData: any) => void;
  logout: () => void;
}


const AuthContext = createContext<AuthContextType>();
export const useAuth = function () : AuthContextType {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error("useAuth must be used within an AuthProvider");
    }
    return context;
}


export function AuthProvider(props: any) {
    const [user, setUser] = createSignal(null);

    createEffect(()=>{
        const storedUser = localStorage.getItem("user");
        if(storedUser){
            setUser(JSON.parse(storedUser))
        }
    });

    // Login function
    const login = (userData: any) => {
        setUser(userData);
        localStorage.setItem('user', JSON.stringify(userData));
    };

    // Logout function
    const logout = () => {
        setUser(null);
        localStorage.removeItem('user');
    };

    return <AuthContext.Provider value={{ user, login, logout }}>{props.children}</AuthContext.Provider>;
}