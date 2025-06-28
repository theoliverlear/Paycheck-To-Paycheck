import {Injectable} from "@angular/core";
import {LoginService} from "../server/login.service";
import {
    ActivatedRouteSnapshot,
    CanActivate,
    Router,
    RouterStateSnapshot
} from "@angular/router";
import {catchError, map, Observable, of} from "rxjs";
import {LoggedInStatusService} from "../server/http/logged-in-status.service";
import {HttpAuthResponse} from "../../models/auth/types";
import {WelcomeService} from "../server/welcome.service";
import {HasCompletedWelcome} from "../../models/welcome/types";

@Injectable({
    providedIn: 'root'
})
export class AuthGuard implements CanActivate {
    constructor(private loggedInStatusService: LoggedInStatusService,
                private welcomeService: WelcomeService,
                private router: Router) {

    }
    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<boolean> {
        return this.loggedInStatusService.isLoggedIn().pipe(
            map((response: HttpAuthResponse): boolean => {
                if (response.payload.isAuthorized) {
                    this.welcomeService.hasCompletedWelcome().subscribe((hasCompletedWelcome: HasCompletedWelcome) => {
                        if (hasCompletedWelcome.hasCompletedWelcome) {
                            return true;
                        } else {
                            this.welcomeService.routeToWelcome();
                            return true;
                        }
                    });
                } else {
                    this.router.navigate(['/authorize'], {
                        queryParams: { returnUrl: state.url }
                    });
                    return false;
                }
            }),
            catchError((error) => {
                console.error('AuthGuard: Error during API call ->', error);
                this.router.navigate(['/authorize'], {
                    queryParams: { returnUrl: state.url } 
                });
                return of(false); 
            })
        );
    }
}