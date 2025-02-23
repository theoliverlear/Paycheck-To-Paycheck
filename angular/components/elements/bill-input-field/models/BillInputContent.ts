import {BillInputFieldType} from "./BillInputFieldType";

export class BillInputContent {
    public fieldType: BillInputFieldType;
    public inputValue: string | number;
    public constructor(fieldType: BillInputFieldType = BillInputFieldType.TITLE,
                       inputValue: string | number = '') {
        this.fieldType = fieldType;
        this.inputValue = inputValue;
    }
}