import {Injectable} from "@angular/core";
import {WebSocketService} from "./websocket.service";
import {Bill} from "../../../models/bill/Bill";

@Injectable({
    providedIn: 'root'
})
export class BillWebSocketService extends WebSocketService<Bill, any> {
    private static readonly URL: string = 'ws://localhost:8001/ws/bill';
    constructor() {
        super(BillWebSocketService.URL);
    }
}