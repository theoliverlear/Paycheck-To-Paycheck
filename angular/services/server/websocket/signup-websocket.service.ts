import {Injectable} from "@angular/core";
import {WebSocketService} from "./websocket.service";
import {
    SignupCredentials
} from "../../../models/auth/credentials/SignupCredentials";

@Injectable({
    providedIn: 'root'
})
export class SignupWebSocketService extends WebSocketService<SignupCredentials> {
    private static readonly URL: string = 'ws://localhost:8001/ws/signup';
    constructor() {
        super(SignupWebSocketService.URL);
    }
}