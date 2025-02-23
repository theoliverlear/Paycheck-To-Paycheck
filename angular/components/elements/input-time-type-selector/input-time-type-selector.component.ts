// input-time-type-selector.component.ts 
import {Component, EventEmitter, Output, ViewChild} from "@angular/core";
import {InputTimeType} from "../../../models/input/InputTimeType";
import {
    InputTimeTypeComponent
} from "../input-time-type/input-time-type.component";

@Component({
    selector: 'input-time-type-selector',
    templateUrl: './input-time-type-selector.component.html',
    styleUrls: ['./input-time-type-selector.component.css']
})
export class InputTimeTypeSelectorComponent {
    @ViewChild('oneTimeButton') oneTimeButton: InputTimeTypeComponent;
    @ViewChild('recurringButton') recurringButton: InputTimeTypeComponent;
    @Output() timeTypeSelected: EventEmitter<InputTimeType> = new EventEmitter<InputTimeType>();
    constructor() {
        
    }

    selectOneTime(): void {
        this.oneTimeButton.select();
        this.recurringButton.deselect();
        this.emitTimeType();
    }

    selectRecurring(): void {
        this.oneTimeButton.deselect();
        this.recurringButton.select();
        this.emitTimeType();
    }

    public emitTimeType(): void {
        if (this.oneTimeButton.selected) {
            this.timeTypeSelected.emit(InputTimeType.ONE_TIME);
        } else {
            this.timeTypeSelected.emit(InputTimeType.RECURRING);
        }
    }
    protected readonly InputTimeType = InputTimeType;
}
