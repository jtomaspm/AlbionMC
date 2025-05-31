import { createSignal } from "solid-js"
import { JSX } from "solid-js/jsx-runtime"

export type FileTabProps = {
    file: any
}
export const FileTab = function (props: { 
    props: () => FileTabProps, 
    setProps: (props: FileTabProps) => void, 
    processCSV: (content:string) => string | null,
    title: string 
}): JSX.Element {

    const [fileContent, setFileContent] = createSignal<string | null>(null);
    const [requestBody, setRequestBody] = createSignal<string | null>(null);
    const defaultInputStyles = "file-input file-input-bordered w-full max-w-xs ";

    const handleFileChange = (event: Event) => {
        const input = event.target as HTMLInputElement;
        if (input.files && input.files.length > 0) {
            const selectedFile = input.files[0];
            props.setProps({
                file: selectedFile
            });
            readFile(selectedFile);
        }
    };

    const readFile = (file: File) => {
        const reader = new FileReader();
        reader.onload = (e) => {
            const content = e.target?.result as string;
            setFileContent(content);
            setRequestBody(props.processCSV(content));
            if(requestBody() == null){
                (document.getElementById("file_in") as HTMLInputElement).className = defaultInputStyles + "file-input-error";
            }else{
                (document.getElementById("file_in") as HTMLInputElement).className = defaultInputStyles;
            }
        };
        reader.readAsText(file);
    };

    return (
        <div class="card-body flex flex-col justify-between">
            <div>
                <h2 class="card-title">{props.title}</h2>
                <label class="form-control w-full max-w-xs mt-2">
                    <div class="label">
                        <span class="label-text">Pick a file</span>
                    </div>
                    <input id="file_in" type="file" class={defaultInputStyles} onChange={handleFileChange} />
                </label>
            </div>
            <div class="card-actions justify-center mt-4">
                <button class="btn btn-outline btn-secondary" onClick={() => props.setProps({file: null})}>Reset</button>
                <button class="btn btn-outline btn-primary">Submit</button>
            </div>
        </div>
    )
}