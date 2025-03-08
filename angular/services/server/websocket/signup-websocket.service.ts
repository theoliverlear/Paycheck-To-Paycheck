import {Injectable} from "@angular/core";
import {WebSocketService} from "./websocket.service";
import {
    SignupCredentials
} from "../../../models/auth/credentials/SignupCredentials";
import {
    AuthResponse
} from "../../../components/elements/auth-console/models/types";

@Injectable({
    providedIn: 'root'
})
export class SignupWebSocketService extends WebSocketService<SignupCredentials, AuthResponse> {
    private static readonly URL: string = 'ws://localhost:8001/ws/signup';
    constructor() {
        super(SignupWebSocketService.URL);
    }
}