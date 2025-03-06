// signup-inputs.component.ts 
import {Component, EventEmitter, Input, Output} from "@angular/core";
import {AuthInputType} from "../../../models/auth/AuthInputType";
import {
    SignupCredentials
} from "../../../models/auth/credentials/SignupCredentials";

@Component({
    selector: 'signup-inputs',
    templateUrl: './signup-inputs.component.html',
    styleUrls: ['./signup-inputs.component.css']
})
export class SignupInputsComponent {
    @Input() signupCredentials: SignupCredentials = new SignupCredentials();
    @Output() credentialsChange: EventEmitter<SignupCredentials> = new EventEmitter<SignupCredentials>();
    constructor() {
        
    }

    protected emitCredentialsChange() {
        this.credentialsChange.emit(this.signupCredentials);
    }
    protected readonly AuthInputType = AuthInputType;
}
