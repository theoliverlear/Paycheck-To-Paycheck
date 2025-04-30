// bill.component.ts 
import {Component, Input} from "@angular/core";
import {OneTimeBill, RecurringBill} from "../../../models/paycheck/types";
import {TagType} from "../../../models/html/TagType";

@Component({
    selector: 'bill',
    templateUrl: './bill.component.html',
    styleUrls: ['./bill.component.css']
})
export class BillComponent {
    @Input() bill: OneTimeBill | RecurringBill;
    constructor() {
        
    }

    getAmountString(): string {
        return this.bill.amount.toLocaleString('en-US', {
            style: 'currency',
            currency: 'USD',
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        });
    }
    getDateString(): string {
        if ('dueDate' in this.bill) {
            if (this.bill.dueDate) {
                return this.bill.dueDate.dueDate.toDateString();
            }
        } else if (this.bill.recurringDate) {
            return this.bill.recurringDate.day.toDateString();
        }
        return 'N/A';
    }
    protected readonly TagType = TagType;
}
