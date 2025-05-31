import { createSignal } from "solid-js"
import { TabedForm } from "../../components/tabedForm"
import { ManualTabProps, ManualTab } from "../../components/items/itemManualTab"
import { FileTab, FileTabProps } from "../../components/items/itemFileTab"
import { UserContextType } from "../../types/user"


export const CreateItems = function (props: {user:()=>UserContextType | null}) {
    const [mtProps, setMtProps] = createSignal<ManualTabProps>({
        name: '',
        unique_name: '',
        description: '',
        current_tag: '',
        tags: [],
        user: props.user
    })
    const [ftProps, setFtProps] = createSignal<FileTabProps>({
        file: null,
    })

    function processCSV(content: string): string|null {
        return null
    }

    const tabs = {
        'Manual': ManualTab({ props: mtProps, setProps: setMtProps }),
        'From File': FileTab({ props: ftProps, setProps: setFtProps, processCSV: processCSV, title: "Create Item" }),
    }
    return (
        <>
            <TabedForm tabs={tabs} />
        </>
    )
}