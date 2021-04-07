const countOnline = (usersObj) => {
    let numOnline = 0;
    for (let user in usersObj) {
        if (usersObj[user].online) {
            numOnline++;
        }
    }
    return numOnline;
}

const test = (obj, result) => {
    countOnline(obj) === result ? console.log('Pass') : console.log('Fail');
}

test({ Alan: { online: false }, Jeff: { online: true }, Sarah: { online: false } }, 1);
test({ Alan: { online: true }, Jeff: { online: false }, Sarah: { online: true } }, 2);
test({ Alan: { online: false }, Jeff: { online: false }, Sarah: { online: false } }, 0);