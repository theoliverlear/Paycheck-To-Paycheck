export class LastPaycheck {
    public lastPaycheckDate: Date;
    public paycheckAmount: number;
    public checkingAccountAmount: number;
    constructor(lastPaycheckDate: Date = new Date(),
                paycheckAmount: number = 0,
                checkingAccountAmount: number = 0) {
        this.lastPaycheckDate = lastPaycheckDate;
        this.paycheckAmount = paycheckAmount;
        this.checkingAccountAmount = checkingAccountAmount;
    }
}