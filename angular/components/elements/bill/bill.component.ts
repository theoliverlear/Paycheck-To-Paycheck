// bill.component.ts 
import {Component, EventEmitter, Input, Output} from "@angular/core";
import {OneTimeBill, RecurringBill} from "../../../models/paycheck/types";
import {TagType} from "../../../models/html/TagType";
import {BillEmitter} from "./models/types";
import {
    HttpDeleteOneTimeBillService
} from "../../../services/server/http/http-delete-one-time-bill.service";
import {
    HttpDeleteRecurringBillService
} from "../../../services/server/http/http-delete-recurring-bill.service";

@Component({
    selector: 'bill',
    templateUrl: './bill.component.html',
    styleUrls: ['./bill.component.css']
})
export class BillComponent {
    @Input() bill: OneTimeBill | RecurringBill;
    @Output() billDeleted: BillEmitter = new EventEmitter<OneTimeBill | RecurringBill>();
    constructor(private deleteOneTimeBillService: HttpDeleteOneTimeBillService,
                private deleteRecurringBillService: HttpDeleteRecurringBillService) {
        
    }

    deleteBill(): void {
        this.deleteBillFromServer();
        this.billDeleted.emit(this.bill);
    }

    deleteBillFromServer() {
        if ('dueDate' in this.bill) {
            this.deleteOneTimeBillService.deleteOneTimeBill(this.bill.id).subscribe(() => {
                console.log('Bill deleted');
            });
        } else {
            this.deleteRecurringBillService.deleteRecurringBill(this.bill.id).subscribe(() => {
                console.log('Bill deleted');
            });
        }
    }

    public getRecurringString(): string {
        if (this.bill.type === 'OneTimeBill') {
            return 'One-Time';
        } else {
            return this.getIntervalString();
        }
    }

    getIntervalString(): string {
        if ('recurringDate' in this.bill) {
            const interval: number = this.bill.recurringDate.interval;
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
