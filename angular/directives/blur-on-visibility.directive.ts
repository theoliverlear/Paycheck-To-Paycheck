// blur-on-visibility.directive.ts
import {
    Directive,
    ElementRef,
    HostBinding,
    Input,
    OnDestroy,
    OnInit,
    Renderer2
} from '@angular/core';

@Directive({
    selector: '[blurOnVisibility]',
})
export class BlurOnVisibilityDirective implements OnInit, OnDestroy {
    private observer: IntersectionObserver;
    @Input() threshold: number = 0.4;
    @HostBinding('class.blurred') isBlurred: boolean = true;

    constructor(private element: ElementRef, private renderer: Renderer2) {

    }

    ngOnInit(): void {
        this.initIntersectionObserver();
    }

    ngOnDestroy(): void {
        this.observer.disconnect();
    }

    private initIntersectionObserver(): void {
        this.observer = new IntersectionObserver(
            (entries: IntersectionObserverEntry[]): void => {
                entries.forEach((entry: IntersectionObserverEntry): void => {
                    this.isBlurred = !entry.isIntersecting;
                });
            },
            {
                threshold: this.threshold,
            }
        );
        this.observer.observe(this.element.nativeElement);
    }
}