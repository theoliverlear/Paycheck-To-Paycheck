// bill-input-field.component.ts 
import {Component, EventEmitter, Input, OnInit, Output} from "@angular/core";
import {TagType} from "../../../models/html/TagType";
import {BillInputFieldType} from "./models/BillInputFieldType";
import {InputType} from "../ss-input/models/InputType";
import {BillInputContent} from "./models/BillInputContent";

@Component({
    selector: 'bill-input-field',
    templateUrl: './bill-input-field.component.html',
    styleUrls: ['./bill-input-field.component.css']
})
export class BillInputFieldComponent implements OnInit {
    @Input() protected fieldType: BillInputFieldType;
    @Input() protected placeholder: string | number;
    @Output() inputEvent: EventEmitter<BillInputContent> = new EventEmitter<BillInputContent>();
    protected inputContent: BillInputContent = new BillInputContent();
    constructor() {
        
    }

    ngOnInit() {
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
            case BillInputFieldType.TITLE:
                return InputType.TEXT;
            case BillInputFieldType.AMOUNT:
                return InputType.NUMBER;
            case BillInputFieldType.DATE:
                return InputType.DATE;
            default:
                return InputType.TEXT;
        }
    }

    protected readonly TagType = TagType;
}
