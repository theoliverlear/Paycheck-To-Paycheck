// auth-type-slider.component.ts
import {Component, EventEmitter, Output, ViewChild} from "@angular/core";
import {AuthType} from "../../../../models/auth/AuthType";
import {
    AuthTypeOptionComponent
} from "../auth-type-option/auth-type-option.component";

@Component({
    selector: 'auth-type-slider',
    templateUrl: './auth-type-slider.component.html',
    styleUrls: ['./auth-type-slider.component.css']
})
export class AuthTypeSliderComponent {
    @ViewChild('signupOption') signupOption: AuthTypeOptionComponent;
    @ViewChild('loginOption') loginOption: AuthTypeOptionComponent;
    @Output() authTypeChange: EventEmitter<AuthType> = new EventEmitter<AuthType>();
    constructor() {
        
    }

    public setSelected(authType: AuthType) {
        if (authType === AuthType.SIGNUP) {
            this.signupOption.select();
            this.loginOption.deselect();
        } else {
            this.signupOption.deselect();
            this.loginOption.select();
        }
        this.authTypeChange.emit(authType);
    }

    protected readonly AuthType = AuthType;
}
