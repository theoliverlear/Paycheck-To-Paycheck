// bill-input-fields.component.ts 
import {Component, EventEmitter, Output} from "@angular/core";
import {
    BillInputFieldType
} from "../bill-input-field/models/BillInputFieldType";
import {Bill} from "../../../models/bill/Bill";
import {BillInputContent} from "../bill-input-field/models/BillInputContent";

@Component({
    selector: 'bill-input-fields',
    templateUrl: './bill-input-fields.component.html',
    styleUrls: ['./bill-input-fields.component.css']
})
export class BillInputFieldsComponent {
    @Output() billChange: EventEmitter<Bill> = new EventEmitter<Bill>();
    bill: Bill = new Bill();
    constructor() {
        
    }

    updateBill(billInputContent: BillInputContent): void {
        switch (billInputContent.fieldType) {
            case BillInputFieldType.TITLE:
                this.bill.name = billInputContent.inputValue as string;
                break;
            case BillInputFieldType.AMOUNT:
                this.bill.amount = Number(billInputContent.inputValue);
                break;
            case BillInputFieldType.DATE:
                this.bill.date = new Date(billInputContent.inputValue as string);
                break;
        }
    }

    emitBillChange(): void {
        this.billChange.emit(this.bill);
    }

    updateAndEmitBill(billInputContent: BillInputContent): void {
        this.updateBill(billInputContent);
        this.emitBillChange();
    }

    protected readonly BillInputFieldType = BillInputFieldType;
}
