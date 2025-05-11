import {Injectable} from "@angular/core";
import {HttpClientService} from "./http-client.service";
import {RecurringBill} from "../../../models/paycheck/types";
import {OperationSuccessResponse} from "../../../models/http/types";
import {httpOptionsWithCredentials} from "./httpProperties";
import {environment} from "../../../environments/environment";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
    providedIn: 'root'
})
export class HttpDeleteRecurringBillService extends HttpClientService<RecurringBill, OperationSuccessResponse> {
    static readonly DELETE_RECURRING_BILL_URL: string = `${environment.apiUrl}/bill/delete/recurring/`;
    constructor(httpClient: HttpClient) {
        super(HttpDeleteRecurringBillService.DELETE_RECURRING_BILL_URL, httpClient);
    }

    public deleteRecurringBill(billId: number): Observable<OperationSuccessResponse> {
        this.url = `${HttpDeleteRecurringBillService.DELETE_RECURRING_BILL_URL}${billId}`;
        return this.delete(httpOptionsWithCredentials);
    }
}