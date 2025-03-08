import {Injectable} from "@angular/core";
import {Observable, Subject} from "rxjs";
import {AuthPopup} from "../models/auth/AuthPopup";

@Injectable({
    providedIn: 'root'
})
export class PasswordMatchService {
    private passwordMismatchSubject: Subject<AuthPopup> = new Subject();
    passwordMismatch$: Observable<AuthPopup> = this.passwordMismatchSubject.asObservable();
    constructor() {

    }
    isMismatchPassword(password: string, confirmPassword: string): boolean {
        return password !== confirmPassword;
    }
    emitPasswordMismatch(authPopup: AuthPopup) {
        this.passwordMismatchSubject.next(authPopup);
    }
    handlePasswordMismatch(password: string, confirmPassword: string, emitNull: boolean = true) {
        const isMismatch: boolean = this.isMismatchPassword(password, confirmPassword);
        const authPopup: AuthPopup = isMismatch ? AuthPopup.PASSWORDS_DONT_MATCH : null;
        this.emitPasswordMismatch(authPopup);
    }
}