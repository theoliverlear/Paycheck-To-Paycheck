// paycheck.component.ts 
import {Component, Input, OnInit} from "@angular/core";
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

@Component({
    selector: 'paycheck',
    templateUrl: './paycheck.component.html',
    styleUrls: ['./paycheck.component.css']
})
export class PaycheckComponent implements OnInit {
    // TODO: Create an asset that holds a default paycheck.
    @Input() paycheckId: number = 0;
    @Input() paycheck: Paycheck = {
        dateRange: {
            endDate: new Date(),
            startDate: new Date()
        },
        leftOverIncome: 0,
        oneTimeBills: [],
        oneTimeIncomes: [],
        recurringBills: [],
        recurringIncomes: [],
        wageIncomes: [],
        totalBills: 0,
        totalIncome: 0
    };
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
            }
        });
    }

    protected readonly PaycheckTotalType = PaycheckTotalType;
}
