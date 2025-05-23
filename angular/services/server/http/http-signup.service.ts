import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {HttpClientService} from "./http-client.service";
import {
    SignupCredentials
} from "../../../models/auth/credentials/SignupCredentials";
import {HttpAuthResponse} from "../../../models/auth/types";
import {Observable} from "rxjs";
import {environment} from "../../../environments/environment";

@Injectable({
    providedIn: 'root'
})
export class HttpSignupService extends HttpClientService<SignupCredentials, HttpAuthResponse> {
    static readonly SIGNUP_URL: string = `${environment.apiUrl}/authorize/signup`;
    constructor(httpClient: HttpClient) {
        super(HttpSignupService.SIGNUP_URL, httpClient);
    }
    public signup(signupCredentials: SignupCredentials): Observable<HttpAuthResponse> {
        return this.post(signupCredentials, true);
    }
}