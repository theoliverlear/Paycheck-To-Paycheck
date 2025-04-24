import {Injectable} from "@angular/core";
import {WebSocketService} from "./websocket.service";
import {Bill} from "../../../models/bill/Bill";
import {environment} from "../../../environments/environment";

@Injectable({
    providedIn: 'root'
})
export class RecurringBillWebSocketService extends WebSocketService<Bill, any> {
    private static readonly URL: string = `${environment.webSocketUrl}/recurring-bill`;
    constructor() {
        super(RecurringBillWebSocketService.URL);
    }
}