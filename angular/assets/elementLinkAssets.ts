import {TargetType} from "../models/html/TargetType";
import {TextElementLink} from "../models/link/TextElementLink";
import {TagType} from "../models/html/TagType";

export const navBarHomeElementLink = new TextElementLink('/',
    TargetType.SELF,
    false,
    'Home',
    TagType.H5);
export const navBarPaychecksElementLink = new TextElementLink('/paychecks',
    TargetType.SELF,
    false,
    'Paychecks',
     TagType.H5);
export const navBarMyAccountElementLink = new TextElementLink('/account',
    TargetType.SELF,
    false,
    'My Account',
    TagType.H5);