export class LoginCredentials {
    public username: string;
    public password: string;
    public constructor(username: string = '',
                       password: string = '') {
        this.username = username;
        this.password = password;
    }
}