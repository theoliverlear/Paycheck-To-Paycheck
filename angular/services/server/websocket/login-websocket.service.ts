import {Injectable} from "@angular/core";
import {WebSocketService} from "./websocket.service";
import {
    LoginCredentials
} from "../../../models/auth/credentials/LoginCredentials";
import {
    AuthResponse
} from "../../../components/elements/auth-console/models/types";

@Injectable({
    providedIn: 'root'
})
export class LoginWebSocketService extends WebSocketService<LoginCredentials, AuthResponse> {
    private static readonly URL: string = 'ws://localhost:8001/ws/login';
    constructor() {
        super(LoginWebSocketService.URL);
    }
}