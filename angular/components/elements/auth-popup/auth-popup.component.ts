// auth-popup.component.ts 
import {Component, Input} from "@angular/core";
import {TagType} from "../../../models/html/TagType";
import {PossibleAuthPopup} from "../auth-console/models/types";

@Component({
    selector: 'auth-popup',
    templateUrl: './auth-popup.component.html',
    styleUrls: ['./auth-popup.component.css']
})
export class AuthPopupComponent {
    @Input() protected authPopup: PossibleAuthPopup;
    constructor() {
        
    }

    protected readonly TagType = TagType;
}
