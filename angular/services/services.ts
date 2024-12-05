import {AuthGuard} from "./guard/auth.guard";
import {LoginService} from "./server/login.service";
import {SignupService} from "./server/signup.service";
import {UserService} from "./server/user.service";
import {WelcomeService} from "./server/welcome.service";
import {ErrorHandlerService} from "./error-handler.service";
import {HashPasswordService} from "./hash-password.service";

export const services: any[] = [
    // Guards
    AuthGuard,
    // Server
    LoginService,
    SignupService,
    UserService,
    WelcomeService,
    // Client Services
    ErrorHandlerService,
    HashPasswordService
]