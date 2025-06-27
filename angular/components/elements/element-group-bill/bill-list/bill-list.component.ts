// bill-list.component.ts 
import {Component, Input, OnInit, ViewChild} from "@angular/core";
import {ElementSize} from "../../../../models/ElementSize";
import {ButtonText} from "../../element-group-native/ss-button/models/ButtonText";
import {SsButtonComponent} from "../../element-group-native/ss-button/ss-button.component";
import {BillInputComponent} from "../bill-input/bill-input.component";
import {TagType} from "../../../../models/html/TagType";
import {
    Bill,
    OneTimeBill,
    RecurringBill
} from "../../../../models/paycheck/types";
import {
    HttpGetAllBillsService
} from "../../../../services/server/http/http-get-all-bills.service";

@Component({
    selector: 'bill-list',
    templateUrl: './bill-list.component.html',
    styleUrls: ['./bill-list.component.css']
})
export class BillListComponent implements OnInit {
    @ViewChild(BillInputComponent) billInput: BillInputComponent;
    @Input() bills: (OneTimeBill | RecurringBill)[] = [];
    isLoading: boolean = true;
    constructor(private getAllBillsService: HttpGetAllBillsService) {
        
    }

    public deleteBill(billToDelete: OneTimeBill | RecurringBill): void {
        this.bills = this.bills.filter(bill => {
            if (bill.type === billToDelete.type) {
                return bill.id !== billToDelete.id;
            } else {
                return true;
            }
        });
    }

    public updateBills(): void {
        this.getAllBillsService.getAllBills().subscribe(bills => {
            if (bills) {
                console.log(bills);
                this.bills = [
                    ...bills.recurringBills.map(item => ({ ...item, type: "RecurringBill" as "RecurringBill" })),
                    ...bills.oneTimeBills.map(item => ({ ...item, type: "OneTimeBill" as "OneTimeBill" }))
                ];
                this.isLoading = false;
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
