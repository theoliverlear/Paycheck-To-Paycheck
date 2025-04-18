import {Injectable} from "@angular/core";
import {WebSocketService} from "./websocket.service";
import {Income} from "../../../models/income/Income";


@Injectable({
    providedIn: 'root'
})
export class WageIncomeWebSocketService extends WebSocketService<Income, any> {
    private static readonly URL: string = 'ws://localhost:8001/ws/wage-income';
    constructor() {
        super(WageIncomeWebSocketService.URL);
    }
}