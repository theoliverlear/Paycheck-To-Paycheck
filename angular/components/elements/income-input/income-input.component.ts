// income-input.component.ts 
import {Component, Input, OnInit} from "@angular/core";
import {fadeInOutAnimation} from "../../animations/animations";
import {InputTimeType} from "../../../models/input/InputTimeType";
import {Income} from "../../../models/income/Income";
import {TagType} from "../../../models/html/TagType";
import {
    closeIconImageAsset,
    confirmIconImageAsset
} from "../../../assets/imageAssets";
import {
    quickFadeInAnimationProperties
} from "../../animations/animationProperties";
import {
    RecurringIncomeTimeInterval
} from "../recurring-income-dropdown/models/RecurringIncomeTimeInterval";

@Component({
    selector: 'income-input',
    templateUrl: './income-input.component.html',
    styleUrls: ['./income-input.component.css'],
    animations: [
        fadeInOutAnimation
    ]
})
export class IncomeInputComponent implements OnInit {
    @Input() inputTimeType: InputTimeType = InputTimeType.ONE_TIME;
    protected shown: boolean = true;
    income: Income = new Income();
    isHourlyIncome: boolean = false;
    constructor() {
        
    }

    public confirm(): void {
        this.shown = false;
    }

    public close(): void {
        this.shown = false;
    }

    ngOnInit() {
        this.setDefaultTimeType();
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
        return this.income.timeType === InputTimeType.RECURRING;
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
