import {HttpClientService} from "./http-client.service";
import {Incomes} from "../../../models/paycheck/types";
import {environment} from "../../../environments/environment";
import {HttpClient} from "@angular/common/http";
import {map, Observable} from "rxjs";
import {httpOptionsWithCredentials} from "./httpProperties";
import {convertToDate} from "../../../models/time/dateTimeHandler";
import {Injectable} from "@angular/core";

@Injectable({
    providedIn: 'root'
})
export class HttpGetAllIncomesService extends HttpClientService<any, Incomes> {
    static readonly GET_ALL_INCOMES_URL: string = `${environment.apiUrl}/income/get/all`;
    constructor(httpClient: HttpClient) {
        super(HttpGetAllIncomesService.GET_ALL_INCOMES_URL, httpClient);
    }
    public getAllIncomes(): Observable<Incomes> {
        return this.get(httpOptionsWithCredentials).pipe(
            map(incomes => convertToDate(incomes))
        );
    }
}