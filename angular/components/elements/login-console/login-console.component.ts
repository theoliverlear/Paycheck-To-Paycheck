// login-console.component.ts
import {
    Component,
    EventEmitter,
    OnDestroy,
    OnInit,
    Output
} from "@angular/core";
import {TagType} from "../../../models/html/TagType";
import {ButtonText} from "../ss-button/models/ButtonText";
import {ElementSize} from "../../../models/ElementSize";
import {
    LoginCredentials
} from "../../../models/auth/credentials/LoginCredentials";
import {WebSocketCapable} from "../../../models/WebSocketCapable";
import {Subscription} from "rxjs";
import {
    LoginWebSocketService
} from "../../../services/server/websocket/login-websocket.service";
import {HashPasswordService} from "../../../services/hash-password.service";
import {
    AuthPopupEventEmitter,
    WebSocketAuthResponse,
    PossibleAuthPopup
} from "../../../models/auth/types";
import {
    CredentialSending
} from "../../../models/auth/credentials/CredentialSending";
import {AuthPopup} from "../../../models/auth/AuthPopup";
import {FilledFieldsService} from "../../../services/filled-fields.service";
import {Router} from "@angular/router";

@Component({
    selector: 'login-console',
    templateUrl: './login-console.component.html',
    styleUrls: ['./login-console.component.css']
})
export class LoginConsoleComponent implements WebSocketCapable, OnInit, OnDestroy, CredentialSending {
    private loginCredentials: LoginCredentials = new LoginCredentials();
    @Output() authPopupChange: AuthPopupEventEmitter = new EventEmitter<PossibleAuthPopup>();
    webSocketSubscription: Subscription;
    constructor(private loginWebSocket: LoginWebSocketService,
                private hashPasswordService: HashPasswordService,
                private filledFieldsService: FilledFieldsService,
                private router: Router) {
        
    }

    isFilledFields(): boolean {
        const fields: string[] = [
            this.loginCredentials.username,
            this.loginCredentials.password,
        ]
        return this.filledFieldsService.isFilledFields(fields);
    }

    subscribeToAuthEvents(): void {
        this.filledFieldsService.fieldsFilled$.subscribe((popup: AuthPopup): void => {
           this.emitAuthPopup(popup);
        });
    }



    isValidCredentialInputs(): boolean {
        return this.isFilledFields();
    }

    sendCredentialsToServer() {
        const originalPassword: string = this.loginCredentials.password;
        const hashedPassword: string = this.hashPasswordService.hashPassword(originalPassword);
        this.loginCredentials.password = hashedPassword;
        this.loginWebSocket.sendMessage(this.loginCredentials);
        this.loginCredentials.password = originalPassword;
    }

    ngOnInit() {
        this.initializeWebSocket();
        this.subscribeToAuthEvents();
    }

    ngOnDestroy() {
        this.emitAuthPopup(null);
        this.loginCredentials = new LoginCredentials();
    }

    emitAuthPopup(authPopup: AuthPopup): void {
        this.authPopupChange.emit(authPopup);
    }

    initializeWebSocket() {
        this.loginWebSocket.connect();
        this.webSocketSubscription = this.loginWebSocket.getMessages().subscribe(
            (response: WebSocketAuthResponse): void => {
                console.log(response);
                if (response) {
                    console.log('WebSocket Login: ', response);
                    if (response.message.payload.isAuthorized) {
                        this.router.navigate(['/budget'])
                    } else {
                        this.emitAuthPopup(AuthPopup.INCORRECT_USERNAME_OR_PASSWORD);
                    }
                } else {
                    console.log('No response found.');
                }
            },
            (error) => {
                console.error('WebSocket error: ', error);
            }
        )
    }

    handleFilledFields(): void {
        this.filledFieldsService.handleFilledFields(this.isFilledFields());
    }

    protected confirm(): void {
        if (!this.isFilledFields()) {
            this.handleFilledFields();
        }
        if (this.isValidCredentialInputs()) {
            this.sendCredentialsToServer();
        }
    }

    protected handleCredentialChange(loginCredentials: LoginCredentials) {
        console.log(loginCredentials);
        this.loginCredentials = loginCredentials;
    }
    protected readonly TagType = TagType;
    protected readonly ButtonText = ButtonText;
    protected readonly ElementSize = ElementSize;
}
