import {TargetType} from "../models/html/TargetType";
import {TextElementLink} from "../models/link/TextElementLink";
import {TagType} from "../models/html/TagType";
import {ElementLink} from "../models/link/ElementLink";

export const navBarHomeElementLink = new ElementLink('/',
    TargetType.SELF);
export const navBarBudgetElementLink = new TextElementLink('/budget',
    TargetType.SELF,
    false,
    'Budget',
    TagType.H5);
export const navBarPaychecksElementLink = new TextElementLink('/paychecks',
    TargetType.SELF,
    false,
    'Paychecks',
     TagType.H5);
export const navBarMyAccountElementLink = new TextElementLink('/authorize',
    TargetType.SELF,
    false,
    'My Account',
    TagType.H5);