// confirm-button.component.ts
import {
    Component,
    EventEmitter,
    HostBinding,
    HostListener,
    Input,
    Output
} from "@angular/core";
import {confirmIconImageAsset} from "../../../assets/imageAssets";
import {ButtonTriggerType} from "../ss-button/models/ButtonTriggerType";

@Component({
    selector: 'confirm-button',
    templateUrl: './confirm-button.component.html',
    styleUrls: ['./confirm-button.component.css']
})
export class ConfirmButtonComponent {
    @Input() protected triggerType: ButtonTriggerType = ButtonTriggerType.ONE_TIME;
    @Output() buttonClicked: EventEmitter<boolean> = new EventEmitter<boolean>();
    selected: boolean;
    @HostBinding('class.selected') get isSelected() {
        return this.selected;
    }
    @HostBinding('class.toggle-type') get isToggleType() {
        return this.triggerType === ButtonTriggerType.TOGGLE;
    }
    constructor() {

    }

    @HostListener('click')
    protected onClick() {
        if (this.triggerType === ButtonTriggerType.TOGGLE) {
            this.selected = !this.selected;
        }
        this.buttonClicked.emit(this.selected);
    }
    protected readonly confirmIconImageAsset = confirmIconImageAsset;
}
