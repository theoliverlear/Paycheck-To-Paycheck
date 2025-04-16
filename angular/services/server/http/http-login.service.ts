// http-login.service.ts
import {Injectable} from "@angular/core";
import {HttpClientService} from "./http-client.service";
import {HttpAuthResponse} from "../../../models/auth/types";
import {HttpClient} from "@angular/common/http";
import {
    LoginCredentials
} from "../../../models/auth/credentials/LoginCredentials";
import {Observable} from "rxjs";

@Injectable({
    providedIn: 'root'
})
export class HttpLoginService extends HttpClientService<LoginCredentials, HttpAuthResponse> {
    static readonly LOGIN_URL: string = 'http://localhost:8000/api/authorize/login';
    constructor(httpClient: HttpClient) {
        super(HttpLoginService.LOGIN_URL, httpClient);
    }
    public login(loginCredentials: LoginCredentials): Observable<HttpAuthResponse> {
        return this.post(loginCredentials, true);
    }
}