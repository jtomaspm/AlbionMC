import { JSX, createSignal } from "solid-js"
import { TabedForm } from "../../components/tabedForm"
import { ManualTabProps, ManualTab } from "../../components/itemManualTab"
import { UserContextType } from "../../types/user"


type FileTabProps = {
    file: any
}
const FileTab = function (props: { props: () => FileTabProps, setProps: (props: FileTabProps) => void }): JSX.Element {

    return (
        <div class="card-body flex flex-col justify-between">
            <div>
                <h2 class="card-title">Create Item</h2>
                <label class="form-control w-full max-w-xs mt-2">
                    <div class="label">
                        <span class="label-text">Pick a file</span>
                    </div>
                    <input type="file" class="file-input file-input-bordered w-full max-w-xs" />
                </label>
            </div>
            <div class="card-actions justify-center mt-4">
                <button class="btn btn-outline btn-secondary">Reset</button>
                <button class="btn btn-outline btn-primary">Submit</button>
            </div>
        </div>
    )
}

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
    const tabs = {
        'Manual': ManualTab({ props: mtProps, setProps: setMtProps }),
        'From File': FileTab({ props: ftProps, setProps: setFtProps }),
    }
    return (
        <>
            <TabedForm tabs={tabs} />
        </>
    )
}