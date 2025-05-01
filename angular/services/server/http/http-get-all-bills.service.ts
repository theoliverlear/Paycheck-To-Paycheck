import {Injectable} from "@angular/core";
import {HttpClientService} from "./http-client.service";
import {Bills} from "../../../models/paycheck/types";
import {environment} from "../../../environments/environment";
import {HttpClient} from "@angular/common/http";
import {map, Observable} from "rxjs";
import {convertToDate} from "../../../models/time/dateTimeHandler";
import {httpOptionsWithCredentials} from "./httpProperties";

@Injectable({
    providedIn: 'root'
})
export class HttpGetAllBillsService extends HttpClientService<any, Bills> {
    static readonly GET_ALL_BILLS_URL: string = `${environment.apiUrl}/bill/get/all`;
    constructor(httpClient: HttpClient) {
        super(HttpGetAllBillsService.GET_ALL_BILLS_URL, httpClient);
    }
    public getAllBills(): Observable<Bills> {
        return this.get(httpOptionsWithCredentials).pipe(
            map(bills => convertToDate(bills))
        );
    }
}