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

@Injectable({
    providedIn: 'root'
})
export class AuthGuard implements CanActivate {
    constructor(private loggedInStatusService: LoggedInStatusService,
                private router: Router) {

    }
    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<boolean> {
        return this.loggedInStatusService.isLoggedIn().pipe(
            map((response: HttpAuthResponse): boolean => {
                if (response.payload.isAuthorized) {
                    return true;
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