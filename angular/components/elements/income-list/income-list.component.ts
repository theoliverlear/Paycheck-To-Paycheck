// income-list.component.ts 
import {Component, Input, OnInit, ViewChild} from "@angular/core";
import {TagType} from "../../../models/html/TagType";
import {ElementSize} from "../../../models/ElementSize";
import {ButtonText} from "../ss-button/models/ButtonText";
import {
    OneTimeIncome,
    RecurringIncome,
    WageIncome
} from "../../../models/paycheck/types";
import {IncomeInputComponent} from "../income-input/income-input.component";
import {
    HttpGetAllIncomesService
} from "../../../services/server/http/http-get-all-incomes.service";
import {DelayService} from "../../../services/delay.service";

@Component({
    selector: 'income-list',
    templateUrl: './income-list.component.html',
    styleUrls: ['./income-list.component.css']
})
export class IncomeListComponent implements OnInit {
    @ViewChild(IncomeInputComponent) incomeInput: IncomeInputComponent;
    @Input() incomes: (OneTimeIncome | RecurringIncome | WageIncome)[] = [];
    isLoading: boolean = true;
    constructor(private getAllIncomesService: HttpGetAllIncomesService,
                private delayService: DelayService) {

    }

    public deleteIncome(incomeToDelete: OneTimeIncome | RecurringIncome | WageIncome): void {
        this.incomes = this.incomes.filter(income => {
            if (income.type === incomeToDelete.type) {
                return income.id !== incomeToDelete.id;
            } else {
                return true;
            }
        });
    }

    ngOnInit(): void {
        this.updateIncomes();
    }


    public updateIncomeAfterAdding(): void {
        this.delayService.delay(1000).then(() => {
            this.updateIncomes();
        });
    }

    public updateIncomes(): void {
        this.getAllIncomesService.getAllIncomes().subscribe(incomes => {
            if (incomes) {
                console.log(incomes);
                this.incomes = [
                    ...incomes.oneTimeIncomes.map(item => ({ ...item, type: "OneTimeIncome" as "OneTimeIncome" })),
                    ...incomes.recurringIncomes.map(item => ({ ...item, type: "RecurringIncome" as "RecurringIncome" })),
                    ...incomes.wageIncomes.map(item => ({ ...item, type: "WageIncome" as "WageIncome" }))
                ];
                this.isLoading = false;
            }
        });
    }

    public showIncomeInput(): void {
        this.incomeInput.open();
    }

    protected readonly TagType = TagType;
    protected readonly ElementSize = ElementSize;
    protected readonly ButtonText = ButtonText;
}
