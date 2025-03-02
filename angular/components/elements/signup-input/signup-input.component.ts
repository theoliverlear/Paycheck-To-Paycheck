// signup-input.component.ts
import {Component, Input} from "@angular/core";
import {AuthInputType} from "../../../models/auth/AuthInputType";
import {TagType} from "../../../models/html/TagType";
import {InputType} from "../ss-input/models/InputType";

@Component({
    selector: 'signup-input',
    templateUrl: './signup-input.component.html',
    styleUrls: ['./signup-input.component.css']
})
export class SignupInputComponent {
    @Input() inputType: AuthInputType;
    constructor() {
        
    }
    protected isUsernameType(): boolean {
        return this.inputType === AuthInputType.USERNAME;
    }
    protected isPasswordType(): boolean {
        return this.inputType === AuthInputType.PASSWORD;
    }
    protected isEmailType(): boolean {
        return this.inputType === AuthInputType.EMAIL;
    }
    protected isTermsServiceType(): boolean {
        return this.inputType === AuthInputType.TERMS;
    }
    protected getTitleText(): string {
        return this.inputType + ":";
    }

    protected getInputType(): InputType {
        switch (this.inputType) {
            case AuthInputType.USERNAME:
                return InputType.TEXT;
            case AuthInputType.PASSWORD:
                return InputType.PASSWORD;
            case AuthInputType.EMAIL:
                return InputType.EMAIL;
            default:
                return InputType.TEXT;
        }
    }

    protected readonly TagType = TagType;
}
