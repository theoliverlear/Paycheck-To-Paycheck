// paycheck-income-list.component.ts
import {ChangeDetectionStrategy, Component, Input} from "@angular/core";
import {
    OneTimeIncome,
    RecurringIncome,
    WageIncome
} from "../../../../models/paycheck/types";

@Component({
    selector: 'paycheck-income-list',
    templateUrl: './paycheck-income-list.component.html',
    styleUrls: ['./paycheck-income-list.component.css'],
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class PaycheckIncomeListComponent {
    @Input() incomes: (OneTimeIncome | RecurringIncome | WageIncome)[] = [];
    constructor() {
        
    }
}
