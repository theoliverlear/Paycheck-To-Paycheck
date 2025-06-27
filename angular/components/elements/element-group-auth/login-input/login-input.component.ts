// login-input.component.ts 
import {
    Component,
    EventEmitter,
    Input,
    Output,
    ViewChild
} from "@angular/core";
import {AuthInputType} from "../../../../models/auth/AuthInputType";
import {
    LoginCredentials
} from "../../../../models/auth/credentials/LoginCredentials";
import {SsInputComponent} from "../../element-group-native/ss-input/ss-input.component";
import {InputType} from "../../element-group-native/ss-input/models/InputType";
import {TagType} from "../../../../models/html/TagType";

@Component({
    selector: 'login-input',
    templateUrl: './login-input.component.html',
    styleUrls: ['./login-input.component.css']
})
export class LoginInputComponent {
    @Input() inputType: AuthInputType;
    @Input() loginCredentials: LoginCredentials;
    @Output() inputEvent: EventEmitter<void> = new EventEmitter<void>();
    @ViewChild(SsInputComponent) inputElement: SsInputComponent;
    constructor() {
        
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
        }
        this.emitInputEvent();
    }

    protected getTitleText(): string {
        return this.inputType + ":";
    }

    protected getPlaceholder(): string {
        return '';
    }

    protected setInputValue(sanitizedInput: string) {
        this.inputElement.value = sanitizedInput;
    }

    protected emitInputEvent() {
        this.inputEvent.emit();
    }

    protected setUsername(username: string) {
        this.loginCredentials.username = username;
    }

    protected setPassword(password: string) {
        this.loginCredentials.password = password;
    }

    protected getInputType(): InputType {
        switch (this.inputType) {
            case AuthInputType.USERNAME:
                return InputType.TEXT;
            case AuthInputType.PASSWORD:
                return InputType.PASSWORD;
            default:
                return InputType.TEXT;
        }
    }

    protected readonly TagType = TagType;
}
