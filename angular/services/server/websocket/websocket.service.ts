import {Injectable} from "@angular/core";
import {BehaviorSubject, Observable, shareReplay} from "rxjs";
import {webSocket, WebSocketSubject} from "rxjs/webSocket";

@Injectable({
    providedIn: 'root'
})
export class WebSocketService<T> {
    private socket$: WebSocketSubject<T> | undefined;
    private messagesSubject$: BehaviorSubject<T> = new BehaviorSubject<T>(null);
    public messages$: Observable<T> = this.messagesSubject$.asObservable().pipe(shareReplay(1));
    private _isConnected: boolean = false;
    private _url: string;

    constructor(url: string) {
        this._url = url;
    }

    public connect(): void {
        if (this.isSocketUnavailable()) {
            this.initializeSocket(this._url);
            this.subscribeToServer();
            this._isConnected = true;
        }
    }

    private isSocketUnavailable() {
        return !this.socket$ || this.socket$.closed;
    }

    private subscribeToServer(): void {
        this.socket$.subscribe(
            (message) => this.messagesSubject$.next(message),
            (error) => console.error('WebSocket error:', error),
            (): boolean => this._isConnected = false
        );
    }

    private initializeSocket(url: string): void {
        this.socket$ = webSocket(url);
    }

    public sendMessage(message: T): void {
        if (this.canSendMessage()) {
            console.log('Sending message:', message);
            this.socket$.next(message);
        } else {
            console.error('WebSocket is not connected.');
        }
    }

    private canSendMessage() {
        return this.socket$ && this.isConnected;
    }

    public disconnect(): void {
        if (this.socket$) {
            this.closeConnection();
        }
    }

    private closeConnection() {
        this._isConnected = false;
        this.socket$.complete();
    }

    public getMessages(): Observable<T> {
        return this.messages$;
    }

    get isConnected(): boolean {
        return this._isConnected;
    }

    get url(): string {
        return this._url;
    }
}