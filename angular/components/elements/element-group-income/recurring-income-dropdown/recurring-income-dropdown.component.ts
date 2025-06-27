// recurring-income-dropdown.component.ts 
import {Component, EventEmitter, Output} from "@angular/core";
import {
    RecurringIncomeTimeInterval
} from "./models/RecurringIncomeTimeInterval";

@Component({
    selector: 'recurring-income-dropdown',
    templateUrl: './recurring-income-dropdown.component.html',
    styleUrls: ['./recurring-income-dropdown.component.css']
})
export class RecurringIncomeDropdownComponent {
    @Output() dropdownSelected: EventEmitter<RecurringIncomeTimeInterval> = new EventEmitter<RecurringIncomeTimeInterval>();
    constructor() {
        
    }
    emitDropdownSelected(dropdownItem: string) {
        const recurringIncomeTimeInterval: RecurringIncomeTimeInterval = RecurringIncomeTimeInterval.from(dropdownItem);
        console.log(recurringIncomeTimeInterval);
        this.dropdownSelected.emit(recurringIncomeTimeInterval);
    }

    protected readonly RecurringIncomeTimeInterval = RecurringIncomeTimeInterval;
}
