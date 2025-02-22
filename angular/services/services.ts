import {AuthGuard} from "./guard/auth.guard";
import {LoginService} from "./server/login.service";
import {SignupService} from "./server/signup.service";
import {UserService} from "./server/user.service";
import {WelcomeService} from "./server/welcome.service";
import {ErrorHandlerService} from "./error-handler.service";
import {HashPasswordService} from "./hash-password.service";
import {
    BillWebSocketService
} from "./server/websocket/bill-websocket.service";
import {WebSocketService} from "./server/websocket/websocket.service";

export const services: any[] = [
    // Guards
    AuthGuard,
    // Server
    LoginService,
    SignupService,
    UserService,
    WelcomeService,
    // WebSocket
    BillWebSocketService,
    WebSocketService,
    // Client Services
    ErrorHandlerService,
    HashPasswordService
]