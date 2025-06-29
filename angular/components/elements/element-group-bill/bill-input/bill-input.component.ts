// bill-input.component.ts
import {Component, EventEmitter, Input, OnInit, Output} from "@angular/core";
import {InputTimeType} from "../../../../models/input/InputTimeType";
import {
    closeIconImageAsset,
    confirmIconImageAsset
} from "../../../../assets/imageAssets";
import {TagType} from "../../../../models/html/TagType";
import {fadeInOutAnimation} from "../../../animations/animations";
import {
    quickFadeInAnimationProperties
} from "../../../animations/animationProperties";
import {Bill} from "../../../../models/bill/Bill";
import {Subscription} from "rxjs";
import {
    OneTimeBillWebsocketService
} from "../../../../services/server/websocket/one-time-bill-websocket.service";
import {WebSocketCapable} from "../../../../models/WebSocketCapable";
import {
    RecurringBillTimeInterval
} from "../recurring-bill-dropdown/models/RecurringBillTimeInterval";
import {
    RecurringBillWebSocketService
} from "../../../../services/server/websocket/recurring-bill-websocket.service";
import {
    WebSocketBill, WebSocketOneTimeBill,
    WebSocketRecurringBill
} from "../../../../models/paycheck/types";

@Component({
    selector: 'bill-input',
    templateUrl: './bill-input.component.html',
    styleUrls: ['./bill-input.component.css'],
    animations: [
        fadeInOutAnimation
    ]
})
export class BillInputComponent implements OnInit, WebSocketCapable {
    @Input() inputTimeType: InputTimeType = InputTimeType.ONE_TIME;
    @Output() billAdded: EventEmitter<WebSocketBill> = new EventEmitter<WebSocketBill>();
    protected shown: boolean = false;
    bill: Bill = new Bill();
    webSocketSubscription: Subscription;
    recurringBillSubscription: Subscription;
    constructor(private billWebSocket: OneTimeBillWebsocketService,
                private recurringBillWebSocket: RecurringBillWebSocketService) {
    }

    ngOnInit(): void {
        this.setDefaultTimeType();
        console.log(this.bill);
        this.initializeWebSocket();
    }

    initializeWebSocket(): void {
        this.initializeOneTimeBillWebSocket();
        this.initializeRecurringBillWebSocket();
    }

    private initializeRecurringBillWebSocket(): void {
        this.recurringBillWebSocket.connect();
        this.recurringBillSubscription = this.recurringBillWebSocket.getMessages().subscribe(
            (bill: WebSocketRecurringBill): void => {
                if (bill) {
                    this.billAdded.emit(bill);
                    console.log('WebSocket bill:', bill);
                }
            },
            (error) => {
                console.error('WebSocket error:', error);
            }
        )
    }

    private initializeOneTimeBillWebSocket(): void {
        this.billWebSocket.connect();
        this.webSocketSubscription = this.billWebSocket.getMessages().subscribe(
            (bill: WebSocketOneTimeBill): void => {
                if (bill) {
                    this.billAdded.emit(bill);
                    console.log('WebSocket bill:', bill);
                }
            },
            (error) => {
                console.error('WebSocket error:', error);
            }
        );
    }

    private setDefaultTimeType(): void {
        this.bill.timeType = InputTimeType.ONE_TIME;
    }

    public clearInputs(): void {
        this.bill = new Bill();
        this.setDefaultTimeType();
    }

    public updateBill(bill: Bill): void {
        const originalTimeType: InputTimeType = this.bill.timeType;
        this.bill = bill;
        this.bill.timeType = originalTimeType;
    }

    public updateBillInterval(billInterval: RecurringBillTimeInterval): void {
        this.bill.billInterval = billInterval;
    }

    public updateInputTimeType(inputTimeType: InputTimeType): void {
        this.bill.timeType = inputTimeType;
    }

    public confirm(): void {
        if (this.isRecurringBill()) {
            this.recurringBillWebSocket.sendMessage(this.bill);
        } else {
            this.billWebSocket.sendMessage(this.bill);
        }
        this.shown = false;
    }

    public open(): void {
        this.shown = true;
    }

    public close(): void {
        this.shown = false;
    }

    protected isRecurringBill(): boolean {
        return this.bill.timeType === InputTimeType.RECURRING;
    }

    public getAnimationProperties() {
        return {
            value: '',
            params: {
                fadeInDuration: quickFadeInAnimationProperties.duration,
                fadeOutDuration: quickFadeInAnimationProperties.duration,
                waitDuration: quickFadeInAnimationProperties.delay
            }
        }
    }
    protected readonly closeIconImageAsset = closeIconImageAsset;
    protected readonly TagType = TagType;
    protected readonly confirmIconImageAsset = confirmIconImageAsset;
}
