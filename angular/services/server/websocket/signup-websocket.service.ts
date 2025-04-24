import {Injectable} from "@angular/core";
import {WebSocketService} from "./websocket.service";
import {
    SignupCredentials
} from "../../../models/auth/credentials/SignupCredentials";
import {
    WebSocketAuthResponse
} from "../../../models/auth/types";
import {environment} from "../../../environments/environment";

@Injectable({
    providedIn: 'root'
})
export class SignupWebSocketService extends WebSocketService<SignupCredentials, WebSocketAuthResponse> {
    private static readonly URL: string = `${environment.webSocketUrl}/signup`;
    constructor() {
        super(SignupWebSocketService.URL);
    }
}