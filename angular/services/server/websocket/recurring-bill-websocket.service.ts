import {Injectable} from "@angular/core";
import {WebSocketService} from "./websocket.service";
import {Bill} from "../../../models/bill/Bill";

@Injectable({
    providedIn: 'root'
})
export class RecurringBillWebSocketService extends WebSocketService<Bill, any> {
    private static readonly URL: string = 'ws://localhost:8001/ws/recurring-bill';
    constructor() {
        super(RecurringBillWebSocketService.URL);
    }
}