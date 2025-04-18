import {InputTimeType} from "../input/InputTimeType";
import {
    RecurringIncomeTimeInterval
} from "../../components/elements/recurring-income-dropdown/models/RecurringIncomeTimeInterval";

export class Income {
    public name: string;
    public amount: number;
    public dateReceived: Date;
    private _timeType: InputTimeType;
    public incomeInterval?: RecurringIncomeTimeInterval;
    public weeklyHours?: number;
    public constructor(name: string = '',
                       amount: number = 0,
                       dateReceived: Date = new Date(),
                       timeType: InputTimeType = InputTimeType.ONE_TIME,
                       incomeInterval?: RecurringIncomeTimeInterval,
                       weeklyHours?: number) {
        this.name = name;
        this.amount = amount;
        this.dateReceived = dateReceived;
        this._timeType = timeType;
        this.incomeInterval = incomeInterval;
        this.weeklyHours = weeklyHours;
    }
    get timeType(): InputTimeType {
        // this.handleDefaultInterval();
        return this._timeType;
    }

    private handleDefaultInterval() {
        if (this._timeType === InputTimeType.RECURRING) {
            this.incomeInterval = RecurringIncomeTimeInterval.SALARY;
        } else {
            this.incomeInterval = undefined;
        }
    }

    handleOneTimeInterval(timeType: InputTimeType) {
        if (timeType === InputTimeType.ONE_TIME) {
            this.incomeInterval = undefined;
        }
    }

    shouldHandleDefault(): boolean {
        return this.incomeInterval === undefined;
    }

    set timeType(timeType: InputTimeType) {
        this.handleOneTimeInterval(timeType);
        if (this.shouldHandleDefault()) {
            this._timeType = timeType;
            this.handleDefaultInterval();
        } else {
            this._timeType = timeType;
        }

    }
}