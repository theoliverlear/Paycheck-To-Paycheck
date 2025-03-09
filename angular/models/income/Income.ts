import {InputTimeType} from "../input/InputTimeType";
import {
    RecurringIncomeTimeInterval
} from "../../components/elements/recurring-income-dropdown/models/RecurringIncomeTimeInterval";

export class Income {
    public name: string;
    public incomeAmount: number;
    public dateReceived: Date;
    private _timeType: InputTimeType;
    public incomeInterval?: RecurringIncomeTimeInterval;
    public hours?: number;
    public constructor(name: string = '',
                       incomeAmount: number = 0,
                       dateReceived: Date = new Date(),
                       timeType: InputTimeType = InputTimeType.ONE_TIME,
                       incomeInterval?: RecurringIncomeTimeInterval,
                       hours?: number) {
        this.name = name;
        this.incomeAmount = incomeAmount;
        this.dateReceived = dateReceived;
        this._timeType = timeType;
        this.incomeInterval = incomeInterval;
        this.hours = hours;
    }
    get timeType(): InputTimeType {
        this.handleDefaultInterval();
        return this._timeType;
    }

    private handleDefaultInterval() {
        if (this._timeType === InputTimeType.ONE_TIME) {
            this.incomeInterval = undefined;
        } else {
            this.incomeInterval = RecurringIncomeTimeInterval.SALARY;
        }
    }

    set timeType(timeType: InputTimeType) {
        this._timeType = timeType;
        this.handleDefaultInterval();
    }
}