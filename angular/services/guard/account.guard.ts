import {Injectable} from "@angular/core";
import {
    ActivatedRouteSnapshot,
    CanActivate, Router,
    RouterStateSnapshot
} from "@angular/router";
import {catchError, map, Observable, of} from "rxjs";
import {LoginService} from "../server/login.service";
import {HttpAuthResponse} from "../../models/auth/types";
import {LoggedInStatusService} from "../server/http/logged-in-status.service";

@Injectable({
    providedIn: 'root'
})
export class AccountGuard implements CanActivate {
    constructor(private loggedInStatusService: LoggedInStatusService,
                private router: Router) {

    }
    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<boolean> {
        return this.loggedInStatusService.isLoggedIn().pipe(
            map((response: HttpAuthResponse): boolean => {
                if (response.payload.isAuthorized) {
                    return true;
                } else {
                    this.router.navigate(['/account'], {
                        queryParams: { returnUrl: state.url } 
                    });
                    return false; 
                }
            }),
            catchError((error) => {
                this.router.navigate(['/authorize'], {
                    queryParams: { returnUrl: state.url } 
                });
                return of(false); 
            })
        );
    }
}