import {HttpHeaders} from "@angular/common/http";

export type HttpOptions = {
    headers: HttpHeaders
}

export const httpOptions: HttpOptions = {
    headers: new HttpHeaders({
        'Content-Type': 'application/json'
    })
};