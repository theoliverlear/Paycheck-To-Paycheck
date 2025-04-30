import {Injectable} from "@angular/core";
import {HttpClientService} from "./http-client.service";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {httpOptionsWithCredentials} from "./httpProperties";
import {environment} from "../../../environments/environment";
import {HttpAuthResponse} from "../../../models/auth/types";
import {OperationSuccessResponse} from "../../../models/http/types";

@Injectable({
    providedIn: 'root'
})
export class HttpLogoutService extends HttpClientService<any, OperationSuccessResponse> {
    static readonly LOGOUT_URL: string = `${environment.apiUrl}/authorize/logout`;

    constructor(httpClient: HttpClient) {
        super(HttpLogoutService.LOGOUT_URL, httpClient);
    }

    public logout(): Observable<OperationSuccessResponse> {
        return this.get(httpOptionsWithCredentials);
    }
}