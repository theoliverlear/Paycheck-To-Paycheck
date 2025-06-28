import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {ErrorHandlerService} from "../error-handler.service";
import {UserService} from "./user.service";
import {httpOptions} from "./httpProperties";
import {catchError, map, Observable, switchMap} from "rxjs";
import {
    HttpHasCompletedWelcomeService
} from "./http/http-has-completed-welcome.service";
import {HasCompletedWelcome} from "../../models/welcome/types";
import {Router} from "@angular/router";
import {HttpWelcomeSurveyService} from "./http/http-welcome-survey.service";
import {
    LastPaycheck
} from "../../components/elements/element-group-welcome/last-paycheck-input/models/LastPaycheck";
import {OperationSuccessResponse} from "../../models/http/types";

@Injectable({
    providedIn: 'root'
})
export class WelcomeService {
    constructor(private hasCompletedWelcomeService: HttpHasCompletedWelcomeService,
                private welcomeSurveyService: HttpWelcomeSurveyService,
                private router: Router) {

    }

    submitWelcomeSurvey(lastPaycheck: LastPaycheck): Observable<OperationSuccessResponse> {
        return this.welcomeSurveyService.submitWelcomeSurvey(lastPaycheck);
    }

    handleWelcomeRedirect(): void {
        this.hasCompletedWelcomeService.hasCompletedWelcome().subscribe(
            (hasCompleted: HasCompletedWelcome) => {
                if (!hasCompleted.hasCompletedWelcome) {
                    this.routeToWelcome();
                }
            },
            (error: any) => {
                console.error('Error checking welcome completion:', error);
            }
        )
    }

    routeToWelcome(): void {
        this.router.navigate(['/welcome']);
    }

    hasCompletedWelcome(): Observable<HasCompletedWelcome> {
        return this.hasCompletedWelcomeService.hasCompletedWelcome();
    }
}