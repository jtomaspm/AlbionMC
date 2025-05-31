export function API_URL(path: string = "") : string {
    while (path !== '' && path[0] == '/') {
        path = path.slice(1)
    } 
    const hostname = window.location.hostname;
    const port = 3000;
    return `http://${hostname}:${port}/api/`+path;
}

export function API_REQUEST(path: string = "", method : "GET" | "POST" | "PATCH" | "PUT" | "DELETE", headers: {[key:string]:string} = {}, body:string | null = "", token: string = '') : Promise<Response> {
    headers['Authorization'] = `Bearer ${token}`;
    headers['Content-Type'] = 'application/json';
    return fetch(API_URL(path), {
      method: method,
      headers: headers,
      body: body
    });
}