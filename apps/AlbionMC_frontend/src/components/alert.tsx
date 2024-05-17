import { Component } from "solid-js";
import { JSX } from "solid-js/jsx-runtime";

export type AlertsContext = {
    [id:string]:()=>JSX.Element
}

export function NewAlert(type: 'success' | 'error' | 'info', text: string, id: string) : JSX.Element {
    const handleDelete = () => {
        const element = document.getElementById(id);
        if (element) {
            element.remove();
        }
    };
    return (
        <>
            <div id={id} onClick={()=>handleDelete()} class={`alert alert-${type} cursor-pointer`}>
                <span>{text}</span>
            </div>
        </>
    )
}

export const Alerts: Component<{ctx:() => AlertsContext}> = function (props) {
    return (
        <>
            <div class="toast toast-end toast-middle">
            {
                Object.entries(props.ctx()).map(([key, value]) => (
                    value()
                ))
            }
            </div>
        </>
    )
}