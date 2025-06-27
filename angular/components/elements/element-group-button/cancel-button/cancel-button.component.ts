// cancel-button.component.ts 
import {Component, EventEmitter, Output} from "@angular/core";
import {closeIconImageAsset} from "../../../../assets/imageAssets";

@Component({
    selector: 'cancel-button',
    templateUrl: './cancel-button.component.html',
    styleUrls: ['./cancel-button.component.css']
})
export class CancelButtonComponent {
    @Output() buttonClicked: EventEmitter<void> = new EventEmitter<void>();
    constructor() {
        
    }

    public onButtonClick(): void {
        this.buttonClicked.emit();
    }

    protected readonly closeIconImageAsset = closeIconImageAsset;
}
