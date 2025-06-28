// welcome.component.ts 
import { Component } from "@angular/core";
import {TagType} from "../../../models/html/TagType";
import {WelcomeService} from "../../../services/server/welcome.service";
import {
    LastPaycheck
} from "../../elements/element-group-welcome/last-paycheck-input/models/LastPaycheck";
import {Router} from "@angular/router";

@Component({
    selector: 'welcome',
    templateUrl: './welcome.component.html',
    styleUrls: ['./welcome.component.css']
})
export class WelcomeComponent {
    constructor(private welcomeService: WelcomeService,
                private router: Router) {
        
    }


    submitWelcomeSurvey(lastPaycheck: LastPaycheck): void {
        console.log('Clicked submit welcome survey with:', lastPaycheck);
        this.welcomeService.submitWelcomeSurvey(lastPaycheck).subscribe(operationSuccessResponse => {
            console.log('Welcome survey submitted successfully:', operationSuccessResponse);
            if (operationSuccessResponse.operationSuccess) {
                this.router.navigate(['/budget']);
                console.log('Redirecting to budget page');
            }
        });
    }

    protected readonly TagType = TagType;
}
