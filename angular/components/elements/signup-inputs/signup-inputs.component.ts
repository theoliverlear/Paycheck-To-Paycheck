// signup-inputs.component.ts 
import { Component } from "@angular/core";
import {AuthInputType} from "../../../models/auth/AuthInputType";

@Component({
    selector: 'signup-inputs',
    templateUrl: './signup-inputs.component.html',
    styleUrls: ['./signup-inputs.component.css']
})
export class SignupInputsComponent {
    constructor() {
        
    }

    protected readonly AuthInputType = AuthInputType;
}
