// paycheck.component.ts 
import {Component, Input, OnInit} from "@angular/core";
import {Paycheck} from "../../../models/paycheck/Paycheck";
import {Income} from "../../../models/income/Income";
import {InputTimeType} from "../../../models/input/InputTimeType";
import {Bill} from "../../../models/bill/Bill";
import {PaycheckTotalType} from "../paycheck-total/models/PaycheckTotalType";

@Component({
    selector: 'paycheck',
    templateUrl: './paycheck.component.html',
    styleUrls: ['./paycheck.component.css']
})
export class PaycheckComponent implements OnInit {
    @Input() protected paycheck: Paycheck = new Paycheck()
    constructor() {
        
    }
    ngOnInit(): void {
        this.paycheck.incomes = [new Income(
            "Job at Target",
            540,
            new Date(),
            InputTimeType.RECURRING
        ),
        new Income(
            "Birthday Money",
            100,
            new Date(),
            InputTimeType.ONE_TIME
        )];
        this.paycheck.bills = [new Bill(
            "Rent",
            1200,
            new Date(),
            InputTimeType.RECURRING
        ),
        new Bill(
            "Car Payment",
            300,
            new Date(),
            InputTimeType.RECURRING
        ),
        new Bill(
            "Haircut",
            38,
            new Date(),
            InputTimeType.RECURRING
        )];
        this.paycheck.totalIncome = 1550.65;

        this.paycheck.bills = [new Bill(
            "Rent",
            1200,
            new Date(),
            InputTimeType.RECURRING
        ),
        new Bill(
            "Car Payment",
            300,
            new Date(),
            InputTimeType.RECURRING
        ),
        new Bill(
            "Haircut",
            38,
            new Date(),
            InputTimeType.ONE_TIME
        )]
        this.paycheck.totalBills = 1538.00;

    }

    protected readonly PaycheckTotalType = PaycheckTotalType;
}
