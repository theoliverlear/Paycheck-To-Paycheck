// auth-console.component.ts
import {Component, Input, ViewChild} from "@angular/core";
import {AuthType} from "../../../../models/auth/AuthType";
import {AuthPopup} from "../../../../models/auth/AuthPopup";
import {
    SignupConsoleComponent
} from "../signup-console/signup-console.component";
import {
    LoginConsoleComponent
} from "../login-console/login-console.component";

@Component({
    selector: 'auth-console',
    templateUrl: './auth-console.component.html',
    styleUrls: ['./auth-console.component.css']
})
export class AuthConsoleComponent {
    @Input() protected authType: AuthType = AuthType.SIGNUP;
    protected authPopup: AuthPopup | null = null;
    @ViewChild(SignupConsoleComponent) signupConsole: SignupConsoleComponent;
    @ViewChild(LoginConsoleComponent) loginConsole: LoginConsoleComponent;
    constructor() {
        
    }
    public setAuthType(authType: AuthType) {
        this.authType = authType;
    }
    public setAuthPopup(authPopup: AuthPopup | null) {
        this.authPopup = authPopup;
    }
    protected isSignup(): boolean {
        return this.authType === AuthType.SIGNUP;
    }
    protected isLogin(): boolean {
        return this.authType === AuthType.LOGIN;
    }
    protected hasPopup(): boolean {
        return this.authPopup !== null;
    }

    protected readonly AuthPopup = AuthPopup;
}
