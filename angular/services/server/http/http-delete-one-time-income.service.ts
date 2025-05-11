import {Injectable} from "@angular/core";
import {HttpClientService} from "./http-client.service";
import {OneTimeIncome} from "../../../models/paycheck/types";
import {OperationSuccessResponse} from "../../../models/http/types";
import {environment} from "../../../environments/environment";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {httpOptionsWithCredentials} from "./httpProperties";


@Injectable({
    providedIn: 'root'
})
export class HttpDeleteOneTimeIncomeService extends HttpClientService<OneTimeIncome, OperationSuccessResponse> {
    static readonly DELETE_ONE_TIME_INCOME_URL: string = `${environment.apiUrl}/income/delete/one-time/`;
    constructor(httpClient: HttpClient) {
        super(HttpDeleteOneTimeIncomeService.DELETE_ONE_TIME_INCOME_URL, httpClient);
    }
    public deleteOneTimeIncome(incomeId: number): Observable<OperationSuccessResponse> {
        this.url = `${HttpDeleteOneTimeIncomeService.DELETE_ONE_TIME_INCOME_URL}${incomeId}`;
        return this.delete(httpOptionsWithCredentials);
    }
}