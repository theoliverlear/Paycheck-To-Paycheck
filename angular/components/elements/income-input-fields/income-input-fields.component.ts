// income-input-fields.component.ts
import {Component, EventEmitter, Input, Output} from "@angular/core";
import {Income} from "../../../models/income/Income";
import {
    IncomeInputContent
} from "../income-input-field/models/IncomeInputContent";
import {
    IncomeInputFieldType
} from "../income-input-field/models/IncomeInputFieldType";

@Component({
    selector: 'income-input-fields',
    templateUrl: './income-input-fields.component.html',
    styleUrls: ['./income-input-fields.component.css']
})
export class IncomeInputFieldsComponent {
    @Output() incomeChange: EventEmitter<Income> = new EventEmitter<Income>();
    income: Income = new Income();
    @Input() isHourlyIncome: boolean = false;
    constructor() {
        
    }
    updateIncome(incomeInputContent: IncomeInputContent): void {
        switch (incomeInputContent.fieldType) {
            case IncomeInputFieldType.TITLE:
                this.income.name = incomeInputContent.inputValue as string;
                break;
            case IncomeInputFieldType.AMOUNT:
                this.income.amount = Number(incomeInputContent.inputValue);
                break;
            case IncomeInputFieldType.HOURS:
                this.income.weeklyHours = Number(incomeInputContent.inputValue);
                break;
            case IncomeInputFieldType.DATE:
                this.income.dateReceived = new Date(incomeInputContent.inputValue as string);
                break;
        }
    }

    emitIncomeChange(): void {
        this.incomeChange.emit(this.income);
    }

    updateAndEmitIncome(incomeInputContent: IncomeInputContent): void {
        this.updateIncome(incomeInputContent);
        this.emitIncomeChange();
    }

    protected readonly IncomeInputFieldType = IncomeInputFieldType;
}
