import {Subscription} from "rxjs";

export interface WebSocketCapable {
    webSocketSubscription: Subscription;
    initializeWebSocket(): void;
}