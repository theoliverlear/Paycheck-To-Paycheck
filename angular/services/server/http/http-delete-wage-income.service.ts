import {Injectable} from "@angular/core";
import {HttpClientService} from "./http-client.service";
import {RecurringBill} from "../../../models/paycheck/types";
import {OperationSuccessResponse} from "../../../models/http/types";
import {httpOptionsWithCredentials} from "./httpProperties";
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";
import {environment} from "../../../environments/environment";

@Injectable({
    providedIn: 'root'
})
export class HttpDeleteWageIncomeService extends HttpClientService<RecurringBill, OperationSuccessResponse> {
    static readonly DELETE_WAGE_INCOME_URL: string = `${environment.apiUrl}/income/delete/wage/`;

    constructor(httpClient: HttpClient) {
        super(HttpDeleteWageIncomeService.DELETE_WAGE_INCOME_URL, httpClient);
    }

    public deleteWageIncome(incomeId: number): Observable<OperationSuccessResponse> {
        this.url = `${HttpDeleteWageIncomeService.DELETE_WAGE_INCOME_URL}${incomeId}`;
        return this.delete(httpOptionsWithCredentials);
    }
}