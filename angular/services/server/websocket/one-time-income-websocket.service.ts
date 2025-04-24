import {Injectable} from "@angular/core";
import {Income} from "../../../models/income/Income";
import {WebSocketService} from "./websocket.service";
import {environment} from "../../../environments/environment";

@Injectable({
    providedIn: 'root'
})
export class OneTimeIncomeWebSocketService extends WebSocketService<Income, any> {
    private static readonly URL: string = `${environment.webSocketUrl}/one-time-income`;
    constructor() {
        super(OneTimeIncomeWebSocketService.URL);
    }
}