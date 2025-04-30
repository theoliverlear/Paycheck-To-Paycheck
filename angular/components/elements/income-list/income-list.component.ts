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

@Component({
    selector: 'income-list',
    templateUrl: './income-list.component.html',
    styleUrls: ['./income-list.component.css']
})
export class IncomeListComponent implements OnInit {
    @ViewChild(IncomeInputComponent) incomeInput: IncomeInputComponent;
    @Input() incomes: (OneTimeIncome | RecurringIncome | WageIncome)[] = [];
    constructor(private getAllIncomesService: HttpGetAllIncomesService) {
        
    }

    ngOnInit(): void {
        this.updateIncomes();
    }

    public updateIncomes(): void {
        this.getAllIncomesService.getAllIncomes().subscribe(incomes => {
            if (incomes) {
                this.incomes = [...incomes.oneTimeIncomes, ...incomes.recurringIncomes, ...incomes.wageIncomes];
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
