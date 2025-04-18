import {HttpClientService} from "./http-client.service";
import {Paycheck} from "../../../models/paycheck/types";
import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {map, Observable} from "rxjs";
import {httpOptionsWithCredentials} from "./httpProperties";
import {convertToDate} from '../../../models/time/dateTimeHandler';

@Injectable({
    providedIn: 'root'
})
export class HttpPaycheckService extends HttpClientService<any, Paycheck> {
    private static readonly URL: string = 'http://localhost:8000/api/paycheck/get/'
    constructor(http: HttpClient) {
        super(HttpPaycheckService.URL, http);
    }
    public getPaycheck(numPaychecksFromNow: number): Observable<Paycheck> {
        this.url = HttpPaycheckService.URL + numPaychecksFromNow;
        return this.get(httpOptionsWithCredentials).pipe(
            map(paycheck => convertToDate(paycheck))
        );
    }
}