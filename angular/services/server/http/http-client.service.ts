// http-client.service.ts
import {Injectable} from "@angular/core";
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {
    HttpOptions,
    httpOptions,
    httpOptionsWithCredentials
} from "./httpProperties";
import {Observable} from "rxjs";

@Injectable({
    providedIn: 'root'
})
export class HttpClientService<Send, Receive> {
    private _url: string;

    constructor(url: string = '',
                private httpClient: HttpClient) {
        this._url = url;
    }

    get url(): string {
        return this._url;
    }

    set url(url: string) {
        this._url = url;
    }

    public get(customHttpOptions?: HttpOptions): Observable<Receive> {
        customHttpOptions = this.resolveHttpOptions(customHttpOptions);
        return this.httpClient.get<Receive>(this._url, customHttpOptions);
    }

    public post(payload: Send, includeCredentials: boolean = false, customHttpOptions?: HttpOptions): Observable<Receive> {
        customHttpOptions = this.resolveHttpOptions(customHttpOptions, includeCredentials);
        return this.httpClient.post<Receive>(this._url, payload, customHttpOptions);
    }

    public put(payload: Send, customHttpOptions?: HttpOptions): Observable<Receive> {
        customHttpOptions = this.resolveHttpOptions(customHttpOptions);
        return this.httpClient.put<Receive>(this._url, payload, customHttpOptions);
    }

    public delete(customHttpOptions?: HttpOptions): Observable<Receive> {
        customHttpOptions = this.resolveHttpOptions(customHttpOptions);
        return this.httpClient.delete<Receive>(this._url, customHttpOptions);
    }

    private resolveHttpOptions(customHttpOptions: HttpOptions, includeCredentials: boolean = false): HttpOptions {
        if (customHttpOptions === undefined) {
            if (includeCredentials) {
                customHttpOptions = httpOptionsWithCredentials;
            } else {
                customHttpOptions = httpOptions;
            }
        }
        return customHttpOptions;
    }
}