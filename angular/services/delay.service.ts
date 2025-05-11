import {Injectable} from "@angular/core";

@Injectable({
    providedIn: 'root'
})
export class DelayService {
    public delay(delayInMilliseconds: number): Promise<void> {
        return new Promise((resolve: () => void): void => {
            setTimeout(resolve, delayInMilliseconds);
        });
    }
}