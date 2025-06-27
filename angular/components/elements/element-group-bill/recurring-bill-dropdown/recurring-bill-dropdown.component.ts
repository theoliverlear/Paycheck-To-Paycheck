// recurring-bill-dropdown.component.ts 
import {Component, EventEmitter, Output} from "@angular/core";
import {RecurringBillTimeInterval} from "./models/RecurringBillTimeInterval";

@Component({
    selector: 'recurring-bill-dropdown',
    templateUrl: './recurring-bill-dropdown.component.html',
    styleUrls: ['./recurring-bill-dropdown.component.css']
})
export class RecurringBillDropdownComponent {
    @Output() dropdownSelected: EventEmitter<RecurringBillTimeInterval> = new EventEmitter<RecurringBillTimeInterval>();
    constructor() {
        
    }

    emitDropdownSelected(dropdownItem: string): void {
        const recurringBillTimeInterval: RecurringBillTimeInterval = RecurringBillTimeInterval.from(dropdownItem);
        console.log(recurringBillTimeInterval);
        this.dropdownSelected.emit(recurringBillTimeInterval);
    }
    protected readonly RecurringBillTimeInterval = RecurringBillTimeInterval;
}
