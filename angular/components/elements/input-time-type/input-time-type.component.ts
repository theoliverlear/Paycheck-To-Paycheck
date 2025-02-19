// input-time-type.component.ts 
import {
    Component, EventEmitter,
    HostBinding,
    HostListener,
    Input,
    OnInit, Output
} from "@angular/core";
import {InputTimeType} from "../../../models/input/InputTimeType";
import {TagType} from "../../../models/html/TagType";

@Component({
    selector: 'input-time-type',
    templateUrl: './input-time-type.component.html',
    styleUrls: ['./input-time-type.component.css']
})
export class InputTimeTypeComponent implements OnInit {
    @Input() protected timeType: InputTimeType;
    @Input() protected isSelected: boolean;
    @HostBinding('class.selected') get selected(): boolean {
        return this.isSelected;
    }
    @Output() clickEvent: EventEmitter<boolean> = new EventEmitter<boolean>();
    constructor() {
        
    }

    ngOnInit() {
        if (this.timeType === InputTimeType.ONE_TIME) {
            this.isSelected = true;
        } else {
            this.isSelected = false;
        }
    }

    select(): void {
        this.isSelected = true;
    }
    deselect(): void {
        this.isSelected = false;
    }

    @HostListener('click')
    onClick() {
        this.clickEvent.emit(this.isSelected);
    }

    protected readonly TagType = TagType;
}
