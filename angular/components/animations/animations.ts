import {
    animate,
    AnimationTriggerMetadata, state,
    style,
    transition,
    trigger
} from "@angular/animations";

export const fadeInOutAnimation: AnimationTriggerMetadata = trigger('fadeInOut', [
    transition(':enter', [
        style({opacity: 0}),
        animate('{{ fadeInDuration }} {{ waitDuration }}', style({opacity: 1}))
    ]),
    transition(':leave', [
        animate('{{ fadeOutDuration }} {{ waitDuration }}', style({opacity: 0}))
    ])
]);
export const fadeInAnimation: AnimationTriggerMetadata = trigger('fadeIn', [
    transition(':enter', [
        style({ opacity: 0 }),
        animate('{{ duration }} {{ delay }}', style({ opacity: 1 }))
    ])
]);
export const accordionPopAnimation: AnimationTriggerMetadata = trigger('accordionPop', [
    state(
        'collapsed',
        style({
            height: '0px',
            opacity: 0,
            padding: '0',
            overflow: 'hidden'
        })
    ),
    state(
        'expanded',
        style({
            height: '*',
            opacity: 1,
            padding: '1rem'
        })
    ),
    transition('collapsed <=> expanded', [animate('300ms ease-in-out')])
]);
export const slideLeftAnimation: AnimationTriggerMetadata = trigger("slideLeft", [
    state(
        "hidden",
        style({
            transform: "translateX(-100%)",
            opacity: 0,
        })
    ),
    state(
        "visible",
        style({
            transform: "translateX(0)",
            opacity: 1,
        })
    ),
    transition("hidden => visible", [
        animate("{{ duration }} {{ delay }} cubic-bezier(0.25, 0.1, 0.25, 1)")
    ]),
    transition("visible => hidden", [
        animate("{{ duration }} {{ delay }} cubic-bezier(0.25, 0.1, 0.25, 1)")
    ]),
]);