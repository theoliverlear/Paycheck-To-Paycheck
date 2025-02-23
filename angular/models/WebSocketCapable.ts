import {Subscription} from "rxjs";

export interface WebSocketCapable {
    subscription: Subscription;
    initializeWebSocket(): void;
}