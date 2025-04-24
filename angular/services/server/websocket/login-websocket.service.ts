import {Injectable} from "@angular/core";
import {WebSocketService} from "./websocket.service";
import {
    LoginCredentials
} from "../../../models/auth/credentials/LoginCredentials";
import {
    WebSocketAuthResponse
} from "../../../models/auth/types";
import {environment} from "../../../environments/environment";

@Injectable({
    providedIn: 'root'
})
export class LoginWebSocketService extends WebSocketService<LoginCredentials, WebSocketAuthResponse> {
    private static readonly URL: string = `${environment.webSocketUrl}/login`;
    constructor() {
        super(LoginWebSocketService.URL);
    }
}