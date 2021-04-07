class Person {
    constructor(firstAndLast) {
        if(arguments.length > 1 || typeof(arguments[0]) !== 'string') {
            throw new Error('invalid arguments');
        }
        
        this.firstName = firstAndLast.split(' ')[0];
        this.lastName = firstAndLast.split(' ')[1];
        this.fullName = firstAndLast;

        this.getFirstName = function () {
            return this.firstName;
        }

        this.getLastName = function () {
            return this.lastName;
        }

        this.getFullName = function () {
            return this.fullName;
        };

        this.setFirstName = function (first) {
            checkError(arguments);
            this.firstName = first;
        }

        this.setLastName = function (last) {
            checkError(arguments);
            this.lastName = last;
        }

        this.setFullName = function (firstAndLast) {
            checkError(arguments);
            this.fullName = firstAndLast;
        }
    }
}

const checkError = (variable) => {
    if(variable.length > 1 || typeof(variable[0]) !== 'string') {
        throw new Error('invalid arguments');
    }
}

// const fail = new Person(9000);
const bob = new Person('Bob Ross');
console.log(bob);
console.log(Object.keys(bob).length);