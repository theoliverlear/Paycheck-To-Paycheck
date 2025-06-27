import {IncomeInputFieldType} from "./IncomeInputFieldType";

export class IncomeInputContent {
    public fieldType: IncomeInputFieldType;
    public inputValue: string | number;
    public constructor(fieldType: IncomeInputFieldType = IncomeInputFieldType.TITLE,
                       inputValue: string | number = '') {
        this.fieldType = fieldType;
        this.inputValue = inputValue;
    }
}