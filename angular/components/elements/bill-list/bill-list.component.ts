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
import {
    HttpGetAllBillsService
} from "../../../services/server/http/http-get-all-bills.service";

@Component({
    selector: 'bill-list',
    templateUrl: './bill-list.component.html',
    styleUrls: ['./bill-list.component.css']
})
export class BillListComponent implements OnInit {
    @ViewChild(BillInputComponent) billInput: BillInputComponent;
    @Input() bills: (OneTimeBill | RecurringBill)[] = [];
    constructor(private getAllBillsService: HttpGetAllBillsService) {
        
    }

    public updateBills(): void {
        this.getAllBillsService.getAllBills().subscribe(bills => {
            if (bills) {
                this.bills = [...bills.recurringBills, ...bills.oneTimeBills];
            }
        });
    }

    ngOnInit(): void {
        this.updateBills();
    }

    showBillInput(): void {
        this.billInput.open();
    }
    protected readonly ElementSize = ElementSize;
    protected readonly ButtonText = ButtonText;
    protected readonly TagType = TagType;
}
