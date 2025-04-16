import {EventEmitter} from "@angular/core";
import {AuthPopup} from "./AuthPopup";

export type PossibleAuthPopup = AuthPopup | null;
export type AuthPopupEventEmitter = EventEmitter<PossibleAuthPopup>;
export type WebSocketAuthResponse = {
    message: {
        payload: {
            isAuthorized: boolean;
        }
    }
};
export type HttpAuthResponse = {
    payload: {
        isAuthorized: boolean;
    }
};