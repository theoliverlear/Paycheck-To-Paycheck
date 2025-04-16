import {HttpHeaders} from "@angular/common/http";

export type HttpOptions = {
    headers: HttpHeaders,
    withCredentials?: boolean
}

export const httpOptions: HttpOptions = {
    headers: new HttpHeaders({
        'Content-Type': 'application/json'
    })
};
export const httpOptionsWithCredentials: HttpOptions = {
    headers: new HttpHeaders({
        'Content-Type': 'application/json'
    }),
    withCredentials: true
};