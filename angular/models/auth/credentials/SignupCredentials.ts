import {LoginCredentials} from "./LoginCredentials";

export class SignupCredentials extends LoginCredentials {
    public confirmPassword: string;
    public email: string;
    public termsAgreed: boolean;
    public constructor(username: string = '',
                       password: string = '',
                       confirmPassword: string = '',
                       email: string = '',
                       termsAgreed: boolean = false) {
        super(username, password);
    }
}