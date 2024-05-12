export function API_URL(path: string = "") : string {
    const hostname = window.location.hostname;
    const port = 3000;
    return `http://${hostname}:${port}/api/`+path;
}