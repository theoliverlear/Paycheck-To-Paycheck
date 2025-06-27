// paycheck-income-fields.component.ts
import {ChangeDetectionStrategy, Component, Input} from "@angular/core";
import {PaycheckFieldType} from "../paycheck/models/PaycheckFieldType";
import {
    OneTimeIncome,
    RecurringIncome,
    WageIncome
} from "../../../../models/paycheck/types";

@Component({
    selector: 'paycheck-income-fields',
    templateUrl: './paycheck-income-fields.component.html',
    styleUrls: ['./paycheck-income-fields.component.css'],
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class PaycheckIncomeFieldsComponent {
    @Input() income: OneTimeIncome | RecurringIncome | WageIncome;
    constructor() {
        
    }

    protected readonly PaycheckFieldType = PaycheckFieldType;
}
