class Person {
    constructor(firstAndLast) {
        if(arguments.length > 1 || typeof(arguments[0]) !== 'string') {
            throw new Error('invalid arguments');
        }
        
        let fullName = firstAndLast;

        this.getFirstName = function () {
            return fullName.split(' ')[0];
        }

        this.getLastName = function () {
            return fullName.split(' ')[1];
        }

        this.getFullName = function () {
            return fullName;
        };

        this.setFirstName = function (first) {
            checkError(arguments);
            fullName = `${first} ${fullName.split(' ')[1]}`;
        }

        this.setLastName = function (last) {
            checkError(arguments);
            fullName = `${fullName.split(' ')[0]} ${last}`;
        }

        this.setFullName = function (firstAndLast) {
            checkError(arguments);
            fullName = firstAndLast;

        }

        this.setLastName = function (last) {
            checkError(arguments);
            fullName = fullName.split(' ')[0] + ' ' + last;
        }

        this.setFullName = function (firstAndLast) {
            checkError(arguments);
            fullName = firstAndLast;
        }
    }
}

const checkError = (variable) => {
    if(variable.length > 1 || typeof(variable[0]) !== 'string') {
        throw new Error('invalid arguments');
    }
}

const bob = new Person('Bob Ross');
bob.setFirstName('Haskell');
console.log(bob.getFullName());