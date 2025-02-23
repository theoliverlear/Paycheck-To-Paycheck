import {Injectable} from "@angular/core";
import {Income} from "../../../models/income/Income";
import {WebSocketService} from "./websocket.service";

@Injectable({
    providedIn: 'root'
})
export class IncomeWebSocketService extends WebSocketService<Income> {
    private static readonly URL: string = 'ws://localhost:8001/ws/income';
    constructor() {
        super(IncomeWebSocketService.URL);
    }
}