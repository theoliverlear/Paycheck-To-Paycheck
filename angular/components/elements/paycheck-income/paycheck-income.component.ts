// paycheck-income.component.ts
import {ChangeDetectionStrategy, Component, Input} from "@angular/core";
import {TagType} from "../../../models/html/TagType";
import {
    OneTimeIncome,
    RecurringIncome,
    WageIncome
} from "../../../models/paycheck/types";

@Component({
    selector: 'paycheck-income',
    templateUrl: './paycheck-income.component.html',
    styleUrls: ['./paycheck-income.component.css'],
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class PaycheckIncomeComponent {
    @Input() income: OneTimeIncome | RecurringIncome | WageIncome;
    constructor() {

    }
    protected getIncomeAmount(): string {
        return `$${this.income.amount}`;
    }
    protected readonly TagType = TagType;
}
