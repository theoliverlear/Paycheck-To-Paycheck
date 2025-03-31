import {HttpClientService} from "./http-client.service";
import {OperationSuccessResponse} from "../../../models/http/types";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

export class LogoutService extends HttpClientService<any, OperationSuccessResponse> {
    static readonly LOGOUT_URL: string = 'http://localhost:8000/api/authorize/logout';

    constructor(httpClient: HttpClient) {
        super(LogoutService.LOGOUT_URL, httpClient);
    }

    public logout(): Observable<OperationSuccessResponse> {
        return this.get();
    }
}