// income-input.component.ts
import {Component, EventEmitter, Input, OnInit, Output} from "@angular/core";
import {fadeInOutAnimation} from "../../../animations/animations";
import {InputTimeType} from "../../../../models/input/InputTimeType";
import {Income} from "../../../../models/income/Income";
import {TagType} from "../../../../models/html/TagType";
import {
    closeIconImageAsset,
    confirmIconImageAsset
} from "../../../../assets/imageAssets";
import {
    quickFadeInAnimationProperties
} from "../../../animations/animationProperties";
import {
    RecurringIncomeTimeInterval
} from "../recurring-income-dropdown/models/RecurringIncomeTimeInterval";
import {WebSocketCapable} from "../../../../models/WebSocketCapable";
import {Subscription} from "rxjs";
import {
    OneTimeIncomeWebSocketService
} from "../../../../services/server/websocket/one-time-income-websocket.service";
import {
    RecurringIncomeWebSocketService
} from "../../../../services/server/websocket/recurring-income-websocket.service";
import {
    WageIncomeWebSocketService
} from "../../../../services/server/websocket/wage-income-websocket.service";

@Component({
    selector: 'income-input',
    templateUrl: './income-input.component.html',
    styleUrls: ['./income-input.component.css'],
    animations: [
        fadeInOutAnimation
    ]
})
export class IncomeInputComponent implements OnInit, WebSocketCapable {
    @Input() inputTimeType: InputTimeType = InputTimeType.ONE_TIME;
    @Output() incomeAdded: EventEmitter<void> = new EventEmitter<void>();
    protected shown: boolean = false;
    income: Income = new Income();
    isHourlyIncome: boolean = false;
    webSocketSubscription: Subscription;
    recurringIncomeSubscription: Subscription;
    wageIncomeSubscription: Subscription;
    constructor(private oneTimeIncomeWebSocket: OneTimeIncomeWebSocketService,
                private recurringIncomeWebSocket: RecurringIncomeWebSocketService,
                private wageIncomeWebSocket: WageIncomeWebSocketService) {

    }

    ngOnInit() {
        this.setDefaultTimeType();
        console.log(this.income);
        this.initializeWebSocket();
    }

    initializeWebSocket(): void {
        this.initializeOneTimeIncomeWebSocket();
        this.initializeRecurringIncomeWebSocket();
        this.initializeWageIncomeWebSocket();
    }

    private initializeRecurringIncomeWebSocket(): void {
        this.recurringIncomeWebSocket.connect();
        this.recurringIncomeSubscription = this.recurringIncomeWebSocket.getMessages().subscribe(
            (income: Income): void => {
                if (income) {
                    console.log('WebSocket income:', income);
                }
            },
        )
    }

    private initializeOneTimeIncomeWebSocket(): void {
        this.oneTimeIncomeWebSocket.connect();
        this.webSocketSubscription = this.oneTimeIncomeWebSocket.getMessages().subscribe(
            (income: Income): void => {
                if (income) {
                    console.log('WebSocket income:', income);
                }
            },
            (error) => {
                console.error('WebSocket error:', error);
            }
        );
    }

    private initializeWageIncomeWebSocket(): void {
        this.wageIncomeWebSocket.connect();
        this.wageIncomeSubscription = this.wageIncomeWebSocket.getMessages().subscribe(
            (income: Income): void => {
                if (income) {
                    console.log('WebSocket income:', income);
                }
            },
            (error) => {
                console.error('WebSocket error:', error);
            }
        )
    }


    clearInputs(): void {
        this.income = new Income();
        this.setDefaultTimeType();
    }

    public confirm(): void {
        if (this.income.timeType === InputTimeType.ONE_TIME) {
            this.oneTimeIncomeWebSocket.sendMessage(this.income);
        } else if (this.income.incomeInterval === RecurringIncomeTimeInterval.HOURLY_WAGE) {
            this.wageIncomeWebSocket.sendMessage(this.income);
        } else {
            this.recurringIncomeWebSocket.sendMessage(this.income);
        }
        this.incomeAdded.emit();
        this.shown = false;
    }

    public open(): void {
        this.shown = true;
    }

    public close(): void {
        this.shown = false;
    }

    setDefaultTimeType() {
        this.income.timeType = this.inputTimeType;
    }

    public updateIncomeTimeType(timeType: InputTimeType): void {
        this.income.timeType = timeType;
        console.log(this.income);
    }

    public updateIncomeInterval(incomeInterval: RecurringIncomeTimeInterval): void {
        this.income.incomeInterval = incomeInterval;
        this.updateIsHourlyIncome(incomeInterval);
        console.log(this.income);
    }

    private updateIsHourlyIncome(incomeInterval: RecurringIncomeTimeInterval) {
        this.isHourlyIncome = incomeInterval === RecurringIncomeTimeInterval.HOURLY_WAGE;
    }

    updateIncome(income: Income): void {
        const originalTimeType: InputTimeType = this.income.timeType;
        this.income = income;
        this.income.timeType = originalTimeType;
        console.log(this.income);
    }

    public isRecurringIncome(): boolean {
        const isRecurring: boolean = this.income.timeType === InputTimeType.RECURRING;
        return isRecurring;
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

    protected readonly TagType = TagType;
    protected readonly confirmIconImageAsset = confirmIconImageAsset;
    protected readonly closeIconImageAsset = closeIconImageAsset;
}
