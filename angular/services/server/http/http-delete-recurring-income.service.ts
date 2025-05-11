import {Injectable} from "@angular/core";
import {HttpClientService} from "./http-client.service";
import {RecurringIncome} from "../../../models/paycheck/types";
import {OperationSuccessResponse} from "../../../models/http/types";
import {httpOptionsWithCredentials} from "./httpProperties";
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";
import {environment} from "../../../environments/environment";

@Injectable({
    providedIn: 'root'
})
export class HttpDeleteRecurringIncomeService extends HttpClientService<RecurringIncome, OperationSuccessResponse> {
    static readonly DELETE_RECURRING_INCOME_URL: string = `${environment.apiUrl}/income/delete/recurring/`;

    constructor(httpClient: HttpClient) {
        super(HttpDeleteRecurringIncomeService.DELETE_RECURRING_INCOME_URL, httpClient);
    }

    public deleteRecurringIncome(incomeId: number): Observable<OperationSuccessResponse> {
        this.url = `${HttpDeleteRecurringIncomeService.DELETE_RECURRING_INCOME_URL}${incomeId}`;
        return this.delete(httpOptionsWithCredentials);
    }
}