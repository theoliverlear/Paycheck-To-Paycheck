import {Injectable} from "@angular/core";
import {WebSocketService} from "./websocket.service";
import {Income} from "../../../models/income/Income";
import {environment} from "../../../environments/environment";

@Injectable({
    providedIn: 'root'
})
export class RecurringIncomeWebSocketService extends WebSocketService<Income, any> {
    private static readonly URL: string = `${environment.webSocketUrl}/recurring-income`;
    constructor() {
        super(RecurringIncomeWebSocketService.URL);
    }
}