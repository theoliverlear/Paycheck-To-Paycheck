// signup-console.component.ts
import {
    Component,
    EventEmitter,
    OnDestroy,
    OnInit,
    Output
} from "@angular/core";
import {TagType} from "../../../../models/html/TagType";
import {ButtonText} from "../../ss-button/models/ButtonText";
import {ElementSize} from "../../../../models/ElementSize";
import {
    SignupCredentials
} from "../../../../models/auth/credentials/SignupCredentials";
import {
    SignupWebSocketService
} from "../../../../services/server/websocket/signup-websocket.service";
import {WebSocketCapable} from "../../../../models/WebSocketCapable";
import {Subscription} from "rxjs";
import {HashPasswordService} from "../../../../services/hash-password.service";
import {AuthPopup} from "../../../../models/auth/AuthPopup";
import {
    AuthPopupEventEmitter,
    WebSocketAuthResponse,
    PossibleAuthPopup, HttpAuthResponse
} from "../../../../models/auth/types";
import {
    EmailValidatorService
} from "../../../../services/email-validator.service";
import {FilledFieldsService} from "../../../../services/filled-fields.service";
import {PasswordMatchService} from "../../../../services/password-match.service";
import {
    CredentialSending
} from "../../../../models/auth/credentials/CredentialSending";
import {Router} from "@angular/router";
import {
    LoggedInStatusService
} from "../../../../services/server/http/logged-in-status.service";
import {
    HttpSignupService
} from "../../../../services/server/http/http-signup.service";


@Component({
    selector: 'signup-console',
    templateUrl: './signup-console.component.html',
    styleUrls: ['./signup-console.component.css']
})
export class SignupConsoleComponent implements OnInit, WebSocketCapable, OnDestroy, CredentialSending {
    @Output() authPopupChange: AuthPopupEventEmitter = new EventEmitter<PossibleAuthPopup>();
    webSocketSubscription: Subscription;
    private signupCredentials: SignupCredentials = new SignupCredentials();
    constructor(
        // private signupWebSocket: SignupWebSocketService,
                private hashPasswordService: HashPasswordService,
                private emailValidatorService: EmailValidatorService,
                private filledFieldsService: FilledFieldsService,
                private passwordMatchService: PasswordMatchService,
                private router: Router,
                private loggedInStatusService: LoggedInStatusService,
                private httpSignupService: HttpSignupService) {
    }

    ngOnInit(): void {
        // this.initializeWebSocket();
        this.subscribeToAuthEvents();
        this.loggedInStatusService.isLoggedIn().subscribe((authResponse: HttpAuthResponse) => {
            if (authResponse.payload.isAuthorized) {
                this.router.navigate(['/budget']);
            } else {
                console.log('User is not logged in.');
            }
        });


    }

    subscribeToAuthEvents(): void {
        this.emailValidatorService.validEmail$.subscribe((popup: AuthPopup): void => {
            this.emitAuthPopup(popup);
        });
        this.filledFieldsService.fieldsFilled$.subscribe((popup: AuthPopup): void => {
            this.emitAuthPopup(popup);
        });
        this.passwordMatchService.passwordMismatch$.subscribe((popup: AuthPopup): void => {
            this.emitAuthPopup(popup);
        });
    }

    ngOnDestroy(): void {
        this.emitAuthPopup(null);
        this.signupCredentials = new SignupCredentials();
    }

    emitAuthPopup(authPopup: AuthPopup): void {
        this.authPopupChange.emit(authPopup);
    }

    initializeWebSocket(): void {
        // this.signupWebSocket.connect();
        // this.webSocketSubscription = this.signupWebSocket.getMessages().subscribe(
        //     (response: WebSocketAuthResponse): void => {
        //         console.log('Message received');
        //         if (response) {
        //             console.log('WebSocket Signup: ', response);
        //             if (response.message.payload.isAuthorized) {
        //                 this.router.navigate(['/budget'])
        //             } else {
        //                 this.emitAuthPopup(AuthPopup.INCORRECT_USERNAME_OR_PASSWORD);
        //             }
        //         } else {
        //             console.log('No response found.');
        //         }
        //     },
        //     (error) => {
        //         console.error('WebSocket error: ', error);
        //     }
        // );
        // console.log('WebSocket subscription setup completed.');
    }


    protected handleCredentialChange(signupCredentials: SignupCredentials): void {
        this.signupCredentials = signupCredentials;
        this.handlePasswordChange(false);
        this.handleEmailChange(false);
    }

    protected handlePasswordChange(emitNull: boolean = true) {
        this.passwordMatchService.handlePasswordMismatch(this.signupCredentials.password,
                                                         this.signupCredentials.confirmPassword,
                                                         emitNull);
    }

    protected handleEmailChange(emitNull: boolean = true): void {
        if (this.signupCredentials.email !== '') {
            this.emailValidatorService.handleEmail(this.signupCredentials.email,
                emitNull);
        }
    }

    private isFilledFields(): boolean {
        const fields: string[] = [
            this.signupCredentials.username,
            this.signupCredentials.password,
            this.signupCredentials.confirmPassword,
            this.signupCredentials.email
        ];
        return this.filledFieldsService.isFilledFields(fields);
    }

    isValidCredentialInputs(): boolean {
        const filledFields: boolean = this.isFilledFields();
        const validEmail: boolean = this.emailValidatorService.isValidEmail(this.signupCredentials.email);
        const passwordsMatch: boolean = !this.passwordMatchService.isMismatchPassword(this.signupCredentials.password,
                                                                                      this.signupCredentials.confirmPassword)
        const termsAgreed: boolean = this.signupCredentials.termsAgreed;
        return filledFields && validEmail && passwordsMatch && termsAgreed;
    }

    protected successfulConfirm(): boolean {
        if (!this.isFilledFields()) {
            this.filledFieldsService.handleFilledFields(false);
            return false;
        }
        if (!this.signupCredentials.termsAgreed) {
            this.emitAuthPopup(AuthPopup.AGREE_TERMS);
            return false
        }
        return true;
    }

    protected confirm(): void {
        if (this.successfulConfirm() && this.isValidCredentialInputs()) {
            this.sendCredentialsToServer();
        }
    }

    sendCredentialsToServer(): void {
        const originalPassword: string = this.signupCredentials.password;
        const originalConfirmPassword: string = this.signupCredentials.confirmPassword;
        const hashedPassword: string = this.hashPasswordService.hashPassword(originalPassword);
        const hashedConfirmPassword: string = this.hashPasswordService.hashPassword(originalConfirmPassword);
        this.signupCredentials.password = hashedPassword;
        this.signupCredentials.confirmPassword = hashedConfirmPassword;
        // this.signupWebSocket.sendMessage(this.signupCredentials);
        this.httpSignupService.signup(this.signupCredentials).subscribe((httoAuthResponse: HttpAuthResponse) => {
            if (httoAuthResponse.payload.isAuthorized) {
                this.router.navigate(['/budget']);
            } else {
                console.log('User is not logged in.');
            }
        }, (error) => {
            console.error('Signup error: ', error);
            this.emitAuthPopup(AuthPopup.INCORRECT_USERNAME_OR_PASSWORD);
        });
        this.signupCredentials.password = originalPassword;
        this.signupCredentials.confirmPassword = originalConfirmPassword;
    }

    protected readonly TagType = TagType;
    protected readonly ButtonText = ButtonText;
    protected readonly ElementSize = ElementSize;
}
