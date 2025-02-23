// bill-input.component.ts
import {Component, Input, OnInit} from "@angular/core";
import {InputTimeType} from "../../../models/input/InputTimeType";
import {
    closeIconImageAsset,
    confirmIconImageAsset
} from "../../../assets/imageAssets";
import {TagType} from "../../../models/html/TagType";
import {fadeInOutAnimation} from "../../animations/animations";
import {
    quickFadeInAnimationProperties
} from "../../animations/animationProperties";
import {Bill} from "../../../models/bill/Bill";
import {Subscription} from "rxjs";
import {
    BillWebSocketService
} from "../../../services/server/websocket/bill-websocket.service";
import {WebSocketCapable} from "../../../models/WebSocketCapable";
import {
    RecurringBillTimeInterval
} from "../recurring-bill-dropdown/models/RecurringBillTimeInterval";

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
    protected shown: boolean = true;
    bill: Bill = new Bill();
    subscription: Subscription;
    constructor(private billWebSocketService: BillWebSocketService) {
        console.log(RecurringBillTimeInterval.values())
    }

    ngOnInit() {
        this.setDefaultTimeType();
        console.log(this.bill);
        this.initializeWebSocket();
    }

    initializeWebSocket(): void {
        this.billWebSocketService.connect();
        this.subscription = this.billWebSocketService.getMessages().subscribe(
            (bill: Bill): void => {
                if (bill) {
                    console.log('WebSocket bill:', bill);
                }
            },
            (error) => {
                console.error('WebSocket error:', error);
            }
        );
    }

    private setDefaultTimeType() {
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
        console.log(this.bill);
    }

    public updateBillInterval(billInterval: RecurringBillTimeInterval): void {
        this.bill.billInterval = billInterval;
        console.log(this.bill);
    }

    public updateInputTimeType(inputTimeType: InputTimeType): void {
        this.bill.timeType = inputTimeType;
        console.log(this.bill);
    }

    public confirm(): void {
        this.billWebSocketService.sendMessage(this.bill);
        this.shown = false;
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
