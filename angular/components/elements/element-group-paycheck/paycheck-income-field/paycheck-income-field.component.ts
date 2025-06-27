// paycheck-income-field.component.ts
import {Component, HostBinding, Input} from "@angular/core";
import {PaycheckFieldType} from "../paycheck/models/PaycheckFieldType";
import {TagType} from "../../../../models/html/TagType";
import {
    OneTimeIncome,
    RecurringIncome,
    WageIncome
} from "../../../../models/paycheck/types";
import {InputTimeType} from "../../../../models/input/InputTimeType";

@Component({
    selector: 'paycheck-income-field',
    templateUrl: './paycheck-income-field.component.html',
    styleUrls: ['./paycheck-income-field.component.css']
})
export class PaycheckIncomeFieldComponent {
    @Input() fieldType: PaycheckFieldType
    @Input() income: OneTimeIncome | RecurringIncome | WageIncome;
    @HostBinding('class.income-text') get isAmount(): boolean {
        return this.fieldType === PaycheckFieldType.AMOUNT;
    }
    constructor() {
        
    }
    protected getFieldValue(): string {
        switch (this.fieldType) {
            case PaycheckFieldType.AMOUNT:
                const amountFormatted: string = new Intl.NumberFormat('en-US', {
                    style: 'currency',
                    currency: 'USD',
                    minimumFractionDigits: 2
                }).format(this.income.amount);
                return `+${amountFormatted}`;
            case PaycheckFieldType.DATE:
                if ('dateReceived' in this.income) {
                    if (this.income.dateReceived) {
                        return this.income.dateReceived.toDateString();
                    }
                } else {
                    if (this.income.recurringDate) {
                        return this.income.recurringDate.day.toDateString();
                    }
                }
                return 'N/A';
            case PaycheckFieldType.TIME_TYPE:
                if ('recurringDate' in this.income) {
                    return InputTimeType.RECURRING;
                } else {
                    return InputTimeType.ONE_TIME;
                }
            default:
                return '';
        }
    }

    protected readonly TagType = TagType;
}
