export interface CredentialSending {
    isValidCredentialInputs(): boolean;
    sendCredentialsToServer(): void;
    subscribeToAuthEvents?(): void;
}