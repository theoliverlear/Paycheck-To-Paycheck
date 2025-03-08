import {EventEmitter} from "@angular/core";
import {AuthPopup} from "../../../../models/auth/AuthPopup";

export type PossibleAuthPopup = AuthPopup | null;
export type AuthPopupEventEmitter = EventEmitter<PossibleAuthPopup>;
export type AuthResponse = {
    message: {
        payload: {
            isAuthorized: boolean;
        }
    }
};