import {Injectable} from "@angular/core";
import {WebSocketService} from "./websocket.service";
import {Bill} from "../../../models/bill/Bill";
import {environment} from "../../../environments/environment";

@Injectable({
    providedIn: 'root'
})
export class OneTimeBillWebsocketService extends WebSocketService<Bill, any> {
    private static readonly URL: string = `${environment.webSocketUrl}/one-time-bill`;
    constructor() {
        super(OneTimeBillWebsocketService.URL);
    }
}