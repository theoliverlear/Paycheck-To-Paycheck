import {Injectable} from "@angular/core";
import {WebSocketService} from "./websocket.service";
import {Income} from "../../../models/income/Income";
import {environment} from "../../../environments/environment";


@Injectable({
    providedIn: 'root'
})
export class WageIncomeWebSocketService extends WebSocketService<Income, any> {
    private static readonly URL: string = `${environment.webSocketUrl}/wage-income`;
    constructor() {
        super(WageIncomeWebSocketService.URL);
    }
}