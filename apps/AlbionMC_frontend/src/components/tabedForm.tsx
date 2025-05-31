import { Component, JSX, createSignal } from "solid-js"

export type TabedFormProps = {
    tabs: { [tabName: string]: JSX.Element }
}

export const TabedForm: Component<TabedFormProps> = props => {
    const [firstKey, firstValue] = Object.entries(props.tabs)[0];
    const [current, setCurrent] = createSignal<string>(firstKey);

    return (
        <div class="md:flex w-5/12 min-h-96">
            <ul class="flex-column space-y space-y-4 text-sm font-medium text-gray-500 dark:text-gray-400 md:me-4 mb-4 md:mb-0">
                {
                    Object.entries(props.tabs).map(([key, value]) => {
                        let css = "inline-flex btn w-full";
                        if (key === current()) {
                            css += " btn-primary"
                        } else {
                            css += " no-animation"
                        }
                        return (
                            <li>
                                <a onClick={() => { setCurrent(key) }} class={css}>
                                    {key}
                                </a>
                            </li>
                        )
                    })
                }
            </ul>
            <div class="card bg-base-100 shadow-xl w-10/12">
                {props.tabs[current()]}
            </div>
        </div>
    )
}