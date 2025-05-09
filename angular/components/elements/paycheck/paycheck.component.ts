// paycheck.component.ts
import {
    Component,
    EventEmitter,
    HostBinding,
    Input,
    OnInit,
    Output
} from "@angular/core";
import {PaycheckTotalType} from "../paycheck-total/models/PaycheckTotalType";
import {
    HttpPaycheckService
} from "../../../services/server/http/http-paycheck.service";
import {
    OneTimeBill,
    OneTimeIncome,
    Paycheck, RecurringBill,
    RecurringIncome, WageIncome
} from "../../../models/paycheck/types";
import {emptyPaycheck, isEmptyPaycheck} from "../../../assets/paycheckAssets";

@Component({
    selector: 'paycheck',
    templateUrl: './paycheck.component.html',
    styleUrls: ['./paycheck.component.css']
})
export class PaycheckComponent implements OnInit {
    // TODO: Create an asset that holds a default paycheck.
    @Input() paycheckId: number = 0;
    @Input() paycheck: Paycheck = emptyPaycheck;
    @Output() isLoaded: EventEmitter<number> = new EventEmitter<number>();
    @HostBinding('style.display') get display(): string {
        return this.isEmpty() ? 'none' : 'flex';
    }

    incomes: (OneTimeIncome | RecurringIncome | WageIncome)[] = [];
    bills: (OneTimeBill | RecurringBill)[] = [];

    constructor(private httpPaycheckService: HttpPaycheckService) {

    }

    ngOnInit(): void {
        this.httpPaycheckService.getPaycheck(this.paycheckId).subscribe(paycheck => {
            if (paycheck) {
                this.paycheck = paycheck;
                this.incomes = [...paycheck.oneTimeIncomes, ...paycheck.recurringIncomes, ...paycheck.wageIncomes];
                this.bills = [...paycheck.oneTimeBills, ...paycheck.recurringBills];
                this.isLoaded.emit(this.paycheckId);
            }
        });
    }

    isEmpty(): boolean {
        return isEmptyPaycheck(this.paycheck);
    }

    protected readonly PaycheckTotalType = PaycheckTotalType;
}
