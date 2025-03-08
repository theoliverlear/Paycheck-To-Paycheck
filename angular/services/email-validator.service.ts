import {Injectable} from "@angular/core";
import {Observable, Subject} from "rxjs";
import {AuthPopup} from "../models/auth/AuthPopup";

@Injectable({
    providedIn: 'root'
})
export class EmailValidatorService {
    private validEmailSubject: Subject<AuthPopup> = new Subject();
    validEmail$: Observable<AuthPopup> = this.validEmailSubject.asObservable();
    constructor() {

    }
    isValidEmail(email: string): boolean {
        const emailPattern: RegExp = new RegExp('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$');
        return emailPattern.test(email);
    }
    emitValidEmail(isValid: boolean, emitNull: boolean = true) {
        const authPopup: AuthPopup = isValid ? null : AuthPopup.INVALID_EMAIL;
        const doesNotEmitNull: boolean = !authPopup && !emitNull;
        if (!doesNotEmitNull) {
            this.validEmailSubject.next(authPopup);
        }
    }
    handleEmail(email: string, emitNull: boolean = true): void {
        const isValid: boolean = this.isValidEmail(email);
        this.emitValidEmail(isValid, emitNull);
    }
}