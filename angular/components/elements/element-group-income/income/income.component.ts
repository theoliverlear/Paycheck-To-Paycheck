// income.component.ts 
import {Component, EventEmitter, Output, Input} from "@angular/core";
import {
    OneTimeIncome,
    RecurringIncome,
    WageIncome
} from "../../../../models/paycheck/types";
import {TagType} from "../../../../models/html/TagType";
import {IncomeEmitter} from "./models/types";
import {
    HttpDeleteOneTimeIncomeService
} from "../../../../services/server/http/http-delete-one-time-income.service";
import {
    HttpDeleteRecurringIncomeService
} from "../../../../services/server/http/http-delete-recurring-income.service";
import {
    HttpDeleteWageIncomeService
} from "../../../../services/server/http/http-delete-wage-income.service";

@Component({
    selector: 'income',
    templateUrl: './income.component.html',
    styleUrls: ['./income.component.css']
})
export class IncomeComponent {
    @Input() income: OneTimeIncome | RecurringIncome | WageIncome;
    @Output() incomeDeleted: IncomeEmitter = new EventEmitter<OneTimeIncome | RecurringIncome | WageIncome>();

    constructor(private deleteOneTimeIncomeService: HttpDeleteOneTimeIncomeService,
                private deleteRecurringIncomeService: HttpDeleteRecurringIncomeService,
                private deleteWageIncomeService: HttpDeleteWageIncomeService) {
        
    }

    deleteIncome(): void {
        this.deleteIncomeFromServer();
        this.incomeDeleted.emit(this.income);
    }

    deleteIncomeFromServer() {
        if ('dateReceived' in this.income) {
            this.deleteOneTimeIncomeService.deleteOneTimeIncome(this.income.id).subscribe(() => {
                console.log('Income deleted');
            });
        } else if ('weeklyHours' in this.income) {
            this.deleteWageIncomeService.deleteWageIncome(this.income.id).subscribe(() => {
                console.log('Income deleted');
            });
        } else {
            this.deleteRecurringIncomeService.deleteRecurringIncome(this.income.id).subscribe(() => {
                console.log('Income deleted');
            });
        }
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

    public getRecurringString(): string {
        if (this.income.type === 'OneTimeIncome') {
            return 'One-Time';
        } else {
            return this.getIntervalString();
        }
    }

    getIntervalString(): string {
        if ('recurringDate' in this.income) {
            const interval: number = this.income.recurringDate.interval;
            switch (interval) {
                case 1:
                    return 'Yearly';
                case 2:
                    return 'Bi-Yearly';
                case 4:
                    return 'Quarterly';
                case 6:
                    return 'Bi-Monthly';
                case 12:
                    return 'Monthly';
                case 26:
                    return 'Bi-Weekly';
                case 52:
                    return 'Weekly';
                case 365:
                    return 'Daily';
                default:
                    throw new Error('Invalid interval value');
            }
        }
    }

    protected readonly TagType = TagType;
}
