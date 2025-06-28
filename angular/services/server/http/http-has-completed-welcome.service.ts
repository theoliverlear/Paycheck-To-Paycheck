import {Injectable} from "@angular/core";
import {HttpClientService} from "./http-client.service";
import {HasCompletedWelcome} from "../../../models/welcome/types";
import {environment} from "../../../environments/environment";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {httpOptionsWithCredentials} from "./httpProperties";

@Injectable({
    providedIn: 'root'
})
export class HttpHasCompletedWelcomeService extends HttpClientService<any, HasCompletedWelcome> {
    static readonly HAS_COMPLETED_WELCOME_URL: string = `${environment.apiUrl}/welcome/has-completed`;
    constructor(httpClient: HttpClient) {
        super(HttpHasCompletedWelcomeService.HAS_COMPLETED_WELCOME_URL, httpClient);
    }
    public hasCompletedWelcome(): Observable<HasCompletedWelcome> {
        return this.get(httpOptionsWithCredentials);
    }
}