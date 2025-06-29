import {Saving, Wallet} from "../models/wallet/types";

export const emptyWallet: Wallet = {
    id: 0,
    checkingAccount: {
        id: 0,
        name: 'Checking Account',
        amount: 0,
        type: 'Saving'
    },
    savings: [],
    debts: []
};

export function isEmptyWallet(wallet: Wallet): boolean {
    return emptyWallet === wallet;
}

export const emptySaving: Saving = {
    id: 0,
    name: 'Default Saving',
    amount: 0,
    type: 'Saving'
};

export function isEmptySaving(saving: Saving): boolean {
    return emptySaving === saving;
}