// income.component.ts 
import {Component, Input} from "@angular/core";
import {
    OneTimeIncome,
    RecurringIncome,
    WageIncome
} from "../../../models/paycheck/types";
import {TagType} from "../../../models/html/TagType";

@Component({
    selector: 'income',
    templateUrl: './income.component.html',
    styleUrls: ['./income.component.css']
})
export class IncomeComponent {
    @Input() income: OneTimeIncome | RecurringIncome | WageIncome;


    constructor() {
        
    }

    getAmountString(): string {
        return this.income.amount.toLocaleString('en-US', {
            style: 'currency',
            currency: 'USD',
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        });
    }

    getDateString(): string {
        if ('dateReceived' in this.income) {
            if (this.income.dateReceived) {
                return this.income.dateReceived.toDateString();
            }
        } else if (this.income.recurringDate) {
            return this.income.recurringDate.day.toDateString();
        }
        return 'N/A';
    }

    protected readonly TagType = TagType;
}
