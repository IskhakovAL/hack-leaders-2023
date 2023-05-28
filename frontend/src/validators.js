export function isTextCorrect(value) {
    if (!value) return true;
    const pattern = new RegExp("^[-А-ЯЁа-яё]+$");
    if (!pattern.test(value)) {
        return false;
    }
    return true;
}

export function isPhoneEntered(value) {
    if (!value) return true;
    const pattern = new RegExp("\\+7 \\([0-9]{3}\\) [0-9]{3}-[0-9]{2}-[0-9]{2}");
    if (!pattern.test(value)) {
        return false;
    }
    return true;
}

export function isInnNumeric(value) {
    if (!value) return true;
    const pattern = new RegExp("^[0-9]+$");
    if (!pattern.test(value)) {
        return false;
    }
    return true;
}

export function isInnLengthCorrect(value) {
    if (!value) return true;
    if (value.length === 10 || value.length === 12) {
        return true;
    }
    return false;
}
