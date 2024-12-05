import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {ErrorHandlerService} from "../error-handler.service";
import {UserService} from "./user.service";
import {httpOptions} from "./httpProperties";
import {catchError, map, Observable, switchMap} from "rxjs";

@Injectable({
    providedIn: 'root'
})
export class WelcomeService {
    private getWelcomeCompletedUrl: string = 'http://localhost:8080/api/welcome/get/completed';
    constructor(private http: HttpClient,
                private errorHandlerService: ErrorHandlerService,
                private userService: UserService) {
        console.log('WelcomeService loaded');
    }
    getWelcomeCompletedFromServer(): Observable<boolean> {
        return this.userService.getCurrentUserIdFromServer().pipe(
            switchMap(userId => {
                const welcomeRequest = {
                    userId: userId
                };
                return this.http.post<{welcomeCompleted: boolean}>(this.getWelcomeCompletedUrl, welcomeRequest, httpOptions)
                    .pipe(
                        map(response => response.welcomeCompleted),
                        catchError(this.errorHandlerService.handleError<boolean>('getWelcomeCompletedFromServer'))
                    );
            })
        );
    }
}