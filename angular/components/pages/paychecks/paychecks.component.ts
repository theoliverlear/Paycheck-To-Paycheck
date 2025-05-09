// paychecks.component.ts
import { Component, HostListener, Input, OnInit } from "@angular/core";

@Component({
    selector: "paychecks",
    templateUrl: "./paychecks.component.html",
    styleUrls: ["./paychecks.component.css"],
})
export class PaychecksComponent implements OnInit {
    @Input() numPaychecks: number = 5;
    @Input() paycheckIds: number[] = [];
    isLoaded: boolean = false;
    isFetching: boolean = false;
    private loadingNewItems: boolean = false;
    private paycheckLoadingStatus: Record<number, boolean> = {};

    constructor() {

    }

    ngOnInit(): void {
        this.initializePaychecks();
    }

    @HostListener("window:scroll", [])
    onScroll(): void {
        if (this.loadingNewItems || this.isFetching) {
            return;
        }
        const scrollPosition: number = window.scrollY + window.innerHeight;
        const pageHeight: number = document.documentElement.scrollHeight;
        if (this.shouldLoadMorePaychecks(scrollPosition, pageHeight)) {
            this.triggerLoadMorePaychecks();
        }

    }

    shouldLoadMorePaychecks(scrollPosition: number, pageHeight: number): boolean {
        return scrollPosition >= pageHeight - 100;
    }

    private triggerLoadMorePaychecks(): void {
        if (this.isFetching) {
            return;
        }
        this.isFetching = true;
        this.loadMorePaychecks();
    }

    private loadMorePaychecks(): void {
        this.loadingNewItems = true;
        setTimeout((): void => {
            let nextPaycheckId: number;
            if (this.paycheckIds.length > 0) {
                nextPaycheckId = Math.max(...this.paycheckIds) + 1;
            } else {
                nextPaycheckId = 0;
            }
            for (let i: number = 0; i < 5; i++) {
                const paycheckId: number = nextPaycheckId + i;
                this.paycheckIds.push(paycheckId);
                this.paycheckLoadingStatus[paycheckId] = false;
            }
            this.loadingNewItems = false;
        }, 1000);
    }

    onPaycheckLoaded(paycheckId: number): void {
        if (this.paycheckLoadingStatus.hasOwnProperty(paycheckId)) {
            this.paycheckLoadingStatus[paycheckId] = true;
        }
        if (this.allPaychecksLoaded() && this.isFetching) {
            this.isFetching = false;
        }
        if (!this.isLoaded && this.initialPaychecksLoaded()) {
            this.isLoaded = true;
        }
    }

    private allPaychecksLoaded(): boolean {
        return Object.values(this.paycheckLoadingStatus).every((value: boolean): boolean => value);
    }

    private initialPaychecksLoaded(): boolean {
        const initialIds: number[] = this.paycheckIds.slice(0, this.numPaychecks);
        return initialIds.every((id: number): boolean => this.paycheckLoadingStatus[id]);
    }

    private initializePaychecks(): void {
        for (let i: number = 0; i < this.numPaychecks; i++) {
            this.paycheckIds.push(i);
            this.paycheckLoadingStatus[i] = false;
        }
    }
}