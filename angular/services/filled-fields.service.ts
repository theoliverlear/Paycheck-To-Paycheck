import {Injectable} from "@angular/core";
import {Observable, Subject} from "rxjs";
import {AuthPopup} from "../models/auth/AuthPopup";

@Injectable({
    providedIn: 'root'
})
export class FilledFieldsService {
    private filledFieldsSubject: Subject<AuthPopup> = new Subject();
    fieldsFilled$: Observable<AuthPopup> = this.filledFieldsSubject.asObservable();
    constructor() {

    }
    isFilledFields(fields: string[]): boolean {
        for (let field of fields) {
            if (!this.isFilledField(field)) {
                return false;
            }
        }
        return true;
    }
    isFilledField(field: string): boolean {
        return field.length > 0;
    }
    emitFilledFields(authPopup: AuthPopup) {
        this.filledFieldsSubject.next(authPopup);
    }
    handleFilledFields(isFilledFields: boolean) {
        const authPopup: AuthPopup = isFilledFields ? null : AuthPopup.FILL_ALL_FIELDS;
        this.emitFilledFields(authPopup);
    }
}