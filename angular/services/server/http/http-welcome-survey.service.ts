import {Injectable} from "@angular/core";
import {HttpClientService} from "./http-client.service";
import {
    LastPaycheck
} from "../../../components/elements/element-group-welcome/last-paycheck-input/models/LastPaycheck";
import {OperationSuccessResponse} from "../../../models/http/types";
import {environment} from "../../../environments/environment";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {httpOptionsWithCredentials} from "./httpProperties";

@Injectable({
    providedIn: 'root'
})
export class HttpWelcomeSurveyService extends HttpClientService<LastPaycheck, OperationSuccessResponse> {
    static readonly WELCOME_SURVEY_URL: string = `${environment.apiUrl}/welcome/survey`;
    constructor(httpClient: HttpClient) {
        super(HttpWelcomeSurveyService.WELCOME_SURVEY_URL, httpClient);
    }

    public submitWelcomeSurvey(lastPaycheck: LastPaycheck): Observable<OperationSuccessResponse> {
        return this.post(lastPaycheck, true);
    }
}