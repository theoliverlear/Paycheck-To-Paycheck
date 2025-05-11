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
import {HttpPaycheckService} from "./server/http/http-paycheck.service";
import {HttpSignupService} from "./server/http/http-signup.service";
import {
    HttpGetAllBillsService
} from "./server/http/http-get-all-bills.service";
import {
    HttpGetAllIncomesService
} from "./server/http/http-get-all-incomes.service";
import {HttpLoginService} from "./server/http/http-login.service";
import {DelayService} from "./delay.service";
import {EmailValidatorService} from "./email-validator.service";
import {FilledFieldsService} from "./filled-fields.service";
import {PasswordMatchService} from "./password-match.service";
import {
    HttpDeleteOneTimeBillService
} from "./server/http/http-delete-one-time-bill.service";
import {
    HttpDeleteOneTimeIncomeService
} from "./server/http/http-delete-one-time-income.service";
import {
    HttpDeleteRecurringBillService
} from "./server/http/http-delete-recurring-bill.service";
import {
    HttpDeleteRecurringIncomeService
} from "./server/http/http-delete-recurring-income.service";
import {
    HttpDeleteWageIncomeService
} from "./server/http/http-delete-wage-income.service";

export const services: any[] = [
    // Guards
    AuthGuard,
    // HTTP
    HttpClientService,
    HttpDeleteOneTimeBillService,
    HttpDeleteOneTimeIncomeService,
    HttpDeleteRecurringBillService,
    HttpDeleteRecurringIncomeService,
    HttpDeleteWageIncomeService,
    HttpGetAllBillsService,
    HttpGetAllIncomesService,
    HttpLoginService,
    LoggedInStatusService,
    LogoutService,
    HttpPaycheckService,
    HttpSignupService,
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
    DelayService,
    EmailValidatorService,
    ErrorHandlerService,
    FilledFieldsService,
    HashPasswordService,
    PasswordMatchService
]