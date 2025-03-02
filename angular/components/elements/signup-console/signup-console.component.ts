// signup-console.component.ts 
import { Component } from "@angular/core";
import {TagType} from "../../../models/html/TagType";

@Component({
    selector: 'signup-console',
    templateUrl: './signup-console.component.html',
    styleUrls: ['./signup-console.component.css']
})
export class SignupConsoleComponent {
    constructor() {
        
    }

    protected readonly TagType = TagType;
}
