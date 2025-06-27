// service-terms-input.component.ts
import {Component, EventEmitter, Output} from "@angular/core";
import {TagType} from "../../../../models/html/TagType";
import {ButtonTriggerType} from "../../element-group-native/ss-button/models/ButtonTriggerType";

@Component({
    selector: 'service-terms-input',
    templateUrl: './service-terms-input.component.html',
    styleUrls: ['./service-terms-input.component.css']
})
export class ServiceTermsInputComponent {
    termsAgreed: boolean;
    @Output() termsAgreedChange: EventEmitter<boolean> = new EventEmitter<boolean>();
    constructor() {

    }

    protected emitTermsAgreedChange(termsAgreed: boolean) {
        this.setTermsAgreed(termsAgreed);
        this.termsAgreedChange.emit(termsAgreed);
    }

    protected setTermsAgreed(termsAgreed: boolean) {
        this.termsAgreed = termsAgreed;
    }

    protected readonly TagType = TagType;
    protected readonly ButtonTriggerType = ButtonTriggerType;
}
