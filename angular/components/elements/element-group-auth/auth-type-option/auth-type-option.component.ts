// auth-type-option.component.ts
import {
    Component, EventEmitter,
    HostBinding,
    HostListener,
    Input,
    OnInit, Output
} from "@angular/core";
import {AuthType} from "../../../../models/auth/AuthType";
import {TagType} from "../../../../models/html/TagType";

@Component({
    selector: 'auth-type-option',
    templateUrl: './auth-type-option.component.html',
    styleUrls: ['./auth-type-option.component.css']
})
export class AuthTypeOptionComponent implements OnInit{
    @Input() authType: AuthType = AuthType.SIGNUP;
    @HostBinding('class.selected') selected: boolean = false;
    @Output() typeSelected: EventEmitter<AuthType> = new EventEmitter<AuthType>();
    constructor() {
        
    }

    ngOnInit() {
        this.selected = this.authType === AuthType.SIGNUP;
    }

    public select(): void {
        this.selected = true;
    }

    public deselect(): void {
        this.selected = false;
    }

    @HostListener('click')
    protected onClick() {
        this.typeSelected.emit(this.authType);
    }
    protected readonly TagType = TagType;
}
