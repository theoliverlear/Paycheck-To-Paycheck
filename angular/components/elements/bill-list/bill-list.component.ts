// bill-list.component.ts 
import {Component, Input, OnInit, ViewChild} from "@angular/core";
import {ElementSize} from "../../../models/ElementSize";
import {ButtonText} from "../ss-button/models/ButtonText";
import {SsButtonComponent} from "../ss-button/ss-button.component";
import {BillInputComponent} from "../bill-input/bill-input.component";
import {TagType} from "../../../models/html/TagType";
import {
    Bill,
    OneTimeBill,
    RecurringBill
} from "../../../models/paycheck/types";

@Component({
    selector: 'bill-list',
    templateUrl: './bill-list.component.html',
    styleUrls: ['./bill-list.component.css']
})
export class BillListComponent {
    @ViewChild(BillInputComponent) billInput: BillInputComponent;
    @Input() bills: (OneTimeBill | RecurringBill)[] = [
        // {
        //     amount: 150,
        //     dueDate: {
        //         name: "Joe's Pay Date",
        //         dueDate: new Date(),
        //     },
        //     name: "Joe's Birthday Gift",
        // }
    ];
    constructor() {
        
    }

    showBillInput(): void {
        this.billInput.open();
    }
    protected readonly ElementSize = ElementSize;
    protected readonly ButtonText = ButtonText;
    protected readonly TagType = TagType;
}
