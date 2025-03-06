// login-console.component.ts 
import {
    Component,
    EventEmitter,
    Input, OnInit,
    Output,
    ViewChild
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

@Component({
    selector: 'login-console',
    templateUrl: './login-console.component.html',
    styleUrls: ['./login-console.component.css']
})
export class LoginConsoleComponent implements WebSocketCapable, OnInit {
    private loginCredentials: LoginCredentials = new LoginCredentials();
    subscription: Subscription;
    constructor(private loginWebSocket: LoginWebSocketService,
                private hashPasswordService: HashPasswordService) {
        
    }

    ngOnInit() {
        this.initializeWebSocket();
    }

    initializeWebSocket() {
        this.loginWebSocket.connect();
        this.subscription = this.loginWebSocket.getMessages().subscribe(
            (response: any): void => {
                if (response) {
                    console.log('WebSocket Signup: ', response);
                } else {
                    console.log('No response found.');
                }
            },
            (error) => {
                console.error('WebSocket error: ', error);
            }
        )
    }

    protected confirm(): void {
        const originalPassword: string = this.loginCredentials.password;
        const hashedPassword: string = this.hashPasswordService.hashPassword(originalPassword);
        this.loginCredentials.password = hashedPassword;
        this.loginWebSocket.sendMessage(this.loginCredentials);
        this.loginCredentials.password = originalPassword;
    }

    protected handleCredentialChange(loginCredentials: LoginCredentials) {
        console.log(loginCredentials);
        this.loginCredentials = loginCredentials;
    }
    protected readonly TagType = TagType;
    protected readonly ButtonText = ButtonText;
    protected readonly ElementSize = ElementSize;
}
