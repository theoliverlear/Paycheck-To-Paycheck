// signup-console.component.ts 
import {Component, OnDestroy, OnInit} from "@angular/core";
import {TagType} from "../../../models/html/TagType";
import {ButtonText} from "../ss-button/models/ButtonText";
import {ElementSize} from "../../../models/ElementSize";
import {
    SignupCredentials
} from "../../../models/auth/credentials/SignupCredentials";
import {
    SignupWebSocketService
} from "../../../services/server/websocket/signup-websocket.service";
import {WebSocketCapable} from "../../../models/WebSocketCapable";
import {Subscription} from "rxjs";
import {HashPasswordService} from "../../../services/hash-password.service";

@Component({
    selector: 'signup-console',
    templateUrl: './signup-console.component.html',
    styleUrls: ['./signup-console.component.css']
})
export class SignupConsoleComponent implements OnInit, WebSocketCapable {
    subscription: Subscription;
    private signupCredentials: SignupCredentials = new SignupCredentials();
    constructor(private signupWebSocket: SignupWebSocketService,
                private hashPasswordService: HashPasswordService) {
        
    }

    ngOnInit() {
        this.initializeWebSocket();
    }

    initializeWebSocket() {
        this.signupWebSocket.connect();
        this.subscription = this.signupWebSocket.getMessages().subscribe(
            (response: any): void => {
                console.log('Message received');
                if (response) {
                    console.log('WebSocket Signup: ', response);
                } else {
                    console.log('No response found.');
                }
            },
            (error) => {
                console.error('WebSocket error: ', error);
            }
        );
        console.log('WebSocket subscription setup completed.');
    }


    protected handleCredentialChange(signupCredentials: SignupCredentials) {
        console.log(signupCredentials);
        this.signupCredentials = signupCredentials;
    }

    protected confirm() {
        const originalPassword: string = this.signupCredentials.password;
        const hashedPassword: string = this.hashPasswordService.hashPassword(originalPassword);
        this.signupCredentials.password = hashedPassword;
        this.signupWebSocket.sendMessage(this.signupCredentials);
        this.signupCredentials.password = originalPassword;
    }

    protected readonly TagType = TagType;
    protected readonly ButtonText = ButtonText;
    protected readonly ElementSize = ElementSize;
}
