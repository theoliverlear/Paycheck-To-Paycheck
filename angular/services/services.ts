import {AuthGuard} from "./guard/auth.guard";
import {LoginService} from "./server/login.service";
import {SignupService} from "./server/signup.service";
import {UserService} from "./server/user.service";
import {WelcomeService} from "./server/welcome.service";
import {ErrorHandlerService} from "./error-handler.service";
import {HashPasswordService} from "./hash-password.service";
import {
    OneTimeBillWebsocketService
} from "./server/websocket/one-time-bill-websocket.service";
import {WebSocketService} from "./server/websocket/websocket.service";
import {
    OneTimeIncomeWebSocketService
} from "./server/websocket/one-time-income-websocket.service";
import {
    SignupWebSocketService
} from "./server/websocket/signup-websocket.service";
import {
    RecurringIncomeWebSocketService
} from "./server/websocket/recurring-income-websocket.service";
import {HttpClientService} from "./server/http/http-client.service";
import {LoggedInStatusService} from "./server/http/logged-in-status.service";
import {LogoutService} from "./server/http/logout.service";
import {
    RecurringBillWebSocketService
} from "./server/websocket/recurring-bill-websocket.service";
import {
    WageIncomeWebSocketService
} from "./server/websocket/wage-income-websocket.service";

export const services: any[] = [
    // Guards
    AuthGuard,
    // HTTP
    HttpClientService,
    LoggedInStatusService,
    LogoutService,
    // Server
    LoginService,
    SignupService,
    UserService,
    WelcomeService,
    // WebSocket
    OneTimeBillWebsocketService,
    OneTimeIncomeWebSocketService,
    RecurringBillWebSocketService,
    RecurringIncomeWebSocketService,
    WageIncomeWebSocketService,
    SignupWebSocketService,
    WebSocketService,
    // Client Services
    ErrorHandlerService,
    HashPasswordService
]