import {
    Component,
    EventEmitter,
    HostBinding,
    HostListener,
    Input,
    OnInit,
    Output
} from "@angular/core";
import {ElementSize} from "../../../models/ElementSize";
import {ButtonText} from "./models/ButtonText";
import {ButtonPosition} from "./models/ButtonPosition";
import {ImageAsset} from "../../../assets/imageAssets";
import {TagType} from "../../../models/html/TagType";

@Component({
    selector: 'ss-button',
    templateUrl: './ss-button.component.html',
    styleUrls: ['./ss-button.component.css']
})
export class SsButtonComponent implements OnInit {
    @Input() text: ButtonText;
    @Input() size: ElementSize;
    @Input() buttonPosition: ButtonPosition;
    @Input() imageAsset?: ImageAsset;
    @Output() buttonClicked: EventEmitter<void> = new EventEmitter<void>();
    @HostBinding('style.align-self') alignSelf: string;
    constructor() {

    }
    ngOnInit() {
        this.setAlignSelf();
    }

    @HostListener('click')
    protected onClick(): void {
        this.emitButtonClicked();
    }

    private emitButtonClicked(): void {
        this.buttonClicked.emit();
    }

    private setAlignSelf(): void {
        switch (this.buttonPosition) {
            case ButtonPosition.START:
                this.alignSelf = ButtonPosition.START;
                break;
            case ButtonPosition.END:
                this.alignSelf = ButtonPosition.END;
                break;
            case ButtonPosition.CENTER:
                this.alignSelf = ButtonPosition.CENTER;
                break;
            default:
                this.alignSelf = ButtonPosition.INHERIT;
        }
    }
    protected isImageButton(): boolean {
        let hasImageAsset: boolean = this.imageAsset !== undefined;
        return hasImageAsset;
    }
    protected getTagType(): TagType {
        switch (this.size) {
            case ElementSize.VERY_LARGE:
                return TagType.H3;
            case ElementSize.LARGE:
                return TagType.H4;
            case ElementSize.MEDIUM:
                return TagType.H5;
            case ElementSize.SMALL:
                return TagType.H6;
            default:
                return TagType.H6;
        }
    }
}