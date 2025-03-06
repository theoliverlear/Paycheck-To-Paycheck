// login-inputs.component.ts 
import {Component, EventEmitter, Input, Output} from "@angular/core";
import {AuthInputType} from "../../../models/auth/AuthInputType";
import {
    LoginCredentials
} from "../../../models/auth/credentials/LoginCredentials";

@Component({
    selector: 'login-inputs',
    templateUrl: './login-inputs.component.html',
    styleUrls: ['./login-inputs.component.css']
})
export class LoginInputsComponent {
    @Input() loginCredentials: LoginCredentials = new LoginCredentials();
    @Output() credentialsChange: EventEmitter<LoginCredentials> = new EventEmitter<LoginCredentials>();
    constructor() {
        
    }

    protected emitCredentialsChange(): void {
        this.credentialsChange.emit(this.loginCredentials);
    }

    protected readonly AuthInputType = AuthInputType;
}
