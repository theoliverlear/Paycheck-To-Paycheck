// signup-input.component.ts
import {
    Component,
    EventEmitter,
    Input,
    Output,
    ViewChild
} from "@angular/core";
import {AuthInputType} from "../../../models/auth/AuthInputType";
import {TagType} from "../../../models/html/TagType";
import {InputType} from "../ss-input/models/InputType";
import {
    SignupCredentials
} from "../../../models/auth/credentials/SignupCredentials";
import {SsInputComponent} from "../ss-input/ss-input.component";

@Component({
    selector: 'signup-input',
    templateUrl: './signup-input.component.html',
    styleUrls: ['./signup-input.component.css']
})
export class SignupInputComponent {
    @Input() inputType: AuthInputType;
    @Input() signupCredentials: SignupCredentials;
    @Output() inputEvent: EventEmitter<void> = new EventEmitter<void>();
    @ViewChild(SsInputComponent) inputElement: SsInputComponent;
    constructor() {
        
    }

    protected emitInputEvent() {
        this.inputEvent.emit();
    }

    protected sanitizeInput(inputValue: string) {
        // FIXME: Email a handling doesn't work.
        if (this.inputType === AuthInputType.EMAIL) {
            console.log(inputValue)
            return inputValue.replace(' ', '');
        }
        return inputValue.replace(/\s+/g, '');
    }

    protected handleInput(inputValue: string) {
        const sanitizedInput = this.sanitizeInput(inputValue);
        this.setInputValue(sanitizedInput);
        switch (this.inputType) {
            case AuthInputType.USERNAME:
                this.setUsername(sanitizedInput);
                break;
            case AuthInputType.PASSWORD:
                this.setPassword(sanitizedInput);
                break;
            case AuthInputType.CONFIRM_PASSWORD:
                this.setConfirmPassword(sanitizedInput);
                break;
            case AuthInputType.EMAIL:
                this.setEmail(sanitizedInput);
                break;
        }
        this.emitInputEvent();
    }

    protected setInputValue(sanitizedInput: string) {
        this.inputElement.value = sanitizedInput;
    }

    protected setUsername(username: string) {
        this.signupCredentials.username = username;
    }

    protected setPassword(password: string) {
        this.signupCredentials.password = password;
    }

    protected setConfirmPassword(confirmPassword: string) {
        this.signupCredentials.confirmPassword = confirmPassword;
    }

    protected setEmail(email: string) {
        this.signupCredentials.email = email;
    }

    protected setTermsAgreed(termsAgreed: boolean) {
        this.signupCredentials.termsAgreed = termsAgreed;
        this.emitInputEvent();
    }

    protected isUsernameType(): boolean {
        return this.inputType === AuthInputType.USERNAME;
    }
    protected isPasswordType(): boolean {
        return this.inputType === AuthInputType.PASSWORD ||
               this.inputType === AuthInputType.CONFIRM_PASSWORD;
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

    protected getPlaceholder(): string {
        switch (this.inputType) {
            // case AuthInputType.USERNAME:
            //     return 'Ex. mike.demarcus1999';
            // case AuthInputType.EMAIL:
            //     return 'Ex. mike.demarcus1999@gmail.com';
            default:
                return '';
        }
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
