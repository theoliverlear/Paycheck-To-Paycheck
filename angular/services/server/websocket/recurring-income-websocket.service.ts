import {Injectable} from "@angular/core";
import {WebSocketService} from "./websocket.service";
import {Income} from "../../../models/income/Income";

@Injectable({
    providedIn: 'root'
})
export class RecurringIncomeWebSocketService extends WebSocketService<Income, any> {
    private static readonly URL: string = 'ws://localhost:8001/ws/recurring-income';
    constructor() {
        super(RecurringIncomeWebSocketService.URL);
    }
}