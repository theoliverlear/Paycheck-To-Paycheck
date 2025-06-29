export type Saving = {
    id: number;
    name: string;
    amount: number;
    type: 'Saving';
};

export type Debt = {
    id: number;
    name: string;
    amount: number;
    type: 'Debt';
};

export type Wallet = {
    id: number;
    checkingAccount: Saving;
    savings: Saving[];
    debts: Debt[];
};