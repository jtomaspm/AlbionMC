import { JSX, createSignal } from "solid-js"
import { TabedForm } from "../../components/tabedForm"

type ManualTabProps = {
    name: string
    unique_name: string
    current_tag: string
    tags: string[]
    description: string
}
const ManualTab = function (props: { props: () => ManualTabProps, setProps: (props: ManualTabProps) => void }): JSX.Element {
    const [itemTier, setItemTier] = createSignal("")
    const setName = (name: string) => {
        props.setProps({
            ...props.props(),
            name: name
        });
    }
    const setUniqueName = (unique_name: string) => {
        props.setProps({
            ...props.props(),
            unique_name: unique_name
        });
    }
    const setDescription = (description: string) => {
        props.setProps({
            ...props.props(),
            description: description
        });
    }
    const setCurrentTag = (tag: string) => {
        props.setProps({
            ...props.props(),
            current_tag: tag
        });
    }
    const addTag = () => {
        let p = { ...props.props() };
        if (p.current_tag != '' && !p.tags.includes(p.current_tag)) {
            p.tags = [...p.tags, p.current_tag]
        }
        p.current_tag = '';
        (document.getElementById('current_tag_in') as HTMLInputElement).value = '';
        props.setProps(p);
    }
    const removeTag = (tag: string) => {
        let p = { ...props.props() };
        const index = p.tags.indexOf(tag);
        if (index > -1) {
            p.tags = [...p.tags.slice(0, index), ...p.tags.slice(index + 1)];
        }
        props.setProps(p);
    }
    const reset = () => {
        (document.getElementById('current_tag_in') as HTMLInputElement).value = '';
        (document.getElementById('name_in') as HTMLInputElement).value = '';
        (document.getElementById('unique_name_in') as HTMLInputElement).value = '';
        (document.getElementById('description_in') as HTMLInputElement).value = '';
        let p = { ...props.props() };
        p.tags = [];
        p.current_tag = ''
        p.description = ''
        p.name = ''
        p.unique_name = ''
        props.setProps(p);
    }
    const setTier = () => {
        let res = '';
        if (props.props().unique_name[0] === 'T' && !isNaN(parseInt(props.props().unique_name[1], 10))) {
            res += props.props().unique_name[1]   
        }
        if (props.props().unique_name.slice(-2, -1) === '@' && !isNaN(parseInt(props.props().unique_name.slice(-1), 10))) {
            res += `.${props.props().unique_name.slice(-1)}`   
        }
        setItemTier(res);
    }
    const validateInputs : () => boolean = () => {
        const p = props.props();
        const valid = 'input input-bordered w-full max-w-xs';
        const invalid = 'input input-bordered input-error w-full max-w-xs';
        let res = true
        if(p.name === ''){
            (document.getElementById("name_in") as HTMLInputElement).className = invalid;
            res = false;
        }else{
            (document.getElementById("name_in") as HTMLInputElement).className = valid;
        }
        if(p.unique_name === ''){
            (document.getElementById("unique_name_in") as HTMLInputElement).className = invalid;
            res = false;
        }else{
            (document.getElementById("unique_name_in") as HTMLInputElement).className = valid;
        }
        return res;
    }
    return (
        <div class="card-body">
            <h2 class="card-title">Create Item</h2>
            <label class="form-control w-full max-w-xs">
                <div class="label">
                    <span class="label-text">Name</span>
                </div>
                <input id="name_in" onChange={() => {
                    setName((document.getElementById("name_in") as HTMLInputElement).value)
                }} type="text" placeholder="Grandmaster's Satchel of Insight" class="input input-bordered w-full max-w-xs" />
            </label>
            <label class="form-control w-full max-w-xs">
                <div class="label">
                    <span class="label-text">Unique Name</span>
                </div>
                <input id="unique_name_in" onChange={() => {
                    setUniqueName((document.getElementById("unique_name_in") as HTMLInputElement).value)
                }} type="text" placeholder="T7_BAG_INSIGHT@3" class="input input-bordered w-full max-w-xs" />
            </label>
            <p>Tags</p>
            <div class="card-actions justify-start items-center">
                <input id="current_tag_in" onChange={() => {
                    setCurrentTag((document.getElementById("current_tag_in") as HTMLInputElement).value)
                }} type="text" placeholder="Bag" class="input input-bordered w-full max-w-xs" />
                <button onClick={() => addTag()} class="btn btn-outline btn-accent">+</button>
            </div>
            <div id="tags_container" class="card-actions justify-start items-center">
                {
                    props.props().tags.map(tag => {
                        return (
                            <>
                                <button onClick={() => removeTag(tag)} class="btn btn-outline btn-info">{tag}</button>
                            </>
                        )
                    })
                }
            </div>
            <label class="form-control">
                <div class="label">
                    <span class="label-text">Description</span>
                </div>
                <textarea id="description_in" onChange={() => {
                    setDescription((document.getElementById("description_in") as HTMLInputElement).value)
                }} class="textarea textarea-bordered h-24" placeholder="The Grandmaster's Satchel of Insight is a Tier 7 accessory that may be obtained by crafting or via the Market Place."></textarea>
            </label>
            <div class="card-actions justify-center mt-4">
                <button onClick={() => reset()} class="btn btn-outline btn-secondary">Reset</button>
                <button onClick={()=>{
                    if (!validateInputs()) return;
                    setTier();
                    (document.getElementById('submit_mo') as HTMLDialogElement).showModal();
                }} class="btn btn-outline btn-primary">Submit</button>
            </div>
            <dialog id="submit_mo" class="modal">
                <div class="modal-box">
                    <h2 class="mb-4 font-bold text-lg">Item Details</h2>
                    <p class=""><b>Name: </b>{props.props().name}</p>
                    <p class=""><b>Unique Name: </b>{props.props().unique_name}</p>
                    <p class=""><b>Tier: </b>{itemTier()}</p>
                    <p class=""><b>Tags: </b>{props.props().tags.join(', ')}</p>
                    <p class=""><b>Description: </b>{props.props().description}</p>
                    <div class="modal-action justify-center">
                        <button onClick={()=>
                            (document.getElementById('submit_mo') as HTMLDialogElement).close()
                        } class="btn btn-secondary">Cancel</button>
                        <button onClick={()=>
                            (document.getElementById('submit_mo') as HTMLDialogElement).close()
                        } class="btn btn-primary">Submit</button>
                    </div>
                </div>
            </dialog>
        </div>
    )
}

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

export const CreateItems = function () {
    const [mtProps, setMtProps] = createSignal<ManualTabProps>({
        name: '',
        unique_name: '',
        description: '',
        current_tag: '',
        tags: []
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