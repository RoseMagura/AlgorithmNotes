const confirmEnding = (string, target) => {
    const diff = string.length - target.length;
    for (let i = target.length - 1; i >= 0; i--) {
        if(string[i + diff] !== target[i]) {
            return false;
        }
    }
    return true;
}

const test = (input, output) => {
    input === output ? console.log('Pass') : console.log('Fail');
}

test(confirmEnding('Bastian', 'n'), true);
test(confirmEnding('Congratulation', 'on'), true);
test(confirmEnding("Abstraction", "action"), true);
test(confirmEnding("If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing", "mountain"), false);
test(confirmEnding("He has to give me a new name", "name"), true);
test(confirmEnding("Open sesame", "same"), true);