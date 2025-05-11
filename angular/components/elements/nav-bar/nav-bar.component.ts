// nav-bar.component.ts 
import {Component, OnInit, ViewChild} from "@angular/core";
import {
    navBarBudgetElementLink,
    navBarMyAccountElementLink, navBarPaychecksElementLink
} from "../../../assets/elementLinkAssets";
import {
    LoggedInStatusService
} from "../../../services/server/http/logged-in-status.service";
import {NavItemComponent} from "../nav-item/nav-item.component";
import {
    HttpLogoutService
} from "../../../services/server/http/http-logout.service";
import {Router} from "@angular/router";
import {OperationSuccessResponse} from "../../../models/http/types";

@Component({
    selector: 'nav-bar',
    templateUrl: './nav-bar.component.html',
    styleUrls: ['./nav-bar.component.css']
})
export class NavBarComponent implements OnInit {
    isLoggedIn: boolean = false;
    @ViewChild('myAccountButton') myAccountButton: NavItemComponent;
    constructor(private loggedInStatusService: LoggedInStatusService,
                private logoutService: HttpLogoutService,
                private router: Router) {

    }

    ngOnInit(): void {
        this.createLoggedInListener();
        this.loggedInStatusService.isLoggedIn();
    }

    public setAccountText(text: string): void {
        this.myAccountButton.setText(text);
    }

    public setAccountButtonFunction(isLoggedIn: boolean) {
        if (isLoggedIn) {
            this.myAccountButton.onClick = (): void => {
                this.logoutService.logout().subscribe(
                    (response: OperationSuccessResponse): void => {
                        console.log('Logout successful:', response);
                        this.clearSessionCookies();
                        this.isLoggedIn = false;
                        this.router.navigate(['/']);
                    },
                    (error) => {
                        console.error('Error during logout:', error);
                    }
                );
            };
        }
    }

    private clearSessionCookies(): void {
        const cookieProperties: string = "=; path=/; expires=Thu, 01 Jan 1970 00:00:00 UTC; secure; SameSite=Lax";
        const cookiesToClear: string[] = [
            'sessionid',
            'devsessionid',
        ];
        cookiesToClear.forEach((cookieName: string): void => {
            document.cookie = `${cookieName}${cookieProperties}`;
        });
    }

    createLoggedInListener(): void {
        this.loggedInStatusService.isLoggedIn().subscribe(
            (response) => {
                console.log('Logged-in status:', response.payload.isAuthorized);
                this.isLoggedIn = response.payload.isAuthorized;
                if (this.isLoggedIn) {
                    this.setAccountText('Logout');
                } else {
                    this.setAccountText('My Account');
                }
                this.setAccountButtonFunction(this.isLoggedIn);
            },
            (error) => {
                console.error('Error fetching logged-in status:', error);
            }
        );
    }

    protected readonly navBarMyAccountElementLink = navBarMyAccountElementLink;
    protected readonly navBarPaychecksElementLink = navBarPaychecksElementLink;
    protected readonly navBarBudgetElementLink = navBarBudgetElementLink;
}
