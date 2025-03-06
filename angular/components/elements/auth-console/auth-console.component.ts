// auth-console.component.ts
import {Component, Input} from "@angular/core";
import {AuthType} from "../../../models/auth/AuthType";
import {AuthPopup} from "../../../models/auth/AuthPopup";

@Component({
    selector: 'auth-console',
    templateUrl: './auth-console.component.html',
    styleUrls: ['./auth-console.component.css']
})
export class AuthConsoleComponent {
    @Input() protected authType: AuthType = AuthType.SIGNUP;
    protected authPopup: AuthPopup | null = null;
    constructor() {
        
    }
    public setAuthType(authType: AuthType) {
        this.authType = authType;
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
}
