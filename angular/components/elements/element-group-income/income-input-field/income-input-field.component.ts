// income-input-field.component.ts 
import {Component, EventEmitter, Input, OnInit, Output} from "@angular/core";
import {IncomeInputFieldType} from "./models/IncomeInputFieldType";
import {IncomeInputContent} from "./models/IncomeInputContent";
import {InputType} from "../../ss-input/models/InputType";
import {TagType} from "../../../../models/html/TagType";

@Component({
    selector: 'income-input-field',
    templateUrl: './income-input-field.component.html',
    styleUrls: ['./income-input-field.component.css']
})
export class IncomeInputFieldComponent implements OnInit {
    // TODO: If the income type of WAGE is selected, then the program should
    //       display hours worked in addition to income.
    @Input() fieldType: IncomeInputFieldType;
    @Input() placeholder: string | number;
    @Output() inputEvent: EventEmitter<IncomeInputContent> = new EventEmitter<IncomeInputContent>();
    protected inputContent: IncomeInputContent = new IncomeInputContent();
    constructor() {
        
    }
    ngOnInit(): void {
        this.inputContent.fieldType = this.fieldType;
    }

    public getInputTitle(): string {
        return this.fieldType + ":";
    }

    public emitInput(value: string | number): void {
        this.inputContent.inputValue = value;
        this.inputEvent.emit(this.inputContent);
    }

    public getInputType(): InputType {
        switch (this.fieldType) {
            case IncomeInputFieldType.TITLE:
                return InputType.TEXT;
            case IncomeInputFieldType.AMOUNT:
                return InputType.NUMBER;
            case IncomeInputFieldType.HOURS:
                return InputType.NUMBER;
            case IncomeInputFieldType.DATE:
                return InputType.DATE;
            default:
                return InputType.TEXT;
        }
    }

    protected readonly TagType = TagType;
}
