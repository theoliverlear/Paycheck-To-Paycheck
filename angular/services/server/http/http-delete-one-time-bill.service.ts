import {HttpClientService} from "./http-client.service";
import {OneTimeBill} from "../../../models/paycheck/types";
import {OperationSuccessResponse} from "../../../models/http/types";
import {environment} from "../../../environments/environment";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Injectable} from "@angular/core";
import {httpOptionsWithCredentials} from "./httpProperties";

@Injectable({
    providedIn: 'root'
})
export class HttpDeleteOneTimeBillService extends HttpClientService<OneTimeBill, OperationSuccessResponse> {
    static readonly DELETE_ONE_TIME_BILL_URL: string = `${environment.apiUrl}/bill/delete/one-time/`;
    constructor(httpClient: HttpClient) {
        super(HttpDeleteOneTimeBillService.DELETE_ONE_TIME_BILL_URL, httpClient);
    }

    public deleteOneTimeBill(billId: number): Observable<OperationSuccessResponse> {
        this.url = `${HttpDeleteOneTimeBillService.DELETE_ONE_TIME_BILL_URL}${billId}`;
        return this.delete(httpOptionsWithCredentials);
    }
}