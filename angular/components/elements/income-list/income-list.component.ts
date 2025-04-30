// income-list.component.ts 
import {Component, Input, ViewChild} from "@angular/core";
import {TagType} from "../../../models/html/TagType";
import {ElementSize} from "../../../models/ElementSize";
import {ButtonText} from "../ss-button/models/ButtonText";
import {
    OneTimeIncome,
    RecurringIncome,
    WageIncome
} from "../../../models/paycheck/types";
import {IncomeInputComponent} from "../income-input/income-input.component";

@Component({
    selector: 'income-list',
    templateUrl: './income-list.component.html',
    styleUrls: ['./income-list.component.css']
})
export class IncomeListComponent {
    @ViewChild(IncomeInputComponent) incomeInput: IncomeInputComponent;
    @Input() incomes: (OneTimeIncome | RecurringIncome | WageIncome)[] = [
        // {
        //     amount: 150,
        //     dateReceived: new Date(),
        //     name: "Joe's Birthday Gift",
        // }
    ];
    constructor() {
        
    }

    public showIncomeInput(): void {
        this.incomeInput.open();
    }

    protected readonly TagType = TagType;
    protected readonly ElementSize = ElementSize;
    protected readonly ButtonText = ButtonText;
}
