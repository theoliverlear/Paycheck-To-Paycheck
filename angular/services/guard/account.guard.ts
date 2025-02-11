import {Injectable} from "@angular/core";
import {
    ActivatedRouteSnapshot,
    CanActivate, Router,
    RouterStateSnapshot
} from "@angular/router";
import {catchError, map, Observable} from "rxjs";
import {LoginService} from "../server/login.service";

@Injectable({
    providedIn: 'root'
})
export class AccountGuard implements CanActivate {
    constructor(private loginService: LoginService,
                private router: Router) {

    }
    canActivate(route: ActivatedRouteSnapshot,
                state: RouterStateSnapshot): Observable<boolean> {
        return this.loginService.getIsLoggedInFromServer().pipe(
            map(isAuthorized => {
                if (isAuthorized) {
                    this.router.navigate(['/account']);
                    return true;
                } else {
                    return false;
                }
            }),
            catchError(() => {
                this.router.navigate(['/authorize']);
                return new Observable<boolean>(observer => {
                    observer.next(false);
                });
            })
        )
    }
}