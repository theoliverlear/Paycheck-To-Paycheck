export class User {
    userId: number;
    username: string;
    name: string;
    constructor(userId: number = 0,
                username: string = '',
                name: string = '') {
        this.userId = userId;
        this.username = username;
        this.name = name;
    }
    hasUserId(): boolean {
        return this.userId > 0;
    }
    hasUsername(): boolean {
        return this.username.length > 0;
    }
    hasName(): boolean {
        return this.name.length > 0;
    }
}