import {HttpClientService} from "./http-client.service";
import {OperationSuccessResponse} from "../../../models/http/types";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Injectable} from "@angular/core";
import {environment} from "../../../environments/environment";

@Injectable({
    providedIn: 'root'
})
export class LogoutService extends HttpClientService<any, OperationSuccessResponse> {
    static readonly LOGOUT_URL: string = `${environment.apiUrl}/authorize/logout`;

    constructor(httpClient: HttpClient) {
        super(LogoutService.LOGOUT_URL, httpClient);
    }

    public logout(): Observable<OperationSuccessResponse> {
        return this.get();
    }
}