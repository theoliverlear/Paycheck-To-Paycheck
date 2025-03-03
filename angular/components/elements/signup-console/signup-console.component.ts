// signup-console.component.ts 
import { Component } from "@angular/core";
import {TagType} from "../../../models/html/TagType";
import {ButtonText} from "../ss-button/models/ButtonText";
import {ElementSize} from "../../../models/ElementSize";
import {
    SignupCredentials
} from "../../../models/auth/credentials/SignupCredentials";

@Component({
    selector: 'signup-console',
    templateUrl: './signup-console.component.html',
    styleUrls: ['./signup-console.component.css']
})
export class SignupConsoleComponent {
    constructor() {
        
    }

    protected handleCredentialChange(signupCredentials: SignupCredentials) {
        console.log(signupCredentials);
    }

    protected readonly TagType = TagType;
    protected readonly ButtonText = ButtonText;
    protected readonly ElementSize = ElementSize;
}
