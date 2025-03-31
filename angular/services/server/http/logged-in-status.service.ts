import {Injectable} from "@angular/core";
import {HttpClientService} from "./http-client.service";
import {
    HttpAuthResponse
} from "../../../models/auth/types";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
    providedIn: 'root'
})
export class LoggedInStatusService extends HttpClientService<any, HttpAuthResponse> {
    static readonly IS_LOGGED_IN_URL: string = 'http://localhost:8000/api/authorize/isloggedin';

    constructor(httpClient: HttpClient) {
        super(LoggedInStatusService.IS_LOGGED_IN_URL, httpClient);
    }
    public isLoggedIn(): Observable<HttpAuthResponse> {
        return this.get();
    }
}