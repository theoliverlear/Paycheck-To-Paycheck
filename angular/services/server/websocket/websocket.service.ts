import {Injectable} from "@angular/core";
import {BehaviorSubject, Observable, shareReplay} from "rxjs";
import {webSocket, WebSocketSubject} from "rxjs/webSocket";

@Injectable({
    providedIn: 'root'
})
export class WebSocketService<Send, Receive> {
    private socket$: WebSocketSubject<Send> | undefined;
    private messagesSubject$: BehaviorSubject<Receive> = new BehaviorSubject<Receive>(null);
    public messages$: Observable<Receive> = this.messagesSubject$.asObservable().pipe(shareReplay(1));
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

    private isSocketUnavailable(): boolean {
        return !this.socket$ || this.socket$.closed;
    }

    private subscribeToServer(): void {
        this.socket$.subscribe(
            (message: Send): void => this.messagesSubject$.next(message as unknown as Receive),
            (error: any): void => console.error('WebSocket error:', error),
            (): boolean => this._isConnected = false
        );
    }

    private initializeSocket(url: string): void {
        this.socket$ = webSocket<Send>({
            url: url,
            serializer: (msg: Send) => JSON.stringify(msg),
            deserializer: (event: MessageEvent<any>) => JSON.parse(event.data) as Send
        });

    }

    public sendMessage(message: Send): void {
        if (this.canSendMessage()) {
            console.log('Sending message:', message);
            this.socket$.next(message);
        } else {
            console.error('WebSocket is not connected.');
        }
    }

    private canSendMessage(): boolean {
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

    public getMessages(): Observable<Receive> {
        return this.messages$;
    }

    get isConnected(): boolean {
        return this._isConnected;
    }

    get url(): string {
        return this._url;
    }
}