// bill-input-field.component.ts 
import {Component, Input} from "@angular/core";
import {TagType} from "../../../models/html/TagType";
import {BillInputFieldType} from "./models/BillInputFieldType";
import {InputType} from "../ss-input/models/InputType";

@Component({
    selector: 'bill-input-field',
    templateUrl: './bill-input-field.component.html',
    styleUrls: ['./bill-input-field.component.css']
})
export class BillInputFieldComponent {
    @Input() protected fieldType: BillInputFieldType;
    constructor() {
        
    }

    public getInputTitle(): string {
        return this.fieldType + ":";
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
